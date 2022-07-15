from turtle import onkeypress
import streamlit as st
import pandas as pd
import numpy as np
import random
showResult = False
numberResult = -1
testingMultipleTimes = 50
# declaring session_state variable that static through process
if 'historyOfRolling' not in st.session_state:
    st.session_state.historyOfRolling = []
if 'variableIfChosen' not in st.session_state:
    st.session_state.variableIfChosen = []
if "hideHistoryStatus" not in st.session_state:
    st.session_state.hideHistoryStatus = False
if "hideDictStatus" not in st.session_state:
    st.session_state.hideDictStatus = False
if "hideBarChartStatus" not in st.session_state:
    st.session_state.hideBarChartStatus = False
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")


st.write("Welcome to Dice Rolling System!")
#st.write("Firstly, type number of re-roll times you want (default is 1): ")
ReRollTimes = st.slider("Firstly, type number of re-roll times you want (default is 1): ",
                        1, 10, key="ReRollTimes")

col1, col2 = st.columns([1, 1])
with col1:
    if(st.button("Roll now!", help="Click here to roll")):
        for i in range(0, testingMultipleTimes):
            for i in range(1, ReRollTimes+1):
                numberResult = random.randint(1, 6)

            st.session_state.historyOfRolling.append(numberResult)
        st.write("The lastest result is: " + str(numberResult))
with col2:
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

mySeriesDiceRolling = pd.Series(myDictionaryDiceRolling)
my_csv = convertToCSV(mySeriesDiceRolling)
st.download_button(
    label="Download history of results as csv",
    file_name="historyOfRolling.csv",
    mime="text/csv",
    data=my_csv
)

# graphic section


def getFrequent(index, array):
    frequent = 0
    for i in range(0, len(array)):
        if array[i] == index:
            frequent += 1
    return frequent


barChartDiceRolling = {}
for i in range(1, 7):
    barChartDiceRolling[str(i)] = getFrequent(i, myDictionaryDiceRolling)
myCharDiceRolling = pd.DataFrame.from_dict(barChartDiceRolling, orient='index')

st.write(st.session_state.hideDictStatus)
st.write("Below is bar charts")
st.write(st.session_state.hideBarChartStatus)
if(st.button("Show/hide frequency by dictionary") == st.session_state.hideDictStatus):
    st.write("Frequency by dictionary: ")
    st.write(barChartDiceRolling)
    st.session_state.hideDictStatus = True
else:
    st.write("Dict was hidden successfully.")
    st.session_state.hideDictStatus = False

if(st.button("Show/hide frequency by bar chart") == st.session_state.hideBarChartStatus):
    st.write("Frequency by bar chart: ")
    st.bar_chart(myCharDiceRolling)
    st.session_state.hideBarChartStatus = True
else:
    st.write("Bar chart was hidden successfully.")
    st.session_state.hideBarChartStatus = False
