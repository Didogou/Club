"""Génère les codes cadeaux uniques (codes.csv) et les planches d'étiquettes A4 (etiquettes.html).
Étiquettes : format Avery L7160 / J8160 (21 par page, 63,5 × 38,1 mm, 3 colonnes × 7 rangées).
Usage : python3 codes.py 105   (nombre de codes, idéalement un multiple de 21)"""
import csv, os, secrets, sys, segno, io
N = int(sys.argv[1]) if len(sys.argv) > 1 else 105
ALPHA = 'ACDEFGHJKLMNPQRTUVWXY3479'   # sans 0/O, 1/I, 2/Z, 5/S, 6/B, 8 : pas de confusion à la lecture
URL = 'https://karine-dietetique.fr/cadeau?code='
seen = set()
if os.path.exists('codes.csv'):           # ne jamais régénérer un code déjà distribué
    seen = {r['code'] for r in csv.DictReader(open('codes.csv'))}
new = []
while len(new) < N:
    c = 'NOEL-' + ''.join(secrets.choice(ALPHA) for _ in range(4)) + '-' + ''.join(secrets.choice(ALPHA) for _ in range(4))
    if c not in seen: seen.add(c); new.append(c)
exists = os.path.exists('codes.csv')
with open('codes.csv', 'a', newline='') as f:
    w = csv.writer(f)
    if not exists: w.writerow(['code', 'url', 'statut', 'date_vente', 'date_activation'])
    for c in new: w.writerow([c, URL + c, 'non vendu', '', ''])
def qr(c):
    b = io.BytesIO(); segno.make(URL + c, error='m').save(b, kind='svg', scale=1, border=0, dark='#7a1f3d', xmldecl=False, svgns=True, omitsize=True); return b.getvalue().decode()
COLS, ROWS, W, H, LEFT, TOP, PX, PY = 3, 7, 63.5, 38.1, 7.2, 15.1, 66.0, 38.1
pages = [new[i:i + COLS * ROWS] for i in range(0, len(new), COLS * ROWS)]
html = ['''<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
@page{size:210mm 297mm;margin:0}
@font-face{font-family:Nunito;font-weight:800;src:url(a/nunito-latin-800-normal.woff2)}
@font-face{font-family:Nunito;font-weight:900;src:url(a/nunito-latin-900-normal.woff2)}
*{box-sizing:border-box;margin:0;padding:0}body{font-family:Nunito,sans-serif;color:#7a1f3d}
.p{position:relative;width:210mm;height:297mm;page-break-after:always;overflow:hidden}
.l{position:absolute;width:63.5mm;height:38.1mm;display:flex;align-items:center;gap:2.5mm;padding:0 3mm}
.l svg{width:26mm;height:26mm;flex:none}
.t{font-size:6pt;font-weight:800;line-height:1.35}.t b{display:block;font-size:8pt;font-weight:900;letter-spacing:0;margin:1mm 0;white-space:nowrap}
</style></head><body>''']
for pg in pages:
    html.append('<div class="p">')
    for k, c in enumerate(pg):
        x, y = LEFT + (k % COLS) * PX, TOP + (k // COLS) * PY
        html.append(f'<div class="l" style="left:{x}mm;top:{y}mm">{qr(c)}<div class="t">Votre code cadeau<b>{c}</b>karine-dietetique.fr<br>/cadeau</div></div>')
    html.append('</div>')
html.append('</body></html>')
open('etiquettes.html', 'w').write(''.join(html))
print(len(new), 'codes générés,', len(pages), 'page(s)')
