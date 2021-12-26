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
        tag, _, sticker = line.split()

        X.append([int(i) / 10 for i in tag])
        y.append([sticker])

# sc = StandardScaler()
# X = sc.fit_transform(X)

X = np.array(X)

print(X)

ohe = OneHotEncoder()
y = ohe.fit_transform(y).toarray()

print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

model = Sequential()
model.add(Dense(len(X[0]), input_dim=len(X[0]), activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(len(y[0]), activation="softmax"))

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

pred = model.predict([[4/10, 5/10, 5/10, 7/10]])
cats = ohe.categories_

for k, v in enumerate(pred[0]):
    print(f"{cats[0][k]}: {v}")

print("most likely:", cats[0][np.argmax(pred[0])])