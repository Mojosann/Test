# Christmas_tree version 5
# coding: utf8

value = input("請輸入樹的層數:")
value = int(value)

gan = input("請輸入樹幹高數:")
gan = int(gan)

for value in range(1, value+1):
    for i in range(5):
        print((5-i)*' '+'*'*(i+i+1))
for gan in range(gan):
    print((5*' '+'*'*1))
    
print('恩, 真是不錯的選擇')
