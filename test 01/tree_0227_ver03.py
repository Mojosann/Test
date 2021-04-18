# Christmas_tree version 3

v = input("請輸入樹的層數:")
v = int(v)

g = input("請輸入樹幹長度:")
g = int(g)
for i in range(4):
    print((5-i)*' '+'*'*(i+i+1))
        
for v in range(1, v):
    for i in range(4):
        print((4-i)*' '+'*'*(i+i+3))
    
for g in range(g):
    print((5*' '+'*'*1))
    
print('恩, 真是不錯的選擇')
