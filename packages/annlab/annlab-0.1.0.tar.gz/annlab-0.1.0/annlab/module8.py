def prog8():
    print('''
import numpy as np

# Simple RNN parameters
input_size = 3
hidden_size = 5
output_size = 2
seq_length = 4

# Random data
X = np.random.randn(seq_length, input_size)
y = np.random.randint(0, output_size, size=(1,))

# Initialize weights and biases
Wh = np.random.randn(hidden_size, hidden_size)
Wx = np.random.randn(input_size, hidden_size)
Wy = np.random.randn(hidden_size, output_size)
bh = np.zeros((1, hidden_size))
by = np.zeros((1, output_size))

# Forward pass
h = np.zeros((1, hidden_size))
for t in range(seq_length):
    h = np.tanh(X[t].dot(Wx) + h.dot(Wh) + bh)  # RNN step
output = h.dot(Wy) + by  # Output layer
pred = np.argmax(output, axis=1)

print(f"Predicted class: {pred}, Actual class: {y}")''')