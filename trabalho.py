from math import log10
from random import Random, random
import bisect

class event(object):
    
    def __init__(self, inp , time):
        self.inp = inp
        self.time = time
        
    def __gt__(self, o):
        return self.time > o.time
    
    def __eq__(self, o):
        return self.time == o.time
    
def lcg():
    anterior = 2000
    modulo = 2**31
    a = 65539
    c = 0
    while(True):
        num_aleatorio = (anterior * a + c) % modulo
        yield num_aleatorio/modulo
        anterior = num_aleatorio
    x0 = gerador_congruente(121, 100, x0)
    
def gerador_exponencial(x):
    return -1/x * log(1-(next(SEI_LA)))


def simulacao(e, s, f):
    tempo_s = 3600000
    t = 0
    N = 0
    Nc = 0
    Nc2 = 0
    Ns = 0
    eventos = []
    C = []
    S = []
    D = 0
    F = 0
    u = 0
    descarte = 0
    evento = event(True, 0)
    bisect.insort(eventos, evento)
    while(t < tempo_s):
        if(eventos[0].inp):
            F += (N*(eventos[0].time - t)) / tempo_s
            t = eventos[0].time
            Nc2 += 1
            if(N == 0):
                u += (eventos[0].time - t) / tempo_s
            if(N < f):
                N += 1
                Nc += 1
                C.append(t)
            else:
                descarte += 1
            evento = event(True, t + int(gerador_exponencial(e)))
            bisect.insort(eventos, evento)
            #if(N == 1):
            if(N < 5):
                evento = event(False, t + int(gerador_exponencial(s)))
                bisect.insort(eventos, evento)
            eventos = eventos[1:]
        else:
            if( N > 0):
                t = eventos[0].time
                N -= 1
                Ns += 1
                S.append(t)
                evento = event(False, t + int(gerador_exponencial(s)))
                bisect.insort(eventos, evento)
            eventos = eventos[1:]
    for i in range(len(S)-1):
        D += (S[i] - C[i])
    D = D / len(S)
    return (C, S, descarte/Nc2, F, D)

SEI_LA = lcg()
C, S, T_descarte, F, D = simulacao(1/90, 1/110, 15)