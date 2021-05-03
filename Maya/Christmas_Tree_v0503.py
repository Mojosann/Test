# 發現沒有辦法一邊複製一邊移動到我想要的位置，所以我想先複製一堆(第一個loop), 並且同時創建座標位置的清單(在一個loop)
# 再把這兩個loop combine起來
# 座標位置的清單：限制停在n*n 如果要依照規律性分開討論 還要再整合清單

'''
1 (0, 0) v
2 (0, 1) v
3 (1, 1) v
4 (1, 0)
5 (1, -1) v
6 (0, -1)
7 (-1, -1) v
8 (-1, 0)
9 (-1, 1)
10 (-1, 2) v
11 (0, 2)
12 (1, 2)
13 (2, 2) v
14 (2, 1)
15 (2, 0)
16 (2, -1)
17 (2, -2) v
18 (1, -2)
19 (0, -2)
20 (-1, -2)
21 (-2, -2) v
22 (-2, -1)
23 (-2, 0)
24 (-2, 1)
25 (-2, 2)
26 (-2, 3) v
...

31 (3, 3)
36 (3, -3) v

'''

import maya.cmds as cmds

# def + input = ?
def make_trunk(trunk_layer):

	# get trunk value
	for trunk in range(trunk_layer):
	    cmds.polyCube( n="Trunk_%s" % str(int(trunk+1)))
	    cmds.setAttr( 'Trunk_%s.translateY' %str(int(trunk+1)), trunk+0.5 )
	    height = trunk+0.5+1 # +1 means the start height of tree layer
	    
	return height


# put root to get coordinate list
def get_moving_list(root, height):
	
	y = float(height)
	
	# set square's coordinate range

	# root = odd situation: 
	# rules: 3: (1, 0, -1); 5: (2, 1, 0, -1, 2); 7:(3, 2, 1, 0, -1, -2, -3)...
	# n_max = (n-1)/2, n_min = -(n-1)/2
	if root % 2 == 1:
		
		root_max = ((int(root-1)/2), (int(root-1)/2))
		root_min = (-(int(root-1)/2), -(int(root-1)/2))

		# get total coordinate(2D) list
		moving_list = []
		for x in range(root_min[0], root_max[0]+1):
			for z in range(root_min[1], root_max[1]+1):
				moving_list.append([x, y, z])

	# root = even situation: 
	# rules: 2*2: (1, 1), (0, 0); 4*4: (2, 2), (-1, -1); 6*6: (3, 3), (-2, -2)...
	# n_max = n/2, n_min = -((n/2)-1)
	elif root % 2 == 0:

		root_max = (int(root/2), int(root/2))
		root_min = (-(int(root/2)-1), -(int(root/2)-1))

		# get total coordinate(2D) list
		moving_list = []
		for x in range(root_min[0], root_max[0]+1):
			for z in range(root_min[1], root_max[1]+1):
				moving_list.append([x-.5, y, z-.5])
		
	return moving_list


# get odd square layer
def make_square_layer(root, height):

	# get total cube
	layer_no = root * root
	
	# make cube and get cube list
	cube_name_list = []
	for no in range(1, layer_no+1):
		cube_name_list.append(cmds.polyCube( n="Cube_%s_%s" % (root, str(no))))
		#cmds.setAttr( 'Cube_%s.translateY' %str(int(num)), 0.5 )
	
	# get x, y, z moving order
	moving_list = get_moving_list(root, height)
	
	# put cube_list in moving_list
	for i in range(len(moving_list)):
		moving_list[i].append(cube_name_list[i])
		
	for x, y, z, cube_name in moving_list:
		cmds.move( x, y, z, cube_name )


query = input('Enter trunk height: ')
height = make_trunk(query)

tree_layer_list = [i for i in range(query+1)][::-1]
for layer in tree_layer_list:
	make_square_layer(layer, height)
	height += 1