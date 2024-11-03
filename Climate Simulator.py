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
    positive_tokens = ["combat","invest more in renewable energy",
    "renewable energy", "clean energy", "sustainable", "eco-friendly", 
    "climate-friendly", "greenhouse gas reduction", "carbon neutral", 
    "carbon footprint reduction", "low-carbon", "zero-carbon", 
    "solar power", "wind power", "hydro power", "geothermal energy", 
    "bioenergy", "energy efficiency", "electric vehicle", "EV", 
    "public transportation", "cycling", "walking", "plant-based diet", 
    "reduce, reuse, recycle", "sustainable agriculture", "conservation", 
    "reforestation", "afforestation", "climate action", "climate justice",
    "climate resilience", "adaptation", "mitigation", "sustainable development",
    "circular economy", "green technology", "eco-innovation", "reduce"
]
    negative_tokens = [
    "do nothing","fossil fuels", "coal", "oil", "gas", "pollution", "emissions", 
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
text2 = "I want to cut down all the trees."

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

#test block
print(climate_sentiment(text1))
print(climate_sentiment(text2))
global clim_rank
clim_rank =0

global year
year=2024

global current_temp
current_temp=14
        
global time_jumps
time_jumps=[]
        
global albedo
albedo = 0.30
        
global budget
budget=100
        
global sea_levels
sea_levels=[]
        
global greenhouse_effect
greenhouse_effect=0.5841

global greenhouse_tracker
greenhouse_tracker=[]
        
global temps
temps=[]
        
global temp_changes
temp_changes=[]

global T_cel
T_cel=0

global level
level=0

global temp_rise
temp_rise=0
    
global sea_level_rise
sea_level_rise=float(0)

global total_temp_rise
total_temp_rise=0

global budget_tracker
budget_tracker = []

global question_index
question_index=0

def expenses_decisions():
    global clim_rank,budget, budget_tracker
    #more dramatic situations have higher cost
    if clim_rank<=-0.2 or clim_rank>=0.2: #most expensive
        budget-=5
    elif clim_rank<=-0.1 or clim_rank>=0.1:
        budget-=3
    elif clim_rank<=-0.05 or clim_rank>=0.05:
        budget-=1 #all decisions have cost 
    budget_tracker.append(budget)

def climate_decisions():
    global greenhouse_effect, clim_rank, greenhouse_tracker
    if clim_rank>=0.2:#best for climate
        print("Well done for making such a great decision!")
    elif 0.1<=clim_rank<0.2:
        print("Not bad, keep going!")
        greenhouse_effect+=0.0005
    elif -0.2<=clim_rank<0.1:
        print("Careful! Remember, there are lots of people counting on you..")
        greenhouse_effect+=0.015
    elif clim_rank<-0.2:#worst for climate
        print("Oh no! People aren't very happy with your decisions...")
        greenhouse_effect+=0.025
    greenhouse_tracker.append(greenhouse_effect)
    
def calculate_temperature():
    global greenhouse_effect, albedo, T_cel
    pi = 3.14159
    sigma = 5.6703e-8 # e is '10^'
    mass_of_sun = 1.989e30
    distance = 1.496e11
    # Albedo and greenhouse_effect are the two variables that can be changed
    solar_luminosity = 3.846e26

    # Effective temperature
    T_eff = math.sqrt(math.sqrt((1 - albedo) * solar_luminosity / (4 * pi * sigma))) * 1 / math.sqrt(2 * distance)
    
    # Equivalent temperature below, which is temperature when the system is in equilibrium (energy is balanced)
    T_eq = (T_eff**2) * (1+(0.24 * greenhouse_effect))

    # Temperature in Kelvin
    T_kel = math.sqrt(T_eq/0.9)
    
    # Converting to Celsius
    T_cel = T_kel - 273

def calculate_sea_level():
    global temp_changes
    if temp_changes: #prevents function from executing when array is empty
        global sea_level_rise
        sea_level_rise=(temp_changes[-1])*2.3
        
def calulate_albedo():
    global albedo,sea_level_rise
    if sea_level_rise!=None:
        albedo-=(0.0005*sea_level_rise)
    
def update_sea():
    global sea_level_rise,temp_changes
    calculate_sea_level()
    calulate_albedo()
    global sea_levels
    sea_levels.append(sea_level_rise)
    
def update_temps():
    global greenhouse_effect, temps, temp_changes, year, albedo, temp_rise, time_jumps
    global current_temp
    calculate_temperature(greenhouse_effect, albedo)
    if temps:
        temp_rise = current_temp - temps[-1]
        temp_changes.append(temp_rise)
        global total_temp_rise
        total_temp_rise+=temp_rise
    temps.append(current_temp) # difference between the current temperature and last year's temperature
    time_jumps.append(year)
    
def endings():
    global budget, temp_rise, T_cel
    if sea_level_rise:
        if  budget<= 0:
            print("Oh no! You ran out of money… Better luck next time!")
            print("You were left with", budget, "budget points.")       
            print("The global average temperature was", T_cel, "degrees Celsius, which was a", temp_rise, "degrees Celsius rise from last year.")
        elif temp_rise >= 1:
            print("Oh no! You failed to stop global warming in time.")
            print("You were left with", budget, "budget points.")       
            print("The global average temperature was", T_cel, "degrees Celsius, which was a", temp_rise, "degrees Celsius rise from last year.")
            
        elif 0.75<=temp_rise<1:
            print("Your city experiences harsh drought due to rising temperatures.")
            print("You have to hand out bottled water and put limits on household use of it too. This uses up 5 budget points....")
            budget-=5
            print("You now have", budget, " budget points.")
            
        elif sea_level_rise>1.85:
            print("Your city experiences flooding due to rising sea levels. The repairs to infrastructure take 5 budget points...")
            budget-=5
            print("You now have", budget, " budget points.")
            
        elif T_cel > 30:
            print("Oh no! The average global temperature rose above 30°C. 35 degrees Celsius is the absolute limit of human tolerance. Better luck next time!")
            print("You were left with", budget, "budget points.")       
            print("The global average temperature was", T_cel, "degrees Celsius, which was a", temp_rise, "degrees Celsius rise from last year.")
        
        elif level == 4:
            print("You led the world through these difficult times. Let’s see how you did!")
            print("You were left with", budget, "budget points.")       
            print("The global average temperature was", T_cel, "degrees Celsius, which was a", temp_rise, "degrees Celsius rise from last year.")


for question in questions:
    text=input(question)
    clim_rank=climate_sentiment(text)
    expenses_decisions()
    climate_decisions()
    calculate_temperature()
    calculate_sea_level()
    calulate_albedo()
    update_sea()
    endings()
    year+=1
    print("Year:",year, "greenhouse:",greenhouse_effect, "temp:",current_temp, "temp rise:",temp_rise, "sea rise:",sea_level_rise, "albedo:", albedo)

    
    
    