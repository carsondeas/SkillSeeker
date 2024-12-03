import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Student, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Skill Tracking', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Persona1_Screen1.py')

if st.button('Skill Comparison', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Persona1_Screen2.py')