import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_chat import message as st_message
from newAPI_test import generateBio


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
    
  left.image('img/bot1.png', )
  right.subheader("I've got the perfect idea for a bio. Please tell me what tone of voice do you want to use?")
  tov = right.text_input("Please write the tone of voice you want?")

  #If you want to have all input fields showing all the time just remove the if statements and make them the same identation. 
  if tov:
    pushcontainers()
    left.image('img/bot2.png')
    right.subheader('Great, now I will need some general information to work with.')
    info = right.text_input("Full Name, Education, Gender...")
    if info:
        pushcontainers()
        left.image('img/bot3.png')
        right.subheader('Nearly done, any sample bio you want to mimic?')
        sample = right.text_input('LinkedIn bio you like.')
        if sample:
            pushcontainers()
            left.image('img/bot5.png')
            right.subheader('Last one, anything you want to emphasize?')
            emphasize = right.text_input('Skill or characteristic you want to emphasize')
            if emphasize:
              list = [tov, info, sample, emphasize]
              left.write('')
              right.write('')
              right.write('')
              right.write('')
              left.image('img/bot6.png')
              right.subheader("🎈Yuhuu we made it. Here's your LinkedIn Bio🎈")
              right.code(generateBio(list))

  

if selected =="Cover Letter":
  st.title("Cover Letter")
  st.text_input("Talk to Tidy")
  history = [
    {
      "message": "Hi, I'm Tidy, your personal assistant for writing cover letters. Please tell me your requirements.",
      "is_user": False
    }
    ,
    {
      "message": "Hi Tidy",
      "is_user": True
    }
  ]
  for chat in history:
    st_message(**chat)
  
if selected =="Resume":
  st.title("Resume Here")
