import pandas as pd
import streamlit as st
from my_Sidebar import Sidebar
import csv

st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🔢",)

#Sidebar
Sidebar.Decorate()
Sidebar.mail()

#Function
def addtohistory():
    columns = ['Operation', '1st Number', '2nd Number', 'Result']
    with open('my_csv/calculator_history.csv', 'a') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(columns)
        writer.writerow([operation, num1, num2, result])

def clear_history():
    empty_df = pd.DataFrame(columns=['Operation', '1st Number', '2nd Number', 'Result'])
    empty_df.to_csv('my_csv/calculator_history.csv', index=False)
    st.success('History cleared successfully! Please refresh the page.')

#Calculator
st.title('Simple Calculator')
num1 = st.number_input('Enter the first number:', step=1)
num2 = st.number_input('Enter the second number:', step=1)
operation = st.selectbox('Select an operation', ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponents'])

if operation == 'Addition':
    result = num1 + num2
elif operation == 'Subtraction':
    result = num1 - num2
elif operation == 'Multiplication':
    result = num1 * num2
elif operation == 'Division':
    if num2 == 0:
        st.error('Division by zero is not allowed')
    else:
        result = num1 / num2
else:
    result = num1 ** num2
if st.button('Calculate'):
    if operation != 'Division' or num2 != 0:
        st.success(f'{operation} of {num1} and {num2} is {result}')
        addtohistory()

#History
st.subheader('Calculator History')
history = pd.read_csv('my_csv/calculator_history.csv')
st.dataframe(history, use_container_width=True)
if st.button('Clear History'):
    clear_history()