MODELDIR="E:/installation/LTP/ltp_data"
import sys
import os
#from test_GRU import 
from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer
#from exttime import date_event
print("正在加载LTP模型... ...")

segmentor = Segmentor()
segmentor.load(os.path.join(MODELDIR, "cws.model"))

postagger = Postagger()
postagger.load(os.path.join(MODELDIR, "pos.model"))

parser = Parser()
parser.load(os.path.join(MODELDIR, "parser.model"))

recognizer = NamedEntityRecognizer()
recognizer.load(os.path.join(MODELDIR, "ner.model"))

print("加载模型完毕。")

def attribute():
	chufaci = ['伤','受伤','重伤','轻伤','死亡','伤亡','遇难','罹难','罹难','丧生','遇难','丧命','死','下落不明','失踪','找不到','受灾人口','受灾面积','受灾区域','经济损失','损失','供电','停电','农业损失','疏散','转移','安置','避难','移动','移动方向','速度','风力','阵风','大风','降雨量','雨量','降雨','致死']
	chufaci1 = ['强台风','超强台风','强热带风暴','热带风暴','热带低压']
	f = open('E:\\timeevents_news.txt', 'r', encoding='utf-8')
	fw = open('E:\\final_att.txt', 'w', encoding='utf-8')
	fh = open('E:\\att_events.txt', 'w', encoding='utf-8')
	position_list = []
	position_lists = []
	while True:
		#w_line = f.readline()
		lines = f.readline()
		w_line = lines
		if lines == '':
			break
		lines = lines.strip().split('/')
		ww = lines[0]
		www = lines[1]
		print(lines[2])
		lines = lines[2].strip().split('。')
		for line in lines:
			ff = 0
			flag = 0
			position = 0
			line = line.replace('　','')
			line = line.replace(' ','')
			line = line.replace('？','')
			words = segmentor.segment(line)
			postags = postagger.postag(words)
			#print(postags[20])
			#for p in postags:
				#print(p)
			for ci in chufaci1:
				for word in words:
					if ci == word:
						fw.write(ww+' '+www+' '+'台风等级'+' '+ci+' '+line+'\n')
			for ci in chufaci:
				position = 0
				for word in words:
					#print(word)
					position = position+1
					if ci == word:
						position_list.append(position)
						#print(position)
			for num in range(len(position_list)):
				try:
					#print(num)
					#print(len(position_list))
					if num < len(position_list)-1:
						if postags[position_list[num]-3] != 'm' and postags[position_list[num]-2] != 'm' and postags[position_list[num]-1] != 'm':
							for nums in range(position_list[num],position_list[num+1]):
								if postags[nums] == 'm':
									#print(words[nums]+words[nums+1])
									ff = ff+1
									if words[nums+1] != '～':
										fw.write(ww+' '+www+' '+words[position_list[num]-1]+' '+words[nums]+words[nums+1]+' '+line+'\n')
									else:
										fw.write(ww+' '+www+' '+words[position_list[num]-1]+' '+words[nums]+words[nums+1]+words[nums+2]+words[nums+3]+' '+line+'\n')
						else:
							for nums in range(position_list[num]-3,position_list[num]):
								if postags[nums] == 'm':
									ff = ff+1
									if words[nums+1] != '～':
										fw.write(ww+' '+www+' '+words[position_list[num]-1]+' '+words[nums]+words[nums+1]+' '+line+'\n')
									else:
										fw.write(ww+' '+www+' '+words[position_list[num]-1]+' '+words[nums]+words[nums+1]+words[nums+2]+words[nums+3]+' '+line+'\n')
					else:
						for nums in range(position_list[num],len(postags)):
							if postags[nums] == 'm':
								flag = flag+1
								ff = ff+1
								if words[nums+1] != '～':
									fw.write(ww+' '+www+' '+words[position_list[num]-1]+' '+words[nums]+words[nums+1]+' '+line+'\n')
								else:
									fw.write(ww+' '+www+' '+words[position_list[num]-1]+' '+words[nums]+words[nums+1]+words[nums+2]+words[nums+3]+' '+line+'\n')
							if flag > 0:
								break
				except:
					pass
				continue
			position_lists.append(position_list)
			position_list = []
			if ff > 0:
				fh.write(line+'\n')
	f.close()
	fw.close()
	fh.close()