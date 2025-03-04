from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
template = PromptTemplate(
    template='''
    You are cricket expert and have vast knowledge of cricket and cricketers. 
    Please tell some facts about {selected_cricketer}'s {selected_topic} life. 
    If personal life selected then it should not include about cricket.
    Please have some careful tone and  be careful about cricketers life and do not include controversial facts. 
    Your response should be containing as many facts available in your knowledge and rank them based on the most suitable one to least.
    Your response should start with some basic information about cricketer such as country played for, birth country, last match played include which is that such as ODI, Test or T20, and position and last fun-facts it should be in bullet points. If information or facts not available then write "Insufficient Information"
    Here is the format for response: 
    Birth Place: 
    Country: 
    Position:
    Last Match Played:
    FunFact: 
    ''',
    input_variables=['selected_cricketer', 'selected_topic'],
)
st.set_page_config(
    page_title="Cricketer Facts",
    page_icon="🏏",
    layout="wide"
)
st.header("FunFacts about Cricketers")
st.write("#### Get some facts about cricketers professional and personal life.")
cricketers = [
    "Virat Kohli", "Sachin Tendulkar", "MS Dhoni", "Ricky Ponting", "Jacques Kallis",
    "Muttiah Muralitharan", "Brian Lara", "AB de Villiers", "Steve Smith", "Kumar Sangakkara",
    "Rahul Dravid", "Glenn McGrath", "Dale Steyn", "Shane Warne", "Wasim Akram",
    "Brett Lee", "Chris Gayle", "Yuvraj Singh", "Anil Kumble", "Adam Gilchrist",
    "Michael Clarke", "James Anderson", "Joe Root", "Kane Williamson", "Ben Stokes",
    "Shaun Pollock", "Lasith Malinga", "Sunil Gavaskar", "Sourav Ganguly", "David Warner",
    "Mitchell Starc", "Jasprit Bumrah", "Shubman Gill", "Babar Azam", "Rohit Sharma",
    "Hardik Pandya", "Shikhar Dhawan", "Pat Cummins", "Faf du Plessis", "Hashim Amla",
    "Virender Sehwag", "Mohammed Shami", "Andre Russell", "Ravindra Jadeja", "Jason Holder",
    "Graeme Smith", "Ross Taylor", "Eoin Morgan", "Alastair Cook", "Kevin Pietersen"
]

col1, col2 = st.columns(2)
with col1:
    selected_cricketer = st.selectbox("Select a cricketer:", cricketers)
with col2:
    selected_topic = st.selectbox("Select Topic:", ["Professional", "Personal"])
if st.button("Get Facts!"):
    chain = template | model
    result = chain.invoke({
        "selected_cricketer": selected_cricketer,
        "selected_topic": selected_topic
    })

    st.write(result.content)
