#! /usr/bin/python
#! encoding: UTF-8
pi= 3.1415926535897931159979634685441852
def aproxpi(n):
  s = 0.0
  for i in range(1,n+1):
   x_i= float((i-0.5)/n)
   f_xi= float(4/(1+x_i**2))
   s = s + f_xi
  r = s / n 
  return r
if __name__ == "__main__":
  import sys
  if(len(sys.argv)==3):
     n=int(sys.argv[1])
     v=int(sys.argv[2])
  else:
    print "Debe introducir los dos parametros: el numero de intervalos que desea y el numero de veces que desea que se repita. Si no lo hace se hará con los valores por defectos n=10 y v=10"
    n=10
    v=10
 
  l=[ ]
  for i in range(1,v+1):
    x=aproxpi(n*i)
    l=l+[x]
    print x
  print l