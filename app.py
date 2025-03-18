import streamlit as st
import re

st.title("Password Strength Meter 🦾🦾")
st.markdown("### An App where you can test your password if it is strong enough or not")

password = st.text_input("Enter Your Password", type='password' )

feedback_for_user = []

user_score = 0

if (password):

    if (len(password) >= 8 ):
        user_score += 1
    else :
         feedback_for_user.append("👉 Password Must contain atleast 8 Letters 👀")

    if (re.search (r"[A-Z]", password) and re.search (r"[a-z]", password)):
        user_score += 1
    else :
        feedback_for_user.append ("👉 Password must contain atleast one Uppercase and one Lowercase Letter")

    if (re.search (r'\d', password) ):
        user_score += 1
    else :
       feedback_for_user.append ("👉 Password must contain atleast one Digit")

    if (re.search (r"[!@#$%&-_]", password)):
        user_score += 1
    else :
        feedback_for_user.append ("👉 Password must contain one special Charecter")

    if (user_score == 4):
        feedback_for_user.append ("🟢 Your Password is Strong 🎉")
    elif (user_score == 3):
        feedback_for_user.append ("🟡Your Password has medium strength! It could get better ✨")
    else :
        feedback_for_user.append("🔴 Your Password is Weak ")

    st.markdown("## Improvement Tips")

    if (feedback_for_user):
        for tips in feedback_for_user:
            st.write(tips)



else :
    st.info("Please Enter your Password to get Started")