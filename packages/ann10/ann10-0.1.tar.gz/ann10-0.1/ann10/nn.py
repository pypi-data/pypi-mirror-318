import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

input_size = 1 
hidden_size = 2 

stock_prices = np.array([100, 102, 104, 103, 105, 107, 106]) / 100 
sequence_length = len(stock_prices) - 1

np.random.seed(42)
Wz = np.random.randn(input_size, hidden_size)
Wr = np.random.randn(input_size, hidden_size)
Wh = np.random.randn(input_size, hidden_size)
Uz = np.random.randn(hidden_size, hidden_size)
Ur = np.random.randn(hidden_size, hidden_size)
Uh = np.random.randn(hidden_size, hidden_size)
bz = np.zeros(hidden_size)
br = np.zeros(hidden_size)
bh = np.zeros(hidden_size)

h_prev = np.zeros(hidden_size)

def gru_step(x, h_prev):
    z = sigmoid(x.dot(Wz) + h_prev.dot(Uz) + bz)  # Update gate
    r = sigmoid(x.dot(Wr) + h_prev.dot(Ur) + br)  # Reset gate
    h_tilde = np.tanh(x.dot(Wh) + (r * h_prev).dot(Uh) + bh)  # Candidate hidden state
    h = (1 - z) * h_prev + z * h_tilde  # New hidden state
    return h

predicted_prices = []
for t in range(sequence_length):
    x = np.array([stock_prices[t]]).reshape(1, input_size)
    
    h_prev = gru_step(x, h_prev)
    
    next_price = h_prev.dot(np.random.randn(hidden_size)) 
    predicted_prices.append(next_price[0]) 

predicted_prices = np.array(predicted_prices) * 100 + 100 
original_prices = stock_prices[1:] * 100 

print("Original Stock Prices:", original_prices)
print("Predicted Stock Prices:", predicted_prices)
