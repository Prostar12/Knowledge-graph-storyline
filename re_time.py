import os
import sys
import re

def addtime():
	f = open('E:\\Code\\knowledge_graph\\my code\\re data.txt','r',encoding='utf-8')
	fw = open('E:\\re data2.txt','w',encoding='utf-8')
	news = 0
	pattern = '[0-9]'
	pattern1 = re.compile(pattern)
	while True:
		line = f.readline()
		news = news+1
		if line == '':
			break
		line = line.strip().split()
		try:
			time = 0
			for pos in range(len(line[2])):
				if line[2][pos] == '日':
					if pattern1.match(line[2][pos-1]):
						time = time+1
						if pattern1.match(line[2][pos-2]):
							#print(line[2][pos-1]+line[2][pos])
							fw.write(line[2][pos-2]+line[2][pos-1]+line[2][pos]+' '+line[0]+' '+line[1]+' '+line[2]+'\n')
						else:
							fw.write(line[2][pos-1]+line[2][pos]+' '+line[0]+' '+line[1]+' '+line[2]+'\n')
				if time > 0:
					break
		except:
			pass
		continue
	f.close()
	fw.close()
addtime()