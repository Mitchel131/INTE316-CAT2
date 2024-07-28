import numpy as np

def power_iteration(A, num_simulations: int = 1000):
    n, d = A.shape
    # Randomly initialize the vector b
    b_k = np.random.rand(n)
    
    for _ in range(num_simulations):
        # Calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)

        # Calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)
        
        # Re-normalize the vector
        b_k = b_k1 / b_k1_norm
    
    # Calculate the eigenvalue
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k)) / np.dot(b_k.T, b_k)
    
    return eigenvalue, b_k

# Define the matrix A
A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

# Compute the dominant eigenvalue and eigenvector
dominant_eigenvalue, dominant_eigenvector = power_iteration(A)
print("Power Iteration Results:")
print("Eigenvalue:", dominant_eigenvalue)
print("Eigenvector:", dominant_eigenvector)

def qr_algorithm(A, num_simulations: int = 1000):
    A_k = A.copy()
    n = A.shape[0]
    
    for _ in range(num_simulations):
        Q, R = np.linalg.qr(A_k)  # QR decomposition
        A_k = R @ Q               # Form a new A_k
        
    eigenvalues = np.diagonal(A_k)
    eigenvectors = Q
    return eigenvalues, eigenvectors

# Compute all eigenvalues and eigenvectors using the QR algorithm
eigenvalues_qr, eigenvectors_qr = qr_algorithm(A)
print("\nQR Algorithm Results:")
print("Eigenvalues:", eigenvalues_qr)
print("Eigenvectors:\n", eigenvectors_qr)