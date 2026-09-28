// node renderTT.js page.html off outdir [full|t1,t2,...]
const { chromium } = require('playwright-core');const fs=require('fs'),path=require('path');
const [page0,off,out,mode='preview']=process.argv.slice(2);const FPS=30;
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.join(__dirname,page0));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const dur=await p.evaluate(()=>window.DURATION);const dir=path.join(__dirname,out);fs.rmSync(dir,{recursive:true,force:true});fs.mkdirSync(dir);
const times=mode==='full'?Array.from({length:Math.round(dur*FPS)},(_,i)=>i/FPS):mode.split(',').map(Number);
for(let i=0;i<times.length;i++){await p.evaluate(async t=>{window.seek(t);if(window.ready)await window.ready();},times[i]);
await p.screenshot({path:path.join(dir,mode==='full'?String(i).padStart(5,'0')+'.jpg':`t${times[i]}.jpg`),type:'jpeg',quality:93});}
await b.close();console.log('done',times.length);})();
