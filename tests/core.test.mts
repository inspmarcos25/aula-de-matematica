import test from "node:test"
import assert from "node:assert/strict"
import { handle, sanitizeState } from "../netlify/functions/dados/core.mts"

function memStore() {
  const m = new Map<string, string>()
  return {
    m,
    async get(k: string) { return m.has(k) ? JSON.parse(m.get(k)!) : null },
    async setJSON(k: string, v: unknown) { m.set(k, JSON.stringify(v)) },
    async delete(k: string) { m.delete(k) },
  }
}
const O = "https://aula.test"
const call = (store: any, user: any, method: string, qs = "", body?: unknown, origin: string | null = O) =>
  handle(new Request(O + "/api/dados" + qs, { method, body: body ? JSON.stringify(body) : undefined, headers: origin ? { origin } : {} }), user, store)
const ana = { id: "u-ana", email: "ana@x.com" }, rui = { id: "u-rui", email: "rui@x.com" }

test("sem login devolve 401", async () => {
  assert.equal((await call(memStore(), null, "GET")).status, 401)
})

test("cria perfil, salva e lê o progresso", async () => {
  const s = memStore()
  assert.deepEqual((await (await call(s, ana, "GET")).json()).profiles, [])
  const r = await call(s, ana, "POST", "", { action: "criar", name: "  Bia   Souza ", ano: 5 })
  assert.equal(r.status, 201)
  const { created, profiles } = await r.json()
  assert.equal(profiles[0].name, "Bia Souza"); assert.equal(profiles[0].ano, 5)
  assert.equal((await (await call(s, ana, "GET", "?perfil=" + created)).json()).state, null)
  const put = await call(s, ana, "PUT", "?perfil=" + created, { state: { ans: { "5-1": ["x"], "lixo": ["y"] }, ok: { "5-1": true, "9-9": true }, tries: { "5-2": 2 }, pos: { g: 5, f: { 5: 3 } }, hack: 1 } })
  assert.equal((await put.json()).certas, 1)
  const got = (await (await call(s, ana, "GET", "?perfil=" + created)).json()).state
  assert.deepEqual(got.ans, { "5-1": ["x"] }); assert.deepEqual(got.ok, { "5-1": true }); assert.equal(got.pos.f[5], 3); assert.equal(got.hack, undefined)
  assert.equal((await (await call(s, ana, "GET")).json()).profiles[0].certas, 1)
})

test("uma conta não enxerga nem altera o perfil de outra", async () => {
  const s = memStore()
  const { created } = await (await call(s, ana, "POST", "", { action: "criar", name: "Bia" })).json()
  await call(s, ana, "PUT", "?perfil=" + created, { state: { ok: { "3-1": true } } })
  assert.equal((await call(s, rui, "GET", "?perfil=" + created)).status, 404)
  assert.equal((await call(s, rui, "PUT", "?perfil=" + created, { state: {} })).status, 404)
  assert.equal((await call(s, rui, "POST", "", { action: "excluir", id: created })).status, 404)
  assert.deepEqual((await (await call(s, rui, "GET")).json()).profiles, [])
  assert.deepEqual((await (await call(s, ana, "GET", "?perfil=" + created)).json()).state.ok, { "3-1": true })
})

test("alterações de outra origem são recusadas", async () => {
  const s = memStore()
  assert.equal((await call(s, ana, "POST", "", { action: "criar", name: "Bia" }, "https://malicioso.test")).status, 403)
  assert.equal((await call(s, ana, "POST", "", { action: "criar", name: "Bia" }, null)).status, 403)
})

test("limites: nome obrigatório, 8 perfis, excluir apaga o progresso", async () => {
  const s = memStore()
  assert.equal((await call(s, ana, "POST", "", { action: "criar", name: "   " })).status, 400)
  let last = ""
  for (let i = 0; i < 8; i++) last = (await (await call(s, ana, "POST", "", { action: "criar", name: "P" + i })).json()).created
  assert.equal((await call(s, ana, "POST", "", { action: "criar", name: "P9" })).status, 400)
  await call(s, ana, "PUT", "?perfil=" + last, { state: { ok: { "3-1": true } } })
  assert.ok(s.m.has("estados/u-ana/" + last))
  const del = await (await call(s, ana, "POST", "", { action: "excluir", id: last })).json()
  assert.equal(del.profiles.length, 7); assert.ok(!s.m.has("estados/u-ana/" + last))
})

test("sanitizeState corrige posições inválidas e guarda rodadas, histórico e tabuada", () => {
  const st = sanitizeState({ pos: { g: 9, f: { 3: 99, 4: "2", 5: 12 } }, view: "tabu", round: { 3: 4, 4: -1 },
    hist: { 3: [{ r: 1, v: 1, t: 200, d: "11/11/2026", ok: 150, first: 120, no: 10, em: 40, x: "lixo" }] },
    tabu: { stars: { 7: 3, mix: 9, z: 2 }, best: { 7: 31 }, t: "mix", mode: "desafio", hide: true }, ans: { "3-151": ["8"] } })
  assert.equal(st.pos.g, 3); assert.equal(st.pos.f[3], 0); assert.equal(st.pos.f[4], 2); assert.equal(st.pos.f[5], 12); assert.equal(st.view, "tabu")
  assert.equal(st.round[3], 4); assert.equal(st.round[4], 1); assert.equal(st.round[6], 1)
  assert.deepEqual(st.hist[3], [{ r: 1, v: 1, t: 200, d: "11/11/2026", ok: 150, first: 120, no: 10, em: 40 }]); assert.deepEqual(st.hist[6], [])
  assert.deepEqual(st.tabu, { stars: { 7: 3 }, best: { 7: 31 }, t: "mix", mode: "desafio", hide: true })
  assert.deepEqual(st.ans, { "3-151": ["8"] })
})
