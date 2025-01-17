import streamlit as st
import numpy as np
import plotly.graph_objects as go
import re

# App Configuration
st.set_page_config(page_title="Parabola Explorer", layout="wide")

# Title and Intro
st.title("🔷 Parabola Explorer 🔷")
st.markdown("**Explore and visualize parabolas in 2D and 3D!**")

# Sidebar Navigation
st.sidebar.header("Navigation")
section = st.sidebar.radio("Go to:", ["📈 2D Parabola", "🕶️ 3D Parabola", "✏️ Sketch Mode", "📐 Tangents & Derivatives", "🎬 Motion Physics", "📡 AR/VR View", "💾 Save & Share", "🌀 Multiple Parabolas"])

# Function to plot 2D parabola and show directrix & focus
def plot_2d_parabola(a, b, c):
    x = np.linspace(-1000, 1000, 400)
    y = a*x**2 + b*x + c
    
    # Calculate focus and directrix
    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    focus_x = vertex_x
    focus_y = vertex_y + (1 / (4 * a))
    directrix_y = vertex_y - (1 / (4 * a))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Parabola', line=dict(color='deepskyblue', width=3)))
    fig.add_trace(go.Scatter(x=[focus_x], y=[focus_y], mode='markers', name='Focus', marker=dict(color='red', size=12, symbol='x')))
    fig.add_trace(go.Scatter(x=[-1000, 1000], y=[directrix_y, directrix_y], mode='lines', name='Directrix', line=dict(color='gold', dash='dash', width=2)))
    
    # Enhance grid lines (boxes) for better visibility
    fig.update_xaxes(showgrid=True, gridwidth=2, gridcolor='white', zeroline=True, zerolinewidth=3, zerolinecolor='red')
    fig.update_yaxes(showgrid=True, gridwidth=2, gridcolor='white', zeroline=True, zerolinewidth=3, zerolinecolor='red')
    
    fig.update_layout(
        title="2D Parabola", 
        xaxis_title="X-Axis", 
        yaxis_title="Y-Axis", 
        template="plotly_dark", 
        height=600, width=800, 
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig, focus_x, focus_y, directrix_y

# 2D Parabola Section
if section == "📈 2D Parabola":
    st.header("📈 Interactive 2D Parabola")
    col1, col2 = st.columns([1, 2])
    with col1:
        equation = st.text_input("Enter quadratic equation (ax^2 + bx + c)", "x^2")
        match = re.match(r"([-+]?[0-9]*\.?[0-9]*)?x\^2\s*([-+]?[0-9]*\.?[0-9]*)?x?\s*([-+]?[0-9]*\.?[0-9]*)?", equation.replace(" ", ""))
        
        if match:
            a = float(match.group(1) or 1)
            b = float(match.group(2) or 0)
            c = float(match.group(3) or 0)
        else:
            st.error("Invalid equation format! Use ax^2 + bx + c")
            a, b, c = 1, 0, 0
        
        st.markdown(f"**Parsed Coefficients:** a = {a}, b = {b}, c = {c}")
    
    with col2:
        fig, focus_x, focus_y, directrix_y = plot_2d_parabola(a, b, c)
        st.plotly_chart(fig, use_container_width=True)
    
    with col1:
        st.markdown(f"**Focus:** ({focus_x:.2f}, {focus_y:.2f})")
        st.markdown(f"**Directrix:** y = {directrix_y:.2f}")

# More sections will be added for 3D, Sketch Mode, Tangents, Motion, etc.

st.sidebar.info("More features coming soon! 🚀")


