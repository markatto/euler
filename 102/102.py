#! /usr/bin/env python3

#TODO: could be simplified by not counting origin as a point

def group_points(points):
	'''group_points([1,2,3,4]) => [(1,2),(3,4)]'''
	pointgens = [iter(points)] * 2
	return [i for i in zip(*pointgens)]


def line(a,b):
	d_y = b[1] - a[1]
	d_x = b[0] - a[0]

	# can't divide by 0
	if d_x == 0:
		return lambda x: a[0]
	m = d_y / d_x
	y = a[1] - (m * a[0])
	#print('y = %s * x + %s' % (m,y))	
	return lambda x: m * x + y

def origin_in_tri(tri):
	for point in tri:
		# make a line with the two other points
		other_points = [i for i in tri if i is not point]
		l = line(*other_points)
		# find "good" side of line (side the unused point is on)
		is_gt = point[1] > l(point[0])
		# determine whether origin is on "good" side
		if (0 > l(0)) != is_gt:
			return False
	return True


#####################################################################3

with open('triangles.txt') as f:
	tris = f.readlines()

# pull out flat arrays of numbers
tris = ([int(n) for n in line.split(',')] for line in tris)

# group the numbers by into coordinate pairs (3 per triangle)
tris = [group_points(tri) for tri in tris]
print('%s total triangles' % len(tris))

# test all the triangles
good_tris = [tri for tri in tris if origin_in_tri(tri)]
print('%s triangles contain the origin' % len(good_tris))
