# [xml module intro]

import xml.etree.ElementTree as ET

# read file
tree = ET.parse('D:/Documents/work/TWR/TD class/file_format/test.xml')
root = tree.getroot()

for child in root:
	print(child.tag)
	print(child.attrib) #dict
	print(child.text)

# write file
root = ET.Element('proj_info')
project = ET.Element('project')
project.set('name', 'P1')

root.append(project)

tree = ET.ElementTree(root)
tree.write('D:/Documents/work/TWR/TD class/file_format/my_test.xml')

'''
data_dict = {

	'Apocalypse_Now':{
		'width':1280,
		'height':920,
		'fps':25,
		'maya_version':2021,
		'renderer':'v-ray'
		},
	'Dune':{
		'width':1080,
		'height':720,
		'fps':50,
		'maya_version':2020,
		'renderer':'mantra'
		}
	}

root = ET.Element('proj_info')
for proj_name in data_dict.keys():
	proj = ET.Element(proj_name)
	info = ET.SubElement(proj, 'info')
	for key, value in data_dict[proj_name].items():
		info.set(key, str(value))

	root.append(proj)
tree = ET.ElementTree(root)
tree.write('D:/Documents/work/TWR/TD class/file_format/my_test.xml')
'''

# XPath for xml
# ET.fromstring(xml_data_string)
# please see the pic!
root = ET.parse('C:/Users/Academy/Desktop/coding/file_format/vgpuconfig.xml')

root.findall('.') # choose first layer's children
root.findall('vgpuType') # choose all vgpuType
root.findall('./vgpuType') # choose first layer's children is vgpuType