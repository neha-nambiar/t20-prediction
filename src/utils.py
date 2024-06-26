def winpLastn(team_id, date, n):
    """
    Calculates the win percentage of team_id in the last n matches.

    """
    df = match_data[(match_data['match_dt']<date)&\
                    ((match_data['team1_id']==team_id)|(match_data['team2_id']==team_id))]\
                        .sort_values(by='match_dt', ascending=False).head(n)
    win_count = df[df['winner_id']==team_id].shape[0]
    if win_count == 0:
        return 0
    return round(win_count*100/df.shape[0], 2)



def no50sLastn(player_list, date, n):

    """
    Calculates the number of 50s scored by the players in a team in the last n matches.

    """
    p1 = player_list[0]
    df = batsman[(batsman['batsman_id']==p1)&(batsman['match_dt']<date)].sort_values(by='match_dt', ascending=False).head(n)
    no_50s_p1 = df['fifties'].sum()
    p2 = player_list[1]
    df = batsman[(batsman['batsman_id']==p2)&(batsman['match_dt']<date)].sort_values(by='match_dt', ascending=False).head(n)
    no_50s_p2 = df['fifties'].sum()
    p3 = player_list[2]
    df = batsman[(batsman['batsman_id']==p3)&(batsman['match_dt']<date)].sort_values(by='match_dt', ascending=False).head(n)
    no_50s_p3 = df['fifties'].sum()
    p4 = player_list[3]
    df = batsman[(batsman['batsman_id']==p4)&(batsman['match_dt']<date)].sort_values(by='match_dt', ascending=False).head(n)
    no_50s_p4 = df['fifties'].sum()
    p5 = player_list[4]
    df = batsman[(batsman['batsman_id']==p5)&(batsman['match_dt']<date)].sort_values(by='match_dt', ascending=False).head(n)
    no_50s_p5 = df['fifties'].sum()
    p6 = player_list[5]
    df = batsman[(batsman['batsman_id']==p6)&(batsman['match_dt']<date)].sort_values(by='match_dt', ascending=False).head(n)
    no_50s_p6 = df['fifties'].sum()
    p7 = player_list[6]
    df = batsman[(batsman['batsman_id']==p7)&(batsman['match_dt']<date)].sort_values(by='match_dt', ascending=False).head(n)
    no_50s_p7 = df['fifties'].sum()
    p8 = player_list[7]
    df = batsman[(batsman['batsman_id']==p8)&(batsman['match_dt']<date)].sort_values(by='match_dt', ascending=False).head(n)
    no_50s_p8 = df['fifties'].sum()
    p9 = player_list[8]
    df = batsman[(batsman['batsman_id']==p9)&(batsman['match_dt']<date)].sort_values(by='match_dt', ascending=False).head(n)
    no_50s_p9 = df['fifties'].sum()
    p10 = player_list[9]
    df = batsman[(batsman['batsman_id']==p10)&(batsman['match_dt']<date)].sort_values(by='match_dt', ascending=False).head(n)
    no_50s_p10 = df['fifties'].sum()
    p11 = player_list[10]
    df = batsman[(batsman['batsman_id']==p11)&(batsman['match_dt']<date)].sort_values(by='match_dt', ascending=False).head(n)
    no_50s_p11 = df['fifties'].sum()

    return (no_50s_p1 + no_50s_p2 + no_50s_p3 + no_50s_p4 + no_50s_p5 + no_50s_p6 + no_50s_p7 + no_50s_p8 + no_50s_p9 + no_50s_p10 + no_50s_p11)



def teamAvgRunsLastn(team_id, date, n):

    """
    Calculates the average number of runs scored by the team in the last n matches.

    """

    df = match_data[(match_data['match_dt']<date)&(match_data['team1_id']==team_id) | (match_data['match_dt']<date)&(match_data['team2_id']==team_id)].sort_values(by='match_dt', ascending=False).head(n)

    avg_runs_ifteam1 = df[df['team1_id']==team_id]['team1_runs'].sum()
    avg_runs_ifteam2 = df[df['team2_id']==team_id]['team2_runs'].sum()

    return (avg_runs_ifteam1 + avg_runs_ifteam2)/n



def teamAvgwicketsLastn(team_id, date, n):

    """
    Calculates the average number of wickets taken by the team in the last n matches.

    """

    df = match_data[(match_data['match_dt']<date)&(match_data['team1_id']==team_id) | (match_data['match_dt']<date)&(match_data['team2_id']==team_id)].sort_values(by='match_dt', ascending=False).head(n)

    avg_wickets_ifteam1 = df[df['team1_id']==team_id]['team1_wickets'].sum()
    avg_wickets_ifteam2 = df[df['team2_id']==team_id]['team2_wickets'].sum()

    return (avg_wickets_ifteam1 + avg_wickets_ifteam2)/n



def winpCrossLastn(team1_id, team2_id, date, n):

    """
    Calculates the win percentage of team1_id against team2_id in the last n matches.

    """

    df = match_data[(match_data['match_dt']<date)&\
                    (((match_data['team1_id']==team1_id)&(match_data['team2_id']==team2_id))|((match_data['team1_id']==team2_id)&(match_data['team2_id']==team1_id)))]\
                        .sort_values(by='match_dt', ascending=False).head(n)
    win_count = df[df['winner_id']==team1_id].shape[0] # Counting number of rows (games) where winner is input team1.
    if win_count == 0:
        return 0
    return round(win_count*100/df.shape[0], 2)



def avg_runs_ground(row, match_data):

    """
    Calculates the average number of runs scored in the ground in the last n matches.
    """

    ground_id = row['ground_id']
    match_dt = row['match_dt']
    n = min(5, len(match_data[(match_data['match_dt'] < match_dt) & (match_data['ground_id'] == ground_id)]))

    if n > 0:
    filtered_df = match_data[(match_data['match_dt'] < match_dt) & (match_data['ground_id'] == ground_id)].sort_values(by='match_dt', ascending=False).head(n)
    avg_runs = (filtered_df['inning1_runs'] + filtered_df['inning2_runs']) / 2
    return avg_runs.mean()
    else:
    return None



def avg_wickets_ground(row, match_data):

    """
    Calculates the average number of wickets taken in the ground in the last n matches.
    """

    ground_id = row['ground_id']
    match_dt = row['match_dt']
    n = min(5, len(match_data[(match_data['match_dt'] < match_dt) & (match_data['ground_id'] == ground_id)]))

    if n > 0:
    filtered_df = match_data[(match_data['match_dt'] < match_dt) & (match_data['ground_id'] == ground_id)].sort_values(by='match_dt', ascending=False).head(n)
    avg_wickets = (filtered_df['inning1_wickets'] + filtered_df['inning2_wickets']) / 2
    return avg_wickets.mean()
    else:
    return None


