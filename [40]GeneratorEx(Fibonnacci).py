# coding:utf8

def fibonacci():

	a=1
	b=1

	yield a #` ilk olarak yield seklinde uretiyoruz
	yield b

	# ` Ve benden istendigi surece bu fibo serisini devam ettirecegim

	while True:
		
		a,b=b,a+b
		
		yield b # ` Yeni sayimiz b olacagi icin bu b yi donduruyoruz 

for i in fibonacci():

		#` Ancak bu for dongusunun bir sure sonra durmasi gerektigi icin

	if i > 1000000000000000000000000000000000000000000000000000000000000000000000000:
		break
	print(i)

