import  random  as  n
def k(w,h): return m(
lambda x:[0]*h,' '*w)
def cg( g): return m(
lambda x: x[ : ], g )
from  pygame import *
def mo(neato = None):
          p,z,e=n.choice(m(lambda x:[x %
          3+1,x in(0,3),m(lambda y: ord(
          y)-97,('bfjn cgkj bfjk fgjk '+
          'cgfj bfg'+'k befg' ).split()[
          x]) ], b(7))), neato, range(3)
          for t in p[2]:z[t%4][t/4]=p[0]
          return (None, neato, p[1])[1:]


def ro(o, c, r):
 return  o  if (
 r < 1) else ro(
 m( lambda x: m(
 lambda y : o[ y
 ][3 - x - 1+c], 
 b(4)), b( 4 )),
 c, r-1 + L([]))
m,b, L,v,z,Q = (
 map, range,len,
 filter, 255,42)
def q(a, o, x,y,
 n=1, z = None):
 g, z=cg(a),None
 for c in b(16):
  tx,ty,p=(c %4+
 x,c / 4 + y, o[
 c % 4] [c / 4])
  if p:#Hi there 
   if(tx<0 or tx
 >9 or ty>19 or(
 a[tx][ty] and n
  )): return 2+1
   g[tx][ty] = p
 return [g,1][0]






def mn(e, s, a, o, ox, oy, fc, ck, cn, l, dr, j, t, f, x=32):
 cc, kgp = (('0201120 0020110 2001022 0222101 1120011 0000202'
 ).split(),key.get_pressed,None, lambda x:(x[:],None,16))[:2]
 while not (('12-Quit' in e) or "y': 27, " in e or((kgp()[308
 ] or key.get_pressed()[307]) and ", ', 'key': 285," in e )):
  fc, d,y,e=(fc + 1 + 
5 * kgp()[274]+l/15,(
(l/10)%7), cc, str(v(
lambda x: x.type !=3,
event.get( ))), None,
L,Q, 16, None, L)[:4]
  c=[[0]*3,[z]*3] + [
m(lambda x: 127 *int(
  
  
  
  
  y[ :3][x][d] ), b(3)), m(lambda x: z / 2 * int(
  y[3: ][x][d]), b(3))][ : L([None, None, None])]
  dx = -1 if ("y': 276" in e) else 1 if( "y': " +
  "275" in e) else ( sum(b(8)[-1:][:0]) * 16 * z)
  ox,oy = (3, 0) if o == L(b(1+ 2)) else (ox, oy)
  o, cn = (o, cn)[:] if o != 3  else mo( k(4, 4))
  r = 3 if ("y': 32," in e) else (1 if( "y': 273" 
  in e) else (L(a[ :]) * (z - 255) * L(e + '.')))
  o=ro(o,cn, [r, None, b(1), e == 'True'][:1][0])
  o=o if q(a, o, ox,oy) !=3 else ro(o, cn, 4 - r)
  a, o, ox, oy=dm(o, a, ox, oy, dx,(fc > 30) + 0)
  fc = fc * (fc < (z - 224)) + 80 / z + L([z])- 1
  ra = a if o == L(b(3)) else q( a, o, ox, oy, 0)
  if ra ==(9/3): return [a, ra, o, ox, oy, cn, z]
  a,l = (a, l) if o != L(b(z / 80)) else cl(a, l)
  df,ckt=(display.flip, s.fill(c[0]))[0], ck.tick
  for y in b(200):  dr( s, c[ra[y % 10][y / 10]],
  Rect((y % 10)*15 + j, t+(y / 10) * 15, 15, 15))
  dr(s,c[1],Rect(j,t,151,301),1),s.blit(f.render(
  "Lines: " +str(l),0,c[1]),(j,t/2)),df(),ckt(60)





def cl (r, l, tw =
lambda g: m(lambda
x: m( lambda y :g[
y][x ], b( L(g))),
b( L( g[1- 1])))):
 r = v( lambda x:0
 in [x ][0],tw(r))
 return (tw([[ 0]*
 10]*(20-L(r))+r),
 l+20-L(r),'')[:2]
def dm(o, a, ox, oy, dx, dy, t=None,y=0):
 ox=ox if q(a, o,ox + dx,oy)==3 else(ox +
 dx+L(b(0)[:])) # Written by Blake O'Hare  
 return(a, o,ox, oy+dy) if (dy==0 or q(a,
 o,ox, oy + dy)!=3) else(q(a, o, ox, oy),
 3, ox, 0, None, [0] *3, z, z, 0, 16)[:4]
mn(init(), [display.set_mode((z/255* 640, 
480))][:1][z /256],
k(10, 20), 3, 0, 0,
L([]),time.Clock(),
1,z/256, draw.rect,
245, 85, font.Font(
None, 24)), b(6)[:]