def prog10():
    print('''
import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # Sigmoid function

# GRU parameters (random initialization)
input_size = 3  # Size of input vector
hidden_size = 2  # Size of hidden state

# Define the input and previous hidden state
X = np.array([0.5, -0.2, 0.1])  # Example input vector (3-dimensional)
h_prev = np.array([0.0, 0.0])   # Initial hidden state (2-dimensional)

# Random weights and biases
Wz = np.random.randn(input_size, hidden_size)  # Update gate weights
Wr = np.random.randn(input_size, hidden_size)  # Reset gate weights
Wh = np.random.randn(input_size, hidden_size)  # Candidate hidden state weights
Uz = np.random.randn(hidden_size, hidden_size)  # Update gate recurrent weights
Ur = np.random.randn(hidden_size, hidden_size)  # Reset gate recurrent weights
Uh = np.random.randn(hidden_size, hidden_size)  # Candidate hidden state recurrent weights
bz = np.zeros(hidden_size)  # Bias for update gate
br = np.zeros(hidden_size)  # Bias for reset gate
bh = np.zeros(hidden_size)  # Bias for candidate hidden state

# GRU operations (single step)
z = sigmoid(X.dot(Wz) + h_prev.dot(Uz) + bz)  # Update gate
r = sigmoid(X.dot(Wr) + h_prev.dot(Ur) + br)  # Reset gate
h_tilde = np.tanh(X.dot(Wh) + (r * h_prev).dot(Uh) + bh)  # Candidate hidden state
h = (1 - z) * h_prev + z * h_tilde  # New hidden state

# Print input, output, and hidden state update
print("Input Vector (X):", X)
print("Previous Hidden State (h_prev):", h_prev)
print("Update Gate (z):", z)
print("Reset Gate (r):", r)
print("Candidate Hidden State (h_tilde):", h_tilde)
print("New Hidden State (h):", h)''')