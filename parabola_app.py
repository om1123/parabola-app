import streamlit as st
import numpy as np
import plotly.graph_objects as go
import re

# Add "Developed by Om" at the top
st.markdown("""
    <div style="text-align: center; font-size: 24px; font-weight: bold; color: darkblue;">
        Developed by Om
    </div>
""", unsafe_allow_html=True)

# Your existing app code
# Function to plot 2D Parabola
def plot_2d_parabola(a):
    # Your existing code here...
    pass

# Section selection in the sidebar
section = st.sidebar.selectbox(
    "Choose the Section",
    ("📈 2D Parabola", "🕶️ 3D Parabola", "📐 Tangents & Derivatives")
)

# Add your existing sections here...
# 2D Parabola Section
if section == "📈 2D Parabola":
    st.header("📈 Interactive 2D Parabola")
    # Your existing code here...
    
# 3D Parabola Section
if section == "🕶️ 3D Parabola":
    st.header("🕶️ Interactive 3D Parabola")
    # Your existing code here...

# Tangents Section
elif section == "📐 Tangents & Derivatives":
    st.header("📐 Tangents & Derivatives")
    # Your existing code here...
