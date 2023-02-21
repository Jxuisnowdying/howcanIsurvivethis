import streamlit as st
from datetime import date, datetime

def Decorate():
    time = datetime.now()
    st.sidebar.metric(label=date.today().strftime('%B %d, %Y'), value=time.strftime('%H:%M'))
    st.sidebar.image('my_Sidebar/mycat.gif')

def submit():
    st.session_state.feedback = st.session_state.widget
    st.session_state.widget = ''

def feedback():
    st.sidebar.subheader('Feedback')
    if 'feedback' not in st.session_state:
        st.session_state.feedback = ''
    st.sidebar.text_area('Feel free to sent me a feedback here!', key='widget', on_change=submit)
    if st.sidebar.button('Submit'):
        st.sidebar.success('Feedback received, thank you for your feedback!')
        with open('feedback.txt', 'a')as f:
            f.write(st.session_state.feedback + '\n')
