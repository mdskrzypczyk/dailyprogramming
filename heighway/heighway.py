from sys import argv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def heighway(degree):
	points = [(0,0),(1,0),(1,1)]
	if degree == 0:
		return (0,0)

	for it in range(1,degree):
		rev_points = points[::-1]
		for pair in range(2**it):
			point1,point2 = rev_points[pair:pair+2]
			movement = (point2[1]-point1[1],point2[0]-point1[0])
			new_point = (points[-1][0]+ movement[0],points[-1][1]-movement[1])
			points.append(new_point)

	return points

fig = plt.figure()
ax = plt.axes(xlim=(-60,40), ylim=(-40,60))
line, = ax.plot([],[],lw=2)

degree = int(argv[1])
heighway_points = heighway(degree)

n=5
xvals = [pair[0] for pair in heighway_points]
yvals = [pair[1] for pair in heighway_points]
x = []
y = []

def init():
	line.set_data([],[])
	return line,

def animate(i):
	x.append(np.linspace(xvals[i],xvals[i+1],n))
	y.append(np.linspace(yvals[i],yvals[i+1],n))
	line.set_data(x,y)
	return line,

anim = animation.FuncAnimation(fig,animate,np.arange(0,len(heighway_points)-1),init_func=init,interval=10,blit=True,repeat=False)
plt.show()