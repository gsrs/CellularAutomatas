################################################################################
# conway.py
#
# Author: electronut.in
# 
# Description:
#
# A simple Python/matplotlib implementation of Conway's Game of Life.
################################################################################

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import random
import math

N = 100
ON = 255
OFF = 0
vals = [ON, OFF]

def rule(tupla):
    
    if tupla in tuplas:
      return ON
    else:
      return OFF

def update(data):
  global grid
  # copy grid since we require 8 neighbors for calculation
  # and we go line by line 
  newGrid = grid.copy()
  for i in range(1,N-1):
    for j in range(1,N-1):
      # compute 8-neghbor sum 
      # using toroidal boundary conditions - x and y wrap around 
      # so that the simulaton takes place on a toroidal surface.

      newGrid[i,j] = rule((grid[i-1,j-1],grid[i-1,j],grid[i-1,j+1],grid[i,j+1],grid[i+1,j+1],grid[i+1,j],grid[i+1,j-1],grid[i,j-1]))

  # update data
  mat.set_data(newGrid)
  grid = newGrid
  return [mat]

def toTupla(n):
  tupla = []
  n = "{0:b}".format(n).zfill(8)
  for c in n:
    if c == "0":
      tupla.append(OFF)
    else:
      tupla.append(ON)
  return tuple(tupla)

def toNumber(tupla):
  n = ''
  for t in tupla:
    if t == ON:
      n += "1"
    else:
      n += "0"
  return int(n,2)

def generate(n):
  tuplas = []
  i = 0
  for c in n[::-1]:
    if c == "1":
      tuplas.append(toTupla(i))
    i+=1

  return tuplas

for primo in [538,626,6362]:
  # populate grid with random on/off - more off than on
  grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

  index = "{0:b}".format(primo).zfill(256)
  tuplas = generate(index)
  print(index)
  print(tuplas)

  # set up animation
  fig, ax = plt.subplots()
  mat = ax.matshow(grid)
  ani = animation.FuncAnimation(fig, update, interval=50,
                                save_count=50)
  plt.show()

'''
n=0

while(True):

  grid = np.zeros((N,N))
  for j in range(N):
    grid[int(N/2),j] = random.choice([ON,OFF])

  index = "{0:b}".format(n).zfill(256)
  tuplas = generate(index)
  print(index)
  print(tuplas)

  # set up animation
  fig, ax = plt.subplots()
  mat = ax.matshow(grid)
  ani = animation.FuncAnimation(fig, update, interval=50,
                                save_count=50)
  plt.show()

  base = input("base")
  potencia = input("potencia")
  n += int(math.pow(int(base),int(potencia)))
'''