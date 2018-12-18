def addin1():
	f = open('E:\\timeevents.txt', 'r', encoding='utf-8')
	fw = open('E:\\timeevents_news.txt', 'w', encoding='utf-8')
	fh = open('E:\\Code\\knowledge_graph\\my code\\important events_clean.txt', 'r', encoding='utf-8')
	i = 0
	news_dic = {}
	while True:
		new = fh.readline()
		if new == '':
			break
		if new == '\n':
			continue
		news_dic[i] = new
		i = i+1

	while True:
		lines = f.readline()
		w_lines = lines
		if lines == '':
			break
		if lines == '\n':
			continue
		lines = lines.strip().split('/')
		for ii in range(0,80):
			if lines[1] in news_dic[ii]:
				fw.write(str(ii)+'/'+lines[0]+'/'+lines[1]+'\n')

	f.close()
	fw.close()
	fh.close()

	
def addin2():
	f = open('E:\\Code\\knowledge_graph\\my code\\re data2.txt', 'r', encoding='utf-8')
	ft = open('E:\\re data3.txt', 'w', encoding='utf-8')
	fh = open('E:\\Code\\knowledge_graph\\my code\\important events_clean.txt', 'r', encoding='utf-8')
	i = 0
	news_dic = {}
	while True:
		new = fh.readline()
		if new == '':
			break
		if new == '\n':
			continue
		news_dic[i] = new
		i = i+1
	while True:
		text = ''
		lines = f.readline()
		if lines == '':
			break
		lines = lines.strip().split()
		line = lines[3]
		#print(line)
		for i in range(9,len(line)):
			text = text+line[i]
		#print(text)
		for ii in range(0,80):
			if text in news_dic[ii]:
				ft.write(str(ii)+' '+lines[0]+' '+lines[1]+' '+lines[2]+' '+lines[3]+'\n')
			
addin2()