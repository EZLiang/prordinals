s="h=lambda z,n=0:((n and(s+'\\nz=%r\\n'%z+i%(n-1)))or(s+'\\nprint %r'%z));i='while 1:\\n print z\\n z=h(z,%i)';s='s=%r;exec(s)'%s";exec(s)
z=""
while 1:
 print(z)
 z=h(s+"\nz=%r\n"%z+i%2)