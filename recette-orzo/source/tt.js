// Variante TikTok (?tt=décalage) : vidéo cuisine en grand carré 1080×1080, sans la fiche appli en bas
(()=>{const q=new URLSearchParams(location.search);if(!q.has('tt'))return;
const OFF=+q.get('tt')||180;
const st=document.createElement('style');st.textContent=`
#sk>.abs.center{top:170px!important}
#sk .kit{top:290px;height:1080px}
#sk .kit>img{width:1440px!important;height:1080px!important;margin-left:${-OFF}px}
.app,.hint,.list{display:none!important}
#sk>.cap{top:1405px;bottom:auto;left:40px;right:40px}
#sk>.cap .tx{font-size:50px}
#sk>.cap img{width:104px;height:104px}`;
document.head.appendChild(st);
if(document.querySelector('.list')){const d=document.createElement('div');d.style.cssText='position:absolute;left:0;width:1080px;text-align:center;top:1405px;font-weight:900;font-size:50px';d.innerHTML='🍽 Pour <span style="color:var(--rose)">4 personnes</span> · ⏱ 17 min';document.getElementById('sk').appendChild(d);const nt=document.getElementById('nt');nt.style.left='640px';nt.style.top='1110px';}
const cap=document.getElementById('cap');if(cap)document.getElementById('sk').appendChild(cap);
})();
// Sans la fiche appli à l'écran, on retire « Et coche l'étape ! » des bulles
(()=>{if(!new URLSearchParams(location.search).has('tt')||typeof S==='undefined')return;
S.forEach(g=>g.cap&&g.cap.forEach(c=>{c[1]=c[1].replace(/ ?(⏱ )?Et coche[^!]*!/,' ⏱');}));})();
