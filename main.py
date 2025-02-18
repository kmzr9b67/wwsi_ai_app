# Korzystam z interpretera Conda 3.11.7

# Konfiguracja środowiska pracy zajęcia 1
import streamlit as st
import pandas as pd
import numpy as np

st.title('Moja pierwsza aplikacja w streamlit.')
st.write("None")

zmienna = st.slider("Wybierz cyfre:", 0, 100,50)
st.write(f'Wybirałes{zmienna}')