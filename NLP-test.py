# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 16:37:35 2018

@author: Administrator
"""

import urllib.request
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

#段落tokenize成句子
from nltk.tokenize import sent_tokenize
#句子tokenize成单个词
from nltk.tokenize import word_tokenize

from nltk.corpus import wordnet

from nltk.stem import PorterStemmer

from nltk.stem import SnowballStemmer

from nltk.stem import WordNetLemmatizer

#nltk.download()

response = urllib.request.urlopen('http://www.huanqiu.com/www/2018/Sports_0326/11695128.html')
html = response.read()
#清洗文字
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
tokens = text.split()

word_tokens = list()
for token in tokens:
    word_tokens.extend(word_tokenize(token))


#清除停用词
clean_tokens = list()
sr = stopwords.words('english')
for token in word_tokens:
    if (not token in sr):
        clean_tokens.append(token)


#统计频率分布

freq = nltk.FreqDist(clean_tokens)

for key,val in freq.items():
    print (str(key) + ':' + str(val))

freq.plot(20, cumulative=False)


#同义词
"""
syn = wordnet.synsets("pain")
print(syn[0].definition())
print(syn[0].examples())
"""

#获取反义词
synonyms = []
for syn in wordnet.synsets('Computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

print(synonyms)

#获取反义词
antonyms = []
for syn in wordnet.synsets("small"):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(antonyms)

#波特词干提取算法
stemmer = PorterStemmer()
print(stemmer.stem('working'))
print(stemmer.stem('worked'))

#Lancaster词干算法

#非英文词干提取
print(SnowballStemmer.languages)

french_stemmer = SnowballStemmer('french')
print(french_stemmer.stem("French word"))


#单词变体还原（和词干类似，但结果可能会是一个同义词或同一个意思的不同单词）
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('increases'))
#得到动词：动词(v)、名词(n)、形容词(a)或副词(r)
print(lemmatizer.lemmatize('playing', pos="v"))

