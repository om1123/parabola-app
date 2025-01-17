import streamlit as st
import numpy as np
import plotly.graph_objects as go

# App Configuration
st.set_page_config(page_title="Parabola Explorer", layout="wide")

# Title and Intro
st.title("🔷 Parabola Explorer 🔷")
st.markdown("**Explore and visualize parabolas in 2D and 3D!**")

# Sidebar Navigation
st.sidebar.header("Navigation")
section = st.sidebar.radio("Go to:", ["📈 2D Parabola", "🕶️ 3D Parabola", "✏️ Sketch Mode", "📐 Tangents & Derivatives", "🎬 Motion Physics", "📡 AR/VR View", "💾 Save & Share", "🌀 Multiple Parabolas"])

# Function to plot 2D parabola
def plot_2d_parabola(a, b, c):
    x = np.linspace(-1000, 1000, 400)
    y = a*x**2 + b*x + c
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Parabola', line=dict(color='cyan')))
    fig.update_layout(title="2D Parabola", xaxis_title="X-Axis", yaxis_title="Y-Axis", template="plotly_dark")
    return fig

# 2D Parabola Section
if section == "📈 2D Parabola":
    st.header("📈 Interactive 2D Parabola")
    col1, col2 = st.columns([1, 2])
    with col1:
        a = st.slider("Quadratic Coefficient (a)", -1000.0, 1000.0, 1.0)
        b = st.slider("Linear Coefficient (b)", -1000.0, 1000.0, 0.0)
        c = st.slider("Constant Term (c)", -1000.0, 1000.0, 0.0)
    with col2:
        st.plotly_chart(plot_2d_parabola(a, b, c))

# More sections will be added for 3D, Sketch Mode, Tangents, Motion, etc.

st.sidebar.info("More features coming soon! 🚀")
