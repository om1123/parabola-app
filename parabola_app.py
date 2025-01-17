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

# 🎨 Plot 2D Parabola with Vertex, Focus, and Directrix
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, label=f'y = {a}x² + {b}x + {c}', color='b')
ax.scatter(*vertex, color='red', zorder=5, label=f'Vertex ({vertex[0]:.2f}, {vertex[1]:.2f})')
ax.scatter(*focus, color='green', zorder=5, label=f'Focus ({focus[0]:.2f}, {focus[1]:.2f})')
ax.axhline(directrix_y, color='orange', linestyle='dashed', label=f'Directrix y={directrix_y:.2f}')
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.legend()
ax.grid(True)
st.pyplot(fig)

# 🌀 3D Paraboloid Visualization
st.subheader("🌀 3D Paraboloid Visualization")
x_vals = np.linspace(-5, 5, 50)
y_vals = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_vals, y_vals)
Z = a * (X**2 + Y**2)

fig_3d = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale="Viridis")])
fig_3d.update_layout(title="3D Paraboloid", scene=dict(xaxis_title="X-axis", yaxis_title="Y-axis", zaxis_title="Z-axis"))
st.plotly_chart(fig_3d, use_container_width=True)

# 🎨 Allow users to draw their own parabola
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

st.write("Developed by Om Danadge for maths project  🚀")
