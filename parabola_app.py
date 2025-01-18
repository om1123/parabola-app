import streamlit as st
import numpy as np
import plotly.graph_objects as go
import re
import os

# App Configuration
st.set_page_config(page_title="Parabola Explorer", layout="wide")

# Title and Intro
st.title("🔷 Parabola Explorer 🔷")
st.markdown("**Explore and visualize parabolas in 2D and 3D!**")

# Sidebar Navigation
st.sidebar.header("Navigation")
section = st.sidebar.radio("Go to:", ["📈 2D Parabola", "🕶️ 3D Parabola", "✏️ Sketch Mode", "📐 Tangents & Derivatives", "🎬 Motion Physics", "📡 AR/VR View", "💾 Save & Share", "🌀 Multiple Parabolas"])

# Function to plot 2D parabola and show directrix & focus
def plot_2d_parabola(a):
    x = np.linspace(-10, 10, 400)  # Set the range from -10 to 10
    y = np.sqrt(4 * a * x)
    y_neg = -np.sqrt(4 * a * x)  # Lower branch for better visualization
    
    # Calculate focus and directrix
    focus_x, focus_y = (a, 0)
    directrix_x = -a
    
    # Calculate additional properties
    axis_of_symmetry = "x = 0"
    directrix_equation = f"x = {-a}"
    latus_rectum_length = 4 * a
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Parabola', line=dict(color='deepskyblue', width=3)))
    fig.add_trace(go.Scatter(x=x, y=y_neg, mode='lines', name='Lower Branch', line=dict(color='deepskyblue', width=3, dash='dot')))
    fig.add_trace(go.Scatter(x=[focus_x], y=[focus_y], mode='markers', name='Focus', marker=dict(color='red', size=12, symbol='x')))
    fig.add_trace(go.Scatter(x=[directrix_x, directrix_x], y=[-10, 10], mode='lines', name='Directrix', line=dict(color='gold', dash='dash', width=2)))
    
    fig.update_xaxes(
        showgrid=True, gridwidth=2, gridcolor='white', zeroline=True, zerolinewidth=3, zerolinecolor='red',
        range=[-10, 10]  # Set x-axis range to [-10, 10]
    )
    fig.update_yaxes(
        showgrid=True, gridwidth=2, gridcolor='white', zeroline=True, zerolinewidth=3, zerolinecolor='red',
        range=[-10, 10]  # Set y-axis range to [-10, 10]
    )
    
    fig.update_layout(
        title="2D Parabola", 
        xaxis_title="X-Axis", 
        yaxis_title="Y-Axis", 
        template="plotly_dark", 
        height=600, width=800, 
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig, focus_x, focus_y, directrix_x, axis_of_symmetry, directrix_equation, latus_rectum_length

# Function to plot 3D parabola
def plot_3d_parabola():
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    x, y = np.meshgrid(x, y)
    z = x**2 + y**2  # Parabola equation
    
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis')])
    fig.update_layout(
        title="3D Parabola",
        scene=dict(
            xaxis=dict(title='X-Axis'),
            yaxis=dict(title='Y-Axis'),
            zaxis=dict(title='Z-Axis')
        ),
        height=600, width=800
    )
    return fig

# 2D Parabola Section
if section == "📈 2D Parabola":
    st.header("📈 Interactive 2D Parabola")
    col1, col2 = st.columns([1, 2])
    with col1:
        equation = st.text_input("Enter the equation of the parabola (y² = 4ax)", "y^2=4x")
        match = re.match(r"y\^2=4\*?([-+]?[0-9]*\.?[0-9]*)x", equation.replace(" ", ""))
        
        if match:
            a = float(match.group(1) or 1)
        else:
            st.error("Invalid equation format! Use y² = 4ax")
            a = 1
        
        fig, focus_x, focus_y, directrix_x, axis_of_symmetry, directrix_equation, latus_rectum_length = plot_2d_parabola(a)
        
        st.markdown(f"**Parsed Parameter:** a = {a}")
        st.markdown(f"**Focus:** ({a:.2f}, 0)")
        st.markdown(f"**Directrix Equation:** {directrix_equation}")
        st.markdown(f"**Axis of Symmetry:** {axis_of_symmetry}")
        st.markdown(f"**Latus Rectum Length:** {latus_rectum_length:.2f}")
    
    with col2:
        st.plotly_chart(fig, use_container_width=True)

# 3D Parabola Section with AR/VR option
if section == "🕶️ 3D Parabola":
    st.header("🕶️ Interactive 3D Parabola")
    
    # Show 3D Plotly Graph
    fig_3d = plot_3d_parabola()
    st.plotly_chart(fig_3d, use_container_width=True)

# AR/VR Section
if section == "📡 AR/VR View":
    st.header("📡 3D Parabola in AR/VR")
    
    # Toggle between AR/VR view
    option = st.radio("Choose View:", ["AR View (Mobile)", "VR View (Mobile)", "Desktop 3D Plot"])
    
    if option == "AR View (Mobile)":
        # AR View using A-Frame
        st.markdown("""
        <a-scene embedded arjs>
            <!-- 3D Parabola Model -->
            <a-entity gltf-model="url(3d_parabola_model.gltf)" scale="1 1 1" position="0 0 0" rotation="0 0 0"></a-entity>
        </a-scene>
        """, unsafe_allow_html=True)

    elif option == "VR View (Mobile)":
        # VR View using A-Frame (similar approach as AR)
        st.markdown("""
        <a-scene embedded vr-mode-ui>
            <!-- 3D Parabola Model -->
            <a-entity gltf-model="url(3d_parabola_model.gltf)" scale="1 1 1" position="0 0 0" rotation="0 0 0"></a-entity>
        </a-scene>
        """, unsafe_allow_html=True)

    elif option == "Desktop 3D Plot":
        # Show 3D Plotly Graph for Desktop users
        fig_3d = plot_3d_parabola()
        st.plotly_chart(fig_3d, use_container_width=True)

# Sidebar Info
st.sidebar.info("More features coming soon! 🚀")
