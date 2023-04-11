import streamlit as st
import numpy as np
import pandas as pd

st.title('My first app')

map_data = pd.DataFrame(
    np.random.randn(500,2) / [50,50] + [35.7, 139.69],
    columns = ['lat','lon']
)

st.map(map_data)