from Dataloader import *
from ERA import *
from util import *

import itertools
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.api import SimpleExpSmoothing, Holt, ExponentialSmoothing

import warnings
warnings.filterwarnings(action='ignore')


class Arima:
    def __init__(self, df, target):
        super(Arima, self).__init__()

        self.df_set = df
        self.target = target
        self.train = self.df_set.iloc[:-20]
        self.test = self.df_set.iloc[-20:]

    def run(self):

        p = list(range(0, 6))
        d = [0, 1, 2]
        q = list(range(0, 6))

        pdq = list(itertools.product(p, d, q))
        best_score = 10000000
        best_param = 0
        for param in pdq:
            try:
                arima_model = ARIMA(self.train[self.target].values, order=param)
                result = arima_model.fit()
                if result.aic < best_score:
                    best_score = result.aic
                    best_param = param
            except:
                continue

        set_arima = ARIMA(self.df_set[self.target].values, order=best_param)
        set_result = set_arima.fit()
        set_pred = set_result.forecast(len(self.test))[0]

        return self.test[self.target].mean(), set_pred.mean()

    def visualize(self):

        p = list(range(0, 6))
        d = [0, 1, 2]
        q = list(range(0, 6))

        pdq = list(itertools.product(p, d, q))
        best_score = 10000000
        best_param = 0
        for param in pdq:
            try:
                arima_model = ARIMA(self.train[self.target].values, order=param)
                result = arima_model.fit()
                if result.aic < best_score:
                    best_score = result.aic
                    best_param = param
            except:
                continue

        set_arima = ARIMA(self.df_set[self.target].values, order=best_param)
        set_result = set_arima.fit()
        set_pred = set_result.forecast(len(self.test))[0]

        print("Mean value of ERA :", self.df_set[self.target].mean())
        print("AIC Score of test :", best_score)
        print("Best parameter of (p, d, q): ", best_param)
        print("Pred ERA mean :", set_pred.mean())
        print("Test ERA mean :", self.test[self.target].mean())

        plot_train_test_pred_graph(self.train, self.test, set_pred)

        return self.test[self.target].mean(), set_pred.mean()

# arima_2016_LG = Arima(df_2016_LG, 'ERA')
# arima_2016_LG.run()