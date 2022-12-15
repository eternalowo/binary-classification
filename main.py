import numpy as np
import matplotlib.pyplot as plot

x_training_sample = np.array([[2, 9], [154, 93], [32, 123], [91, 135],
                              [190, 55], [65, 134], [116, 136], [90, 31],
                              [192, 135], [5, 175], [175, 17], [31, 29],
                              [189, 120], [191, 17], [28, 146], [42, 74],
                              [65, 193], [53, 133], [195, 15], [108, 118]])

y_training_sample = np.array([-1, 1, -1, -1,
                              1, -1, -1, 1,
                              1, -1, 1, 1,
                              1, 1, -1, -1,
                              -1, -1, 1, -1])

training_sample_len = len(x_training_sample)
sign_func = lambda x: np.sign(w[0] * x[0] + w[1] * x[1])
n = 50
l = 0.1
w = [0, -1]

for _ in range(n):
    for i in range(training_sample_len):
        margin = sign_func(x_training_sample[i])
        if margin * y_training_sample[i] < 0:
            w[0] = w[0] + l * y_training_sample[i]
    Q = sum([j for j in range(training_sample_len) if y_training_sample[j] * sign_func(x_training_sample[j])])
    if Q == 0:
        break

line_x = list(range(max(x_training_sample[:, 0]) + 10))
line_y = [w[0] * i for i in line_x]

x_0 = x_training_sample[y_training_sample == 1]
x_1 = x_training_sample[y_training_sample == -1]

plot.scatter(x_0[:, 0], x_0[:, 1], color='red')
plot.scatter(x_1[:, 0], x_1[:, 1], color='blue')
plot.plot(line_x, line_y, color='green')

plot.xlim([0, max([x[0] for x in x_training_sample]) + 10])
plot.ylim([0, max([x[1] for x in x_training_sample]) + 10])
plot.xlabel("x")
plot.ylabel("y")
plot.grid(True)
plot.show()
