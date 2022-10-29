#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:12:51 2022

@author: sofiamuollo
"""

import pandas as pd 
import nltk

from nltk.sentiment import SentimentIntensityAnalyzer

Twitter_data = pd.read_csv ("/Users/sofiamuollo/Desktop/WORKING WITH DATA AND CODE/DATA A3/AUS.Tweets .csv") # Replace this file with the intended file to be used


Twitter_data = Twitter_data.dropna (how = 'all') # remove rows with missing values

sia = SentimentIntensityAnalyzer () # For each tweet, this function will return a dictionary with the sentiment scores: for example, {'neg': 0.095, 'neu': 0.905, 'pos': 0.0, 'compound': -0.296} for negative, neutral, positive and overall ("compound") score.


 
df = pd.DataFrame (Twitter_data) # take my DataFrame and create a new columm, call it "polarity_score"
df2 = df.assign (polarity_score = 0) 
print (df2)


for row in df2['text']: # Correctly selecting the column
  print (row)
  tweet_score = sia.polarity_scores(row)
  print (tweet_score)


tweet_score = pd.DataFrame(columns=list('compound'), index=['x', 'y']) # take 'compound' from tweet_score and place it back into your dataframe
df.append (Twitter_data)


t_df = df.append (Twitter_data) # takes 'comound' and further cleans output dataframe
t_df_cleaned = t_df.columns=list('compound')
print(t_df2_cleaned.head(10))
  
df.to_csv (Twitter_data.A3Tweets.csv) # Write/Save Twitter_data as new csv file.






