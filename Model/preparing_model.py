import numpy as np
import pandas as pd

import keras
from keras.layers import Convolution2D, MaxPooling2D, Activation, Dense, Flatten, Reshape
from keras.models import Sequential
from keras.utils import np_utils

ds = pd.read_csv('./symbols.csv')
data = ds.values
print data.shape

np.random.shuffle(data)

DICT = {}
# labels = ['+', 'c', '8', 'l', 't', 'q', '0', 'p', 'times', 'x', 'm', 'z',  '-', 'g', '5', 'k', 'pi', 'y', '4', 'f', ')', '3', 'j', 'w', '6', 'a', 'h', 'b', 'r', 'i', 'd', 'n', '9', 'v', '7', 'o', '2', 's', '(', 'forward_slash', 'e', 'u', '1']

labels = ['+', 'c', '8', 'l', 't', '0', 'x', '-', 'g', '5', 'h', '4', ')', '3', '6', 'a', 'i', 'n', '9', '7', '2', 's', '(', 'sum', 'e', '1', 'o']
labels.sort()
for ix in range(len(labels)):
    DICT[labels[ix]] = ix

for row in range(data.shape[0]):
	data[row][0] = DICT[str(data[row][0])]

split = int(0.9 * data.shape[0])
X_train = data[:split, 1:]/255.0
X_val = data[split:, 1:]/255.0

y_train = np_utils.to_categorical(data[:split, 0])
y_val = np_utils.to_categorical(data[split:, 0])

X_train = X_train.reshape((split, 32, 32, 1))
X_val = X_val.reshape((data.shape[0]-split, 32, 32, 1))

print X_train.shape, y_train.shape
print X_val.shape, y_val.shape

model = Sequential()

model.add(Convolution2D(32, (5, 5), input_shape=(32, 32, 1)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Activation('relu'))

model.add(Convolution2D(16, (3, 3)))
model.add(Activation('relu'))
model.add(Convolution2D(8, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Activation('relu'))

model.add(Flatten())
model.add(Dense(len(labels)))
model.add(Activation('softmax'))

model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

hist = model.fit(X_train, y_train, epochs = 25, shuffle=True, batch_size = 80, validation_data = (X_val, y_val))

#model_json = model.to_json()
#with open("model.json", "w") as json_file:
#    json_file.write(model_json)
#model.save_weights("model.h5")
model.save("model_all.h5")

print("Saved model to disk")
