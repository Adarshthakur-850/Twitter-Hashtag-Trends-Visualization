import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

PLOTS_DIR = "plots"

def save_plot(fig, filename):
    if not os.path.exists(PLOTS_DIR):
        os.makedirs(PLOTS_DIR)
    fig.savefig(os.path.join(PLOTS_DIR, filename))
    print(f"Plot saved to {filename}")
    plt.close(fig)

def plot_top_hashtags(df_hashtags):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='Count', y='Hashtag', data=df_hashtags, ax=ax, palette='viridis')
    ax.set_title("Top Trending Hashtags")
    save_plot(fig, "top_hashtags.png")

def plot_wordcloud(wc):
    if wc:
        fig = plt.figure(figsize=(10, 6))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        save_plot(fig, "wordcloud.png")

def plot_heatmap(df):
    if 'date' in df.columns:
        df['hour'] = df['date'].dt.hour
        df['day'] = df['date'].dt.day_name()
        pivot = df.pivot_table(index='day', columns='hour', values='user_followers', aggfunc='count')
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.heatmap(pivot, cmap='coolwarm', ax=ax)
        ax.set_title("Tweet Activity Heatmap (Day vs Hour)")
        save_plot(fig, "activity_heatmap.png")
