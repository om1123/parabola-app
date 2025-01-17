import streamlit as st
import numpy as np
import plotly.graph_objects as go
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
    x = np.linspace(-15, 15, 400)  # Extended range for larger coefficient values
    y = a * x**2 + b * x + c
    
    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x**2 + b * vertex_x + c
    focus_x = vertex_x
    focus_y = vertex_y + 1 / (4 * a)
    directrix_y = vertex_y - 1 / (4 * a)
    
    return x, y, (vertex_x, vertex_y), (focus_x, focus_y), directrix_y

# Custom CSS for styling and borders
st.markdown("""
    <style>
        .section-block {
            border: 2px solid #4CAF50;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            background-color: #f9f9f9;
        }
        .section-title {
            font-size: 1.5em;
            color: #4CAF50;
            font-weight: bold;
        }
        .code-block {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)

# ** Layout Structure **
col1, col2 = st.columns([1, 2])  # Columns for UI organization

# Equation and Parabola Properties Block
with col1:
    st.markdown('<div class="section-block">', unsafe_allow_html=True)
    st.subheader("Real-time Equation Feedback")
    equation_preview = f"y = {a}x² + {b}x + {c}"
    st.write(f"**Current Equation:** {equation_preview}")

    st.subheader("Parabola Properties")
    x, y, vertex, focus, directrix_y = calculate_parabola(a, b, c)  # Recalculate parabola with updated coefficients
    st.write(f"**Vertex:** ({vertex[0]:.2f}, {vertex[1]:.2f})")
    st.write(f"**Focus:** ({focus[0]:.2f}, {focus[1]:.2f})")
    st.write(f"**Directrix:** y = {directrix_y:.2f}")
    st.write(f"**Axis of Symmetry:** x = {vertex[0]:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

# 2D Interactive Plot Block
with col2:
    st.markdown('<div class="section-block">', unsafe_allow_html=True)
    st.subheader("📊 2D Interactive Parabola")
    
    # Get updated values of x, y, vertex, focus, and directrix_y after the user adjusts the coefficients
    x, y, vertex, focus, directrix_y = calculate_parabola(a, b, c)

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

    # Updating layout to allow zoom/pan and wider ranges
    fig.update_layout(
        title=f"Interactive Parabola: y = {a}x² + {b}x + {c}",
        xaxis_title="X-axis",
        yaxis_title="Y-axis",
        showlegend=True,
        template="plotly_dark",
        autosize=True,  # Allow auto scaling of the graph
        dragmode="pan",  # Allow pan functionality
        hovermode="closest"
    )

    # Display the plot
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Interactive Drawing Mode Block
with col1:
    st.markdown('<div class="section-block">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)

# Additional Interactions: Sliders for `a`, `b`, and `c`
with st.sidebar:
    st.subheader("Adjust Coefficients")
    a = st.slider('Coefficient a', -1000.0, 1000.0, 1.0, step=0.01)  # Increased range for coefficient a
    b = st.slider('Coefficient b', -1000.0, 1000.0, 0.0, step=0.01)  # Increased range for coefficient b
    c = st.slider('Coefficient c', -1000.0, 1000.0, 0.0, step=0.01)  # Increased range for coefficient c

# Recalculate and update the values based on new sliders
x, y, vertex, focus, directrix_y = calculate_parabola(a, b, c)

# ** Updated Equation Feedback and Properties **
with col1:
    st.markdown('<div class="section-block">', unsafe_allow_html=True)
    st.subheader("Real-time Equation Feedback")
    equation_preview = f"y = {a}x² + {b}x + {c}"
    st.write(f"**Current Equation:** {equation_preview}")

    st.subheader("Parabola Properties")
    st.write(f"**Vertex:** ({vertex[0]:.2f}, {vertex[1]:.2f})")
    st.write(f"**Focus:** ({focus[0]:.2f}, {focus[1]:.2f})")
    st.write(f"**Directrix:** y = {directrix_y:.2f}")
    st.write(f"**Axis of Symmetry:** x = {vertex[0]:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("Developed by Om Dandage for a math project 🚀")
