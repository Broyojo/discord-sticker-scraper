import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from keras.layers import Dense
from keras.models import Sequential
import keras
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

X = []
y = []

with open("data.txt", "r") as f:
    for line in f.readlines():
        tag, sticker = line.split()
        X.append([int(tag[0]), int(tag[1]), int(tag[2]), int(tag[3])])
        y.append([sticker])

sc = StandardScaler()
X = sc.fit_transform(X)

print(X)

ohe = OneHotEncoder()
print(y[0])
y = ohe.fit_transform(y).toarray()
print(y)

print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

model = Sequential()
model.add(Dense(4, input_dim=4, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(4, activation="softmax"))

model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

history = model.fit(X_train, y_train, validation_data=(
    X_test, y_test), epochs=100, batch_size=64)

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

print(model.predict([[6,9,4,2]]))
