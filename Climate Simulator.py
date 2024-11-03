import random
import math
import time

import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def climate_sentiment(text):
  sia = SentimentIntensityAnalyzer()
  sentiment = sia.polarity_scores(text)

  # Add custom sentiment scores for climate-related terms
 positive_tokens = [
    "renewable energy", "clean energy", "sustainable", "eco-friendly", 
    "climate-friendly", "greenhouse gas reduction", "carbon neutral", 
    "carbon footprint reduction", "low-carbon", "zero-carbon", 
    "solar power", "wind power", "hydro power", "geothermal energy", 
    "bioenergy", "energy efficiency", "electric vehicle", "EV", 
    "public transportation", "cycling", "walking", "plant-based diet", 
    "reduce, reuse, recycle", "sustainable agriculture", "conservation", 
    "reforestation", "afforestation", "climate action", "climate justice",
    "climate resilience", "adaptation", "mitigation", "sustainable development",
    "circular economy", "green technology", "eco-innovation"
]
    for keyword in positive_keywords:
        if keyword in text.lower():
          sentiment['compound'] += 0.2  # Adjust this value as needed
    for keyword in negative_keywords:
        if keyword in text.lower():
          sentiment['compound'] -= 0.2  # Adjust this value as needed
        

    
    

  return sentiment['compound']

# Example usage:
text1 = "We should invest more in renewable energy to combat climate change."
text2 = "Fossil fuels are essential for economic growth."

print(climate_sentiment(text1))
print(climate_sentiment(text2))