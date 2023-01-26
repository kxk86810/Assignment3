import numpy as np

# random vector of size 20 with float in the range 1-20
vector = np.random.uniform(1,20,20)
print("The original vector is:" ,vector)

# reshape vector to 4 by 5
vector_reshaped = vector.reshape(4,5)
print("The reshaped vector before replace: ", vector_reshaped)

# replace max in each row by 0
vector_reshaped[np.arange(4),vector_reshaped.argmax(axis=1)] = 0
print("The reshaped vector after replace: " ,vector_reshaped)