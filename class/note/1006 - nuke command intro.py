# [Nuke command intro]

import nuke

# 如果只選一個
# nuke.selectedNode()

# 先創建node
# 執行下一行
cont_list = nuke.selectedNodes() # nuke.selectedNode() # Last selected.
# 發現沒東西
# 執行cont_list得到結果

# 'name'的地方要放attr的名稱
# knob是attribute

# set與get要先確定它在不在
# {node}.knob('name').getValue()
# {node}.knob('name').setValue()
# {node}.knob({attr}).getValue() # 也可直接用value()
# {node}.knob({attr}).setValue()
# nuke.delete({node})

# nuke的knob近似於get
# {node}.['name'].setValue()

index = 1
for node in cont_list:
    old_name = node.knob('name').getValue()
    new_name = 'Color_' + str(index)

    index += 1
    #rename
    node.knob('name').setValue(new_name)
    
    #get value of color
    color_value = node.knob('color').getValue()
    print(color_value)

    #set value for color
    node.knob('color').setValue([0.0, 0.0, 0.0, 0.0])
    
    nuke.delete(node)

# 查找所有node的all attr
for knobs in nuke.selectedNode().knobs():
    print(knobs)