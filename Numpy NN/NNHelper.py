import numpy as np

class Activation:
    def __init__(self):
        self.input = 0
        self.output = 0

    def __call__(self, x):
        """
        Outputs Activation Function
        
        :param x: Hidden State
        """

        self.input = x
        self.output = self.forward(x)
        return self.output

    def backward(self, grad):
        """
        Returns dZ
        
        :param grad: Loss function gradient.
        """
        return grad * self.derivative()
    
    def forward(self, x):
        raise NotImplementedError
    
    def derivative(self):
        raise NotImplementedError

class ReLU(Activation):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return np.maximum(0,x)
    
    def derivative(self):
        return np.where(self.input > 0, 1, 0)
        
class Sigmoid(Activation):
    def __init__(self):
        super().__init__()
    
    def forward(self, x):
        return 1/(1 + np.exp(-x))
    
    def derivative(self):
        return self.output  * (1 - self.output)

class tanh(Activation):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return np.tanh(x)
    
    def derivative(self):
        return 1 - self.output ** 2
    
class Loss:
    def __init__(self):
        """
        Initiates Loss Function. Calling the loss function returns loss, calling backward returns gradient.
        """
        pass

    def __call__(self, y_true, y_pred):
        raise NotImplementedError
    
    def backward(self, y_true, y_pred):
        raise NotImplementedError
    
class MSE(Loss):
    """
    Mean Squared-Error
    """
    def __init__(self):
        super().__init__()

    def __call__(self, y_true, y_pred):
        return np.mean((y_pred - y_true) ** 2)
    
    def backward(self, y_true, y_pred):
        return 2 * (y_pred - y_true)

class BCE(Loss): # Unfinished
    """
    Binary Cross-Entropy
    """
    def __init__(self):
        super().__init__()

    def __call__(self, y_true, y_pred):
        return -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    
    def backward(self, y_true, y_pred):
        return (y_pred - y_true)/(y_pred * (1 - y_pred))
    
class Optimizer:
    def __init__(self):
        raise NotImplementedError
    
    def step(self):
        raise NotImplementedError
    
class Momentum(Optimizer):
    def __init__(self, parameters, lr, momentum = 0.9):
        self.lr = lr
        
        self.parameters = parameters

        self.velocities = []

        # Gradients and Momenta
        for param in parameters:
            self.velocities.append(np.zeros_like(param[0]))
        
        self.momentum = momentum

    def step(self):
        for param, velocity in zip(self.parameters, self.velocities):
            unit = param[0]
            dunit = param[1]

            velocity[:] = self.momentum * velocity - self.lr * dunit
            unit += velocity

            dunit.fill(0)