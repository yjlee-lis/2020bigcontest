from IPython.display import display
import warnings
warnings.filterwarnings(action='ignore')

from experiment import *
from Dataloader import *
from util import *
from Models import *
from ERA import *


def main():
    experiment1 = Experiment(team_pitcher_eda1, Arima, 'ERA')
    experiment1.run()


if __name__ == '__main__':
    main()