# -*- coding: utf-8 -*-
"""Movie_Review.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ae6vbDl48MAbFZykhcbGQTRjwahNwQhf
"""

import nltk
nltk.download()

import pandas as pd
import numpy as np
from nltk.tokenize import RegexpTokenizer
from sklearn.preprocessing import LabelEncoder
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

tokenizer = RegexpTokenizer(r'\w+')
stopword = set(stopwords.words('english'))
ps = PorterStemmer()

df = pd.read_csv('/content/drive/My Drive/Moview Review/Train/Train.csv')
df1 = pd.read_csv('/content/drive/My Drive/Moview Review/Test/Test.csv')

df = df.values
df1 = df1.values

x = df[:,0]
y = df[:,1]
xt = df1.reshape(-1)

xt.shape

def getStemmedReview(review):
  review = review.lower()
  review = review.replace("<br /><br />", " ")
  tokens = tokenizer.tokenize(review)
  tokens = [token for token in tokens if token not in stopword]
  tokens = [ps.stem(token) for token in tokens]
  return ' '.join(tokens)

def getStemmedDocument(x):
  for i in range(x.shape[0]):
    x[i] = getStemmedReview(x[i])
  return x

x = getStemmedDocument(x)
xt = getStemmedDocument(xt)

cv = CountVectorizer()
x_vec = cv.fit_transform(x[:20000]).toarray()
xt_vec = cv.transform(xt).toarray()

mnb = MultinomialNB()

mnb.fit(x_vec,y[:20000])

res = mnb.predict(xt_vec)









