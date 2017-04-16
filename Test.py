#coding='utf-8'
import re
from collections import Counter
import csv
from nltk.corpus import stopwords
from nltk import pos_tag
from numpy import character
import json
from numpy.core.defchararray import lower
def question_one():
    c = Counter()   #统计单词出现的次数
    with open('exam1_capital.txt','r') as f:#打开文件
        for line in f.readlines():
            if line =='\n':#如果没有内容，不作处理
                continue
            
            words = re.findall('\w*',line)#正则表达式匹配字母和数字，过滤掉标点，空格和换行符
            c.update(words)#统计line中单词的个数，有新的单词次数为1，已经出现过的单词在原有的基础上加上line中出现的次数
            
    csvfile = open('question_one.csv','wb+')#输出文件
    w = csv.writer(csvfile)
    for item in c.items():
        w.writerow(item)#按行写入
    csvfile.close()
def question_two():
    c = Counter()
    english_stopwords = stopwords.words('english')#停用词
    #print english_stopwords
    with open('exam1_capital.txt','r') as f:
        for line in f.readlines():
            if line =='\n':#如果没有内容，不作处理
                continue
            
            words = re.findall('\w*',line)#正则表达式匹配字母和数字，过滤掉标点，空格和换行符
            words = [word.lower() for word in words if word !='']#对单词取小写并去掉空字符
            words = [word for word in words if word not in english_stopwords]#去掉停用词
            words = [word for word in words if word.isdigit() == False]#去掉数字字符
            
            c.update(words)#统计line中单词的个数，有新的单词次数为1，已经出现过的单词在原有的基础上加上line中出现的次数
    c = sorted(c.items(),key = lambda k :k[1])#按照次数对字典排序
    csvfile = open('question_two.csv','wb+')
    w = csv.writer(csvfile)
    for item in c:
        w.writerow(item)#按行写入
    csvfile.close()
def question_three():
    c = Counter()
    with open('exam1_capital.txt','r') as f:
        for line in f.readlines():
            if line =='\n':#如果没有内容，不作处理
                continue
            
            words = re.findall('\w*',line)#正则表达式匹配字母和数字，过滤掉标点，空格和换行符
            words = [word for word in words if word !='']#去掉空字符
            c.update(words)#统计line中单词的个数，有新的单词次数为1，已经出现过的单词在原有的基础上加上line中出现的次数
    fp = open('question_three.json','w+')
    for item in c.items():
         property = pos_tag([item[0]])[0]#获得词性
         property = [property[0],property[1],item[1]]#（单词，词性，词频）
         fp.write(json.dumps(property)+'\n')#写入json文件
    fp.close()
         
         
        
    
    
question_one()
question_two()
question_three()