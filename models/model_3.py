X_3 = match_3
y_3 = y_train

X_train_3, X_validation_3, y_train_3, y_validation_3 = train_test_split(X_3, y_3, train_size=0.7, random_state=7544)
X_val_3, X_test_3, y_val_3, y_test_3 = train_test_split(X_validation_3, y_validation_3, train_size=0.5, random_state=877)
model_3 = CatBoostClassifier(verbose=100)
model_3.fit(X_train_3, y_train_3, eval_set=(X_val_3, y_val_3))