from xml.etree.ElementTree import *
import random

root = Element('proj_info')

data_list = []
test_list = ['animation', 'fx']
enable_list = ['True', 'False']

for i in range(1, 51):
	project = Element('project')
	name = 'mini_%02d' % i
	type = test_list[random.randint(0, 1)]
	enable = enable_list[random.randint(0, 1)]

	project.set('name', name)
	project.set('type', type)
	project.set('enable', enable)

	root.append(project)

tree = ElementTree(root)
tree.write('D:/Documents/work/TWR/TD class/file_format/random.xml')