import streamlit as st
import numpy as np
import plotly.graph_objects as go
import re
import matplotlib.pyplot as plt
st.markdown("""
    <div style="text-align: center; font-size: 24px; font-weight: bold; color: blue;">
        Developed by Om
    </div>
""", unsafe_allow_html=True)

if section == "📈 2D Parabola":
    st.header("📈 Interactive 2D Parabola")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Input equation of the parabola
        equation = st.text_input("Enter the equation of the parabola (y² = 4ax)", "y^2=4x")
        
        # Match and extract the constant on the right side of the equation
        match = re.match(r"y\^2=([-+]?[0-9]*\.?[0-9]*)", equation.replace(" ", ""))
        
        if match:
            constant = float(match.group(1))
            a = constant / 4  # Compute 'a' from the constant
        else:
            st.error("Invalid equation format! Use y² = 4ax or y^2 = constant.")
            a = 1  # Default value of 'a'
        
        # Call the updated plot function
        fig, focus_x, focus_y, directrix_x, axis_of_symmetry, directrix_equation, latus_rectum_length = plot_2d_parabola(a)
        
        # Display computed values
        st.markdown(f"**Parsed Parameter:** a = {a}")
        st.markdown(f"**Focus:** ({a:.2f}, 0)")
        st.markdown(f"**Directrix Equation:** {directrix_equation}")
        st.markdown(f"**Axis of Symmetry:** {axis_of_symmetry}")
        st.markdown(f"**Latus Rectum Length:** {latus_rectum_length:.2f}")
    
    with col2:
        # Display the plot
        st.plotly_chart(fig, use_container_width=True)



# Section selection in the sidebar
section = st.sidebar.selectbox(
    "Choose the Section",
    ("📈 2D Parabola", "🕶️ 3D Parabola", "📐 Tangents & Derivatives")
)

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

# 3D Parabola Section with Resolution Slider
elif section == "🕶️ 3D Parabola":
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

# Tangent Section
elif section == "📐 Tangents & Derivatives":
    st.header("📐 Tangents & Derivatives")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        a = st.slider('Value of a', -10, 10, 1)
        b = st.slider('Value of b', -10, 10, 0)
        c = st.slider('Value of c', -10, 10, 0)
        
        # Derivative calculation
        def derivative(x, a, b):
            return 2 * a * x + b
        
        # Select x-coordinate for the tangent
        x_tangent = st.slider('Select x-value for tangent', -10, 10, 0)
        y_tangent = a * x_tangent**2 + b * x_tangent + c
        slope_tangent = derivative(x_tangent, a, b)
        
        # Display the equation of the parabola and tangent line
        st.markdown(f"**Parabola Equation:** y = {a}x² + {b}x + {c}")
        st.markdown(f"**Tangent Point:** ({x_tangent}, {y_tangent})")
        st.markdown(f"**Slope of Tangent Line:** {slope_tangent}")

    with col2:
        # Plotting the parabola and tangent line using Matplotlib
        x = np.linspace(-10, 10, 400)
        fig_tangent, ax_tangent = plt.subplots()
        ax_tangent.plot(x, a * x**2 + b * x + c, label=f'y = {a}x² + {b}x + {c}')
        ax_tangent.plot(x_tangent, y_tangent, 'ro', label="Tangent Point")
        ax_tangent.plot(x, slope_tangent * (x - x_tangent) + y_tangent, label="Tangent Line")
        ax_tangent.legend()
        st.pyplot(fig_tangent)
