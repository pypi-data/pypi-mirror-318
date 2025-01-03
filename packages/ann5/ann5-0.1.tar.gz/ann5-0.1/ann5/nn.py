import numpy as np

# Define a simple neural network using numpy
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Forward pass for a simple 2-layer network
def simple_nn(x, weights1, weights2):
    z1 = np.dot(x, weights1)  # Linear transformation for first layer
    a1 = sigmoid(z1)          # Activation function (sigmoid)
    z2 = np.dot(a1, weights2) # Linear transformation for second layer
    return z2

# Define the input and weights
x = np.array([1.0, 2.0, 3.0])  # Input vector (3-dimensional)
weights1 = np.random.randn(3, 3)  # Weights for the first layer (3x3)
weights2 = np.random.randn(3, 1)  # Weights for the second layer (3x1)

# Perform a forward pass
output = simple_nn(x, weights1, weights2)

# Function to compute the Jacobian matrix (dy/dx)
def compute_jacobian(x, weights1, weights2):
    jacobian = np.zeros((1, len(x)))
    
    epsilon = 1e-5  # Small perturbation for numerical differentiation
    for i in range(len(x)):
        x_perturbed = x.copy()
        x_perturbed[i] += epsilon
        output_perturbed = simple_nn(x_perturbed, weights1, weights2)
        
        # Access the scalar output value by using output[0]
        jacobian[0, i] = (output_perturbed - output) / epsilon
    return jacobian

# Function to compute the Hessian matrix (d²y/dx²)
def compute_hessian(x, weights1, weights2):
    hessian = np.zeros((len(x), len(x)))
    
    epsilon = 1e-5  # Small perturbation for numerical differentiation
    for i in range(len(x)):
        for j in range(len(x)):
            x_perturbed = x.copy()
            x_perturbed[i] += epsilon
            x_perturbed[j] += epsilon
            output_perturbed = simple_nn(x_perturbed, weights1, weights2)
            
            # Access the scalar output value by using output[0]
            hessian[i, j] = (output_perturbed - output) / (epsilon ** 2)
    return hessian

# Compute Jacobian and Hessian
jacobian_matrix = compute_jacobian(x, weights1, weights2)
hessian_matrix = compute_hessian(x, weights1, weights2)

# Print the results
print("Jacobian Matrix (dy/dx):")
print(jacobian_matrix)

print("Hessian Matrix (d²y/dx²):")
print(hessian_matrix)
