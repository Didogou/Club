const { chromium } = require('playwright-core');const path=require('path');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
const p=await b.newPage({viewport:{width:1075,height:720},deviceScaleFactor:2});
for(const s of ['recto','verso']){await p.goto('file://'+path.join(__dirname,'carte.html')+'?side='+s);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.screenshot({path:path.join(__dirname,s+'.png')});}
await b.close();})();
