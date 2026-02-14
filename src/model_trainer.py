<<<<<<< HEAD
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_models(df):
    print("Training models...")
    features = ['user_followers', 'user_friends', 'user_favourites', 'hashtag_count', 'hour', 'day_of_week']
    target = 'is_high_engagement'
    
    df_model = df.dropna(subset=features + [target])
    X = df_model[features]
    y = df_model[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    models = {
        'LogisticRegression': LogisticRegression(max_iter=1000),
        'RandomForest': RandomForestClassifier(n_estimators=100)
    }
    
    if not os.path.exists("models"):
        os.makedirs("models")
        
    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"{name} Accuracy: {acc:.4f}")
        joblib.dump(model, os.path.join("models", f"{name}.pkl"))
        
    return models
=======
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_models(df):
    print("Training models...")
    features = ['user_followers', 'user_friends', 'user_favourites', 'hashtag_count', 'hour', 'day_of_week']
    target = 'is_high_engagement'
    
    df_model = df.dropna(subset=features + [target])
    X = df_model[features]
    y = df_model[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    models = {
        'LogisticRegression': LogisticRegression(max_iter=1000),
        'RandomForest': RandomForestClassifier(n_estimators=100)
    }
    
    if not os.path.exists("models"):
        os.makedirs("models")
        
    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"{name} Accuracy: {acc:.4f}")
        joblib.dump(model, os.path.join("models", f"{name}.pkl"))
        
    return models
>>>>>>> 79634237ea655520f03b06be34bcf794e690af6c
