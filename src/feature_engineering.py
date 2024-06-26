batsman['century'] = (batsman['runs'] // 100).astype(int)
batsman['fifties'] = (batsman['runs'] // 50).astype(int)
bowler['4_wicket_hauls'] = (bowler['wicket_count'] // 4).astype(int)
bowler['5_wicket_hauls'] = (bowler['wicket_count'] // 5).astype(int)

won_toss_and_batted = (match_data['toss winner'] == match_data['winner']) & (match_data['toss decision'] == 'bat')
lost_toss_and_fielded = (match_data['toss winner'] != match_data['winner']) & (match_data['toss decision'] == 'field')
match_data['winner_1st_bat'] = won_toss_and_batted.astype(int) | lost_toss_and_fielded.astype(int)

for i in range(len(match_data)):
    if ((match_data['toss winner'][i] == 'team_1') and (match_data['toss decision'][i] == 'bat') or (match_data['toss winner'][i] == 'team_2') and (match_data['toss decision'][i] == 'field')):
        match_data['team1_runs'][i] = match_data['inning1_runs'][i]
        match_data['team2_runs'][i] = match_data['inning2_runs'][i]
        match_data['team1_wickets'][i] = match_data['inning1_wickets'][i]
        match_data['team2_wickets'][i] = match_data['inning2_wickets'][i]
        match_data['team1_balls'][i] = match_data['inning1_balls'][i]
        match_data['team2_balls'][i] = match_data['inning2_balls'][i]
    else:
        match_data['team1_runs'][i] = match_data['inning2_runs'][i]
        match_data['team2_runs'][i] = match_data['inning1_runs'][i]
        match_data['team1_wickets'][i] = match_data['inning2_wickets'][i]
        match_data['team2_wickets'][i] = match_data['inning1_wickets'][i]
        match_data['team1_balls'][i] = match_data['inning2_balls'][i]
        match_data['team2_balls'][i] = match_data['inning1_balls'][i]
    
match_data['diff_runs'] = match_data['team1_runs'] - match_data['team2_runs']
match_data['diff_wickets'] = match_data['team1_wickets'] - match_data['team2_wickets']
match_data['diff_balls'] = match_data['team1_balls'] - match_data['team2_balls']

match_data['team1_batting_avg'] = match_data['team1_runs'] / match_data['team2_balls']
match_data['team1_bowling_avg'] = match_data['team1_wickets'] / match_data['team2_balls']
match_data['team2_batting_avg'] = match_data['team2_runs'] / match_data['team1_balls']
match_data['team2_bowling_avg'] = match_data['team2_wickets'] / match_data['team1_balls']

match_data['diff_bowling_avg'] = match_data['team1_bowling_avg'] - match_data['team2_bowling_avg']
match_data['diff_batting_avg'] = match_data['team1_batting_avg'] - match_data['team2_batting_avg']

match_data['winner_team1'] = np.where(match_data['winner_id'] == match_data['team1_id'], 1, 0)

match_data['toss_winner'] = np.where(match_data['toss winner'] == match_data['team1'], 1, 0)

match_data['team1_win%_last3'] = match_data.apply(lambda row: winpLastn(row['team1_id'], row['match_dt'], 3), axis=1)
match_data['team2_win%_last3'] = match_data.apply(lambda row: winpLastn(row['team2_id'], row['match_dt'], 3), axis=1)
match_data['diff_win%_last3'] = match_data['team1_win%_last3'] - match_data['team2_win%_last3']

match_data['team1_no_50s_last3'] = match_data.apply(lambda row: no50sLastn(row['team1_roster_ids'], row['match_dt'], 3), axis=1)
match_data['team2_no_50s_last3'] = match_data.apply(lambda row: no50sLastn(row['team2_roster_ids'], row['match_dt'], 3), axis=1)
match_data['diff_no_50s_last3'] = match_data['team1_no_50s_last3'] - match_data['team2_no_50s_last3']

match_data['team1_avg_runs_last3'] = match_data.apply(lambda row: teamAvgRunsLastn(row['team1_id'], row['match_dt'], 3), axis=1)
match_data['team2_avg_runs_last3'] = match_data.apply(lambda row: teamAvgRunsLastn(row['team2_id'], row['match_dt'], 3), axis=1)
match_data['diff_avg_runs_last3'] = match_data['team1_avg_runs_last3'] - match_data['team2_avg_runs_last3']

match_data['team1_avg_wickets_last3'] = match_data.apply(lambda row: teamAvgwicketsLastn(row['team1_id'], row['match_dt'], 3), axis=1)
match_data['team2_avg_wickets_last3'] = match_data.apply(lambda row: teamAvgwicketsLastn(row['team2_id'], row['match_dt'], 3), axis=1)
match_data['diff_avg_wickets_last3'] = match_data['team1_avg_wickets_last3'] - match_data['team2_avg_wickets_last3']

match_data['win_pct_3'] = match_data.apply(lambda row: winpCrossLastn(row['team1_id'], row['team2_id'], row['match_dt'], 3), axis=1)

match_data['ground_avg_runs'] = match_data.apply(lambda row: avg_runs_ground(row, match_data), axis=1)

# Filling NaN values for grounds where previous data is not available using the next available value for that ground id.
for ground_id in match_data['ground_id'].unique():
    ground_data = match_data[match_data['ground_id'] == ground_id]
    first_non_nan = ground_data['ground_avg_runs'].notna().idxmax()
    match_data.loc[ground_data.index, 'ground_avg_runs'] = ground_data['ground_avg_runs'].fillna(ground_data['ground_avg_runs'].shift(-1), limit=first_non_nan)
  
# Filling remaining values with mean values
average_runs = match_data['ground_avg_runs'].mean()
match_data['ground_avg_runs'] = match_data['ground_avg_runs'].fillna(average_runs)

match_data['ground_avg_wickets'] = match_data.apply(lambda row: avg_wickets_ground(row, match_data), axis=1)

# Filling NaN values for grounds where previous data is not available using the next available value for that ground id.
for ground_id in match_data['ground_id'].unique():
    ground_data = match_data[match_data['ground_id'] == ground_id]
    first_non_nan = ground_data['ground_avg_wickets'].notna().idxmax()
    match_data.loc[ground_data.index, 'ground_avg_wickets'] = ground_data['ground_avg_wickets'].fillna(ground_data['ground_avg_wickets'].shift(-1), limit=first_non_nan)
  
# Filling remaining values with mean values
average_wickets = match_data['ground_avg_wickets'].mean()
match_data['ground_avg_wickets'] = match_data['ground_avg_wickets'].fillna(average_wickets)

match_data.drop(['inning1_runs', 'inning2_runs', 'inning1_wickets', 'inning2_wickets', 'inning1_balls', 'inning2_balls'], axis=1, inplace=True)

match_data['team1_batting_avg'] = match_data['team1_runs'] / match_data['team2_balls']
match_data['team1_bowling_avg'] = match_data['team1_wickets'] / match_data['team2_balls']
match_data['team2_batting_avg'] = match_data['team2_runs'] / match_data['team1_balls']
match_data['team2_bowling_avg'] = match_data['team2_wickets'] / match_data['team1_balls']

match_data['diff_runs'] = match_data['team1_runs'] - match_data['team2_runs']
match_data['diff_wickets'] = match_data['team1_wickets'] - match_data['team2_wickets']
match_data['diff_balls'] = match_data['team1_balls'] - match_data['team2_balls']

match_data['diff_bowling_avg'] = match_data['team1_bowling_avg'] - match_data['team2_bowling_avg']
match_data['diff_batting_avg'] = match_data['team1_batting_avg'] - match_data['team2_batting_avg']

# Setting winner_id column to binary, ie 1 if team 1 wins else 0
match_data['winner_team1'] = np.where(match_data['winner_id'] == match_data['team1_id'], 1, 0)

batsman_temp = batsman.drop('match_dt', axis=1)
bowler_temp = bowler.drop('match_dt', axis=1)


for i in range(len(match_data)):
    
    match_batsman = batsman_temp[batsman_temp['match id']==match_data['match id'][i]]
    match_bowler = bowler_temp[bowler_temp['match id']==match_data['match id'][i]]
    team1_batsman = match_batsman[match_batsman['batsman_id'].isin(match_data['team1_roster_ids'][i])]
    team1_bowler = match_bowler[match_bowler['bowler_id'].isin(match_data['team1_roster_ids'][i])]
    team2_batsman = match_batsman[match_batsman['batsman_id'].isin(match_data['team2_roster_ids'][i])]
    team2_bowler = match_bowler[match_bowler['bowler_id'].isin(match_data['team2_roster_ids'][i])]
# team 1
    team1_rhb = len(team1_batsman[team1_batsman['batsman_style'] == 'Right-hand bat'])
    team1_lhb = len(team1_batsman[team1_batsman['batsman_style'] == 'Left-hand bat'])
# team 2
    team2_rhb = len(team2_batsman[team2_batsman['batsman_style'] == 'Right-hand bat'])
    team2_lhb = len(team2_batsman[team2_batsman['batsman_style'] == 'Left-hand bat'])
    
    
for i in range(len(match_data)):
    
  match_batsman = batsman_temp[batsman_temp['match id']==match_data['match id'][i]]
  match_bowler = bowler_temp[bowler_temp['match id']==match_data['match id'][i]]
  team1_batsman = match_batsman[match_batsman['batsman_id'].isin(match_data['team1_roster_ids'][i])]
  team1_bowler = match_bowler[match_bowler['bowler_id'].isin(match_data['team1_roster_ids'][i])]
  team2_batsman = match_batsman[match_batsman['batsman_id'].isin(match_data['team2_roster_ids'][i])]
  team2_bowler = match_bowler[match_bowler['bowler_id'].isin(match_data['team2_roster_ids'][i])]
# team 1
    match_data['team1_rmf'][i] = team1_bowler[team1_bowler['bowler_style']=='Right-arm medium-fast'].shape[0]
    match_data['team1_lg'][i] = team1_bowler[team1_bowler['bowler_style']=='Legbreak googly'].shape[0]
    match_data['team1_slo'][i] = team1_bowler[team1_bowler['bowler_style']=='Slow left-arm orthodox'].shape[0]
    match_data['team1_rm'][i] = team1_bowler[team1_bowler['bowler_style']=='Right-arm medium'].shape[0]
    match_data['team1_ro'][i] = team1_bowler[team1_bowler['bowler_style']=='Right-arm offbreak'].shape[0]
    match_data['team1_rfm'][i] = team1_bowler[team1_bowler['bowler_style']=='Right-arm fast-medium'].shape[0]
    match_data['team1_lfm'][i] = team1_bowler[team1_bowler['bowler_style']=='Left-arm fast-medium'].shape[0]
    match_data['team1_l'][i] = team1_bowler[team1_bowler['bowler_style']=='Legbreak'].shape[0]
    match_data['team1_lws'][i] = team1_bowler[team1_bowler['bowler_style']=='Left-arm wrist-spin'].shape[0]
    match_data['team1_rf'][i] = team1_bowler[team1_bowler['bowler_style']=='Right-arm fast'].shape[0]
    match_data['team1_lmf'][i] = team1_bowler[team1_bowler['bowler_style']=='Left-arm medium-fast'].shape[0]
    match_data['team1_lm'][i] = team1_bowler[team1_bowler['bowler_style']=='Left-arm medium'].shape[0]
    match_data['team1_lf'][i] = team1_bowler[team1_bowler['bowler_style']=='Left-arm fast'].shape[0]
    match_data['team1_lsm'][i] = team1_bowler[team1_bowler['bowler_style']=='Left-arm slow-medium'].shape[0]
    match_data['team1_ls'][i] = team1_bowler[team1_bowler['bowler_style']=='Left-arm slow'].shape[0]
    match_data['team1_ls'][i] = 0
# team 2
    match_data['team2_rmf'][i] = team2_bowler[team2_bowler['bowler_style']=='Right-arm medium-fast'].shape[0]
    match_data['team2_lg'][i] = team2_bowler[team2_bowler['bowler_style']=='Legbreak googly'].shape[0]
    match_data['team2_slo'][i] = team2_bowler[team2_bowler['bowler_style']=='Slow left-arm orthodox'].shape[0]
    match_data['team2_rm'][i] = team2_bowler[team2_bowler['bowler_style']=='Right-arm medium'].shape[0]
    match_data['team2_ro'][i] = team2_bowler[team2_bowler['bowler_style']=='Right-arm offbreak'].shape[0]
    match_data['team2_rfm'][i] = team2_bowler[team2_bowler['bowler_style']=='Right-arm fast-medium'].shape[0]
    match_data['team2_lfm'][i] = team2_bowler[team2_bowler['bowler_style']=='Left-arm fast-medium'].shape[0]
    match_data['team2_l'][i] = team2_bowler[team2_bowler['bowler_style']=='Legbreak'].shape[0]
    match_data['team2_lws'][i] = team2_bowler[team2_bowler['bowler_style']=='Left-arm wrist-spin'].shape[0]
    match_data['team2_rf'][i] = team2_bowler[team2_bowler['bowler_style']=='Right-arm fast'].shape[0]
    match_data['team2_lmf'][i] = team2_bowler[team2_bowler['bowler_style']=='Left-arm medium-fast'].shape[0]
    match_data['team2_lm'][i] = team2_bowler[team2_bowler['bowler_style']=='Left-arm medium'].shape[0]
    match_data['team2_lf'][i] = team2_bowler[team2_bowler['bowler_style']=='Left-arm fast'].shape[0]
    match_data['team2_lsm'][i] = team2_bowler[team2_bowler['bowler_style']=='Left-arm slow-medium'].shape[0]
    match_data['team2_ls'][i] = team2_bowler[team2_bowler['bowler_style']=='Left-arm slow'].shape[0]


for i in range(len(match_data)):

    match_batsman = batsman_temp[batsman_temp['match id']==match_data['match id'][i]]
    match_bowler = bowler_temp[bowler_temp['match id']==match_data['match id'][i]]
    team1_batsman = match_batsman[match_batsman['batsman_id'].isin(match_data['team1_roster_ids'][i])]
    team1_bowler = match_bowler[match_bowler['bowler_id'].isin(match_data['team1_roster_ids'][i])]
    team2_batsman = match_batsman[match_batsman['batsman_id'].isin(match_data['team2_roster_ids'][i])]
    team2_bowler = match_bowler[match_bowler['bowler_id'].isin(match_data['team2_roster_ids'][i])]
    # team 1
    match_data['team1_not_out'][i] = len(team1_batsman[team1_batsman['wicket kind'] == 'not out'])
    match_data['team1_caught'][i] = len(team1_batsman[team1_batsman['wicket kind'] == 'caught'])
    match_data['team1_bowled'][i] = len(team1_batsman[team1_batsman['wicket kind'] == 'bowled'])
    match_data['team1_lbw'][i] = len(team1_batsman[team1_batsman['wicket kind'] == 'lbw'])
    match_data['team1_stumped'][i] = len(team1_batsman[team1_batsman['wicket kind'] == 'stumped'])
    match_data['team1_runout'][i] = len(team1_batsman[team1_batsman['wicket kind'] == 'run out'])
    match_data['team1_retired_hurt'][i] = len(team1_batsman[team1_batsman['wicket kind'] == 'retired hurt'])
    match_data['team1_hit_wicket'][i] = len(team1_batsman[team1_batsman['wicket kind'] == 'hit wicket'])
    match_data['team1_caught_bowled'][i] = len(team1_batsman[team1_batsman['wicket kind'] == 'caught and bowled'])
    match_data['team1_retired_not_out'][i] = len(team1_batsman[team1_batsman['wicket kind'] == 'retired not out'])
    match_data['team1_retired_out'][i] = len(team1_batsman[team1_batsman['wicket kind'] == 'retired out'])
    match_data['team1_retired_out'][i] = 0
# team 2
    match_data['team2_not_out'][i] = len(team2_batsman[team2_batsman['wicket kind'] == 'not out'])
    match_data['team2_caught'][i] = len(team2_batsman[team2_batsman['wicket kind'] == 'caught'])
    match_data['team2_bowled'][i] = len(team2_batsman[team2_batsman['wicket kind'] == 'bowled'])
    match_data['team2_lbw'][i] = len(team2_batsman[team2_batsman['wicket kind'] == 'lbw'])
    match_data['team2_stumped'][i] = len(team2_batsman[team2_batsman['wicket kind'] == 'stumped'])
    match_data['team2_runout'][i] = len(team2_batsman[team2_batsman['wicket kind'] == 'run out'])
    match_data['team2_retired_hurt'][i] = len(team2_batsman[team2_batsman['wicket kind'] == 'retired hurt'])
    match_data['team2_hit_wicket'][i] = len(team2_batsman[team2_batsman['wicket kind'] == 'hit wicket'])
    match_data['team2_caught_bowled'][i] = len(team2_batsman[team2_batsman['wicket kind'] == 'caught and bowled'])
    match_data['team2_retired_not_out'][i] = len(team2_batsman[team2_batsman['wicket kind'] == 'retired not out'])
    match_data['team2_retired_out'][i] = len(team2_batsman[team2_batsman['wicket kind'] == 'retired out'])


for i in range(len(match_data)):

    match_batsman = batsman_temp[batsman_temp['match id']==match_data['match id'][i]]
    match_bowler = bowler_temp[bowler_temp['match id']==match_data['match id'][i]]
    team1_batsman = match_batsman[match_batsman['batsman_id'].isin(match_data['team1_roster_ids'][i])]
    team1_bowler = match_bowler[match_bowler['bowler_id'].isin(match_data['team1_roster_ids'][i])]
    team2_batsman = match_batsman[match_batsman['batsman_id'].isin(match_data['team2_roster_ids'][i])]
    team2_bowler = match_bowler[match_bowler['bowler_id'].isin(match_data['team2_roster_ids'][i])]

# team 1
    match_data['team1_strike_rate'][i] = team1_batsman['strike_rate'].sum()
    match_data['team1_fours'][i] = team1_batsman['Fours'].sum()
    match_data['team1_sixes'][i] = team1_batsman['Sixes'].sum()
    match_data['team1_century'][i] = team1_batsman['century'].sum()
    match_data['team1_fifties'][i] = team1_batsman['fifties'].sum()
    match_data['team1_runs_conceded'][i] = team1_bowler['runs'].sum()
    match_data['team1_wicket_count'][i] = team1_bowler['wicket_count'].sum()
    match_data['team1_4_wicket_hauls'][i] = team1_bowler['4_wicket_hauls'].sum()
    match_data['team1_5_wicket_hauls'][i] = team1_bowler['5_wicket_hauls'].sum()
    match_data['team1_economy'][i] = team1_bowler['economy'].sum()
    match_data['team1_maiden'][i] = team1_bowler['maiden'].sum()
    match_data['team1_dots'][i] = team1_bowler['dots'].sum()
    match_data['team1_fours'][i] = team1_batsman['Fours'].sum()
    match_data['team1_sixes'][i] = team1_batsman['Sixes'].sum()
    match_data['team1_wides'][i] = team1_bowler['wides'].sum()
    match_data['team1_noballs'][i] = team1_bowler['noballs'].sum()
# team 2
    match_data['team2_strike_rate'][i] = team2_batsman['strike_rate'].sum()
    match_data['team2_fours'][i] = team2_batsman['Fours'].sum()
    match_data['team2_sixes'][i] = team2_batsman['Sixes'].sum()
    match_data['team2_century'][i] = team2_batsman['century'].sum()
    match_data['team2_fifties'][i] = team2_batsman['fifties'].sum()
    match_data['team2_runs_conceded'][i] = team2_bowler['runs'].sum()
    match_data['team2_wicket_count'][i] = team2_bowler['wicket_count'].sum()
    match_data['team2_4_wicket_hauls'][i] = team2_bowler['4_wicket_hauls'].sum()
    match_data['team2_5_wicket_hauls'][i] = team2_bowler['5_wicket_hauls'].sum()
    match_data['team2_economy'][i] = team2_bowler['economy'].sum()
    match_data['team2_maiden'][i] = team2_bowler['maiden'].sum()
    match_data['team2_dots'][i] = team2_bowler['dots'].sum()
    match_data['team2_fours'][i] = team2_batsman['Fours'].sum()
    match_data['team2_sixes'][i] = team2_batsman['Sixes'].sum()
    match_data['team2_wides'][i] = team2_bowler['wides'].sum()
    match_data['team2_noballs'][i] = team2_bowler['noballs'].sum()
    
match_data['team1_boundary_rate'] = (match_data['team1_fours'] + match_data['team1_sixes'])/match_data['team2_balls']
match_data['team2_boundary_rate'] = (match_data['team2_fours'] + match_data['team2_sixes'])/match_data['team1_balls']

match_data['diff_boundary_rate'] = match_data['team1_boundary_rate'] - match_data['team2_boundary_rate']
match_data['diff_strike_rate'] = match_data['team1_strike_rate'] - match_data['team2_strike_rate']
match_data['diff_fours'] = match_data['team1_fours'] - match_data['team2_fours']
match_data['diff_sixes'] = match_data['team1_sixes'] - match_data['team2_sixes']
match_data['diff_century'] = match_data['team1_century'] - match_data['team2_century']
match_data['diff_fifties'] = match_data['team1_fifties'] - match_data['team2_fifties']
match_data['diff_runs_conceded'] = match_data['team1_runs_conceded'] - match_data['team2_runs_conceded']
match_data['diff_wicket_count'] = match_data['team1_wicket_count'] - match_data['team2_wicket_count']
match_data['diff_4_wicket_hauls'] = match_data['team1_4_wicket_hauls'] - match_data['team2_4_wicket_hauls']
match_data['diff_5_wicket_hauls'] = match_data['team1_5_wicket_hauls'] - match_data['team2_5_wicket_hauls']
match_data['diff_economy'] = match_data['team1_economy'] - match_data['team2_economy']
match_data['diff_noballs'] = match_data['team1_noballs'] - match_data['team2_noballs']
match_data['diff_maiden'] = match_data['team1_maiden'] - match_data['team2_maiden']
match_data['diff_dots'] = match_data['team1_dots'] - match_data['team2_dots']
match_data['diff_wides'] = match_data['team1_wides'] - match_data['team2_wides']
match_data['diff_not_out'] = match_data['team1_not_out'] - match_data['team2_not_out']

