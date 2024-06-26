# Match Data

- `match id`: Unique id of match
- `batsman_id`: Unique player id of the batsman
- `inning`: Inning order – 1st or 2nd
- `batsman`: Batsman name (masked)
- `batsman_details`: ':' separated fields for the batsman - <Nationality>:<Batting style>:<Bowling style>.
- `is_batsman_captain`: 0/1 field for is batsman captain
- `is_batsman_keeper`: 0/1 field for is batsman keeper
- `runs`: Runs scored by the batsman in the inning
- `balls_faced`: Balls faced by batsman in the inning
- `over_faced_first`: First over.delivery faced by the batsman
- `wicket kind`: Kind of dismissal of the batsman
- `out_by_bowler`: Name of the bowler dimissing the batsman (masked)
- `out_by_fielder`: Name of the fielders assisting in the dismissal (masked)
- `bowler_id`: Unique player id of the bowler
- `bowler_details`: ':' separated fields for the bowler - <Nationality>:<Batting style>:<Bowling style>
- `is_bowler_captain`: 0/1 field for is bowler captain
- `is_bowler_keeper`: 0/1 field for is bowler keeper
- `strike_rate`: Strike rate of the batsman in the inning
- `Fours`: Number of Fours scored by the batsman in the inning
- `Sixes`: Number of Sixes scored by the batsman in the inning
- `match_dt`: Match date

# Batsman Data

- `match id`: Unique id of match
- `batsman_id`: Unique player id of the batsman
- `inning`: Inning order – 1st or 2nd
- `batsman`: Batsman name (masked)
- `batsman_details`: ':' separated fields for the batsman - <Nationality>:<Batting style>:<Bowling style>.
- `is_batsman_captain`: 0/1 field for is batsman captain
- `is_batsman_keeper`: 0/1 field for is batsman keeper
- `runs`: Runs scored by the batsman in the inning
- `balls_faced`: Balls faced by batsman in the inning
- `over_faced_first`: First over.delivery faced by the batsman
- `wicket kind`: Kind of dismissal of the batsman
- `out_by_bowler`: Name of the bowler dimissing the batsman (masked)
- `out_by_fielder`: Name of the fielders assisting in the dismissal (masked)
- `bowler_id`: Unique player id of the bowler
- `bowler_details`: ':' separated fields for the bowler - <Nationality>:<Batting style>:<Bowling style>
- `is_bowler_captain`: 0/1 field for is bowler captain
- `is_bowler_keeper`: 0/1 field for is bowler keeper
- `strike_rate`: Strike rate of the batsman in the inning
- `Fours`: Number of Fours scored by the batsman in the inning
- `Sixes`: Number of Sixes scored by the batsman in the inning
- `match_dt`: Match date

# Bowler data 

- `match id`: Unique id of match
- `bowler_id`: Unique player id of the bowler
- `inning`: Inning order – 1st or 2nd
- `bowler`: Name of the bowler (masked)
- `bowler_details`: ':' separated fields for the bowler - <Nationality>:<Batting style>:<Bowling style>.
- `is_bowler_captain`: 0/1 field for is bowler captain
- `is_bowler_keeper`: 0/1 field for is bowler keeper
- `runs`: Runs conceded by the bowler
- `wicket_count`: Wickets taken by the bowler
- `balls_bowled`: Number of balls bowled by the bowler
- `economy`: Economy of the bowler - ratio of runs conceded and balls bowled
- `maiden`: Number of maiden overs (overs with 0 runs conceded) bowled by the bowler
- `dots`: Number of dot balls (balls with 0 runs conceded) bowled by the bowler
- `wides`: Number of wides bowled by the bowler
- `noballs`: Number of no-balls bowled by the bowler
- `Fours`: Number of Fours conceded by the Bowler
- `Sixes`: Number of Sixes conceded by the Bowler
- `match_dt`: Match date

