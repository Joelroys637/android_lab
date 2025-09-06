import streamlit as st
import java as ap

org_name="admin"
org_pass="password"
username = st.text_input("Username", placeholder="Enter Username")
password = st.text_input("Password", type="password", placeholder="Enter Password")

if st.button("login"):
    if org_name==username:
        if org_pass==password:
            ap.main()
        else:
            st.error("password is worng ")
    else:
        st.error("username is worng")
