import string
fr= open("dlltry3.txt",'r',encoding='ISO-8859-1')
fw=open('dll3.txt','w')
for line in fr:
	sr=line.split(' ')
	# for i in sr:
	# 	if i!='':
	# 		if (i[-3:-1]+i[-1] =='dll'):
	fw.write(sr[-1]+'\n')		
fr.close()
fw.close()