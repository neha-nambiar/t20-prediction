import numpy as np
import pandas as pd

match_data = pd.read_csv('/data/match.csv')
batsman = pd.read_csv('/data/batsman.csv')
bowler = pd.read_csv('/data/bowler.csv')

## match_data preprocessing

match_data['team1_roster_ids'] = match_data['team1_roster_ids'].str.split(':')
match_data['team2_roster_ids'] = match_data['team2_roster_ids'].str.split(':')

# setting data types
match_data['team1_roster_ids'] = match_data['team1_roster_ids'].apply(lambda x: [int(round(float(val))) for val in x])
match_data['team2_roster_ids'] = match_data['team2_roster_ids'].apply(lambda x: [int(round(float(val))) for val in x])

match_data['win amount'] = [int(round(float(val))) for val in match_data['win amount']]

match_data['inning1_runs'] = [int(round(float(val))) for val in match_data['inning1_runs']]
match_data['inning1_wickets'] = [int(round(float(val))) for val in match_data['inning1_wickets']]
match_data['inning1_balls'] = [int(round(float(val))) for val in match_data['inning1_balls']]

match_data['inning2_runs'] = [int(round(float(val))) for val in match_data['inning2_runs']]
match_data['inning2_wickets'] = [int(round(float(val))) for val in match_data['inning2_wickets']]
match_data['inning2_balls'] = [int(round(float(val))) for val in match_data['inning2_balls']]

match_data['match_dt'] = pd.to_datetime(match_data['match_dt'], format='%Y-%m-%d')

## batsman data preprocessing

# Imputing missing strike rates with median
batsman['strike_rate'] = batsman['strike_rate'].fillna(batsman['strike_rate'].median())

# Notice that the columns 'wicket kind' is NaN wherever the batsman was not out.
batsman['wicket kind'].fillna('not out', inplace=True)

batsman['Fours'].fillna(0, inplace=True)
batsman['Sixes'].fillna(0, inplace=True)
batsman['bowler_id'].fillna(0, inplace=True)

# Extracting batting style from batsman details
batsman['batsman_details'] = batsman['batsman_details'].apply(lambda x: x.split(':'))
batsman['batsman_style'] = batsman['batsman_details'].apply(lambda x: x[1])
batsman.drop(['batsman_details'],axis=1, inplace=True)

# Extracting bowling style from bowler details
batsman['bowler_details'] = batsman['bowler_details'].astype(str).apply(lambda x: x.split(':'))
batsman['bowler_style'] = batsman['bowler_details'].apply(lambda x: x[2] if len(x) > 2 else 'none') # Handle cases with less than 3 elements
batsman.drop(['bowler_details'],axis=1, inplace=True)

# Extracting bowling style from bowler details
batsman['bowler_details'] = batsman['bowler_details'].astype(str).apply(lambda x: x.split(':'))
batsman['bowler_style'] = batsman['bowler_details'].apply(lambda x: x[2] if len(x) > 2 else 'none') # Handle cases with less than 3 elements
batsman.drop(['bowler_details'],axis=1, inplace=True)

# Setting data types
batsman['batsman_id'] = [round(val) for val in batsman['batsman_id']]
batsman['match_dt'] = pd.to_datetime(batsman['match_dt'], format='%Y-%m-%d')

batsman.drop(['is_batsman_captain', 'is_batsman_keeper', 'over_faced_first',
            'is_bowler_keeper', 'is_bowler_captain'], axis=1, inplace=True)

## bowler data preprocessing

# Extracting bowling style from bowler details
bowler['bowler_details'] = bowler['bowler_details'].apply(lambda x: x.split(':'))
bowler['bowler_style'] = bowler['bowler_details'].apply(lambda x: x[2] if len(x) > 2 else 'none') # Handle cases with less than 3 elements
bowler.drop(['bowler_details'],axis=1, inplace=True)

# Setting data types
bowler['bowler_id'] = [round(val) for val in bowler['bowler_id']]
bowler['dots'] = [round(val) for val in bowler['dots']]
bowler['match_dt'] = pd.to_datetime(bowler['match_dt'], format='%Y-%m-%d')
bowler['maiden'] = [round(val) for val in bowler['maiden']]
bowler['match_dt'] = pd.to_datetime(bowler['match_dt'], format='%Y-%m-%d')

bowler.drop(['is_bowler_captain', 'is_bowler_keeper'], axis=1, inplace=True)

match_data.to_csv('match_data.csv', index=False)
batsman.to_csv('batsman.csv', index=False)
bowler.to_csv('bowler.csv', index=False)