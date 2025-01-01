import numpy as np

X = np.array([[2, 9], [1, 5], [3, 6]], dtype=float)
X = X / np.amax(X, axis=0)
y = np.array([[92], [86], [89]], dtype=float) / 100

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.W1 = np.random.randn(input_size, hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_prime(self, x):
        return x * (1 - x)

    def forward(self, X):
        self.z1 = np.dot(X, self.W1)
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2)
        return self.sigmoid(self.z2)

    def backward(self, X, y, output):
        output_error = y - output
        output_delta = output_error * self.sigmoid_prime(output)
        hidden_error = output_delta.dot(self.W2.T)
        hidden_delta = hidden_error * self.sigmoid_prime(self.a1)
        self.W1 += X.T.dot(hidden_delta)
        self.W2 += self.a1.T.dot(output_delta)

    def train(self, X, y):
        output = self.forward(X)
        self.backward(X, y, output)

NN = NeuralNetwork(input_size=2, hidden_size=3, output_size=1)
for i in range(1000):
    output = NN.forward(X)
    loss = np.mean(np.square(y - output))
    print(f"Input:\n{X}\nActual Output:\n{y}\nPredicted Output:\n{output}\nLoss: {loss}")
    NN.train(X, y)
