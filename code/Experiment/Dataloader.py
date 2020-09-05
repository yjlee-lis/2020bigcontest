import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

data_dir = './datasets'
data_list = os.listdir(data_dir)

#년도별 저장
def df_per_year():
    data_list_2016 = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-1].startswith('2016') ]
    data_2016 = [pd.read_csv(os.path.join(data_dir,data_list_2016[x]),encoding='cp949') for x in range(len(data_list_2016))]
    data_list_2017 = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-1].startswith('2017') ]
    data_2017 = [pd.read_csv(os.path.join(data_dir,data_list_2017[x]),encoding='cp949') for x in range(len(data_list_2017))]
    data_list_2018 = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-1].startswith('2018') ]
    data_2018 = [pd.read_csv(os.path.join(data_dir,data_list_2018[x]),encoding='cp949') for x in range(len(data_list_2018))]
    data_list_2019 = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-1].startswith('2019') ]
    data_2019 = [pd.read_csv(os.path.join(data_dir,data_list_2019[x]),encoding='cp949') for x in range(len(data_list_2019))]
    data_list_2020 = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-1].startswith('2020') ]
    data_2020 = [pd.read_csv(os.path.join(data_dir,data_list_2020[x]),encoding='cp949') for x in range(len(data_list_2020))]
    return data_2016, data_2017, data_2018, data_2019, data_2020

#항목별 저장
def df_per_category():
    data_list_single_hitter = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-2].startswith('개인타자')]
    data_single_hitter = [pd.read_csv(os.path.join(data_dir, data_list_single_hitter[x]), encoding='cp949') for x in range(len(data_list_single_hitter))]
    data_list_single_pitcher = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-2].startswith('개인투수')]
    data_single_pitcher = [pd.read_csv(os.path.join(data_dir, data_list_single_pitcher[x]), encoding='cp949') for x in range(len(data_list_single_pitcher))]
    data_list_games = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-2].startswith('경기')]
    data_games = [pd.read_csv(os.path.join(data_dir, data_list_games[x]), encoding='cp949') for x in range(len(data_list_games))]
    data_list_player_enroll = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-2].startswith('등록선수')]
    data_player_enroll = [pd.read_csv(os.path.join(data_dir, data_list_player_enroll[x]), encoding='cp949') for x in range(len(data_list_player_enroll))]
    data_list_players = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-2].startswith('선수')]
    data_players = [pd.read_csv(os.path.join(data_dir, data_list_players[x]), encoding='cp949') for x in range(len(data_list_players))]
    data_list_teams = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-2].startswith('팀')]
    data_teams = [pd.read_csv(os.path.join(data_dir, data_list_teams[x]), encoding='cp949') for x in range(len(data_list_teams))]
    data_list_team_hitter = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-2].startswith('팀타자')]
    data_team_hitter = [pd.read_csv(os.path.join(data_dir, data_list_team_hitter[x]), encoding='cp949') for x in range(len(data_list_team_hitter))]
    data_list_team_pitcher = [data_list[x] for x in range(len(data_list)) if data_list[x].split('_')[-2].startswith('팀투수')]
    data_team_pitcher = [pd.read_csv(os.path.join(data_dir, data_list_team_pitcher[x]), encoding='cp949') for x in range(len(data_list_team_pitcher))]
    return data_single_hitter, data_single_pitcher, data_games, data_player_enroll, data_players, data_teams, data_team_hitter, data_team_pitcher

data_2016, data_2017, data_2018, data_2019, data_2020 = df_per_year()
data_single_hitter, data_single_pitcher, data_games, data_player_enroll, data_players, data_teams, data_team_hitter, data_team_pitcher = df_per_category()