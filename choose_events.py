import csv
import codecs
import sys
import os
import jieba
import jieba.analyse
import pandas as pd
import math
from collections import Counter
import pickle
from numpy import *
import networkx as nx
import numpy as np
import copy
import matplotlib.pyplot as plt
from gensim import corpora, models, similarities
from gensim.models import word2vec 
from math import radians
from math import tan
from math import atan
from math import acos
from math import cos
from math import sin

def find_min(dic,k):      #返回k个最小的位置
    min_list=[]
    for j in range(k):
        minone=9999999999999
        for i in dic:
            if i[1] < minone:
                minone=i[1]
                minpos=i[0]
                mini=i
        min_list.append(minpos)
        dic.remove(mini)
    return min_list

def find_min_one(xlist):
    minx=99999
    for i in xlist:
        if i < minx:
            minx=i
    return minx

def find_max_one(xlist):
    maxx=-1
    for i in xlist:
        if i > maxx:
            maxx=i
    return maxx
def guiyihua(tar_list):
    max_one=find_max_one(tar_list)
    min_one=find_min_one(tar_list)
    new_list=[]
    for i in tar_list:
        new_list.append((i-min_one)/(max_one-min_one))
    return new_list
def final():
	print ("开始接邻矩阵生成")
	sim_array=[]
	csvFile = codecs.open("clear_up_2016_sina_尼伯特.csv", 'rb', 'gbk')	
	reader = csv.reader(csvFile)

	train_set1 = [] 
	ss = []
	for line in reader:
		ss.append(line[0])
		train_set1.append(ss)
		ss = []

	textcut = []
	for text1 in train_set1:
		for text2 in text1:
			text_cut = jieba.lcut(text2)
			textcut.append(text_cut)
	textcut.pop(0)		
	#print(textcut)
	stopwords = {}.fromkeys([ line.rstrip() for line in open('结巴词性停用表.txt') ])
	final = []
	for text1 in textcut:
		text = ''
		for text2 in text1:
			if text2 not in stopwords:
				if(text2 != '。'and text2 != '，'):
					text = text+' '+text2
		a=jieba.analyse.extract_tags(text, topK = 10, allowPOS = ())
		final.append(a)		
	#print(final)		

	train_set = []
	csvFile = codecs.open("E:\\Code\\knowledge_graph\\cuchuli\\clear_up_2015_sina_杜鹃.csv", 'rb', 'gbk')	
	reader = csv.reader(csvFile)
	ss = []
	for line in reader:
		ss.append(line[0])
		train_set.append(ss)
		ss = []

	csvFile = codecs.open("E:\\Code\\knowledge_graph\\cuchuli\\clear_up_2015_sina_灿鸿.csv", 'rb', 'gbk')	
	reader = csv.reader(csvFile)	
	for line in reader:
		ss.append(line[0])
		train_set.append(ss)
		ss = []
		
	csvFile = codecs.open("E:\\Code\\knowledge_graph\\cuchuli\\clear_up_2015_sina_苏迪罗.csv", 'rb', 'gbk')	
	reader = csv.reader(csvFile)	
	ss = []
	for line in reader:
		ss.append(line[0])
		train_set.append(ss)
		ss = []	

	csvFile = codecs.open("E:\\Code\\knowledge_graph\\cuchuli\\clear_up_2016_sina_海马.csv", 'rb', 'gbk')	
	reader = csv.reader(csvFile)	
	ss = []
	for line in reader:
		ss.append(line[0])
		train_set.append(ss)
		ss = []	

	csvFile = codecs.open("E:\\Code\\knowledge_graph\\cuchuli\\clear_up_2016_sina_莫兰蒂.csv", 'rb', 'gbk')	
	reader = csv.reader(csvFile)	
	ss = []
	for line in reader:
		ss.append(line[0])
		train_set.append(ss)
		ss = []	
		
	csvFile = codecs.open("E:\\Code\\knowledge_graph\\cuchuli\\clear_up_2016_sina_尼伯特.csv", 'rb', 'gbk')	
	reader = csv.reader(csvFile)	
	ss = []
	for line in reader:
		ss.append(line[0])
		train_set.append(ss)
		ss = []	
	textcut1 = []	
	for text1 in train_set:
		for text2 in text1:
			text_cut = jieba.lcut(text2)
			textcut1.append(text_cut)

	#print(textcut1)	
	model = word2vec.Word2Vec(textcut1,min_count=1,size=100)	
	print ("    keyword_list生成完毕")
	print ("    开始计算矩阵")
	lenx = 0
	for line in reader:
		lenx =lenx + 1  
		
	for i in range(272):
		line_list=[]
		#main_time=reader[i][2]
		for j in range(272):
			#print(i,j)
			if i==j:
				line_list.append(0.0000)
			else:
				#compare_time=reader[j][2]
				sim=model.n_similarity(final[i],final[j])
				threshold=0.87                #相似度阈值
				if (sim >= threshold):
					line_list.append(sim)
				else:
					line_list.append(0.0000)
		sim_array.append(line_list)
	#for i in sim_array:
	#    print (i)
	#print (sim_array)



	print("开始节点联通重要性计算")
	fi_list=[]
	ci_list=[]
	ei_list=[]
	gi_list=[]
	pi_list=[]               #最终结果
	Matrix = np.array(sim_array) #sim_array是接邻矩阵
	num_connect_list=[]
	spe_connect_list=[]
	for i in range(len(Matrix)):  #计算每个点的相邻点个数
		 connect_list=[]
		 for j in range(len(Matrix)): 
			  if (sim_array[i][j] != 0):
				  connect_list.append(j)
		 num_connect_list.append(len(connect_list))    
		 spe_connect_list.append(connect_list) 

	for i in range(len(Matrix)): #计算fi的个数
		 sumx=0
		 for j in range(len(Matrix)): 
			 if (sim_array[i][j] != 0):
				 sumx=sumx+num_connect_list[j]
		 sumx=sumx+num_connect_list[i]
		 fi_list.append(sumx)

	for i in range(len(Matrix)): #计算ei的个数
		 sumx=0
		 for j in range(len(spe_connect_list[i])):
			 for jj in range(j,len(spe_connect_list[i])):
				 x=spe_connect_list[i][j]
				 y=spe_connect_list[i][jj]
				 if (sim_array[x][y] != 0):
					 sumx=sumx+1
		 ei_list.append(sumx)

	for i in range(len(Matrix)): #计算ci的个数
		if (num_connect_list[i] > 1):
			ci=2*ei_list[i]/(num_connect_list[i]*(num_connect_list[i]-1))     
			ci_list.append(ci)
		else:
			ci=0
			ci_list.append(ci)
	fi_ci_list=[]
	for i in range(len(Matrix)): #计算ci/fi的个数   
		if(fi_list[i] == 0):
			fi_ci_list.append(0)
		else:
			fi_ci=ci_list[i]/fi_list[i]
			fi_ci_list.append(fi_ci)
		
	fi_ci_max=-1
	fi_ci_min=9999999999

	for i in fi_ci_list:          #计算ci/fimax,min
		if i <= fi_ci_min:
			fi_ci_min=i
		if i >= fi_ci_max:
			fi_ci_max=i    

	for i in range(len(Matrix)): #计算gi的个数          
		gi=(fi_ci_max-fi_ci_list[i])/(fi_ci_max-fi_ci_min)
		gi_list.append(gi)

	sumx=0
	for i in gi_list:            #计算gi归一化因子
		sumx=sumx+i*i
	gi_guiyi=math.sqrt(sumx)

	sumx=0
	for i in fi_list:            #计算fi归一化因子
		sumx=sumx+i*i
	fi_guiyi=math.sqrt(sumx)
		  
	for i in range(len(Matrix)): #计算pi的个数   
		pi=fi_list[i]/fi_guiyi-gi_list[i]/gi_guiyi 
		pi_list.append(pi) 
		
	guiyi_pi_list=guiyihua(pi_list)    #最终结果
	#for i in guiyi_pi_list:
	#    print(i)
	#print(len(guiyi_pi_list))



	max_important_pos=80   #取最重要的前n个点pos
	count=max_important_pos
	most_important_list_pos=[]
	while(count):
		maxx=-1
		for i in range(len(guiyi_pi_list)):
			if (guiyi_pi_list[i]>=maxx and i not in most_important_list_pos):
				pos=i
				maxx=guiyi_pi_list[i]
		most_important_list_pos.append(pos)
		count=count-1
	#print(most_important_list_pos)

	imp = []
	csvFile = codecs.open("clear_up_2016_sina_尼伯特.csv", 'rb', 'gbk')	
	reader = csv.reader(csvFile)
	for index,rows in enumerate(reader):
		for pos in most_important_list_pos:
			if index == pos:
				imp.append(rows[0])
	#print(imp)
	#print(len(imp))
	fw = open('E:\\important events.txt', 'w', encoding='utf-8')
	for text in imp:
		i += 1
		fw.write(text+'\r\n')
	S_list=most_important_list_pos