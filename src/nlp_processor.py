<<<<<<< HEAD
import pandas as pd
from collections import Counter
from wordcloud import WordCloud

def get_common_hashtags(df, n=20):
    all_hashtags = []
    for tags in df['hashtags']:
        all_hashtags.extend(tags)
    
    counter = Counter(all_hashtags)
    return pd.DataFrame(counter.most_common(n), columns=['Hashtag', 'Count'])

def get_wordcloud_object(df):
    all_hashtags = []
    for tags in df['hashtags']:
        all_hashtags.extend(tags)
    
    text = " ".join(all_hashtags)
    if not text:
        return None
        
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wc
=======
import pandas as pd
from collections import Counter
from wordcloud import WordCloud

def get_common_hashtags(df, n=20):
    all_hashtags = []
    for tags in df['hashtags']:
        all_hashtags.extend(tags)
    
    counter = Counter(all_hashtags)
    return pd.DataFrame(counter.most_common(n), columns=['Hashtag', 'Count'])

def get_wordcloud_object(df):
    all_hashtags = []
    for tags in df['hashtags']:
        all_hashtags.extend(tags)
    
    text = " ".join(all_hashtags)
    if not text:
        return None
        
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wc
>>>>>>> 79634237ea655520f03b06be34bcf794e690af6c
