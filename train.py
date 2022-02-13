import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import SimpleRNN, Embedding, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM
import os
from sklearn.ensemble import RandomForestClassifier

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

#1 데이터 불러오기
trainData=pd.read_csv(r'C:\Users\clari\Desktop\bigdata\train.csv', encoding='utf-8')
x_data = trainData['text']
y_data = trainData['smishing']

#2 토큰화 및 패딩
tokenizer = Tokenizer()
tokenizer.fit_on_texts(x_data) #5572개의 행을 가진 X의 각 행에 토큰화를 수행
sequences = tokenizer.texts_to_sequences(x_data) #단어를 숫자값, 인덱스로 변환하여 저장
#print(sequences[:5])
word_to_index = tokenizer.word_index
#print(word_to_index)
vocab_size = len(word_to_index)+1
#print('단어 집합의 크기: {}'.format((vocab_size)))
x_data=sequences
max_len=max(len(l) for l in x_data)
x_data = pad_sequences(x_data, maxlen=max_len)

#3 데이터 전처리
features=x_data
target=y_data
features=features[100:,]
target=target[100:]

target=np.where((target==0), 0, 1)
weights={0: 0.05, 1: 0.95}
rf=RandomForestClassifier(n_estimators=100, random_state=0, class_weight=weights)
#각 클래스의 샘플 인덱스
class0=np.where(target==0)[0]
class1=np.where(target==1)[0]
#각 클래스의 샘플 개수
n_class0=len(class0)
n_class1=len(class1)
class0_downsampled=np.random.choice(class0, size=n_class1, replace=True)

x=np.vstack((features[class0_downsampled,:], features[class1,:]))
y=np.hstack((target[class0_downsampled], target[class1]))

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test  = train_test_split(x, y, test_size=0.2, random_state=0)
print(len(x_train))
print(len(x_test))

weight = {1: 0.94, 0: 0.06}
#4 네트워크
model = Sequential()
model.add(Embedding(vocab_size,32)) # 임베딩 벡터의 차원은 32
model.add(Dense(32, input_dim=32, activation='relu'))
model.add(LSTM(32)) # RNN 셀의 hidden_size는 32
 # RNN 셀의 hidden_size는 32
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(x_train, y_train, epochs=5, batch_size=512, validation_split=0.2, class_weight=weight)
model.save("TEST4.h5")

print("\n 테스트 정확도: %.6f" % (model.evaluate(x_test, y_test, batch_size=512))[1])

history_dict = history.history
loss = history_dict['loss']
val_loss = history_dict['val_loss']

print("\n\n")
epochs = range(1,len(loss)+1)
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

print("\n\n")
plt.clf() # 그래프 초기화
acc = history_dict['acc']
val_acc = history_dict['val_acc']
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label= 'validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()