import numpy as np

# Generate synthetic dataset
np.random.seed(123)
blue_crabs = np.random.normal([5.4, 3.1, 0.35], 0.4, (50, 3))
orange_crabs = np.random.normal([6.2, 3.6, 0.55], 0.4, (50, 3))
data = np.vstack((blue_crabs, orange_crabs))
labels = np.array([0] * 50 + [1] * 50)

# Split data into training and test sets
def train_test_split(data, labels, test_size=0.2, seed=42):
    np.random.seed(seed)
    indices = np.random.permutation(len(data))
    test_size = int(len(data) * test_size)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    return data[train_indices], data[test_indices], labels[train_indices], labels[test_indices]

X_train, X_test, y_train, y_test = train_test_split(data, labels)

# Initialize weights and biases
def initialize_weights(input_size, hidden_layer_sizes, output_size):
    weights = []
    biases = []
    layer_sizes = [input_size] + hidden_layer_sizes + [output_size]
    for i in range(len(layer_sizes) - 1):
        weights.append(np.random.randn(layer_sizes[i], layer_sizes[i+1]) * 0.1)
        biases.append(np.zeros((1, layer_sizes[i+1])))
    return weights, biases

# Forward pass
def forward_pass(X, weights, biases):
    activations = [X]
    z_values = []
    for w, b in zip(weights, biases):
        z = np.dot(activations[-1], w) + b
        z_values.append(z)
        activations.append(relu(z) if w is not weights[-1] else sigmoid(z))
    return activations, z_values

# Activation functions
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Backward pass
def backward_pass(activations, z_values, weights, biases, y_true):
    gradients_w = [np.zeros_like(w) for w in weights]
    gradients_b = [np.zeros_like(b) for b in biases]
    m = y_true.shape[0]

    # Output layer error
    delta = activations[-1] - y_true.reshape(-1, 1)
    for i in reversed(range(len(weights))):
        gradients_w[i] = np.dot(activations[i].T, delta) / m
        gradients_b[i] = np.sum(delta, axis=0, keepdims=True) / m
        if i > 0:
            delta = np.dot(delta, weights[i].T) * relu_derivative(z_values[i-1])
    return gradients_w, gradients_b

# Update weights
def update_weights(weights, biases, gradients_w, gradients_b, lr):
    for i in range(len(weights)):
        weights[i] -= lr * gradients_w[i]
        biases[i] -= lr * gradients_b[i]

# Training the model
def train(X, y, hidden_layer_sizes, lr, epochs):
    input_size = X.shape[1]
    output_size = 1
    weights, biases = initialize_weights(input_size, hidden_layer_sizes, output_size)

    for epoch in range(epochs):
        activations, z_values = forward_pass(X, weights, biases)
        gradients_w, gradients_b = backward_pass(activations, z_values, weights, biases, y)
        update_weights(weights, biases, gradients_w, gradients_b, lr)

        if epoch % 100 == 0:
            loss = -np.mean(y * np.log(activations[-1]) + (1 - y) * np.log(1 - activations[-1]))
            print(f"Epoch {epoch}, Loss: {loss:.4f}")

    return weights, biases

# Predict function
def predict(X, weights, biases):
    activations, _ = forward_pass(X, weights, biases)
    return (activations[-1] > 0.5).astype(int).flatten()

# Train the model
weights, biases = train(X_train, y_train, hidden_layer_sizes=[8, 8], lr=0.01, epochs=1000)

# Evaluate the model
y_pred = predict(X_test, weights, biases)
accuracy = np.mean(y_pred == y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Predict a new crab's species
new_crab = np.array([[5.9, 3.3, 0.5]])
prediction = predict(new_crab, weights, biases)
species = ["Blue", "Orange"]
print(f"The predicted species for the new crab is: {species[prediction[0]]}")
