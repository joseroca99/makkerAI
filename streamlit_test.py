import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
from newAPI_test import generateBio, writeShorter


#Navbar assignment
selected = option_menu(
  menu_title=None,
  options=['LinkedIn Bio', 'Cover Letter', 'Resume'],
  icons=["blockquote-left", "envelope", "file-earmark-person"],
  menu_icon="cast",
  default_index=0,
  orientation="horizontal"
)
    
with st.sidebar:
  st.title('Welcome to TidyAI :robot_face:')
  st.subheader('TidyAI is our project for Build your AI Startup Hackathon Episode 2')
  code ='''hackathonParticipants =[
    Arianit Sylafeta,
    Manuel Palazzo,
    Jose Campo,
    Saira Asghar,
    Bright Boakye
  ]'''
  st.code(code)



#Main pages
if selected =="LinkedIn Bio":
  st.title("Let's get you a LinkedIn bio")
  st.write("")

  #Seperate containers into columns 
  left = st.container()
  right = st.container()
  left, right = st.columns([1,5])
 
  def pushcontainers():
    left.write('')
    left.write('')
    left.write('')
    right.write('')
    right.write('')
    
  left.image('https://i.imgur.com/H4f9t8E.png', )
  right.subheader("I've got the perfect idea for a bio. Please tell me what tone of voice do you want to use?")
  tov = right.selectbox("Please input the tone of voice you want?", ('...','Professional', 'Informal', 'Enthusiastic', 'Neutral', 'Other'))

  #If you want to have all input fields showing all the time just remove the if statements and make them the same identation. 
  if tov != '...':
    if tov == 'Other':
      left.write('')
      left.write('')
      left.write('')
      left.write('')
      tov = right.text_input('Please specify?')
    pushcontainers()
    left.image('https://i.imgur.com/UCMEUwo.png')
    right.subheader('Great, now I will need some general information to work with.')
    info = right.text_input("Full Name, Education, Work Experience...")
    if info:
        pushcontainers()
        left.image('https://i.imgur.com/pgHUU2X.png')
        right.subheader('Nearly done, any sample bio you want to mimic?')
        sample = right.text_input('LinkedIn bio you like.')
        if sample:
            pushcontainers()
            left.image('https://i.imgur.com/MK73xxW.png')
            right.subheader('Last one, anything you want to emphasize?')
            emphasize = right.text_input('Skill or characteristic you want to emphasize')
            if emphasize:
              list = [tov, info, sample, emphasize]
              left.write('')
              right.write('')
              right.write('')
              right.write('')
              left.image('https://i.imgur.com/tKBSrKn.png')
              right.subheader("🎈Yuhuu we made it. Here's your LinkedIn Bio🎈")
              response = generateBio(list)
              if left.button('Want it Shorter?'): 
                writeShorter(response)
              right.code(response)
              
                

  

if selected =="Cover Letter":
  st.title("Cover Letter")
 
  
if selected =="Resume":
  st.title("Resume Here")
