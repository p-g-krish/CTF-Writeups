#!/usr/bin/env python3
from Crypto.Util.number import long_to_bytes
def cbrt(x):
    y, y1 = None, 2
    while y!=y1:
        y = y1
        y3 = y**3
        d = (2*y3+x)
        y1 = (y*(y3+2*x)+d//2)//d
    return y
c = 2205316413931134031046440767620541984801091216351222789180967130585669043554866325905770867150377611820746759815247778516899403229047066700396787852388511389893043279713280998235746440322483431305358901578692935378439077796777060321410661
print(long_to_bytes(cbrt(c)).decode('utf-8'))