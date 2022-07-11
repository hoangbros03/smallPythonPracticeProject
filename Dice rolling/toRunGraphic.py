

"""
# My first app
Here's our first attempt at using data to create a table:
"""

from turtle import onkeypress
import streamlit as st
import pandas as pd
import numpy as np
import random
showResult = False
numberResult = -1
if 'historyOfRolling' not in st.session_state:
    st.session_state.historyOfRolling = ""
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")


def testFunction():

    pass


st.write("Welcome to Dice Rolling System!")
#st.write("Firstly, type number of re-roll times you want (default is 1): ")
ReRollTimes = st.slider("Firstly, type number of re-roll times you want (default is 1): ",
                        1, 10, key="ReRollTimes")


if(st.button("Roll now!")):
    for i in range(1, ReRollTimes+1):
        numberResult = random.randint(1, 6)
    st.write("The result is: " + str(numberResult))
    if(len(st.session_state.historyOfRolling) == 0):
        st.session_state.historyOfRolling = st.session_state.historyOfRolling + \
            str(numberResult)
    else:
        st.session_state.historyOfRolling = st.session_state.historyOfRolling + \
            ", " + str(numberResult)


st.write("The history of rolling is: " +
         str(st.session_state.historyOfRolling))

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_typeInforLabel = st.sidebar.text_input(
    label="Type your contact information here!")
if(st.sidebar.button("Submit my information")):
    if(add_typeInforLabel):
        st.sidebar.write("Thanks for submitting!")
    else:
        st.sidebar.write("Please input your information!")


# Add a slider to the sidebar:
