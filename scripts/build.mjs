// Monta a pasta dist/ que a Netlify publica: o caderno com o login ligado + a biblioteca de login.
// O "Caderno de Matemática.html" do repositório continua sendo um arquivo único que funciona sem internet e sem login.
import { mkdirSync, readFileSync, writeFileSync, copyFileSync } from "node:fs"

const NOME = "Caderno de Matemática.html"
const MARCA = "<!--__CLOUD__-->"
const html = readFileSync(NOME, "utf8")
if (html.split(MARCA).length !== 2) throw new Error(`Não achei a marca ${MARCA} uma única vez em ${NOME}`)
mkdirSync("dist", { recursive: true })
// Na Netlify o caderno fica na raiz do site: é para lá que o Google devolve o visitante depois do login.
writeFileSync("dist/index.html", html.replace(MARCA, '<script>window.CADERNO_CLOUD = true</script>\n<script src="/auth.js"></script>'))
// O endereço antigo continua valendo e leva para a raiz (mantendo o que vier depois do #).
writeFileSync("dist/" + NOME, '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Caderno de Matemática</title>' +
  '<script>location.replace("/" + location.hash)</script></head><body><p><a href="/">Abrir o Caderno de Matemática</a></p></body></html>')
copyFileSync("auth.js", "dist/auth.js")
console.log("dist/ pronta")
