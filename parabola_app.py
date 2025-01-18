import streamlit as st
import numpy as np
import plotly.graph_objects as go
import re

# Bullet point navigation menu
st.sidebar.header("Navigation")
section = st.sidebar.radio(
    "Choose a section:",
    [
        "📈 2D Parabola",
        "📐 Tangent & Derivatives",
        "🕶️ 3D Parabola",
        "🎬 Motion Physics",
        "📡 AR/VR 3D View",
        "💾 Save & Share",
        "🌀 Multiple Parabolas"
    ]
)

# Function to plot 2D parabola with focus and directrix
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
    
    # Enhance grid lines (boxes) for better visibility
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

# Function to plot tangent and derivatives
def plot_tangent(a, tangent_x):
    x = np.linspace(-10, 10, 400)
    y = np.sqrt(4 * a * x)
    y_neg = -np.sqrt(4 * a * x)

    # Tangent line calculation
    slope = 2 * a * tangent_x
    tangent_y = slope * (x - tangent_x)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Parabola', line=dict(color='deepskyblue', width=3)))
    fig.add_trace(go.Scatter(x=x, y=y_neg, mode='lines', name='Lower Branch', line=dict(color='deepskyblue', width=3, dash='dot')))
    fig.add_trace(go.Scatter(x=x, y=tangent_y, mode='lines', name='Tangent Line', line=dict(color='green', dash='dash', width=2)))
    fig.add_trace(go.Scatter(x=[tangent_x], y=[slope * (tangent_x - tangent_x)], mode='markers', name='Tangent Point', marker=dict(color='red', size=10, symbol='x')))
    
    fig.update_layout(
        title="2D Parabola with Tangent Line",
        xaxis_title="X-Axis",
        yaxis_title="Y-Axis",
        template="plotly_dark",
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

# Tangent Section
elif section == "📐 Tangent & Derivatives":
    st.header("📐 Tangents & Derivatives")
    tangent_x = st.slider("Select the x-coordinate of the Tangent Point", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)
    a = st.number_input("Enter value for 'a' in y^2 = 4ax", value=1.0, step=0.1)
    
    fig = plot_tangent(a, tangent_x)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown(f"**Tangent at x = {tangent_x}:** y = {2*a*tangent_x}")

# 3D Parabola Section
elif section == "🕶️ 3D Parabola":
    st.header("🕶️ Interactive 3D Parabola")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        a = st.number_input("Enter value for 'a'", value=1.0, step=0.1)
        b = st.number_input("Enter value for 'b'", value=1.0, step=0.1)
        resolution = st.slider("Resolution", min_value=50, max_value=200, value=100, step=10, help="Higher values may decrease responsiveness.")
        
        fig = plot_3d_parabola(a, b, resolution)
        
        st.markdown(f"**Parsed Parameters:** a = {a}, b = {b}")
    
    with col2:
        st.plotly_chart(fig, use_container_width=True)

# Additional sections would be added in a similar way as above
