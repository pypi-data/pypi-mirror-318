import numpy as np
import matplotlib.pyplot as plt

def simple_lstm(x, h_prev, c_prev, Wf, Wi, Wo, Wc, bf, bi, bo, bc):
    z = np.concatenate((x, h_prev))  # Concatenate input and previous hidden state

    f = sigmoid(np.dot(Wf, z) + bf)  # Forget gate
    i = sigmoid(np.dot(Wi, z) + bi)  # Input gate
    o = sigmoid(np.dot(Wo, z) + bo)  # Output gate
    c_tilde = np.tanh(np.dot(Wc, z) + bc)  # Candidate cell state

    c = f * c_prev + i * c_tilde  # New cell state
    h = o * np.tanh(c)  # New hidden state

    return h, c

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Generate synthetic weather data (temperature)
np.random.seed(42)
time_steps = 100
time = np.arange(time_steps)
temperature = 20 + 10 * np.sin(0.2 * time) + np.random.randn(time_steps)  # Sine wave with noise

# Normalize the data
temperature = (temperature - np.mean(temperature)) / np.std(temperature)

# Prepare the data for LSTM (creating input-output pairs)
sequence_length = 10  # Number of previous time steps to predict the next value
X = []
y = []

for i in range(len(temperature) - sequence_length):
    X.append(temperature[i:i + sequence_length])
    y.append(temperature[i + sequence_length])

X = np.array(X)
y = np.array(y)

# Reshape X for LSTM (samples, time_steps, features)
X = X.reshape(X.shape[0], X.shape[1], 1)

# Initial hidden and cell state
h_prev = np.zeros(1)  # Initial hidden state
c_prev = np.zeros(1)  # Initial cell state

# Random LSTM weights and biases for a single hidden unit
Wf = np.random.randn(1, 2)  # Forget gate weight
Wi = np.random.randn(1, 2)  # Input gate weight
Wo = np.random.randn(1, 2)  # Output gate weight
Wc = np.random.randn(1, 2)  # Candidate cell state weight

bf = np.zeros(1)  # Forget gate bias
bi = np.zeros(1)  # Input gate bias
bo = np.zeros(1)  # Output gate bias
bc = np.zeros(1)  # Cell state bias

# Predict the next temperature value using the LSTM
predictions = []

for i in range(X.shape[0]):
    x = X[i][-1]  # Use the last input from the sequence for prediction
    h_prev, c_prev = simple_lstm(x, h_prev, c_prev, Wf, Wi, Wo, Wc, bf, bi, bo, bc)
    predictions.append(h_prev[0])

predictions = np.array(predictions)

# Denormalize the predictions to match the original scale
predictions = predictions * np.std(temperature) + np.mean(temperature)

# Plot the results
plt.plot(time[sequence_length:], temperature[sequence_length:], label="Actual Temperature")
plt.plot(time[sequence_length:], predictions, label="Predicted Temperature", linestyle="dashed")
plt.xlabel("Time Steps")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.title("Weather Prediction using LSTM")
plt.show()

# Print first few predictions
print("Predicted Temperatures:", predictions[:5])
print("Actual Temperatures:", temperature[:5])
