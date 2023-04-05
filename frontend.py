import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
from API import generateBio, writeShorter


#Navbar assignment
selected = option_menu(
  menu_title=None,
  options=['LinkedIn Bio', 'Cover Letter'],
  icons=["blockquote-left", "envelope"],
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
    
  left.image('https://i.imgur.com/H4f9t8E.png')
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
        sample = right.text_input("LinkedIn bio you like.(Type 'N' for none)")
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
  st.title("AI Cover Letter Generator🚀")
  
  with st.form(key='my_form_to_submit'):
    st.subheader('Your Personal Information')
    col1,col2 = st.columns(2)    
    first_name = col1.text_input("👤FIRST NAME: ", placeholder="John")
    last_name = col2.text_input("👤LAST NAME: ", placeholder="Doe")
    col1,col2,col3 = st.columns(3)
    email = col1.text_input("📧EMAIL ADDRESS ", placeholder="Johndoe@gmail.com")
    desired_pos = col2.text_input("👨DESIRED POSITION", placeholder="Data Scientist")
    experience = col3.number_input('💻YEARS of EXPERIENCE', 0, 25)
    skills = col1.text_input('🦾 SKILLS:', placeholder='Python')
    experience_level = col2.select_slider('EXPERIENCE LEVEL ', ['Fresh','Internee','Entry-Level', 'Junior', 'Senior'])
    achievements = col3.text_input('🌟 ACHIEVEMENTS:', placeholder='Employee of the month') 
    st.subheader('Company Information')
    col1, col2, col3 = st.columns(3)
    company_name = col1.text_input('🏢 COMPANY NAME:', placeholder='Company')
    company_representative = col2.text_input('👨‍💼 COMPANY REPRESENTATIVE:', placeholder='Jane Doe')
    company_email = col3.text_input("📧COMPANY EMAIL: ", placeholder="HR@company.com")
    st.subheader('Cover Letter Specifics')
    col1, col2 = st.columns(2)
    option = col1.selectbox(
    '💭SELECT TONE of VOICE',
    ("Authoritative","Caring","Funny","Cheerful","Coarse","Conservative","Conversational","Casual","Dry", "Other"))
    if option == "Other":
       option = col1.text_input('Please specify...')
    goodfit = col2.text_input("Why are you a good fit for the job?", placeholder="Let Tidy decide?(Leave Blank)")
    st.write('')
    st.write('')
    submit_button = st.form_submit_button(label='GET COVER LETTER :robot_face:')

  if submit_button:
     #Here we write the generate cover letter function
     pass

  # prompt = ("Write a cover letter to " + contact_person + " from " + your_name +" for a " + role + " job at " + company_name +"." + " I have experience in " +personal_exp + " I am excited about the job because " +job_desc + " I am passionate about "+ passion)


