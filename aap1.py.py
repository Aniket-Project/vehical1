#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import requests

def fetch_vehicle_info(reg_no):
    url = "https://rto-vehicle-information-verification-india.p.rapidapi.com/api/v1/rc/vehicleinfo"
    payload = {
        "reg_no": reg_no,
        "consent": "Y",
        "consent_text": "I hereby declare my consent agreement for fetching my information via AITAN Labs API"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "0dadfc164emshca05ae62b741445p1f3de6jsn00e22fa58b53",
        "X-RapidAPI-Host": "rto-vehicle-information-verification-india.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

st.title("Vehicle Information")
reg_no = st.text_input("Enter Vehicle Number")

if st.button("Fetch Details"):
    if reg_no:
        vehicle_info = fetch_vehicle_info(reg_no)
        st.json(vehicle_info)
    else:
        st.warning("Please enter a valid vehicle number.")

