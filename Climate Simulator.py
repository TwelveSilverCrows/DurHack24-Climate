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
    negative_tokens = [
    "fossil fuels", "coal", "oil", "gas", "pollution", "emissions", 
    "carbon emissions", "greenhouse gas emissions", "climate change", 
    "global warming", "climate crisis", "climate emergency", "deforestation", 
    "overconsumption", "waste", "plastic pollution", "air pollution", 
    "water pollution", "land degradation", "species extinction", 
    "extreme weather events", "heatwave", "drought", "flood", 
    "hurricane", "wildfire", "sea level rise", "ocean acidification",
    "climate denial", "climate skepticism", "doesn't exist"
]
    for keyword in positive_tokens:
        if keyword in text.lower():
          sentiment['compound'] += 0.2  # Adjust this value as needed
    for keyword in negative_tokens:
        if keyword in text.lower():
          sentiment['compound'] -= 0.2  # Adjust this value as needed
        
    return sentiment['compound']

# Example usage:
text1 = "We should invest more in renewable energy to combat climate change."
text2 = "Fossil fuels are essential for economic growth."

questions = [
    "The UK is considering a new energy plan to reduce carbon emissions. Which energy source should you prioritize for the future?",
    "To combat traffic congestion and reduce emissions in India, what transportation policy should you implement?",
    "Nigeria is facing deforestation. What action should you take?",
    "China is growing rapidly, leading to increased emissions. What urban planning strategy should you adopt?",
    "Your government wants to stimulate green technology development. Where should you allocate funding?",
    "How should you address carbon emissions from industries in the US?",
    "Rising sea levels threaten Costa Rica. What strategy should you prioritize?",
    "How can you reduce energy consumption in China?",
    "How can you address emissions from agriculture in Bangladesh?",
    "How can you raise awareness about climate change in the US?",
    "Australia is experiencing extreme heatwaves due to climate change. How should you respond?",
    "Somalia is susceptible to droughts due to changing climate patterns. What's the best strategy?",
    "South Africa relies heavily on coal for energy. How can you reduce carbon emissions?",
    "Norway faces increased hurricane risks due to climate change. What should you prioritize?",
    "Bahrain suffers from air pollution, impacting public health. What's the best approach?",
    "The UK's energy grid is outdated and inefficient. How should you modernize it?",
    "Gibraltar is at risk of saltwater intrusion due to rising sea levels. What's your plan?",
    "Ghana's agricultural sector is struggling due to climate change. What's your response?",
    "Vietnam faces frequent flooding due to climate change. What's your top priority?",
    "The US relies heavily on cars with internal combustion engines. How can you reduce emissions from transportation?",
    "Tunisia is experiencing beach erosion due to rising sea levels. What's your plan?",
    "Your government is aiming to achieve carbon neutrality. What's your primary strategy?",
    "There's a waste management crisis in Turkey! How should you address it?",
    "Greece is facing water scarcity. What's the best approach to conserve water?",
    "Russia has significant forest cover. How will you protect it from deforestation?",
    "Burundi's transportation system is outdated. What's your priority for improvement?",
    "Japan faces ocean acidification. How should you address this issue?",
    "Brazil is a major emitter of methane. How can you reduce methane emissions?",
    "How can you address emissions from agriculture?",
    "How can you reduce energy consumption in Europe?",
    "You're trying to promote the use of sustainable transportation options in urban areas. How do you do it?"
]


print(climate_sentiment(text1))
print(climate_sentiment(text2))