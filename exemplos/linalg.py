from FGAme import *
from smallvectors import Mat
from math import *
Mat = Mat[2, 2, float]

L = []
for i in range(20):
	for j in range(20):
		x = 10 * i
		y = 10 * j
		circle = draw.Circle(
			5, pos=pos.middle + (x, y), 
		    color=(10 * j, 0, 10 * i)
	    )
		world.add(circle)
		L.append(circle)
		
M1 = Mat([1, 2], 
		 [2, 5])
vals, vecs = M1.eig()
l1, l2 = vals
v1, v2 = vecs

x, y = v1
Pr1 = Mat([x*x, x*y], [x*y, y*y])

x, y = v2
Pr2 = Mat([x*x, x*y], [x*y, y*y])

M1 = 1.5 * Pr1 + 0.75 * Pr2
M2 = (1.5)**(1/60) * Pr1 + (0.75)**(1/60) * Pr2
print(M1)


@listen('key-down', 'up', args=[M1])
@listen('key-down', 'down', args=[M1.inv()])
def T1(M):
	for circle in L:
		circle.pos = M * (circle.pos - pos.middle) + pos.middle		

@listen('long-press', 'right', args=[M2])
@listen('long-press', 'left', args=[M2.inv()])
def T2(M):
	for circle in L:
		circle.pos = M * (circle.pos - pos.middle) + pos.middle		


M3 = Mat([cos(pi/30), -sin(pi/30)],
         [sin(pi/30),  cos(pi/30)])

@listen('long-press', 'a', args=[M3])
@listen('long-press', 'd', args=[M3.inv()])
def T2(M):
	for circle in L:
		r0 = (500, 400)
		b = - M * r0 + r0
		circle.pos = M * circle.pos + b
		#circle.pos = M * circle.pos

run()




