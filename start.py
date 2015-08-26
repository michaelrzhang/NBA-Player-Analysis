# Things to analyze:
# most common shot type
# when percentage of shots is highest
# shot distance
# whether team wins with more shots

import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

shot_chart_url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPAR'\
                'AMS=2014-15&ContextFilter=&ContextMeasure=FGA&DateFrom=&D'\
                'ateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Loca'\
                'tion=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&'\
                'PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=201935&Plu'\
                'sMinus=N&Position=&Rank=N&RookieYear=&Season=2014-15&Seas'\
                'onSegment=&SeasonType=Regular+Season&TeamID=0&VsConferenc'\
                'e=&VsDivision=&mode=Advanced&showDetails=0&showShots=1&sh'\
                'owZones=0'

# Get the webpage containing the data
response = requests.get(shot_chart_url)
# Grab the headers to be used as column headers for our DataFrame
headers = response.json()['resultSets'][0]['headers']
#['GRID_TYPE', 'GAME_ID', 'GAME_EVENT_ID', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME', 'PERIOD', 'MINUTES_REMAINING', 'SECONDS_REMAINING', 'EVENT_TYPE', 'ACTION_TYPE', 'SHOT_TYPE', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_AREA', 'SHOT_ZONE_RANGE', 'SHOT_DISTANCE', 'LOC_X', 'LOC_Y', 'SHOT_ATTEMPTED_FLAG', 'SHOT_MADE_FLAG']
#['Shot Chart Detail', '0021401219', 137, 201935, 'James Harden', 1610612745, 'Houston Rockets', 1, 0, 0, 'Missed Shot', 'Jump Shot', '3PT Field Goal', 'Above the Break 3', 'Left Side Center(LC)', '24+ ft.', 25, -127, 225, 1, 0], ['Shot Chart Detail', '0021401219', 250, 201935, 'James Harden', 1610612745, 'Houston Rockets', 2, 3, 0, 'Made Shot', 'Step Back Jump shot', '3PT Field Goal', 'Above the Break 3', 'Center(C)', '24+ ft.', 25, -67, 242, 1, 1], ['Shot Chart Detail', '0021401219', 279, 201935, 'James Harden', 1610612745, 'Houston Rockets', 2, 0, 27, 'Missed Shot', 'Driving Jump shot', '2PT Field Goal', 'In The Paint (Non-RA)', 'Left Side(L)', '8-16 ft.', 8, -67, 47, 1, 0], ['Shot Chart Detail', '0021401219', 286, 201935, 'James Harden', 1610612745, 'Houston Rockets', 2, 0, 1, 'Made Shot', 'Step Back Jump shot', '3PT Field Goal', 'Above the Break 3', 'Center(C)', '24+ ft.', 24, -5, 242, 1, 1], ['Shot Chart Detail', '0021401219', 295, 201935, 'James Harden', 1610612745, 'Houston Rockets', 3, 11, 21, 'Missed Shot', 'Jump Shot', '3PT Field Goal', 'Above the Break 3', 'Center(C)', '24+ ft.', 25, 0, 254, 1, 0]]
# Grab the shot chart data
shots = response.json()['resultSets'][0]['rowSet']

# shot_df = pd.DataFrame(shots, columns=headers)
# sns.set_style("white")
# sns.set_color_codes()
# plt.figure(figsize=(12,11))
# plt.scatter(shot_df.LOC_X, shot_df.LOC_Y)
# plt.show()