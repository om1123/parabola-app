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
section = st.sidebar.radio("Go to:", ["📈 2D Parabola", "🕶️ 3D Parabola", "📡 AR/VR View"])

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
if section == "📡 AR/VR View":
    st.header("📡 3D Parabola in AR/VR")

    # Detect if the user is on a mobile device for AR/VR features
    if st.experimental_get_query_params().get('mobile', None):
        option = st.radio("Choose View:", ["AR View", "VR View"])

        if option == "AR View":
            st.markdown("""
            <a-scene embedded arjs>
                <!-- Placeholder AR content, you can add your 3D model here -->
                <a-box position="0 0.5 -3" rotation="0 45 0" color="#4CC3D9"></a-box>
            </a-scene>
            """, unsafe_allow_html=True)

        elif option == "VR View":
            st.markdown("""
            <a-scene embedded vr-mode-ui>
                <!-- Placeholder VR content, you can add your 3D model here -->
                <a-box position="0 0.5 -3" rotation="0 45 0" color="#4CC3D9"></a-box>
            </a-scene>
            """, unsafe_allow_html=True)

    else:
        # Desktop 3D Plot: Displaying a Plotly 3D graph for desktop
        st.markdown("**3D Parabola for Desktop**")
        fig_3d = plot_2d_parabola(1)[0]  # Use 2D plot as placeholder for 3D parabola
        st.plotly_chart(fig_3d, use_container_width=True)

# Sidebar Info
st.sidebar.info("More features coming soon! 🚀")
