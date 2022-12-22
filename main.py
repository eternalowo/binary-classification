import numpy as np


def binary_classify(x_training_sample, y_training_sample):
    x_training_sample = np.array(x_training_sample)
    y_training_sample = np.array(y_training_sample)
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
    return w
