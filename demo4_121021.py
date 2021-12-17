import streamlit as st
import numpy as np
import pandas as pd
# from sklearn import model_selection
# from sklearn.ensemble import RandomForestClassifier
# import sklearn
import matplotlib.pyplot as plt
from PIL import Image
from scipy import stats
# import plotly.figure_factory as ff
# from matplotlib.figure import Figure
# import seaborn as sns
import pickle

@st.cache
def load_data():
   df_demo = pd.read_csv('df_demo_4.csv')
   df_demo = df_demo
   return df_demo



#sidebar width setup
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 500px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 500px;
        margin-left: -500px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)



#load data
df_demo = load_data()

#create Early, mid and later life cohort
df_early = df_demo[df_demo.Age < 6]
df_mid = df_demo[(df_demo.Age >= 6) & (df_demo.Age < 10)]
df_later = df_demo[df_demo.Age > 10]

#create a title
#st.title('Life Style Factor Analysis')

#sidebar is for general info
st.sidebar.image(Image.open('vivid_logo3.png'), use_column_width=True)
st.sidebar.header("Demographic information")
#For gender
gender = st.sidebar.selectbox(
    "What is your gender?",
    ("Female", "Male")
)

gender = 1 if gender == "Male" else 2

#For age
age = st.sidebar.selectbox(
    "What is your age?",
    ('18 to 24', '25 to 29', '30 to 34' ,'35 to 39', '40 to 44', '45 to 49', '50 to 54', '55 to 59' , '60 to 64', '65 to 69', '70 to 74', '75 to 79', '80 or older')
)

if age == "18 to 24":
  age = 1
elif age == "25 to 29":
  age = 2
elif age == "30 to 34":
  age = 3
elif age == "35 to 39":
  age = 4
elif age == "40 to 44":
  age = 5
elif age == "45 to 49":
  age = 6
elif age == "50 to 54":
  age = 7
elif age == "55 to 59":
  age = 8
elif age == "60 to 64":
  age = 9
elif age == "65 to 69":
  age = 10
elif age == "70 to 74":
  age = 11
elif age == "80 or older":
  age = 12
else: 
  age = 13


#For Race
race = st.sidebar.selectbox(
    "What is your Race?",
    ('White only, non-Hispanic', 'Black only, non-Hispanic', 'American Indian or Alaskan Native only' ,'Asian only, non-Hispanic', 'Native Hawaiian or other Pacific Islander only, Non-Hispanic', 'Other race only, non-Hispanic', 'Multiracial, non-Hispanic', 'Hispanic')
)
if race == "White only, non-Hispanic":
  race = 1
elif race == "Black only, non-Hispanic":
  race = 2
elif race == "American Indian or Alaskan Native only":
  race = 3
elif race == "Asian only, non-Hispanic":
  race = 4
elif race == "Native Hawaiian or other Pacific Islander only, Non-Hispanic":
  race = 5
elif race == "Other race only, non-Hispanic":
  race = 6
elif race == "Multiracial, non-Hispanic":
  race = 7
else: 
  race = 8

#behavior information
st.sidebar.header("Behavioral information")

#For Educational level Analysis
Edu= st.sidebar.selectbox(
    "What is the highest grade or year of school you completed?",
    ('Never attended school or only kindergarten', 'Grades 1 through 8 (Elementary)', 'Grades 9 through 11 (Some high school)' ,'Grade 12 or GED (High school graduate)', 'College 1 year to 3 years (Some college or technical school)', 'College 4 years or more (College graduate)')
)
if Edu == "Never attended school or only kindergarten":
  Edu = 1
elif Edu == "Grades 1 through 8 (Elementary)":
  Edu = 2
elif Edu == "Grades 9 through 11 (Some high school)":
  Edu = 3
elif Edu == "Grade 12 or GED (High school graduate)":
  Edu = 4
elif Edu == "College 1 year to 3 years (Some college or technical school)":
  Edu = 5
else: 
  Edu = 6 

#For BMI condition Analysis
BMI = st.sidebar.selectbox(
     "Four-categories of Body Mass Index (BMI)?",
     ('Underweight BMI < 18.5', 'Normal Weight 18.5 <= BMI < 25', 'Overweight 25 <= BMI < 30', 'Obese BMI >= 30')
)
if BMI == "Underweight BMI < 18.5":
  BMI = 1
elif BMI == "Normal Weight 18.5 <= BMI < 25":
  BMI = 2
elif BMI == "Overweight 25 <= BMI < 30":
  BMI = 3
else: 
  BMI = 4

#For Metropolitan Status Analysis
metro = st.sidebar.selectbox(
     "What is your metropolitan status?",
     ('In the center city of an MSA', 'Outside the center city of an MSA but inside the county containing the center city', 'Inside a suburban county of the MSA', 'Not in an MSA')
)
if metro == "In the center city of an MSA":
  metro = 1
elif metro == "Inside a suburban county of the MSA":
  metro = 3
elif metro == "Not in an MSA":
  metro = 4
else: 
  metro = 2

#For smoking status
Smoke = st.sidebar.selectbox(
    "Please choose your level of smoker status", 
    ('I smoke every day', 'I smoke some day', 'I used to smoke' ,'I never smoke')
)
if Smoke == "I smoke every day":
  Smoke = 1
elif Smoke == "I smoke some day":
  Smoke = 2
elif Smoke == "I used to smoke":
  Smoke = 3
else: 
  Smoke = 4

#For Alcohol Consumption Analysis
st.header('Alcohol Consumption :beer:')
#get input value: drinks number per week DrinkNum_week
DrinkNum_week = st.sidebar.slider("How many drinks do you have on the average every week? (1 drink = a 12 ounce beer)", max_value=78) 
DrinkNum = int(DrinkNum_week / 7)
#for early life cohort: age < 6 
if age < 6:
  df_early_sample = df_demo[(df_demo['Age'] == age) & (df_demo['Gender'] == gender) & (df_demo['Race'] == race)]
  #remove decimals
  avg_week_drink = int(round(df_early_sample['DrinkNum'].mean() * 7, 0))
  st.write('People with the same age range, race and gender as you take: ' + str(avg_week_drink) + ' drink(s) per week on average.')
  #the cutoff (>21units/week) is equivalent to 2drinks/day in CDC
  #here the participant's weekly drink amount does not reach the cutoff
  if DrinkNum < 2:
    st.write("good job! :clap::clap::clap::clap:")
    percent_early = int(round(stats.percentileofscore(df_early['DrinkNum'], DrinkNum, kind='strict'),0))
    #here I used "weak"!
    less_percent_early = 100 - int(round(stats.percentileofscore(df_early['DrinkNum'], DrinkNum, kind='weak'),0))
    col1, col2 = st.columns(2)
    col1.metric(label="Your alcohol consumption is better than ", value=str(less_percent_early) + "%", delta= "people in early life in America")
    drink_mid_perc_good = int(df_mid['DrinkNum'].quantile(percent_early / 100) * 7) 
    #I noticed for early life sample whose drink DrinkNum < 2, to maintain the same alcohol consumption percentile in the middle life, the daily drink num is always 0 by using df_mid['DrinkNum'].quantile()
    col2.metric(label="To maintain the same alcohol consumption percentile in the mid life ", value="< 7 drinks/week", delta= "is recommanded", delta_color="off")
  #here the participant's weekly drink amount is higher than the cutoff  
  else:
    #for excessive drinker, use "strict" ranking kind
    percent_early_excessive = int(round(stats.percentileofscore(df_early['DrinkNum'], DrinkNum, kind='strict'),0))
    col1, col2 = st.columns(2)
    col1.metric(label="Your alcohol consumption is more than ", value=str(percent_early_excessive) + "%", delta= "people in early life in America", delta_color="inverse")
    drink_mid_perc = int(df_mid['DrinkNum'].quantile(percent_early_excessive / 100) * 7)
    col2.metric(label="Alcohol consumption percentile at " + str(percent_early_excessive) + "% among people in mid life is ", value=str(drink_mid_perc) + " drinks/week", delta= "on average", delta_color="off")

elif age < 10:
  df_mid_sample = df_mid[(df_mid['Age'] == age) & (df_mid['Gender'] == gender) & (df_mid['Race'] == race)]
  #remove decimals
  avg_week_drink_mid = int(round(df_mid_sample['DrinkNum'].mean() * 7, 0))
  st.write('People with the same age range, race and gender as you take: ' + str(avg_week_drink_mid) + ' drink(s) per week on average.')
  col1, col2, col3 = st.columns(3)
  value_early = str(int((round(stats.percentileofscore(df_early['DrinkNum'], DrinkNum, kind='strict'),0))))
  value_mid = str(int((round(stats.percentileofscore(df_mid['DrinkNum'], DrinkNum, kind='strict'),0))))
  value_later = str(int((round(stats.percentileofscore(df_later['DrinkNum'], DrinkNum, kind='strict'),0))))
  col1.metric(label="Your alcohol consumption is more than ", value=value_early + "%", delta= "people in early life in America")
  col2.metric(label="Your alcohol consumption is more than ", value=value_mid + "%", delta= "people in mid life in America")
  col3.metric(label="Your alcohol consumption is more than ", value=value_later + "%", delta= "people in later life in America")

else:
  df_later_sample = df_later[(df_later['Age'] == age) & (df_later['Gender'] == gender) & (df_later['Race'] == race)]
  #remove decimals
  avg_week_drink_later = int(round(df_later_sample['DrinkNum'].mean() * 7, 0))
  st.write('People with the same age range, race and gender as you take: ' + str(avg_week_drink_later) + ' drink(s) per week on average ')
  value_later = str(int((round(stats.percentileofscore(df_later['DrinkNum'], DrinkNum, kind='strict'),0))))
  st.metric(label="Your alcohol consumption is more than ", value=value_later + "%", delta= "people in later life in America")

st.write("Click the button to see the risk of alcohol consumption factor in mid life to dementia")
if st.button('For 🍺 risk, click me 👈'):
  image = Image.open('lancet.png')
  st.image(image, width=500)

#For sleeping analysis 

Sleep_hour = st.sidebar.slider("How many hours of sleep do you get?", max_value=24) 


#For Smoking Analysis
st.header('Smoking status :smoking:')

if (Smoke == 3) or (Smoke == 4):
  st.write("good job! :clap::clap::clap::clap:")
else:
  if age < 6:
    smoke_percent_early = 100 - int(round(stats.percentileofscore(df_early['Smoke'], Smoke, kind='weak'),0))
    col1, col2 = st.columns(2)
    col1.metric(label="Your smoking status is worse than ", value=str(smoke_percent_early) + "%", delta= "people in early life in America", delta_color="inverse")
    col2.metric(label="Early life people merely ", value="18%", delta= "are smoking", delta_color="off")
  elif age < 10:
    smoke_percent_mid = 100 - int(round(stats.percentileofscore(df_mid['Smoke'], Smoke, kind='weak'),0))
    col1, col2 = st.columns(2)
    col1.metric(label="Your smoking status is worse than ", value=str(smoke_percent_mid) + "%", delta= "people in mid life in America", delta_color="inverse")
    col2.metric(label="Mid life people merely ", value="17%", delta= "are smoking", delta_color="off")
  else:
    smoke_percent_later = 100 - int(round(stats.percentileofscore(df_later['Smoke'], Smoke, kind='weak'),0))
    col1, col2 = st.columns(2)
    col1.metric(label="Your smoking status is worse than ", value=str(smoke_percent_later) + "%", delta= "people in later life in America", delta_color="inverse")
    col2.metric(label="Later life people merely ", value="8%", delta= "are smoking", delta_color="off")  

st.write("Click the button to see the risk of smoking in later life to dementia")
if st.button('For 🚬 risk, click me 👈'):
  image = Image.open('lancet.png')
  st.image(image, width=500)


#For hearing condition Analysis
hearing = st.sidebar.checkbox('I have serious difficulty hearing')
hearing = 1 if hearing else 0

# hearing = st.sidebar.radio(
#      "Are you deaf or do you have serious difficulty hearing?",
#      ('Yes', 'No')
# )
# hearing = 1 if hearing == "Yes" else 0

#For depression condition Analysis
depression = st.sidebar.checkbox('I have a depressive disorder')
depression = 1 if depression else 0

# depression = st.sidebar.radio(
#      "(Ever told) you have a depressive disorder (including depression, major depression, dysthymia, or minor depression)?",
#      ('Yes', 'No')
# )
# depression = 1 if depression == "Yes" else 0

#For physical activity condition Analysis
PhysAct = st.sidebar.checkbox('I exercised during the last month')
PhysAct = 1 if PhysAct else 0

# PhysAct = st.sidebar.radio(
#      "During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise?",
#      ('Yes', 'No')
# )
# PhysAct = 1 if PhysAct == "Yes" else 0

#For social isolation condition Analysis
alone = st.sidebar.checkbox('I live alone')
alone = 1 if alone else 0

# alone = st.sidebar.radio(
#      "Do you live alone?",
#      ('Yes', 'No')
# )
# alone = 1 if alone == "Yes" else 0

#For Diabetes condition Analysis
diabetes = st.sidebar.checkbox('I have diabetes')
diabetes = 1 if diabetes else 0

# diabetes = st.sidebar.radio(
#      "(Ever told) you have diabetes?",
#      ('Yes', 'No')
# )
# diabetes = 1 if diabetes == "Yes" else 0

#For Preiabetes condition Analysis
prediabetes = st.sidebar.checkbox('I have pre-diabetes')
prediabetes = 1 if prediabetes else 0

# prediabetes = st.sidebar.radio(
#      "(Ever told) you have pre-diabetes or borderline diabetes?",
#      ('Yes', 'No')
# )
# prediabetes = 1 if prediabetes == "Yes" else 0

#Other feature plot by pie chart
col1, col2, col3 = st.columns(3)
df_plot_age = df_early if age < 6 else df_later if age > 10 else df_mid

with col1:
    st.header("BMI :hotdog:")
    fig, ax1 = plt.subplots(1, 1, figsize=(10, 10))
    Tasks = [df_plot_age.BMI[df_plot_age.BMI == 1].count(),df_plot_age.BMI[df_plot_age.BMI == 2].count(),df_plot_age.BMI[df_plot_age.BMI == 3].count(),df_plot_age.BMI[df_plot_age.BMI == 4].count()]
    my_labels = 'Underweight','Normal Weight','Overweight', 'Obese'
    plt.pie(Tasks,labels=my_labels,autopct='%1.1f%%',textprops={'fontsize': 30})
    st.pyplot(fig)

with col2:
    st.header("Exercise :weight_lifter:")
    fig, ax1 = plt.subplots(1, 1, figsize=(2, 2))
    Tasks = [df_plot_age.PhysAct[df_plot_age.PhysAct == 1].count(),df_plot_age.PhysAct[df_plot_age.PhysAct == 0].count()]
    my_labels = 'Exercise','No exercise'
    plt.pie(Tasks,labels=my_labels,autopct='%1.1f%%',textprops={'fontsize': 9})
    st.pyplot(fig)

with col3:
    st.header("Depression :cloud:")
    fig, ax1 = plt.subplots(1, 1, figsize=(3, 3))
    Tasks = [df_plot_age.Depression[df_plot_age.Depression == 1].count(),df_plot_age.Depression[df_plot_age.Depression == 0].count()]
    my_labels = 'Depression','No depression'
    plt.pie(Tasks,labels=my_labels,autopct='%1.1f%%',textprops={'fontsize': 10.5})
    st.pyplot(fig)

#load model
# @st.cache
with open('Pickle_RL_Model.pkl', 'rb') as f:
    model = pickle.load(f)

#generate input data
dftest = pd.DataFrame({
  'Gender': [gender],
  'Race': [race],
  'Age': [age],
  'Edu': [Edu],
  'Deaf': [hearing],
  'DrinkDays': [DrinkNum],
  'BMI': [BMI],
  'Smoke': [Smoke],
  'Depression': [depression],
  'HouseMember': [alone],
  'PhysAct': [PhysAct],
  'MSCODE': [metro],
  'Diabetes': [diabetes],
  'PreDiabetes': [prediabetes]
})

test = model.predict_proba(dftest)

#Your risk
st.header('Risk probability :mag_right:')

st.write('You are probably at risk of dementia: ' + str(round(test[0][1],3) * 100)[0 : 4] +    ' % :chart_with_upwards_trend:')
