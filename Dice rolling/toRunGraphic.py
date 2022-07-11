

"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np
import random
showResult = False
numberResult = -1
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")


def testFunction():

    pass


st.write("Welcome to Dice Rolling System!")
#st.write("Firstly, type number of re-roll times you want (default is 1): ")
ReRollTimes = st.slider("Firstly, type number of re-roll times you want (default is 1): ",
                        1, 10, key="ReRollTimes")

if (st.button("Roll now!")):
    for i in range(1, ReRollTimes+1):
        numberResult = random.randint(1, 6)
    st.write("The result is: " + str(numberResult))

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
add_typeInforLabel = st.sidebar.text_input(
    label="Type your contact information here!")
# Add a slider to the sidebar:
