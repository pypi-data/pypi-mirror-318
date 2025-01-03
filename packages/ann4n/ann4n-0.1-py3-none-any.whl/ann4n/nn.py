import numpy as np

# Generate synthetic dataset with ranges matching the Wine dataset
np.random.seed(123)

# Wine dataset feature ranges:
# Alcohol: ~12.0 to 14.0
# Malic acid: ~1.0 to 3.0
# Ash: ~1.5 to 3.5

# Class 0 (e.g., wine class 1)
wine_class_0 = np.random.normal([13.0, 2.0, 2.0], 0.5, (50, 3))

# Class 1 (e.g., wine class 2)
wine_class_1 = np.random.normal([13.5, 2.2, 2.5], 0.5, (50, 3))

# Class 2 (e.g., wine class 3)
wine_class_2 = np.random.normal([12.5, 1.8, 2.3], 0.5, (50, 3))

# Combine the classes into one dataset
data = np.vstack((wine_class_0, wine_class_1, wine_class_2))

# Labels for the three classes
labels = np.array([0] * 50 + [1] * 50 + [2] * 50)

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
        activations.append(relu(z) if w is not weights[-1] else softmax(z))
    return activations, z_values

# Activation functions
def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))  # For numerical stability
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)

def softmax_derivative(x):
    s = softmax(x)
    return s * (1 - s)

# Backward pass
def backward_pass(activations, z_values, weights, biases, y_true):
    gradients_w = [np.zeros_like(w) for w in weights]
    gradients_b = [np.zeros_like(b) for b in biases]
    m = y_true.shape[0]

    # Output layer error
    delta = activations[-1] - y_true
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

# One-hot encoding of labels
def one_hot_encode(labels, num_classes):
    return np.eye(num_classes)[labels]

# Training the model
def train(X, y, hidden_layer_sizes, lr, epochs):
    input_size = X.shape[1]
    output_size = 3  # 3 classes
    weights, biases = initialize_weights(input_size, hidden_layer_sizes, output_size)

    # One-hot encode the labels
    y_encoded = one_hot_encode(y, output_size)

    for epoch in range(epochs):
        activations, z_values = forward_pass(X, weights, biases)
        gradients_w, gradients_b = backward_pass(activations, z_values, weights, biases, y_encoded)
        update_weights(weights, biases, gradients_w, gradients_b, lr)

        if epoch % 100 == 0:
            loss = -np.mean(np.sum(y_encoded * np.log(activations[-1]), axis=1))
            print(f"Epoch {epoch}, Loss: {loss:.4f}")

    return weights, biases

# Predict function
def predict(X, weights, biases):
    activations, _ = forward_pass(X, weights, biases)
    return np.argmax(activations[-1], axis=1)  # Return the class with highest probability

# Train the model
weights, biases = train(X_train, y_train, hidden_layer_sizes=[8, 8], lr=0.01, epochs=1000)

# Evaluate the model
y_pred = predict(X_test, weights, biases)
accuracy = np.mean(y_pred == y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Predict the class of a new sample
new_sample = np.array([[13.9, 1.8, 2.6]])  # Example wine sample (adjusted for the feature ranges)
prediction = predict(new_sample, weights, biases)
class_names = ["Class_0", "Class_1", "Class_2"]
print(f"The predicted class for the new sample is: {class_names[prediction[0]]}")
