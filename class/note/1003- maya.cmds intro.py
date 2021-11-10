# [Maya cmds intro]

import maya.cmds as cmds

#列出所選出來的東西
# sl = selection
selected_list = cmds.ls(sl=True)

# 不排序的話會依照選取順序印出來
for i in sorted(selected_list):
    print(i)

cont = 1
for item in sorted(selected_list):
    target_name = 'box_geo_00%s' % cont
    #print(target_name)
    cont += 1
    cmds.rename(item, target_name)

# 重新再選一次new name list
selected_list = cmds.ls(sl= True)
for item in sorted(selected_list):
    #get translateX attract
    attr = item + '.translateX'
    attr_data = cmds.getAttr(attr)
    print(attr_data)

# setAttr
selected_list = cmds.ls(sl=True)
for item in sorted(selected_list):
    #get translateX attr
    attr = item + '.translateX'
    attr_data = 10
    cmds.setAttr(attr, attr_data)
    print(cmds.getAttr(attr))

# delete
selected_list = cmds.ls(sl=True)
for item in sorted(selected_list):
    cmds.delete(item)

# 可以直接刪清單
selected_list = cmds.ls(sl=True)
cmds.delete(selected_list)

# 把球排成一列
# 現在場景製造10顆球

import maya.cmds as cmds
selected_list = cmds.ls(sl=True)

cont = 0
for order in range(len(selected_list)):
    print(selected_list[order]+'.translateX', order+cont)
    cmds.setAttr(selected_list[order]+'.translateX', order+cont)

# testing 
list_a = [1, 2, 3, 4, 5]
for i in range(len(list_a)):
    print(list_a[i], i)