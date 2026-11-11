"""Confere o arquivo único (sem login): as 50 questões do 6º ano aceitam a resposta certa e todas as fichas abrem."""
import os, sys
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1000, "height": 900}); errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    url = "file://" + os.path.join(ROOT, "Caderno de Matemática.html").replace(" ", "%20")
    pg.goto(url); pg.wait_for_selector(".q")
    # progresso antigo, salvo antes de existir o 6º ano
    pg.evaluate("localStorage.setItem('caderno-mat-v1', JSON.stringify({ans:{'3-2':['1346']}, ok:{'3-2':true}, tries:{}, peek:{}, pos:{g:5, f:{3:0,4:2,5:11}}, round:{3:2,4:1,5:1}, hist:{3:[],4:[],5:[]}}))")
    pg.reload(); pg.wait_for_selector(".q")
    print("progresso antigo:", pg.inner_text("#score"), pg.evaluate("JSON.stringify([st.pos, st.round])"))
    res = pg.evaluate("""() => {
      const fails = [], opened = {};
      for (const g of GR) { st.view = 'fichas'; st.pos.g = g; opened[g] = DATA.grades[g].length;
        for (let f = 0; f < DATA.grades[g].length; f++) { st.pos.f[g] = f; render();
          if (g !== 6) continue;
          for (const q of $$('.q')) { for (const el of fields(q)) { const t = el.dataset.t, a = (el.dataset.a || '').split('|')[0];
              if (t === 'ch') el.querySelector(`.opt[data-v="${a}"]`).click();
              else if (t === 'pk') { for (const k of a.split(',')) el.querySelector(`button[data-k="${k}"]`).click(); }
              else { el.value = a; el.dispatchEvent(new Event('input')); } }
            check(q); if (!q.classList.contains('ok')) fails.push(q.dataset.id); } } }
      st.view = 'res'; st.pos.g = 6; render(); const resOk = document.querySelector('#results').innerText.includes('50 de 50');
      st.view = 'tabu'; render(); st.view = 'fichas'; st.pos.g = 6; st.pos.f[6] = 2; render();
      return {fails, opened, certas6: gradeCount(6), total: allTotal(), resOk, rbar6: document.querySelector('#rbar').hidden};
    }""")
    print(res, errs)
    pg.screenshot(path=os.path.join(ROOT, "tests/shots/off-desktop.png"))
    pg.set_viewport_size({"width": 375, "height": 760}); pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(200)
    pg.screenshot(path=os.path.join(ROOT, "tests/shots/off-celular.png")); print("largura celular:", pg.evaluate("document.documentElement.scrollWidth"))
    b.close()
    sys.exit(1 if (res["fails"] or errs or res["certas6"] != 50) else 0)
