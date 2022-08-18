from collections import namedtuple

def doppelgangerEnigma():
    LENGTH_UNITS= namedtuple('LENGTH_UNITS', ['pc', 'AU', 'km','mm','µm','nm'])
    length = LENGTH_UNITS(pc=3.08567758149137e16, AU=149597870700, km= 10**3,mm=10**-3 ,µm= 10**-6,nm= 10**-9)        
    EM_LABELS = namedtuple('EM_LABELS', ['A','V','Ω','W'])
    em = EM_LABELS(A='current',V='voltage',Ω='resistance',W='power')

    return [length,em]