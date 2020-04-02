'''crypto.py'''

import random
import os,sys
import numpy 

from PIL import Image
from flask import request
def power1(x,y,m):
	ans=1
	while(y>0):
		if(y%2==1):
			ans=(ans*x)%m
		y=y//2
		x=(x*x)%m
	return ans

def encrypt():
	jpgfile=Image.open(request.files['e_file'])
	print (jpgfile.bits, jpgfile.size, jpgfile.format)
	row,col = jpgfile.size
	pixels = jpgfile.load()

	row1 = 1000003
	phi = [0 for x1 in range(row1)]
	occ = [0 for x1 in range(row1)]
	primes = [] 
	phi[1] = 1
	#phi[2] = 1
	#print (phi)
	for i in range(2,1000001):
		#print (i)
		if(phi[i] == 0):
			phi[i] = i-1
			#print (i)
			primes.append(i)
			#j = 2*i
			for j in range (2*i,1000001,i):
				#print("j ",j)
				#print(j)
				if(occ[j] == 0):
					#print ("inside if2")
					occ[j] = 1
					phi[j] = j
					#print (phi[j])
					#print ((i-1)//i)
				phi[j] = (phi[j]*(i-1))//i
				#print(phi[j])
				#j = j + i
	#print (primes)
	p = primes[random.randrange(1,167)]
	q = primes[random.randrange(1,167)]
	print( p," ", q)
	n = p*q
	mod = n
	phin1 = phi[n]
	phin2 = phi[phin1]
	mod1 = phin1
	e = primes[random.randrange(1,9000)]
	d = power1(e,phin2-1,mod1)
	enc = [[0 for x in range(row)] for y in range(col)]
	for i in range(col):
		for j in range(row):
			r,g,b = pixels[j,i]
			r1 = power1(r+10,e,mod)
			g1 = power1(g+10,e,mod)
			b1 = power1(b+10,e,mod)
			enc[i][j] = [r1,g1,b1]
	print (pixels[row-1,col-1])
	img = numpy.array(enc,dtype = numpy.uint8)
	img1 = Image.fromarray(img,"RGB")
	#pixels2 = img1.load()
	img1.show()
	img1.save('oute.bmp')
	j = Image.open("oute.bmp")
	img = j.save("oute.jpg")
	print("Prime Numbers Used:",p,", ",q)
	print("d = ",d," e= ",e)
	return "oute.jpg"

