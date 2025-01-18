import streamlit as st
import numpy as np
import plotly.graph_objects as go
import re

# Function to plot 2D Parabola with tangent line
def plot_2d_parabola_with_tangent(a, tangent_x):
    x = np.linspace(-10, 10, 400)  # Set the range from -10 to 10
    y = np.sqrt(4 * a * x)
    y_neg = -np.sqrt(4 * a * x)  # Lower branch for better visualization
    
    # Calculate tangent line at the given x
    tangent_y = 2 * a * tangent_x  # Derivative of y = sqrt(4ax) gives dy/dx = 2a
    tangent_y_neg = -2 * a * tangent_x  # For the lower branch
    
    # Tangent line equation: y = m(x - x0) + y0, where m is the slope
    slope = 2 * a * tangent_x  # Derivative of the parabola at the point
    tangent_line_y = slope * (x - tangent_x) + np.sqrt(4 * a * tangent_x)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Parabola', line=dict(color='deepskyblue', width=3)))
    fig.add_trace(go.Scatter(x=x, y=y_neg, mode='lines', name='Lower Branch', line=dict(color='deepskyblue', width=3, dash='dot')))
    fig.add_trace(go.Scatter(x=[tangent_x], y=[np.sqrt(4 * a * tangent_x)], mode='markers', name='Tangent Point', marker=dict(color='red', size=12, symbol='x')))
    fig.add_trace(go.Scatter(x=x, y=tangent_line_y, mode='lines', name='Tangent Line', line=dict(color='yellow', width=3, dash='dash')))
    
    fig.update_xaxes(
        showgrid=True, gridwidth=2, gridcolor='white', zeroline=True, zerolinewidth=3, zerolinecolor='red',
        range=[-10, 10]  # Set x-axis range to [-10, 10]
    )
    fig.update_yaxes(
        showgrid=True, gridwidth=2, gridcolor='white', zeroline=True, zerolinewidth=3, zerolinecolor='red',
        range=[-10, 10]  # Set y-axis range to [-10, 10]
    )
    
    fig.update_layout(
        title="2D Parabola with Tangent", 
        xaxis_title="X-Axis", 
        yaxis_title="Y-Axis", 
        template="plotly_dark", 
        height=600, width=800, 
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

# Function to plot 3D Paraboloid with resolution control
def plot_3d_parabola(a, b, resolution=100):
    x = np.linspace(-10, 10, resolution)
    y = np.linspace(-10, 10, resolution)
    x, y = np.meshgrid(x, y)
    
    z = a * x**2 + b * y**2
    
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis', cmin=-100, cmax=100)])
    
    fig.update_layout(
        title="3D Paraboloid",
        scene=dict(
            xaxis_title="X-Axis",
            yaxis_title="Y-Axis",
            zaxis_title="Z-Axis"
        ),
        template="plotly_dark",
        height=600, width=800,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

# Section selection in the sidebar
section = st.sidebar.selectbox(
    "Choose the Section",
    ("📈 2D Parabola", "🕶️ 3D Parabola")
)

# 2D Parabola Section with Tangent Feature
if section == "📈 2D Parabola":
    st.header("📈 Interactive 2D Parabola with Tangent")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        equation = st.text_input("Enter the equation of the parabola (y² = 4ax)", "y^2=4x")
        match = re.match(r"y\^2=4\*?([-+]?[0-9]*\.?[0-9]*)x", equation.replace(" ", ""))
        
        if match:
            a = float(match.group(1) or 1)
        else:
            st.error("Invalid equation format! Use y² = 4ax")
            a = 1
        
        # Tangent Point Selection
        tangent_x = st.slider("Select the x-coordinate of the Tangent Point", min_value=-10, max_value=10, value=0, step=0.1)
        
        fig = plot_2d_parabola_with_tangent(a, tangent_x)
        
        st.markdown(f"**Parsed Parameter:** a = {a}")
        st.markdown(f"**Tangent Point:** x = {tangent_x}")
    
    with col2:
        st.plotly_chart(fig, use_container_width=True)

# 3D Parabola Section with Resolution Slider
if section == "🕶️ 3D Parabola":
    st.header("🕶️ Interactive 3D Parabola")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Inputs for 3D parabola equation (z = ax^2 + by^2)
        a = st.number_input("Enter value for 'a'", value=1.0, step=0.1)
        b = st.number_input("Enter value for 'b'", value=1.0, step=0.1)
        
        # Resolution slider to control plot responsiveness
        resolution = st.slider("Resolution", min_value=50, max_value=200, value=100, step=10, help="Higher values may decrease responsiveness.")
        
        # Generate the 3D plot with the provided parameters and resolution
        fig = plot_3d_parabola(a, b, resolution)
        
        st.markdown(f"**Parsed Parameters:** a = {a}, b = {b}")
    
    with col2:
        st.plotly_chart(fig, use_container_width=True)
