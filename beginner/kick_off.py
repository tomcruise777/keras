from keras.models import Sequential
from keras.layers import Dense, Activation

# 可以通过向Sequential模型传递一个layer的list来构造该模型
model = Sequential([
Dense(32, units=784),
Activation('relu'),
Dense(10),
Activation('softmax'),
])

# 也可以通过.add()方法一个个的将layer加入模型中
model = Sequential()
model.add(Dense(32, input_shape=(784,)))
model.add(Activation('relu'))