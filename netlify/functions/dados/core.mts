// Regras do servidor para perfis e progresso. Não depende da Netlify, então pode ser testado localmente.

export interface Caller { id: string; email?: string; name?: string }
export interface BlobStore {
  get(key: string, opts: { type: "json" }): Promise<any>
  setJSON(key: string, value: unknown): Promise<unknown>
  delete(key: string): Promise<void>
}
interface Profile { id: string; name: string; ano: number; certas: number; createdAt: string }
interface Account { profiles: Profile[] }

const MAX_PROFILES = 8
const MAX_BODY = 300_000
const ANOS = [3, 4, 5, 6]
const QID = /^[3-6]-[1-9]\d{0,2}$/
const TB_KEYS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "mix"]
const int = (v: unknown, min: number, max: number, dflt: number) => {
  const n = Number(v)
  return Number.isInteger(n) && n >= min && n <= max ? n : dflt
}

const json = (data: unknown, status = 200) =>
  Response.json(data, { status, headers: { "cache-control": "no-store" } })

function plainMap(v: unknown, keep: (val: unknown) => unknown): Record<string, unknown> {
  const out: Record<string, unknown> = {}
  if (!v || typeof v !== "object" || Array.isArray(v)) return out
  for (const [k, val] of Object.entries(v as Record<string, unknown>)) {
    if (!QID.test(k)) continue
    const kept = keep(val)
    if (kept !== undefined) out[k] = kept
  }
  return out
}

/** Mantém só os campos conhecidos do progresso, para que nada estranho seja gravado. */
export function sanitizeState(raw: unknown) {
  const s = (raw && typeof raw === "object" ? raw : {}) as Record<string, any>
  const f: Record<string, number> = {}, round: Record<string, number> = {}, hist: Record<string, unknown[]> = {}
  for (const g of ANOS) {
    f[g] = int(s.pos?.f?.[g], 0, 39, 0)
    round[g] = int(s.round?.[g], 1, 9999, 1)
    hist[g] = (Array.isArray(s.hist?.[g]) ? s.hist[g] : []).slice(-200).map((h: any) => ({
      r: int(h?.r, 1, 9999, 1), v: int(h?.v, 1, 99, 1), t: int(h?.t, 0, 999, 0), d: String(h?.d ?? "").slice(0, 12),
      ok: int(h?.ok, 0, 999, 0), first: int(h?.first, 0, 999, 0), no: int(h?.no, 0, 999, 0), em: int(h?.em, 0, 999, 0),
    }))
  }
  const stars: Record<string, number> = {}, best: Record<string, number> = {}
  for (const k of TB_KEYS) {
    const st = int(s.tabu?.stars?.[k], 1, 3, 0), b = int(s.tabu?.best?.[k], 1, 999, 0)
    if (st) stars[k] = st
    if (b) best[k] = b
  }
  return {
    ans: plainMap(s.ans, (v) =>
      Array.isArray(v) && v.length <= 12
        ? v.map((x) => (Array.isArray(x) ? x.slice(0, 80).map((y) => String(y).slice(0, 12)) : String(x ?? "").slice(0, 120)))
        : undefined),
    ok: plainMap(s.ok, (v) => (v === true ? true : undefined)),
    tries: plainMap(s.tries, (v) => (Number.isInteger(v) && (v as number) > 0 ? Math.min(v as number, 999) : undefined)),
    peek: plainMap(s.peek, (v) => (v === true ? true : undefined)),
    view: ["res", "tabu"].includes(s.view) ? s.view : "fichas",
    rfilter: ["no", "nc", "em", "ok"].includes(s.rfilter) ? s.rfilter : "all",
    pos: { g: ANOS.includes(Number(s.pos?.g)) ? Number(s.pos.g) : 3, f },
    round, hist,
    tabu: {
      stars, best, t: TB_KEYS.includes(String(s.tabu?.t)) ? String(s.tabu.t) : "2",
      mode: ["treinar", "desafio"].includes(s.tabu?.mode) ? s.tabu.mode : "estudar", hide: s.tabu?.hide === true,
    },
  }
}

export async function handle(req: Request, user: Caller | null, store: BlobStore): Promise<Response> {
  if (!user) return json({ error: "nao_autenticado" }, 401)
  const url = new URL(req.url)
  const method = req.method.toUpperCase()
  if (method !== "GET") {
    // Só aceita alterações vindas da própria página (proteção contra CSRF).
    if (req.headers.get("origin") !== url.origin) return json({ error: "origem_invalida" }, 403)
  }

  const accKey = `contas/${user.id}`
  const account: Account = (await store.get(accKey, { type: "json" })) ?? { profiles: [] }
  if (!Array.isArray(account.profiles)) account.profiles = []
  const pid = url.searchParams.get("perfil")

  if (!pid) {
    if (method === "GET") {
      return json({ user: { id: user.id, email: user.email ?? null, name: user.name ?? null }, profiles: account.profiles })
    }
    if (method !== "POST") return json({ error: "metodo_invalido" }, 405)
    let body: any
    try { body = JSON.parse((await req.text()).slice(0, 2000)) } catch { return json({ error: "corpo_invalido" }, 400) }

    if (body?.action === "criar") {
      const name = String(body.name ?? "").trim().replace(/\s+/g, " ").slice(0, 30)
      if (!name) return json({ error: "nome_obrigatorio" }, 400)
      if (account.profiles.length >= MAX_PROFILES) return json({ error: "limite_de_perfis" }, 400)
      const ano = ANOS.includes(Number(body.ano)) ? Number(body.ano) : 3
      const profile: Profile = { id: crypto.randomUUID(), name, ano, certas: 0, createdAt: new Date().toISOString() }
      account.profiles.push(profile)
      await store.setJSON(accKey, account)
      return json({ profiles: account.profiles, created: profile.id }, 201)
    }
    if (body?.action === "excluir") {
      const before = account.profiles.length
      account.profiles = account.profiles.filter((p) => p.id !== body.id)
      if (account.profiles.length === before) return json({ error: "perfil_nao_encontrado" }, 404)
      await store.delete(`estados/${user.id}/${body.id}`)
      await store.setJSON(accKey, account)
      return json({ profiles: account.profiles })
    }
    return json({ error: "acao_invalida" }, 400)
  }

  const profile = account.profiles.find((p) => p.id === pid)
  if (!profile) return json({ error: "perfil_nao_encontrado" }, 404)
  const stateKey = `estados/${user.id}/${pid}`

  if (method === "GET") {
    const saved = await store.get(stateKey, { type: "json" })
    return json({ state: saved?.state ?? null, updatedAt: saved?.updatedAt ?? null })
  }
  if (method === "PUT") {
    const text = await req.text()
    if (text.length > MAX_BODY) return json({ error: "muito_grande" }, 413)
    let body: any
    try { body = JSON.parse(text) } catch { return json({ error: "corpo_invalido" }, 400) }
    const state = sanitizeState(body?.state)
    const updatedAt = new Date().toISOString()
    await store.setJSON(stateKey, { state, updatedAt })
    const certas = Object.keys(state.ok).length
    if (profile.certas !== certas) {
      profile.certas = certas
      await store.setJSON(accKey, account)
    }
    return json({ ok: true, updatedAt, certas })
  }
  return json({ error: "metodo_invalido" }, 405)
}
