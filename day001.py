import numpy as np

def dense(a_in, W, b):
    """
    Computes the output of a dense layer.
    Args:
      a_in (ndarray): Data from previous layer (or input data)
      W (ndarray): Weight matrix (columns = units)
      b (ndarray): Bias vector
    """
    units = W.shape[1]             # Number of neurons = number of columns
    a_out = np.zeros(units)        # Initialize output vector
    
    for j in range(units):         # Loop through each neuron
        w = W[:, j]                # Extract weights for neuron j
        z = np.dot(w, a_in) + b[j] # Compute z
        a_out[j] = g(z)            # Apply sigmoid (g)
        
    return a_out