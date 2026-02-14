<<<<<<< HEAD
import pandas as pd
import ast

def preprocess_data(df):
    print("Preprocessing data...")
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.dropna(subset=['date', 'hashtags'], inplace=True)
    
    def parse_hashtags(x):
        try:
            return ast.literal_eval(x)
        except:
            if isinstance(x, str):
                return [h.strip().replace("'", "") for h in x.strip("[]").split(',') if h.strip()]
            return []

    df['hashtags'] = df['hashtags'].apply(parse_hashtags)
    
    df['user_location'] = df['user_location'].fillna('Unknown')
    print(f"Data processed. Rows remaining: {df.shape[0]}")
    return df
=======
import pandas as pd
import ast

def preprocess_data(df):
    print("Preprocessing data...")
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.dropna(subset=['date', 'hashtags'], inplace=True)
    
    def parse_hashtags(x):
        try:
            return ast.literal_eval(x)
        except:
            if isinstance(x, str):
                return [h.strip().replace("'", "") for h in x.strip("[]").split(',') if h.strip()]
            return []

    df['hashtags'] = df['hashtags'].apply(parse_hashtags)
    
    df['user_location'] = df['user_location'].fillna('Unknown')
    print(f"Data processed. Rows remaining: {df.shape[0]}")
    return df
>>>>>>> 79634237ea655520f03b06be34bcf794e690af6c
