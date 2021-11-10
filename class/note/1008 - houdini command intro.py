# [Houdini command intro]

import hou 

# hou.selectedNodes()
# {node}.setName()
# {node}.parm({attr}).eval()
# {node}.parm({attr}).set()
# {node}.destory()

node_list = hou.selectedNodes()

number = 1
for node in node_list:

    print(node)

    new_name = 'ball_' + str(number)
    print(new_name)

    node.setName(new_name)
    number += 1


for node in node_list:
    
    # Get attribute
    tx = node.parm('tx').eval()
    print(node)
    print(tx)

    # Set attribute
    node.parm('tx').set(0)
    node.parm('ty').set(10)
    node.parm('tz').set(10)
    
    # destroy
    node.destory()