import numpy as np

# Parameters
input_size, hidden_size, output_size, seq_length = 3, 5, 2, 4
learning_rate = 0.01

# Random data
X = np.random.randn(seq_length, input_size)
y = np.random.randint(0, output_size, size=(1,))

# Initialize weights and biases
Wh, Wx, Wy = np.random.randn(hidden_size, hidden_size), np.random.randn(input_size, hidden_size), np.random.randn(hidden_size, output_size)
bh, by = np.zeros((1, hidden_size)), np.zeros((1, output_size))

# Forward pass
h = np.zeros((1, hidden_size))
h_list = []
for t in range(seq_length):
    h = np.tanh(X[t].dot(Wx) + h.dot(Wh) + bh)  # RNN step
    h_list.append(h)
output = h.dot(Wy) + by  # Output layer
pred = np.argmax(output)

# Compute loss (cross-entropy)
loss = -np.log(np.exp(output[0, y[0]]) / np.sum(np.exp(output)))

# Backpropagation
doutput = np.exp(output) / np.sum(np.exp(output))
doutput[0, y[0]] -= 1  # Cross-entropy gradient
dWy, dby = h.T.dot(doutput), doutput

# Backpropagate through time
dh = doutput.dot(Wy.T) * (1 - h ** 2)  # Derivative of tanh
for t in reversed(range(seq_length)):
    X_t = X[t].reshape(1, -1)  # Ensure X[t] has shape (1, input_size)
    dWx = X_t.T.dot(dh)  # Compute gradient for Wx at time step t
    dWh = h_list[t-1].T.dot(dh) if t > 0 else np.zeros_like(dh)  # Compute gradient for Wh at time step t
    dbh = np.sum(dh, axis=0, keepdims=True)  # Gradient for bh
    
    # Update gradients for weights
    Wx -= learning_rate * dWx
    Wh -= learning_rate * dWh
    Wy -= learning_rate * dWy
    bh -= learning_rate * dbh
    by -= learning_rate * dby
    
    if t > 0:
        dh = dh.dot(Wh.T) * (1 - h_list[t-1] ** 2)  # Propagate dh backward through the time steps

print(f"Predicted class: {pred}, Actual class: {y}")
print(f"Loss: {loss}")
