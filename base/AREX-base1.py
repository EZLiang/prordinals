# The base of AREX_phi_w_0.py
# Takes an ARE string and gives a generator of the ARE strings in its fs
# Somewhat golfed
def a(x):
  if x=="":return
  if x[-1]==")":yield a(x[1:-1]);return
  if x[-1]=="A":yield x[:-1];return
  p=0;c="";d=""
  y=list(x)
  while True:
    h=y.pop(-2)
    c+=h
    p+=1 if h==")" else -1 if h=="(" else 0
    if p==0:break
  if x[-1]=="R":
    c=c[1:-1]
    if y[-2]==")":
      while True:
        h=y.pop(-2)
        d+=h
        p+=1 if h==")" else -1 if h=="(" else 0
        if p==0:break
    else:
      d="("+c+")"
    y="".join(y[:-1])
    while True:yield y+d;d="("+d+")"+c
  y="".join(y[:-1])
  d=c[1:-1]
  e=c
  while True:yield y+d;d=e+d
