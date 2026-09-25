import sys,glob
from multiprocessing import Pool
from PIL import Image
from blacken import fix
def one(f): fix(Image.open(f)).save(f,quality=90)
if __name__=='__main__':
    fs=[f for d in sys.argv[1:] for f in sorted(glob.glob(d+'/*.jpg'))]
    with Pool(8) as p: p.map(one,fs,chunksize=16)
    print(len(fs))
