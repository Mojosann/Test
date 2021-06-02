# ver.solve the problem let tree_layer decay / growing by trunk height
import maya.cmds as cmds
 

def default_tree(*args):
		
	# check to see if model exists
	if cmds.objExists('Tree_main'):
		cmds.delete('Tree_main')
				
	# set default tree_model
	tree  = make_tree_layer()
	trunk = make_trunk(value=7)	
		
	# adjust Tree_Grp's ty value 
	cmds.setAttr('Tree_Grp.translateY', 7.5)

	# group tree layer and trunk
	cmds.group(em=True, n='Tree_main')
	cmds.parent(tree,trunk, 'Tree_main')


def make_trunk(value):
	
	# check to see if model exists
	if cmds.objExists('Trunk_Grp'):
		cmds.delete('Trunk_Grp')

	# build trunk and get trunk height
	trunk_list = []
	for trunk in range(value):
		trunk_list.append(cmds.polyCube(n='Trunk_%s' % str(int(trunk+1))))
		cmds.setAttr( 'Trunk_%s.translateY' % str(int(trunk+1)), trunk+0.5 )
			
	# get trunk name
	trunk_name_list = []
	# trunk_name: user's define name
	# cube: maya's define name
	for trunk_name, cube in trunk_list:
		trunk_name_list.append(trunk_name)
	
	# group trunk
	trunk_Grp = cmds.group([trunk_name for trunk_name in trunk_name_list], n='Trunk_Grp')
	height = value +.5
	
	return trunk_Grp


def adjust_trunk(value):
	
	# check to see if model exists
	if cmds.objExists('Trunk_Grp'):
		cmds.delete('Trunk_Grp')

	# build trunk and get trunk height
	trunk_list = []
	for trunk in range(value):
		trunk_list.append(cmds.polyCube(n='Trunk_%s' % str(int(trunk+1))))
		cmds.setAttr( 'Trunk_%s.translateY' % str(int(trunk+1)), trunk+0.5 )
			
	# get trunk name
	trunk_name_list = []
	# trunk_name: user's define name
	# cube: maya's define name
	for trunk_name, cube in trunk_list:
		trunk_name_list.append(trunk_name)
	
	# group trunk
	trunk_Grp = cmds.group([trunk_name for trunk_name in trunk_name_list], n='Trunk_Grp')
	height = value +.5
	
	# because Tree_Grp.ty exists change height
	cmds.setAttr('Tree_Grp.translateY', height)
	cmds.parent(trunk_Grp, 'Tree_main')
	
	return height


def make_tree_layer(value=3, trunk_height=0):
	
	# check to see if model exists
	if cmds.objExists('Tree_Grp'):
		cmds.delete('Tree_Grp')
		
	# set tree Grp
	tree_Grp = cmds.group(em=True, n='Tree_Grp')
	
	# decide how many layer of tree and group
	for value in range(value):		
		tree_layer_grp = cmds.group(em=True, n='Tree_layer_%s' % int(value+1))
		cmds.parent(tree_layer_grp, 'Tree_Grp')
			
		# set squares of each layer and group
		tree_layer_list = [i for i in range(1, 7)][::-1]	
		for layer in tree_layer_list:
			cmds.parent(make_square_layer(layer, trunk_height), 'Tree_layer_%s' % int(value+1) )
			trunk_height += 1
	
	return tree_Grp


def adjust_tree_layer(value, trunk_height=0):
	
	# check to see if model exists
	if cmds.objExists('Tree_Grp'):
		cmds.delete('Tree_Grp')
		
	# set tree Grp
	tree_Grp = cmds.group(em=True, n='Tree_Grp')
	
	# decide how many layer of tree and group
	for value in range(value):		
		tree_layer_grp = cmds.group(em=True, n='Tree_layer_%s' % int(value+1))
		cmds.parent(tree_layer_grp, 'Tree_Grp')
			
		# set squares of each layer and group
		
		tree_layer_list = [i for i in range(1, 7)][::-1]	
		for layer in tree_layer_list:
			cmds.parent(make_square_layer(layer, trunk_height), 'Tree_layer_%s' % int(value+1) )
			trunk_height += 1
	
	# because Tree_Grp.ty exists change height
	cmds.setAttr('Tree_Grp.translateY', adjust_trunk(cmds.intSliderGrp(switch_trunk, query = True, value = True)))
	cmds.parent(tree_Grp, 'Tree_main')
	

def get_moving_list(root, height):
		
	y = float(height)
		
	# set square's coordinate range: put root to get coordinate list

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
		
	# get x, y, z moving list
	moving_list = get_moving_list(root, height)

	# group cube_name
	group_name = cmds.group([cube_name for cube_name in cube_name_list], n='Square_layer_%s' % root)

	# put cube_list in moving_list
	for i in range(len(moving_list)):
		moving_list[i].append(cube_list[i])
		
	# let cube move to the coordinate
	for x, y, z, cube_name in moving_list:
		#print (cube_name[0])
		#print '|%s|%s'%(group_name, cube_name[0])
		cmds.move( x, y, z, '|%s|%s'% (group_name, cube_name[0]) )
		
	return group_name


# create new window
my_win = cmds.window('Creat tree viz', widthHeight=(400, 160))

# deesign title / button position
cmds.columnLayout(adjustableColumn=True)
cmds.separator(height=20, width=100)
cmds.text('Creat tree viz')

# set reset button and connect default_tree()
cmds.separator(height=20, width=100)
reset_tree = cmds.button(label='Default / Reset', command=default_tree)

# set tree_layer slider 
cmds.separator(height=20, width=100)
switch_layer = cmds.intSliderGrp(field=True, label='Tree layer  ', minValue=1, maxValue=10, value=1, changeCommand=adjust_tree_layer)

# set trunk_height slider
cmds.separator(height=20, width=100)
switch_trunk = cmds.intSliderGrp(field=True, label='Trunk height  ', minValue=1, maxValue=10, value=1, dragCommand=adjust_trunk)

# display window
cmds.showWindow(my_win)