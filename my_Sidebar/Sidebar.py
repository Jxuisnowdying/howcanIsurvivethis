import streamlit as st
from datetime import *

def Decorate():
    tz = timezone(timedelta(hours=7))
    time = datetime.now()
    new_time = time.astimezone(tz)
    st.sidebar.metric(label=date.today().strftime('%B %d, %Y'), value=new_time.strftime('%H:%M'))
    st.sidebar.image('my_Sidebar/mycat.gif')

def mail():
    st.sidebar.subheader('Feedback')
    st.sidebar.text('Feel free to sent me a feedback!')
    contact_form = """
    <form action="https://formsubmit.co/8f853b9be805e09053f21f3b64698a59" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.sidebar.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.sidebar.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


    local_css('my_style/style.css')