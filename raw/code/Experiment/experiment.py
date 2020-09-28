from IPython.display import display
import warnings
warnings.filterwarnings(action='ignore')

from Dataloader import *
from util import *
from Models import *
from ERA import *

class Experiment:
    def __init__(self, eda, model, target):
        super(Experiment, self).__init__()

        self.eda = eda
        self.model = model
        self.target = target

    def run(self):
        model_key = 'Pred.{}.{}'.format(self.target, self.model.__name__)
        test_key = 'Test.{}'.format(self.target)
        dict = {'year': [], 'team': [], test_key: [], model_key: []}

        # 2016~2019, OB, LG, WO, SK, KT, HH, HT, SS, LT, NC
        for i in range(1):  # 4
            year = 2016 + i
            for team in ['OB', 'LG', 'WO', 'SK', 'KT', 'HH', 'HT', 'SS', 'LT', 'NC']:
                dict['year'].append(year)
                dict['team'].append(team)

                df = self.eda(year, team)

                model_obj = self.model(df, self.target)
                model_test, model_pred = model_obj.run()

                dict[test_key].append(model_test)
                dict[model_key].append(model_pred)

        df = pd.DataFrame(dict)

        # 모델 오차의 절대값
        difference_column = '{}_abs_difference'.format(self.model.__name__)
        df[difference_column] = abs(df[test_key] - df[model_key])
        model_difference_mean = df[difference_column].mean()
        model_difference_std = df[difference_column].std()

        print("{} 모델의 오차 절대값 평균:".format(self.model.__name__), model_difference_mean)
        print("{} 모델의 오차 절대값 표준편차:".format(self.model.__name__), model_difference_std)
        display(df)

        return model_difference_mean, model_difference_std, df