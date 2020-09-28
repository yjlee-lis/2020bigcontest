import pandas as pd
from Dataloader import *
from sklearn.preprocessing import LabelEncoder

def team_pitcher_eda1(year, team_name):
    pd.options.mode.chained_assignment = None #mapping 과정에서 chain error가 발생하는데 나중에 해결
    year_index = year - 2016

    # team_pitcher data에 해당 경기의 해당 팀의 홈 어웨이 여부 column 추가
    data_games_year = data_games[year_index]
    data_games_year = data_games_year[['G_ID', 'VISIT_KEY', 'HOME_KEY']]
    data_games_year = data_games_year.set_index('G_ID')

    data_team_pitcher_year = data_team_pitcher[year_index]
    data_team_pitcher_year = pd.merge(data_team_pitcher_year, data_games_year, how='left', on=['G_ID'])

    data_team_pitcher_year_team = data_team_pitcher_year[data_team_pitcher_year.T_ID == team_name]
    df = data_team_pitcher_year_team
    df['HOME_AWAY'] = df['HOME_KEY'].map(lambda x: 1 if x == team_name else 0)

    df = df.drop(columns=['VISIT_KEY', 'GDAY_DS', 'HOME_KEY'])

    # LabelEncoding
    encoder = LabelEncoder()

    df['VS_T_ID'] = encoder.fit_transform(df['VS_T_ID'])  # 상대편
    df['TB_SC'] = encoder.fit_transform(df['TB_SC'])  # 이닝 초/말
    df['WLS'] = encoder.fit_transform(df['WLS'])  # 승패무 여부

    # 시계열 데이터(경기당 방어율 계산)이기 때문에 경기 코드를 index로
    df = df.set_index('G_ID')

    # 경기당 방어율 column 생성
    df['ERA'] = df['ER'] * 27 / df['INN2']

    df = df.drop(columns=['T_ID'])
    df_year_team_name = df

    return df_year_team_name

