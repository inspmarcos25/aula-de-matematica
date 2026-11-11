// Empacotado com esbuild em auth.js (npm run build:auth). Expõe a biblioteca de login da Netlify para a página.
import * as NI from "@netlify/identity";
window.NI = NI;
