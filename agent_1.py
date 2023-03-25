import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

class Agent:

    def __init__(self, status):
        print('Agent init...')
        self.n_game = 0
        data_shape = (len(status))
        inputs = keras.Input(shape=data_shape, name='digits')
        x = layers.Dense(64, activation='tanh', name='dense_1')(inputs)
        y = layers.Dense(64, activation='tanh', name='dense_2')(x)
        outputs = layers.Dense(3, activation='softmax', name='predictions')(y)
        self.model = keras.Model(inputs=inputs, outputs=outputs)
        self.model.compile(optimizer='sgd', loss='mse')
#        self.model.summary()

    def move(self, status):
        q = np.reshape(status, newshape=(1,6))
        control = self.model.predict(q, verbose=0)
        return control

    def train(self, status_list, control_list, finish):
        if len(status_list)<3:
            return
        print('Training data...')
        # prepare data
        print('Before: ',control_list)
        if finish==1: # wall kick
            print(len(control_list))
            print(len(control_list[0][0]))
            for i in range(len(control_list)):
               q = np.argmax(control_list[i])
               control_list[i][0][q] -= 1/len(control_list[0][0])*i;
        elif finish==2: # apple eating
            for i in range(len(control_list)):
                q = np.argmax(control_list[i])
                control_list[i][0][q] += 10.0 / status_list[i][0][6];
        # train
        print('After: ',control_list)
        x = np.array(status_list, dtype='float32')
        y = np.array(control_list, dtype='float32')
        self.model.train_on_batch(x, y)

    def save_nn(self):
        self.model.save('my_nn.keras')
