import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'src'))

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.nlp_processor import get_common_hashtags, get_wordcloud_object
from src.visualization import plot_top_hashtags, plot_wordcloud, plot_heatmap
from src.feature_engineering import create_features
from src.model_trainer import train_models

def main():
    print("Starting Twitter Hashtag Trends Visualization Pipeline...")
    
    df = load_data()
    df = preprocess_data(df)
    
    top_hashtags = get_common_hashtags(df)
    wc = get_wordcloud_object(df)
    
    plot_top_hashtags(top_hashtags)
    plot_wordcloud(wc)
    plot_heatmap(df)
    
    df = create_features(df)
    train_models(df)
    print("Pipeline completed.")

if __name__ == "__main__":
    main()
