"""
Plot Generator Module
Creates visualizations from tweet data
"""

import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class PlotGenerator:
    def __init__(self, style='seaborn'):
        plt.style.use(style)
    
    def plot_tweet_timeline(self, tweets, save_path=None):
        """
        Plot tweets over time
        
        Args:
            tweets: List of tweet dictionaries
            save_path: Optional path to save figure
        """
        dates = [datetime.strptime(t['created_at'], '%Y-%m-%d %H:%M:%S') for t in tweets]
        
        plt.figure(figsize=(12, 6))
        plt.hist(dates, bins=30, edgecolor='black')
        plt.xlabel('Date')
        plt.ylabel('Number of Tweets')
        plt.title('Tweet Timeline')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300)
        plt.show()
    
    def plot_engagement_stats(self, tweets, save_path=None):
        """
        Plot engagement statistics
        
        Args:
            tweets: List of tweet dictionaries
            save_path: Optional path to save figure
        """
        retweets = [t['retweet_count'] for t in tweets]
        likes = [t['like_count'] for t in tweets]
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        
        axes[0].hist(retweets, bins=20, edgecolor='black')
        axes[0].set_xlabel('Retweets')
        axes[0].set_ylabel('Frequency')
        axes[0].set_title('Retweet Distribution')
        
        axes[1].hist(likes, bins=20, edgecolor='black')
        axes[1].set_xlabel('Likes')
        axes[1].set_ylabel('Frequency')
        axes[1].set_title('Like Distribution')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300)
        plt.show()
