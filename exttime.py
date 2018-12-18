import csv 
import codecs
import re
import pickle

#csvFile = codecs.open("chinese+maria.csv", 'rb', 'utf_8_sig')	
#reader = csv.reader(csvFile)
title = []
content = []
contents = []
text_clean = []
word_positionnums = []
date_double = {'1':'1st','2':'2nd','3':'3rd','4':'4th','5':'5th','6':'6th',
'7':'7th','8':'8th','9':'9th','10':'10th','11':'11th','12':'12th',
'13':'13th','14':'14h','15':'15th','16':'16th','17':'17th','18':'18th',
'19':'19th','20':'20th','21':'21th','22':'22th','23':'23th','24':'24th','25':'25th','26':'26th','27':'27th','28':'28th','29':'29th','30':'30th'}
#for line in reader:
	#title.append(line[0])
	#content.append(line[2])
	
def times():
	f = open('E:\\important events.txt', 'r', encoding='utf-8')
	while True:
		sens = f.readline()
		content.append(sens)
		if sens == '':
			break
	f.close()
	for news in content:
		news_clean = ''
		for word in news:
			if word != '\n' and word != '\u3000' and word != '\xa0':
				news_clean = news_clean+word
		text_clean.append(news_clean)
	date_event = {}
	time = []
	pattern = '[0-9]'
	pattern1 = re.compile(pattern)
	for con in text_clean:
		time_fen = []
		word_positionnum = []
		word_position = 0
		date_number = 0
		for word in con:
			ti = ''
			word_position += 1
			if word == '日':
				if pattern1.match(con[word_position-2]):
					date_number += 1
					#word_positionnum.append(word_position-1)
					if pattern1.match(con[word_position-3]):
						ti = con[word_position-3]+con[word_position-2]
						word_positionnum.append(word_position-3)
					else:
						ti = con[word_position-2]
						word_positionnum.append(word_position-2)
				if ti != '':
					time_fen.append(ti)
		word_positionnums.append(word_positionnum)
		time.append(time_fen)
	#print(word_positionnums)	
	for positions in range(len(word_positionnums)):
		#print(len(word_positionnums[positions])-1)
		for position in range(len(word_positionnums[positions])):
			text = ''
			texts = []
			if position == 0:
				if len(word_positionnums[positions]) != 1:
					for i in range(0,word_positionnums[positions][position+1]):
						text = text+text_clean[positions][i]
					texts.append(text)
				if len(word_positionnums[positions]) == 1:
					text = text+text_clean[positions]
				texts.append(text)
				#print('key'.dtype())
				date_event.setdefault(date_double[time[positions][position]],[]).append(texts)
			else:
				if position == len(word_positionnums[positions])-1:
					for i in range(word_positionnums[positions][position],len(text_clean[positions])-1):
						text = text+text_clean[positions][i]
					texts.append(text)
				if position != len(word_positionnums[positions])-1:
					for i in range(word_positionnums[positions][position],word_positionnums[positions][position+1]):
						text = text+text_clean[positions][i]
					texts.append(text)
				date_event.setdefault(date_double[time[positions][position]],[]).append(texts)
			
	#print(time)
	#print(date_event.keys())
	#print(word_positionnums)		
	#print(date_event)			
	fw = open('E:\\timeevents.txt', 'w', encoding='utf-8')
	for i in range(1,30,1):
		judge = str(i)+'th'
		if i == 1:
			judge = '1st'
		if i == 2:
			judge = '2nd'
		if i == 3:
			judge == '3rd'
		if judge in date_event:
			for texts in date_event[judge]:
				for text in texts:
					fw.write(judge+'/'+text+'\r\n')
	fw.close()
