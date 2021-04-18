# Christmas_tree version 2

v = input("請輸入樹的層數:")
v = int(v)

for v in range(1, v+1):
    for i in range(5):
        print((5-i)*' '+'*'*(i+i+1))
for g in range(5):
    print((5*' '+'*'*1))
    
print('恩, 真是不錯的選擇')
