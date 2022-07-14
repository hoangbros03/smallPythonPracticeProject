from turtle import onkeypress
import streamlit as st
import pandas as pd
import numpy as np
import random
showResult = False
numberResult = -1
# declaring session_state variable that static through process
if 'historyOfRolling' not in st.session_state:
    st.session_state.historyOfRolling = []
if 'variableIfChosen' not in st.session_state:
    st.session_state.variableIfChosen = []
if "hideHistoryStatus" not in st.session_state:
    st.session_state.hideHistoryStatus = False

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")


st.write("Welcome to Dice Rolling System!")
#st.write("Firstly, type number of re-roll times you want (default is 1): ")
ReRollTimes = st.slider("Firstly, type number of re-roll times you want (default is 1): ",
                        1, 10, key="ReRollTimes")


if(st.button("Roll now!", help="Click here to roll")):
    for i in range(1, ReRollTimes+1):
        numberResult = random.randint(1, 6)
    st.write("The result is: " + str(numberResult))
    st.session_state.historyOfRolling.append(numberResult)


if(st.button("Hide/show history", help="Click here to hide the history of dice rolling") == st.session_state.hideHistoryStatus):
    st.write("The history of rolling is: " +
             str(', '.join(map(str, st.session_state.historyOfRolling))))
    st.session_state.hideHistoryStatus = False
else:
    st.write("History was hidden successfully")
    st.session_state.hideHistoryStatus = True

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

# download part


@st.cache
def convertToCSV(df):
    return df.to_csv().encode('UTF-8')


# this happen because only 1 static is enough. Shouldn't be use in other projects
myDictionaryDiceRolling = {}
for i in range(0, len(st.session_state.historyOfRolling)):
    myDictionaryDiceRolling[i] = st.session_state.historyOfRolling[i]
myDictionaryDiceRolling = pd.Series(myDictionaryDiceRolling)
my_csv = convertToCSV(myDictionaryDiceRolling)
st.download_button(
    label="Download history of results as csv",
    file_name="historyOfRolling.csv",
    mime="text/csv",
    data=my_csv
)
