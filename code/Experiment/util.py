import itertools
from sklearn.metrics import make_scorer
import matplotlib.pyplot as plt

def mae(prediction, correct):
    prediction = np.array(prediction)
    correct = np.array(correct)

    difference = correct - prediction
    abs_val = abs(difference)

    score = abs_val.mean()

    return score

def mse(prediction, correct):
    prediction = np.array(prediction)
    correct = np.array(correct)

    difference = correct - prediction
    sqr_val = difference ** 2

    score = sqr_val.mean()

    return score

def plot_train_test_pred_graph(trainset, testset, pred):
    plt.figure(figsize=(15,3))
    plt.plot(trainset.ERA, label='train')
    plt.plot(testset.ERA, label='test')
    plt.plot(testset.index, pred, label='prediction')
    plt.legend()
    plt.show()


