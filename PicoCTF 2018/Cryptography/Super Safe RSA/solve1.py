#!/usr/bin/env python2
from Crypto.Util.number import long_to_bytes
from gmpy import invert
c = 6837189899983702670428948967404672144182024179748934035078246961445770135586208
n = 17006056418709353211281561147312266487529504798342794694573614778052921315875503
e = 65537
#https://www.alpertron.com.ar/ECM.HTM
p = 164949888113147768186945114397360146119
q = 103098320424709887353200858431580624798937
d = invert(e,(p-1)*(q-1))
print(long_to_bytes(pow(c,d,n)))