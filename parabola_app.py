import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from streamlit_drawable_canvas import st_canvas
import re

# Streamlit App Title
st.set_page_config(page_title="Interactive Parabola Web App", layout="wide")
st.title("🎯 Interactive Parabola Web App")

# Sidebar Controls
st.sidebar.header("🎨 Customize Your Parabola")

# Option for Custom Equation Input
equation_input = st.sidebar.text_input("Enter your Parabola Equation", value="y = x²")

# Function to parse and extract coefficients from equation
def parse_equation(equation):
    match = re.match(r"y = ([-+]?\d*\.?\d*)x\²\s*([+-]?\d*\.?\d*)x\s*([+-]?\d*\.?\d*)", equation.replace(" ", ""))
    if match:
        a = float(match.group(1)) if match.group(1) != '' else 1.0
        b = float(match.group(2)) if match.group(2) != '' else 0.0
        c = float(match.group(3)) if match.group(3) != '' else 0.0
    else:
        # Default to y = x² if equation is invalid
        a, b, c = 1.0, 0.0, 0.0
    return a, b, c

# Parse the equation
a, b, c = parse_equation(equation_input)

# Function to calculate parabola
def calculate_parabola(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    
    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    focus_x = vertex_x
    focus_y = vertex_y + 1 / (4 * a)
    directrix_y = vertex_y - 1 / (4 * a)
    
    return x, y, (vertex_x, vertex_y), (focus_x, focus_y), directrix_y

# Get calculated values
x, y, vertex, focus, directrix_y = calculate_parabola(a, b, c)

# ** Layout Structure **
col1, col2 = st.columns([1, 2])  # Columns for UI organization

# Real-time Equation Feedback
with col1:
    st.subheader("Real-time Equation Feedback")
    equation_preview = f"y = {a}x² + {b}x + {c}"
    st.write(f"**Current Equation:** {equation_preview}")

# Parabola Properties
with col1:
    st.subheader("Parabola Properties")
    st.write(f"**Vertex:** ({vertex[0]:.2f}, {vertex[1]:.2f})")
    st.write(f"**Focus:** ({focus[0]:.2f}, {focus[1]:.2f})")
    st.write(f"**Directrix:** y = {directrix_y:.2f}")
    st.write(f"**Axis of Symmetry:** x = {vertex[0]:.2f}")

# 🎨 2D Interactive Parabola Plot with Plotly
with col2:
    st.subheader("📊 2D Interactive Parabola")
    fig = go.Figure()

    # Adding the parabola trace
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'y = {a}x² + {b}x + {c}', line=dict(color='blue')))
    
    # Adding vertex and focus points
    fig.add_trace(go.Scatter(x=[vertex[0]], y=[vertex[1]], mode='markers', name=f'Vertex ({vertex[0]:.2f}, {vertex[1]:.2f})', marker=dict(color='red')))
    fig.add_trace(go.Scatter(x=[focus[0]], y=[focus[1]], mode='markers', name=f'Focus ({focus[0]:.2f}, {focus[1]:.2f})', marker=dict(color='green')))

    # Directrix line
    fig.add_trace(go.Scatter(x=x, y=[directrix_y]*len(x), mode='lines', name=f'Directrix y={directrix_y:.2f}', line=dict(color='orange', dash='dash')))

    # Axis of symmetry
    fig.add_trace(go.Scatter(x=[vertex[0]]*2, y=[min(y), max(y)], mode='lines', name=f'Axis of Symmetry x={vertex[0]:.2f}', line=dict(color='purple', dash='dot')))

    # Updating layout
    fig.update_layout(
        title=f"Interactive Parabola: y = {a}x² + {b}x + {c}",
        xaxis_title="X-axis",
        yaxis_title="Y-axis",
        showlegend=True,
        template="plotly_dark"
    )

    # Display the plot
    st.plotly_chart(fig, use_container_width=True)

# 🌀 3D Paraboloid Visualization
with col2:
    st.subheader("🌀 3D Paraboloid Visualization")
    x_vals = np.linspace(-5, 5, 50)
    y_vals = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = a * (X**2 + Y**2)

    fig_3d = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale="Viridis")])
    fig_3d.update_layout(title="3D Paraboloid", scene=dict(xaxis_title="X-axis", yaxis_title="Y-axis", zaxis_title="Z-axis"))
    st.plotly_chart(fig_3d, use_container_width=True)

# 🎨 Interactive Drawing Mode
st.subheader("✍️ Draw Your Own Parabola")
draw_mode = st.checkbox("Enable Drawing Mode ✏️")
if draw_mode:
    st.write("Click and drag on the canvas to draw your own parabola!")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=3,
        stroke_color="black",
        background_color="white",
        height=300,
        width=600,
        drawing_mode="freedraw",
        key="canvas",
    )

# Additional Interactions: Sliders for `a`, `b`, and `c`
with st.sidebar:
    st.subheader("Adjust Coefficients")
    a = st.slider('Coefficient a', -5.0, 5.0, 1.0)
    b = st.slider('Coefficient b', -5.0, 5.0, 0.0)
    c = st.slider('Coefficient c', -5.0, 5.0, 0.0)

# Recalculate and update the values based on new sliders
x, y, vertex, focus, directrix_y = calculate_parabola(a, b, c)

# ** Updated Equation Feedback and Properties **
with col1:
    st.subheader("Real-time Equation Feedback")
    equation_preview = f"y = {a}x² + {b}x + {c}"
    st.write(f"**Current Equation:** {equation_preview}")

    st.subheader("Parabola Properties")
    st.write(f"**Vertex:** ({vertex[0]:.2f}, {vertex[1]:.2f})")
    st.write(f"**Focus:** ({focus[0]:.2f}, {focus[1]:.2f})")
    st.write(f"**Directrix:** y = {directrix_y:.2f}")
    st.write(f"**Axis of Symmetry:** x = {vertex[0]:.2f}")

st.write("Developed by Om Dandage for a math project 🚀")
