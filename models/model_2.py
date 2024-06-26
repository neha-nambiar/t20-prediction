X_2 = match_2
y_2 = y_train

X_train_2, X_validation_2, y_train_2, y_validation_2 = train_test_split(X_2, y_2, train_size=0.7, random_state=7544)
X_val_2, X_test_2, y_val_2, y_test_2 = train_test_split(X_validation_2, y_validation_2, train_size=0.5, random_state=877)
model_2 = CatBoostClassifier(verbose=100)
model_2.fit(X_train_2, y_train_2, eval_set=(X_val_2, y_val_2))