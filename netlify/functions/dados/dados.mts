import type { Config, Context } from "@netlify/functions"
import { getStore } from "@netlify/blobs"
import { getUser } from "@netlify/identity"
import { handle } from "./core.mts"

// Perfis e progresso do Caderno de Matemática, guardados por conta (Netlify Identity + Netlify Blobs).
export default async (req: Request, context: Context) => {
  const user = await getUser()
  const store = getStore({ name: "caderno-matematica", consistency: "strong" })
  return handle(req, user ? { id: user.id, email: user.email, name: user.name } : null, store)
}

export const config: Config = { path: "/api/dados" }
