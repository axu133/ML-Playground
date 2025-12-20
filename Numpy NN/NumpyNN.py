import numpy as np
import NNHelper

class Model:
    def __init__(self, loss):
        self.layers = []
        self.loss = loss
    
    def add(self, layer):
        self.layers.append(layer)
    
    def forward(self, X):
        output = X
        for layer in self.layers:
            output = layer.forward(output)
        return output
    
    def backward(self, y_true, y_pred):
        grad = self.loss.backward(y_true, y_pred)
        for layer in reversed(self.layers):
            grad = layer.backward(grad)

    def update(self, lr, momentum=0.9): # Later replace w/ optimizer implementation
        for layer in self.layers:
            layer.update(lr, momentum)
    
    def predict(self, X): # Update for things such as binary classification etc.
        return self.forward(X)
    
    def parameters(self):
        parameters = {"weights": [], "bias": []}
        for layer in self.layers:
            layer_params = layer.get_params()
            parameters["weights"].append(layer_params[:2])
            parameters["bias"].append(layer_params[2:])
        return parameters

class DenseLayer:
    def __init__(self, in_dim: int, out_dim: int, activation: NNHelper.Activation):
        """
        Initializing Dense Layer in Neural Network
        
        :param in_dim: Input Dimension
        :param out_dim: Output Dimension
        :param activation: Activation Function (default: ReLU)
        """

        self.in_dim = in_dim
        self.out_dim = out_dim

        rng = np.random.default_rng()

        # Weights and Biases
        self.W = rng.normal(loc = 0.0, scale = 1.0, size = (in_dim, out_dim))*np.sqrt(2/in_dim) # He Initialization
        self.b = rng.normal(loc = 0.0, scale = 1.0, size = (1, out_dim))*0.01 
        
        self.dW = np.zeros_like(self.W)
        self.db = np.zeros_like(self.b)

        self.input = np.array(0)

        self.activation = activation

    def forward(self, x):
        """
        Forward Pass
        
        :param x: Input
        """
        self.input = x
        z = np.dot(x, self.W) + self.b
        a = self.activation(z)
        return a
    
    def backward(self, grad):
        """
        Backward Pass
        
        :param grad: Gradient of Loss Function
        :param derivative: Derivative of Activation Function (default: ReLU)
        """
        dZ = self.activation.backward(grad)
        self.dW = np.dot(self.input.T, dZ)
        self.db = np.sum(dZ, axis=0, keepdims=True)
        grad = np.dot(dZ, self.W.T)
        return grad
    
    def get_params(self):
        return [self.W, self.dW, self.b, self.db]

    def update(self, lr, momentum = 0):
        self.vW = momentum * self.vW - lr * self.dW
        self.vb = momentum * self.vb - lr * self.db
        self.W += self.vW
        self.b += self.vb

        self.dW.fill(0)
        self.db.fill(0)