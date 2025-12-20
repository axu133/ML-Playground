import numpy as np
from NumpyNN import Model, DenseLayer
import NNHelper

sigmoid = lambda z: 1/(1 + np.exp(-z))

epochs = 1000
lr = 0.01
momentum = 0

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0] , [1], [1], [0]])

model = Model(NNHelper.MSE())

model.add(DenseLayer(2, 8, activation = NNHelper.ReLU()))
model.add(DenseLayer(8, 1, activation = NNHelper.Sigmoid()))

optimizer = NNHelper.Momentum(model.parameters(), lr=lr, momentum=momentum)

preds = []

for i in range(epochs):
    y_pred = model.forward(x)
    loss = model.loss(y, y_pred)
    model.backward(y, y_pred)
    optimizer.step()
    print(f"Epoch: {i+1:4d} | Loss: {loss:.3f}")