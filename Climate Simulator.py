import random
import math
import time

import nltk
nltk.download()
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

def process_user_input(user_input):
  # Tokenize the input
  tokens = word_tokenize(user_input)

  # Perform sentiment analysis
  sia = SentimentIntensityAnalyzer()
  sentiment = sia.polarity_scores(user_input)

  # Basic decision-making based on sentiment
  if sentiment['compound'] > 0.5:
    print("Positive decision: Consider the environmental impact.")
  elif sentiment['compound'] < -0.5:
    print("Negative decision: This could worsen climate change.")
  else:
    print("Neutral decision: Please consider the long-term consequences.")

# Example usage
user_input = "I want to invest in renewable energy."
process_user_input(user_input)