import numpy as np

# Random 5x5 input and 3x3 kernel
X = np.random.randn(5, 5)
W = np.random.randn(3, 3)

# Convolution operation (without padding, stride = 1)
conv_out = np.array([[np.sum(X[i:i+3, j:j+3] * W) for j in range(3)] for i in range(3)])

# ReLU activation
relu_out = np.maximum(0, conv_out)

# Max pooling (2x2)
pool_out = np.max(relu_out[:2, :2])

print("Convolution Output:\n", conv_out)
print("ReLU Output:\n", relu_out)
print("Max Pooling Output:", pool_out)
