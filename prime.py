while True:
	try:
		b=input()
		
		b=int(b)
		break
	except:
		print("Invalid input");
		break
if b>1:
	for x in range(2,b):
		if b%x==0:
			print('no');
			break
		else:
			print('yes');
			break
else:
	print('no');
