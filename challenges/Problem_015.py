# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

# this is a cartesion pathing problem.
# A 20 x 20 grid will have 21 nodes

# we are trying to get from [0,0] to [20,20]: looks like a list...
# But here's a hypothesis: the number of steps required for any given journey is the same
# So that zig-zagging across the middle is the same number of paces as along the perimeter which is 40.

# The method of movement should dictate if the path has been explored.
# if its a for loop, then go down then out, starting at 0.

# This is stupid. Because its recursive. or needs to be. Nested the number of times that there are rows.
# Also, I only need to calculate for one axis: then double for the other axis.
# the paths will be mirrored across the line x=y


# in grid sized n:
# for x0 in range(n)
# 	for y0 in range(n)
# 		for x1 in range(x0 to n)
# 			for y1 in range(y0 to n)
# 				...
# 				for xn in range(xn-1 to n)
# 					for yn in range(yn-1 to n)
# 						Test Location


# grid = []

# def recurseLoop(nest): # where nest is the number of loops we need
# 	depth = 0
# 	counter = 0
# 	while depth <= nest:
# 		print "Starting the loop"
# 		for e in range(depth, nest+1):
# 			print "here's e: " + str(e)
# 			for i in range(depth, nest+1):
# 				print "Here's i: " + str(i)
# 				depth += 1
# 				print "now I'm recursing"
# 				recurseLoop(nest-depth)
# 				if [e,i] == [nest, nest]:
# 					counter += 1
# 				print "here's the count: " + str(counter)
# 	return counter

# def findPath(n): # where n and m are dimensions of grid
# 	pathCount = 0
# 	# for row in range(n+1):
# 	# 	for column in range(n+1):
# 	pathCount = recurseLoop(n)
# 	return pathCount

# print findPath(2)

# here's Recursive that works.... but it takes all day!

# import time
 
 
# gridSize = [15,15]
 
# def recPath(gridSize):
#     """
#     Recursive solution to grid problem. Input is a list of x,y moves remaining.
#     """
#     # base case, no moves left
#     if gridSize == [0,0]: return 1
#     # recursive calls
#     paths = 0
#     # move left when possible
#     if gridSize[0] > 0:
#         paths += recPath([gridSize[0]-1,gridSize[1]])
#     # move down when possible
#     if gridSize[1] > 0:
#         paths += recPath([gridSize[0],gridSize[1]-1])
 
#     return paths
 
# start = time.time()
# result = recPath(gridSize)
# elapsed = time.time() - start
 
# print "result %s found in %s seconds" % (result, elapsed)

import time

# this thing is only good for square grids.
# we'd have to initialize a 2d list or array to have unequal sides.

def route_num(cube_size):
    L = [1] * cube_size # Initialize a list of length cube_size. notice this is one row, not 2D.
    for i in range(cube_size): # along one axis, do this for each point.
        for j in range(i): # at each point, do this along the other axis.
            L[j] = L[j]+L[j-1] # here's the magic: each node's path count is equal to the sum of its upper and left-hand neighbors'.
        L[i] = 2 * L[i - 1] # and here we simulate a second dimension, and make our list the pathcount of all the diagonals.
    return L[cube_size - 1] # hmmmmmmm... why minus 1?
 
start = time.time()
n = route_num(20)
elapsed = (time.time() - start)
print "%s found in %s seconds" % (n,elapsed)