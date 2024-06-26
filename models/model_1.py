cat_features_1 = ['toss decision', 'venue', 'lighting', 'series_name', 'season', 'series_type', 'ground_id',
                  'toss winner', 'by', 'city', 'umpire1', 'umpire2', 'team1_id', 'team2_id', 'winner_1st_bat']

X_1 = match_1
y_1 = y_train

X_train_1, X_validation_1, y_train_1, y_validation_1 = train_test_split(X_1, y_1, train_size=0.7, random_state=1234)
X_val_1, X_test_1, y_val_1, y_test_1 = train_test_split(X_validation_1, y_validation_1, train_size=0.5, random_state=1234)
model_1 = CatBoostClassifier(verbose=100)
model_1.fit(X_train_1, y_train_1, eval_set=(X_val_1, y_val_1))

