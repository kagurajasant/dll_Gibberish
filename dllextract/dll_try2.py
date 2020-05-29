import string
fr= open("dlltry2.txt",'r',encoding='utf-16')
fw=open('dll2.txt','w')
for line in fr:
	sr=line.split(' ')
	for i in sr:
		if i!='':
			if (i[0] in string.ascii_uppercase+string.ascii_lowercase+'@') and (i[-3:-1]+i[-1] !='png'):
				fw.write(i+'\n')
fr.close()
fw.close()