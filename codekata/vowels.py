y=raw_input()
b=y.isalpha()
if len(y)==1:
	if b==True:
			if y in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
				print('Vowel');
			else:
				print('Consonant');
else:
	print('invalid');		
