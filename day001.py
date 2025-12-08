def sequential_model(x):
    # Layer 1
    a1 = dense(x, W1, b1)
    
    # Layer 2
    a2 = dense(a1, W2, b2)
    
    # Layer 3 (Output)
    a3 = dense(a2, W3, b3)
    
    return a3