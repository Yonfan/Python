# -*- coding: utf-8 -*-
import math 

def quadratic(a,b,c):
	t = b*b - 4*a*c
	if t < 0:
		print('该方程无解！')
	elif t == 0:
		x = -b/(2*a) 
		print('方程有唯一解：\n')
		print('x = %d' %x )
	else:
		x1 = (-b + math.sqrt(t))/(2*a)
		x2 = (-b - math.sqrt(t))/(2*a)
		print('方程有二个解：\n')
		print(x1, x2)
