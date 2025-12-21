import numpy as np
from NumpyNN import Model, DenseLayer
import NNHelper

sigmoid = lambda z: 1/(1 + np.exp(-z))

epochs = 100
lr = 0.1
tests = 100

x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0] , [1], [1], [0]])

model = Model(NNHelper.MSE())

model.add(DenseLayer(2, 8, activation = NNHelper.ReLU()))
model.add(DenseLayer(8, 1, activation = NNHelper.Sigmoid()))

optimizers = [["Momentum", NNHelper.Momentum(model.parameters(), lr=lr)], 
              ["RMSProp", NNHelper.RMSProp(model.parameters(), lr=lr)],
              ["Adam", NNHelper.Adam(model.parameters(), lr=lr)]]

preds = []

for name, optimizer in optimizers:
    losses = []
    for _ in range(tests):
        optimizer.lr = lr
        scheduler = NNHelper.StepLR(optimizer, 10, 0.1)
        for i in range(epochs):
            y_pred = model.forward(x)
            loss = model.loss(y, y_pred)
            model.backward(y, y_pred)
            optimizer.step()
            scheduler.step()
            # if i%10 == 0: print(f"Epoch: {i+1:2d} | Loss: {loss:.3f} | LR: {optimizer.lr}")
        losses.append(loss)
    print(f"{name}: ", np.mean(losses))