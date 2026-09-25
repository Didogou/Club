const { chromium } = require('playwright-core');
const fs = require('fs');
const path = require('path');

const mode = process.argv[2] || 'preview2'; // preview | full
const FPS = 30;

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.join(__dirname, 'etape2.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const dur = await page.evaluate(() => window.DURATION);
  const dir = path.join(__dirname, mode === 'full' ? 'frames2' : 'preview2');
  fs.rmSync(dir, { recursive: true, force: true });
  fs.mkdirSync(dir);
  const times = mode === 'full'
    ? Array.from({ length: Math.round(dur * FPS) }, (_, i) => i / FPS)
    : (process.argv[3] || '1,2.5,3.8,5,6.5,8.5,10,12,13.7,15,16.5,18.3,20,22.5').split(',').map(Number);
  for (let i = 0; i < times.length; i++) {
    await page.evaluate(async t => { window.seek(t); if (window.ready) await window.ready(); }, times[i]);
    const name = mode === 'full' ? String(i).padStart(5, '0') + '.jpg' : `t${times[i]}.jpg`;
    await page.screenshot({ path: path.join(dir, name), type: 'jpeg', quality: 93 });
  }
  await browser.close();
  console.log('done', times.length);
})();
