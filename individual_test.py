from tensorflow.keras.models import load_model
import flask
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import layers
from tensorflow.keras.layers import SimpleRNN, Embedding, Dense
from tensorflow.keras.models import Sequential
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

#trainData=pd.read_csv('trainDataMod.csv', encoding='utf-8')
#testData=pd.read_csv(r'C:\bigdata\public_test.csv', encoding='utf-8')

#for i in range(295945):
#    if trainData['smishing'][i] == 1:
#        print(trainData['text'][i])


#x_data = trainData['text']
#str로 테스트할 문자열 입력받음
def function(str1):
    str=[str1]
    tokenizer = Tokenizer()
#    tokenizer.fit_on_texts(x_data) #5572개의 행을 가진 X의 각 행에 토큰화를 수행
#sequences = tokenizer.texts_to_sequences(x_data) #단어를 숫자값, 인덱스로 변환하여 저장
#print(sequences[:5])
#word_to_index = tokenizer.word_index

#입력받은 str을 인덱스로 변환하는 과정
    seq=tokenizer.texts_to_sequences(str)

#인덱스로 변환한 seq의 데이터 형식을 train할 때와 동일하게 맞춤
    x_pre = pad_sequences(seq, maxlen=317)
#훈련 뒤 저장된 model을 불러오는 과정
    model = tf.keras.models.load_model('modelModify.h5')
#불러온 model을 통해 스팸 여부를 판단하는 과정
    result=model.predict_classes(x_pre)
#print(result)
    if result[0][0] == 1:
        str2="스미싱"
    else:
        str2="정상"
    return str2
