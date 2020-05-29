import string
fr= open("dlltry.txt",'r',encoding='utf-16')
fw=open('dll1.txt','w')
for line in fr:
	sr=line.split(' ')
	for i in sr:
		if i!='':
			if i[0] in string.ascii_uppercase+string.ascii_lowercase+'@':
				fw.write(i+'\n')
fr.close()
fw.close()