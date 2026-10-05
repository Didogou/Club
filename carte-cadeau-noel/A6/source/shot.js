// Rend les aperçus PNG (300 dpi) et les PDF prêts à imprimer
const { chromium } = require('playwright-core');const path=require('path');
const DPR=300/96;
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
const go=async(file,q,w,h,out)=>{const p=await b.newPage({viewport:{width:Math.round(w/25.4*96),height:Math.round(h/25.4*96)},deviceScaleFactor:DPR});
 await p.goto('file://'+path.join(__dirname,file)+q);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
 await p.screenshot({path:path.join(__dirname,'out',out+'.png')});
 await p.pdf({path:path.join(__dirname,'out',out+'.pdf'),width:w+'mm',height:h+'mm',printBackground:true,pageRanges:''});await p.close();};
await go('carte-a6.html','?side=recto',111,154,'carte-A6-recto');
await go('carte-a6.html','?side=verso',111,154,'carte-A6-verso');
await go('enveloppe-c6.html','',168,120,'enveloppe-C6');
const p=await b.newPage();await p.goto('file://'+path.join(__dirname,'etiquettes.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
await p.pdf({path:path.join(__dirname,'out','etiquettes-codes-A4.pdf'),width:'210mm',height:'297mm',printBackground:true});
await p.setViewportSize({width:794,height:1123});await p.screenshot({path:path.join(__dirname,'out','etiquettes-apercu.png')});
await b.close();})();
