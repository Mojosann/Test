import maya.cmds as cmds

# default cube : height, width, depth = (1, 1, 1)
def make_trunk(trunk_layer):

	# build trunk and get trunk height
	trunk_list = []
	for trunk in range(trunk_layer):
		trunk_list.append(cmds.polyCube(n='Trunk_%s' % str(int(trunk+1))))
		cmds.setAttr( 'Trunk_%s.translateY' % str(int(trunk+1)), trunk+0.5 )
	
		# 0.5: YMAX of cube
		# +1: the start height of tree layer
		height = trunk+0.5 +1
	
	# get trunk name
	trunk_name_list = []
	# trunk_name: user's define name
	# cube: maya's define name
	for trunk_name, cube in trunk_list:
		trunk_name_list.append(trunk_name)

	# group trunk
	cmds.group([trunk_name for trunk_name in trunk_name_list], n='Trunk_Grp')

	return height


# put root to get coordinate list
def get_moving_list(root, height):
	
	y = float(height)
	
	# set square's coordinate range

	# root = odd situation: 
	# rules: 3: (1, 0, -1); 5: (2, 1, 0, -1, 2); 7:(3, 2, 1, 0, -1, -2, -3)...
	# root_max = (n-1)/2, root_min = -(n-1)/2
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
	# root_max = n/2, root_min = -((n/2)-1)
	elif root % 2 == 0:

		root_max = (int(root/2), int(root/2))
		root_min = (-(int(root/2)-1), -(int(root/2)-1))

		# get total coordinate(2D) list
		moving_list = []
		for x in range(root_min[0], root_max[0]+1):
			for z in range(root_min[1], root_max[1]+1):
				moving_list.append([x-.5, y, z-.5])
		
	return moving_list


# get square layer
def make_square_layer(root, height):

	# get total cube
	layer_no = root * root
	
	# make square's unit cube and get cube_list
	cube_list = []
	for no in range(1, layer_no+1):
		cube_list.append(cmds.polyCube( n='Cube_%s_%s' % (root, str(no))))

	# get cube name list
	cube_name_list = []
	# cube_name: user's define name
	# leave: maya's define name
	for cube_name, leave in cube_list:
		cube_name_list.append(cube_name)

	# group cube_name
	group_name = cmds.group([cube_name for cube_name in cube_name_list], n='Square_layer_%s' % root)
	#print group_name
	
	# get x, y, z moving list
	moving_list = get_moving_list(root, height)
	
	# put cube_list in moving_list
	for i in range(len(moving_list)):
		moving_list[i].append(cube_list[i])
	
	# let cube move to the coordinate
	for x, y, z, cube_name in moving_list:
		#print (cube_name[0])
		#print '|%s|%s'%(group_name, cube_name[0])
		cmds.move( x, y, z, '|%s|%s'%(group_name, cube_name[0]) )

	return group_name


# make tree layer
def make_tree_layer(query_tree_layer, trunk_height):

	cmds.group(em=True, n='Tree_Grp')
	
	for query_tree_layer in range(query_tree_layer):		
		tree_layer_grp = cmds.group(em=True, n='Tree_layer_%s' % int(query_tree_layer+1))
		cmds.parent(tree_layer_grp, 'Tree_Grp')
		
		tree_layer_list = [i for i in range(1, 7)][::-1]	
		for layer in tree_layer_list:
			cmds.parent( make_square_layer(layer, trunk_height), 'Tree_layer_%s' % int(query_tree_layer+1) )
			trunk_height += 1



def create_tree(num):
	for num in range(1, num+1):
		cmds.group(em=True, n='Tree_%s' % num)


create_tree(5)
make_tree_layer(5, make_trunk(15))