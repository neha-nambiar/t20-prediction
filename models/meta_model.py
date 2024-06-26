# Using X_val to train combined model

x1 = X_val[['team1_rf', 'team1_rfm','team1_l', 'team1_lf', 'team1_lfm', 'team1_lg','team2_lhb', 'team2_lm',
            'team1_lmf', 'team1_ls', 'team1_lsm', 'team1_lws',  'team2_l', 'team2_lbw', 'team2_lf', 'team2_lg',
            'team2_ls', 'team2_lsm', 'team2_lws', 'team2_rmf','team2_ro','team1_lbw','team2_rhb', 'team1_slo', 'team2_slo',
            'team1_rhb','team1_ro','team2_rm','team2_lfm','team2_rfm','team2_rf','team1_lhb','team1_lm','team2_lmf',
            'by','city','win amount','umpire1','umpire2','venue','win_pct_3',
            'ground_avg_wickets', 'ground_avg_runs','ground_id', 'lighting', 'team1_id', 'team2_id',
            'season', 'series_name', 'series_type',  'winner_1st_bat','toss decision','toss winner',
            ]]
x2= X_val[['team1_runs','team2_runs','team1_balls','team2_avg_runs_last3','team1_fours','team2_caught',
           'team2_wides','team2_boundary_rate','team2_sixes','team2_bowling_avg','team1_batting_avg','team1_no_50s_last3','team1_wickets',
           'team2_balls','team2_wicket_count','team2_fours','team1_sixes','team1_wides','team2_fifties','team2_wickets',
           'team1_runs_conceded','team1_maiden','team2_batting_avg','team1_bowling_avg', 'team1_strike_rate','team2_avg_wickets_last3',
           'team1_boundary_rate','team1_avg_wickets_last3','team2_century', 'team2_dots','team1_4_wicket_hauls', 'team1_5_wicket_hauls',
           'team1_avg_runs_last3', 'team1_bowled', 'team1_caught_bowled','team1_century', 'team1_dots', 'team1_economy',
           'team1_fifties', 'team1_hit_wicket', 'team1_wicket_count','team2_4_wicket_hauls','team2_5_wicket_hauls','team2_maiden',
           'team2_no_50s_last3','team2_runs_conceded','team2_strike_rate','team1_noballs', 'team1_not_out', 'team1_retired_hurt',
           'team1_retired_not_out', 'team1_retired_out','team2_retired_out','team2_noballs','team2_retired_hurt','team2_retired_not_out',
           'team1_rm', 'team1_rmf', 'team1_runout', 'team1_stumped', 'team2_bowled',
           'team2_caught_bowled',  'team2_hit_wicket','team2_runout','team2_stumped','team2_not_out','team1_caught'
            ]]
x3 = X_val[['diff_century', 'diff_dots', 'diff_fours', 'diff_maiden', 'diff_wicket_count', 'diff_wickets','diff_sixes',
            'diff_4_wicket_hauls', 'diff_5_wicket_hauls', 'diff_avg_runs_last3','diff_strike_rate','diff_noballs','diff_boundary_rate',
            'diff_avg_wickets_last3', 'diff_batting_avg','diff_not_out','diff_no_50s_last3','diff_runs','diff_bowling_avg',
            'diff_runs_conceded', 'diff_economy', 'diff_wides','diff_balls','diff_fifties'
            ]]

# Prediction of models 1, 2 and 3 on X_val will be combined and this will be the training data for the meta-model.
pred_1 = model_1.predict(x1)
pred_2 = model_2.predict(x2)
pred_3 = model_3.predict(x3)

# Combining predictions
combined_predictions = np.vstack((pred_1, pred_2, pred_3)).T

meta_model = GradientBoostingClassifier().fit(combined_predictions, y_val)
final_predictions = meta_model.predict(combined_predictions)

