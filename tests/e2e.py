import subprocess, time, json, os, sys
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); PORT = 8899; B = f"http://localhost:{PORT}"
SHOTS = os.path.join(HERE, "shots"); os.makedirs(SHOTS, exist_ok=True)
srv = subprocess.Popen(["node", "--experimental-strip-types", "--no-warnings", os.path.join(HERE, "dev-server.mts"), str(PORT)], stdout=subprocess.PIPE, text=True)
srv.stdout.readline()
FAKE_NI = """
window.NI = {
  async handleAuthCallback(){ if (location.hash.startsWith('#access_token=')) { document.cookie = 'nf_jwt=' + location.hash.split('=')[1] + '; path=/'; history.replaceState(null, '', location.pathname); return {type: 'oauth'}; } return null; },
  async getUser(){ const m = document.cookie.match(/nf_jwt=([^;]+)/); return m ? {id: m[1], email: m[1] + '@gmail.com', name: 'Responsável'} : null; },
  async getSettings(){ return {autoconfirm: true, disableSignup: false, providers: {google: true}}; },
  oauthLogin(p){ location.hash = '#access_token=' + 'u1'; location.reload(); },
  async logout(){ document.cookie = 'nf_jwt=; path=/; max-age=0'; },
  async refreshSession(){ return null; },
};"""
ok = lambda c, m: print(("OK   " if c else "FALHOU ") + m) or (c or FAILS.append(m))
FAILS = []
def store(pg): return json.loads(pg.request.get(B + "/__store").text())
def answer(pg, n, right=True):
    pg.evaluate("""([n, right]) => { const q = $$('.q')[n]; for (const el of fields(q)) { const a = (el.dataset.a||'').split('|')[0];
        if (el.dataset.t === 's') el.value = a; else el.value = right ? a : '12345'; el.dispatchEvent(new Event('input')); } check(q); }""", [n, right])
try:
  with sync_playwright() as pw:
    br = pw.chromium.launch()
    # A) biblioteca real, Identity inexistente -> aviso e uso local
    cx = br.new_context(viewport={"width": 1000, "height": 800}); pg = cx.new_page(); errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(B); pg.wait_for_selector("#gbox >> text=ainda não está ativado", timeout=15000)
    ok(pg.evaluate("typeof NI.oauthLogin") == "function", "A: biblioteca de login real carregou")
    pg.click("#glocal"); ok(pg.is_hidden("#gate") and pg.inner_text("#score") == "0 / 650", "A: sem Identity, cai no modo local"); ok(not errs, f"A: sem erros de script {errs}")
    cx.close()

    # B) fluxo completo com login simulado
    cx = br.new_context(viewport={"width": 1000, "height": 800}); cx.route("**/auth.js", lambda r: r.fulfill(body=FAKE_NI, content_type="text/javascript"))
    pg = cx.new_page(); errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(B); pg.evaluate("localStorage.setItem('caderno-mat-v1', JSON.stringify({ans:{'5-22':['25','20','32']}, ok:{'5-22':true}, tries:{}, pos:{g:5,f:{3:0,4:0,5:4}}}))")
    pg.reload(); pg.wait_for_selector("#glogin"); pg.screenshot(path=SHOTS + "/1-login.png")
    ok(pg.is_visible("#gate") and not pg.is_visible("#pchip"), "B: sem login mostra a tela de entrada")
    pg.click("#glogin"); pg.wait_for_selector("#pform"); pg.screenshot(path=SHOTS + "/2-primeiro-perfil.png")
    ok("a resposta já salva" in pg.inner_text("#pform"), "B: oferece trazer as respostas do aparelho")
    pg.click("#pcreate"); ok("nome" in pg.inner_text("#perr").lower(), "B: exige o nome")
    pg.fill("#pname", "Bia"); pg.select_option("#pano", "5"); pg.click("#pcreate"); pg.wait_for_selector("#gate", state="hidden")
    ok(pg.inner_text("#pchipname") == "Bia" and pg.inner_text("#score") == "1 / 650", "B: perfil criado com a resposta importada")
    ok(pg.get_attribute("#tab5", "aria-selected") == "true", "B: abre no ano da criança")
    answer(pg, 0); pg.wait_for_function("document.querySelector('#sync').textContent === 'Salvo na conta'", timeout=8000)
    st = store(pg); key = [k for k in st if k.startswith("estados/u1/")][0]
    ok(len(json.loads(st[key])["state"]["ok"]) == 2, "B: progresso gravado no servidor")
    pg.screenshot(path=SHOTS + "/3-caderno.png")
    pg.reload(); pg.wait_for_selector("#gate", state="hidden"); ok(pg.inner_text("#score") == "2 / 650", "B: ao reabrir, o progresso volta da conta")

    # C) segundo perfil e troca
    pg.click("#pchip"); pg.wait_for_selector("#padd"); pg.click("#padd"); pg.fill("#pname", "Léo"); pg.select_option("#pano", "6"); pg.click("#pcreate"); pg.wait_for_selector("#gate", state="hidden")
    ok(pg.inner_text("#pchipname") == "Léo" and pg.inner_text("#score") == "0 / 650" and pg.get_attribute("#tab6", "aria-selected") == "true", "C: segundo perfil começa zerado no 6º ano")
    answer(pg, 1); pg.wait_for_function("document.querySelector('#sync').textContent === 'Salvo na conta'")
    pg.click("#pchip"); pg.wait_for_selector("[data-open]"); pg.screenshot(path=SHOTS + "/4-perfis.png")
    cards = pg.locator("[data-open]").all_inner_texts(); ok("2 de 650" in cards[0] and "1 de 650" in cards[1], f"C: cartões mostram os acertos {cards}")
    pg.locator("[data-open]").first.click(); pg.wait_for_selector("#gate", state="hidden"); ok(pg.inner_text("#score") == "2 / 650", "C: voltar para Bia mantém os 2 acertos")
    pg.reload(); pg.wait_for_selector("[data-open]"); ok(pg.locator("[data-open]").count() == 2, "C: com 2 perfis, pergunta quem vai estudar")

    # D) outra conta não vê nada
    cx2 = br.new_context(); cx2.route("**/auth.js", lambda r: r.fulfill(body=FAKE_NI.replace("'u1'", "'u2'"), content_type="text/javascript"))
    p2 = cx2.new_page(); p2.goto(B); p2.click("#glogin"); p2.wait_for_selector("#pform")
    ok(p2.locator("[data-open]").count() == 0 and "u2@gmail.com" in p2.inner_text(".gfoot"), "D: outra conta Google começa sem perfis"); cx2.close()

    # E) sem conexão: guarda no aparelho e envia depois
    pg.locator("[data-open]").first.click(); pg.wait_for_selector("#gate", state="hidden")
    cx.route("**/api/dados?perfil=*", lambda r: r.abort() if r.request.method == "PUT" else r.continue_())
    answer(pg, 2); pg.wait_for_function("document.querySelector('#sync').textContent.startsWith('Sem conexão')", timeout=8000)
    ok(pg.inner_text("#score") == "3 / 650", "E: sem conexão, continua respondendo")
    cx.unroute("**/api/dados?perfil=*"); pg.reload(); pg.wait_for_selector("[data-open]"); pg.locator("[data-open]").first.click(); pg.wait_for_selector("#gate", state="hidden")
    pg.wait_for_function("document.querySelector('#sync').textContent === 'Salvo na conta'"); st = store(pg)
    ok(pg.inner_text("#score") == "3 / 650" and len(json.loads(st[key])["state"]["ok"]) == 3, "E: a resposta feita sem conexão foi enviada depois")

    # F) zerar, excluir perfil, sair
    pg.click("#zerar"); pg.click(".zopt[data-z='all']"); pg.wait_for_function("document.querySelector('#sync').textContent === 'Salvo na conta'")
    ok(len(json.loads(store(pg)[key])["state"]["ok"]) == 0, "F: zerar respostas também zera na conta")
    pg.click("#pchip"); pg.click("#pmanage"); pg.locator("[data-ask]").nth(1).click(); pg.click("[data-del]"); pg.wait_for_function("document.querySelectorAll('[data-ask]').length === 1")
    ok(len([k for k in store(pg) if k.startswith("estados/u1/")]) == 1, "F: excluir o perfil apaga o progresso dele")
    pg.click("#pmanage"); pg.click("#gout"); pg.wait_for_selector("#glogin"); ok(pg.is_hidden("#pchip"), "F: sair volta para a tela de entrada")
    pg.reload(); pg.wait_for_selector("#glogin"); ok(True, "F: depois de sair, continua pedindo login")
    ok(not errs, f"sem erros de script {errs}")

    # rodadas e tabuada também vão para a conta
    pg.click("#glogin"); pg.wait_for_selector("#pchip"); pg.click("#tab3"); pg.click("#nova"); pg.click(".zopt.go-new"); pg.evaluate("st.tabu.stars['7'] = 3; save()")
    pg.wait_for_function("document.querySelector('#sync').textContent === 'Salvo na conta'"); sv = json.loads(store(pg)[key])["state"]
    ok(sv["round"]["3"] == 2 and len(sv["hist"]["3"]) == 1 and sv["tabu"]["stars"] == {"7": 3}, "G: rodada, histórico e estrelas da tabuada gravados na conta")
    pg.reload(); pg.wait_for_selector("#pchip"); ok("Rodada 2" in pg.inner_text("#rbar"), "G: ao reabrir, continua na rodada 2")
    pg.click("#pchip"); pg.click("#gout"); pg.wait_for_selector("#glogin")
    # o endereço antigo leva para a raiz
    pg.goto(B + "/Caderno%20de%20Matem%C3%A1tica.html"); pg.wait_for_selector("#glogin"); ok(pg.url.rstrip("/") == B, "G: endereço antigo redireciona")

    # celular
    pg.set_viewport_size({"width": 400, "height": 800}); pg.click("#glogin"); pg.wait_for_selector("#pchip"); pg.wait_for_timeout(300); pg.evaluate("window.scrollTo(0,0)"); pg.screenshot(path=SHOTS + "/5-celular.png")
    ok(pg.evaluate("document.documentElement.scrollWidth") == 400, "celular: sem rolagem lateral")
    pg.click("#pchip"); pg.wait_for_selector(".gfoot"); pg.screenshot(path=SHOTS + "/6-celular-perfis.png")
    br.close()
finally:
    srv.terminate()
print("\nFALHAS:", FAILS if FAILS else "nenhuma"); sys.exit(1 if FAILS else 0)
