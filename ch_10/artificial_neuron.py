# Sigmoid activation function is really good. Why ? 
# Because:
# # It is bounded between 0 and 1.
# # It is very smooth.
# # It can be diffrentiated and has nice derivative.
import math

def sigmoid(x):
	y = 1.0/(1 + math.exp(-x))
	return y


def activate(inputs, weights):
	h = 0
	for x, w in zip(inputs, weights):
		h += x*w

	return sigmoid(h)

if __name__ == "__main__":
	inputs = [0.5, 0.3, 0.2]
	weights = [0.4, 0.7, 0.2]
	output = activate(inputs, weights)
	print(output)

	