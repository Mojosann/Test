# [Maya cmds intro]

import maya.cmds as cmds

# create 10 boxes
sl_list = cmds.ls(sl=True)

# adjust tx, sy
cont = 0
for order in range(len(sl_list)):
# TD說直接寫in list就好！
    order_tx = sl_list[order]+'.translateX'
    order_sy = sl_list[order]+'.scaleY'
    print(order_tx, order+cont)
    cmds.setAttr(order_tx, order+cont)
    cmds.setAttr(order_sy, order)
    cont += 5

list_a = [1, 2, 3, 4, 5]
# print index and item
for i in list_a:
    print(list_a[i], i)

import random
# number = random.randint(1, 10)
sl_list = cmds.ls(sl=True)

cont = 0
number = 0
for order in sl_list:
    order_tx = order + '.translateX'
    ordet_ty = order + '.translateY'
    order_tz = order + '.translateZ'
    # print(order_tx, cont)
    cmds.setAttr(order_tx, cont)
    cont += 1
    cmds.setAttr(order_ty, number)
    cmds.setAttr(order_tz, 0)
    number = random.randint(1, 10)

# make layout boxes
sl_list = cmds.ls(sl=True)
order_list = []
for i in range(10):
    for j in range(10):
        order_list.append([i, 0, j])

for i in sl_list, order_list:
    cmds.move(…)

# other method
cmds.group([item for item in selected_list], n='cubegroup_1')

cont = 1
for i in range(1, 11):
    cmds.duplicate('cubegroup' + str(i), rr=True)
    cmds.move(0, 0, cont, 'cubegroup_' + str(i))
    cont += 1