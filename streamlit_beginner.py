
# python -m streamlit run ./streamlit_beginner.py
import openai as ai
import json
import streamlit as st 
from PIL import Image

#tidy_image = Image.open('tidy_mobile.png')



print("** Loading API Key")
ai.api_key = "API KEY HERE"



with st.sidebar: 

    st.title("AI Cover Letter Generator🚀")
    st.subheader("A cover letter is a one-page document that you submit as part of your job application (alongside your CV or Resume). Its purpose is to introduce you and briefly summarize your professional background.")

with st.form(key='my_form_to_submit'):
    col1,col2 = st.columns(2)    
    first_name = col1.text_input("👤FIRST NAME: ", "John")
    last_name = col2.text_input("👤LAST NAME: ", "Doe")
    col1,col2,col3 = st.columns(3)
    email = col1.text_input("📧EMAIL ADDRESS ", "Johndoe@gmail.com")
    phone = col2.text_input("📞PHONE NUMBER", "0900-78601")
    country = col3.text_input("🏠COUNTRY ", "Austria")
    desired_pos = col1.text_input("👨DESIRED POSITION", "Data Scientist")
    experience = col2.number_input('💻YEARS of EXPERIENCE', 0, 25)
    experience_level = st.select_slider('EXPERIENCE LEVEL ', ['Fresh','Internee','Entry-Level', 'Junior', 'Senior'])
    option = st.selectbox(
    '💭SELECT TONE of VOICE',
    ("Authoritative","Caring","Funny","Cheerful","Coarse","Conservative","Conversational","Casual","Dry"))
    st.write("Why are you a good fit for the job?")
    #st.image(tidy_image)
    submit_button = st.form_submit_button(label='Let Tidy Decide For Me')
    

# prompt = ("Write a cover letter to " + contact_person + " from " + your_name +" for a " + role + " job at " + company_name +"." + " I have experience in " +personal_exp + " I am excited about the job because " +job_desc + " I am passionate about "+ passion)

if submit_button:
    tab1, tab2, tab3 = st.tabs(["Sample 1", "Sample 2", "Sample 3"])
    tab1.markdown("This is the first Sample Cover Letter by AI")
    tab2.markdown("This is the second Sample Cover Letter by AI")
    tab3.markdown("This is the third Sample Cover Letter by AI")
