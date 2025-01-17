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
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Parabola', line=dict(color='cyan')))
    fig.add_trace(go.Scatter(x=[focus_x], y=[focus_y], mode='markers', name='Focus', marker=dict(color='red', size=10)))
    fig.add_trace(go.Scatter(x=[-1000, 1000], y=[directrix_y, directrix_y], mode='lines', name='Directrix', line=dict(color='yellow', dash='dash')))
    
    # Add grid lines (boxes)
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='gray', zeroline=True, zerolinewidth=2, zerolinecolor='white')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='gray', zeroline=True, zerolinewidth=2, zerolinecolor='white')
    
    fig.update_layout(title="2D Parabola", xaxis_title="X-Axis", yaxis_title="Y-Axis", template="plotly_dark")
    return fig, focus_x, focus_y, directrix_y

# 2D Parabola Section
if section == "📈 2D Parabola":
    st.header("📈 Interactive 2D Parabola")
    col1, col2 = st.columns([1, 2])
    with col1:
        a = st.slider("Quadratic Coefficient (a)", -1000.0, 1000.0, 1.0)
        b = st.slider("Linear Coefficient (b)", -1000.0, 1000.0, 0.0)
        c = st.slider("Constant Term (c)", -1000.0, 1000.0, 0.0)
    with col2:
        fig, focus_x, focus_y, directrix_y = plot_2d_parabola(a, b, c)
        st.plotly_chart(fig)
        st.markdown(f"**Focus:** ({focus_x:.2f}, {focus_y:.2f})")
        st.markdown(f"**Directrix:** y = {directrix_y:.2f}")

# More sections will be added for 3D, Sketch Mode, Tangents, Motion, etc.

st.sidebar.info("More features coming soon! 🚀")
