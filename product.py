import os
products = []
if os.path.isfile('product.csv'):
	print('找到檔案！')
	#讀取檔案
	with open('product.csv' , 'r' , encoding='utf-8')as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products)

else :
	print('沒找到檔案！')




#使用者輸入
products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q' :
		break
	price = input('請輸入商品價格')
	products.append([name,price])
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0],'的價格是',p[1])

#寫入檔案
with open('product.csv', 'w',encoding='utf-8') as f:
	for p in products:
		f.write(p[0]+','+p[1]+'\n')