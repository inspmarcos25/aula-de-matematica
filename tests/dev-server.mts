// Servidor de teste: entrega dist/ (rode `npm run build` antes) e liga /api/dados às regras reais (core.mts) com um armazenamento em memória.
// O usuário vem do cookie nf_jwt (no site real quem valida esse cookie é a Netlify Identity).
import http from "node:http"
import { readFile } from "node:fs/promises"
import { handle } from "../netlify/functions/dados/core.mts"

const mem = new Map<string, string>()
const store = {
  async get(k: string) { return mem.has(k) ? JSON.parse(mem.get(k)!) : null },
  async setJSON(k: string, v: unknown) { mem.set(k, JSON.stringify(v)) },
  async delete(k: string) { mem.delete(k) },
}
const port = Number(process.argv[2] || 8899)
const types: Record<string, string> = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8" }

http.createServer(async (q, s) => {
  const url = new URL(q.url!, `http://localhost:${port}`)
  if (url.pathname === "/__store") { s.setHeader("content-type", "application/json"); return s.end(JSON.stringify(Object.fromEntries(mem))) }
  if (url.pathname === "/api/dados") {
    const chunks: Buffer[] = []; for await (const c of q) chunks.push(c as Buffer)
    const m = /nf_jwt=([^;]+)/.exec(q.headers.cookie || "")
    const headers = new Headers(); if (q.headers.origin) headers.set("origin", String(q.headers.origin))
    const req = new Request(url, { method: q.method, headers, body: ["GET", "HEAD"].includes(q.method!) ? undefined : Buffer.concat(chunks) })
    const r = await handle(req, m ? { id: m[1], email: m[1] + "@gmail.com", name: "Responsável" } : null, store)
    s.writeHead(r.status, Object.fromEntries(r.headers)); return s.end(await r.text())
  }
  const path = decodeURIComponent(url.pathname === "/" ? "/index.html" : url.pathname)
  try { const body = await readFile(new URL("../dist" + encodeURI(path), import.meta.url)); s.writeHead(200, { "content-type": types[path.slice(path.lastIndexOf("."))] || "application/octet-stream" }); s.end(body) }
  catch { s.writeHead(404); s.end("not found") }
}).listen(port, () => console.log("pronto", port))
