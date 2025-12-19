import numpy as np
from NumpyNN import Model, DenseLayer

lossfn = lambda y_true, y_pred: np.average((y_pred - y_true)**2) # MSE
lossfn_derivative = lambda y_true, y_pred: 2 * (y_pred - y_true)
sigmoid = lambda z: 1/(1 + np.exp(-z))

epochs = 1000
lr = 0.01

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0] , [1], [1], [0]])

model = Model(lossfn, lossfn_derivative)

model.add(DenseLayer(2, 8))
model.add(DenseLayer(8, 1, activation = sigmoid, derivative = lambda Z: sigmoid(Z) * (1 - sigmoid(Z))))

preds = []

for i in range(epochs):
    y_pred = model.forward(x)
    loss = model.loss(y, y_pred)
    model.backward(y, y_pred)
    model.update(lr, 0.9)
    print(f"Epoch: {i+1:3d} | Loss: {loss:.3f}")