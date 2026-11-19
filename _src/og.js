const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const out=process.argv[2];const jobs=JSON.parse(fs.readFileSync(__dirname+'/og-jobs.json'));
const T={pt:'Head de Marketing & Martech',en:'Head of Marketing & Martech',es:'Head de Marketing & Martech'};
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630}});
const seen=new Set();
for(const j of jobs){if(seen.has(j.out))continue;seen.add(j.out);
const art=j.kind==='article';
const html=`<html><head><style>@font-face{font-family:'Inter Tight';font-weight:100 900;src:url(file://${__dirname}/fonts/inter-tight-latin-wght-normal.woff2) format('woff2')}</style><style>
body{margin:0;width:1200px;height:630px;background:#04130F;color:#E6E4DE;font-family:'Inter Tight',sans-serif;position:relative;overflow:hidden}
.g{position:absolute;inset:0;background:radial-gradient(circle at 85% 20%,rgba(194,164,107,.18),transparent 55%)}
.br{position:absolute;left:72px;top:60px;font-size:44px;font-weight:500;letter-spacing:-.07em}
.nm{position:absolute;left:150px;top:62px;font-size:18px;line-height:1.1;font-weight:500}
.cat{position:absolute;left:72px;top:${art?190:0}px;font-size:20px;letter-spacing:.14em;text-transform:uppercase;color:#C2A46B}
h1{position:absolute;left:72px;right:72px;${art?'top:230px;font-size:'+(j.title.length>70?56:68)+'px':'top:200px;font-size:150px'};margin:0;font-weight:500;letter-spacing:-.05em;line-height:1}
.ft{position:absolute;left:72px;bottom:56px;font-size:22px;color:#9fb0a9}
</style></head><body><div class="g"></div><div class="br">rv.</div><div class="nm">Rodolfo<br>Vasco</div>
${art?`<div class="cat">${esc(j.cat)}</div><h1>${esc(j.title)}</h1>`:`<h1>IA &amp;<br>Martech</h1>`}
<div class="ft">${art?'rodolfovasco.com.br':T[j.lang]}</div></body></html>`;
const hf=path.join(require('os').tmpdir(),'rv-og.html');fs.writeFileSync(hf,html);await p.goto('file://'+hf);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const f=path.join(out,j.out);if(fs.existsSync(f)&&!process.argv.includes('--force'))continue;fs.mkdirSync(path.dirname(f),{recursive:true});await p.screenshot({path:f});}
await b.close();})();
