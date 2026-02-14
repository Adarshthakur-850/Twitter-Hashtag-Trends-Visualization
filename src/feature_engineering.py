<<<<<<< HEAD
import pandas as pd
import numpy as np

def create_features(df):
    print("Feature Engineering...")
    df['engagement'] = df['user_followers'] + df['user_friends'] + df['user_favourites']
    
    threshold = df['engagement'].quantile(0.8)
    df['is_high_engagement'] = (df['engagement'] > threshold).astype(int)
    
    df['hashtag_count'] = df['hashtags'].apply(len)
    
    if 'date' in df.columns:
        df['hour'] = df['date'].dt.hour
        df['day_of_week'] = df['date'].dt.dayofweek
    
    return df
=======
import pandas as pd
import numpy as np

def create_features(df):
    print("Feature Engineering...")
    df['engagement'] = df['user_followers'] + df['user_friends'] + df['user_favourites']
    
    threshold = df['engagement'].quantile(0.8)
    df['is_high_engagement'] = (df['engagement'] > threshold).astype(int)
    
    df['hashtag_count'] = df['hashtags'].apply(len)
    
    if 'date' in df.columns:
        df['hour'] = df['date'].dt.hour
        df['day_of_week'] = df['date'].dt.dayofweek
    
    return df
>>>>>>> 79634237ea655520f03b06be34bcf794e690af6c
