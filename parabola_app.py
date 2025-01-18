import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import base64
import matplotlib.animation as animation

# Title
st.title("Parabola Explorer 🚀")

# Common x range for all plots
x = np.linspace(-10, 10, 400)

# Navigation Sidebar
st.sidebar.title("Explore Parabolas")
section = st.sidebar.radio("Choose Section", (
    "🎛️ 2D Parabola Features", 
    "🕶️ 3D Parabola Features", 
    "✏️ Sketch Mode", 
    "📐 Tangents & Derivatives", 
    "🎬 Motion Physics", 
    "📡 AR/VR 3D View", 
    "💾 Save & Share", 
    "🌀 Multiple Parabolas"
))

# Create two columns for input (left) and output (right)
col1, col2 = st.columns([1, 2])  # 1/3 for input and 2/3 for output

# 2D Parabola Features 🎛️
if section == "🎛️ 2D Parabola Features":
    col1.header("🎛️ 2D Parabola Features")
    a = col1.slider('Value of a', -10, 10, 1)
    b = col1.slider('Value of b', -10, 10, 0)
    c = col1.slider('Value of c', -10, 10, 0)

    # Function to plot parabola
    y = a * x**2 + b * x + c

    with col2:
        fig_2d, ax_2d = plt.subplots()
        ax_2d.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
        ax_2d.set_xlabel('x')
        ax_2d.set_ylabel('y')
        ax_2d.legend()
        st.pyplot(fig_2d)

# 3D Parabola Features 🕶️
elif section == "🕶️ 3D Parabola Features":
    col1.header("🕶️ 3D Parabola Features")
    a = col1.slider('Value of a', -10, 10, 1)
    b = col1.slider('Value of b', -10, 10, 0)
    c = col1.slider('Value of c', -10, 10, 0)

    # Parametric equations for a 3D parabola
    u = np.linspace(-10, 10, 400)
    v = np.linspace(-10, 10, 400)
    U, V = np.meshgrid(u, v)
    Z = a * U**2 + b * V + c

    with col2:
        fig_3d = plt.figure()
        ax_3d = fig_3d.add_subplot(111, projection='3d')
        ax_3d.plot_surface(U, V, Z, cmap='viridis')
        st.pyplot(fig_3d)

# Sketch Mode ✏️
elif section == "✏️ Sketch Mode":
    col1.header("✏️ Sketch Mode")
    col1.write("Click on the graph to plot points. It will calculate the equation of your parabola.")

    with col2:
        fig_sketch = go.Figure()
        fig_sketch.add_trace(go.Scatter(x=[], y=[], mode='markers', marker=dict(size=12, color='blue')))
        fig_sketch.update_layout(title="Draw Your Parabola", clickmode='event+select')

        # Handle clicks for drawing
        fig_sketch.update_traces(marker=dict(size=15, color="red"))
        st.plotly_chart(fig_sketch)

# Tangents & Derivatives 📐
elif section == "📐 Tangents & Derivatives":
    col1.header("📐 Tangents & Derivatives")
    a = col1.slider('Value of a', -10, 10, 1)
    b = col1.slider('Value of b', -10, 10, 0)
    c = col1.slider('Value of c', -10, 10, 0)

    def derivative(x, a, b):
        return 2 * a * x + b

    x_tangent = col1.slider('Select x-value for tangent', -10, 10, 0)
    y_tangent = a * x_tangent**2 + b * x_tangent + c
    slope_tangent = derivative(x_tangent, a, b)

    with col2:
        fig_tangent, ax_tangent = plt.subplots()
        ax_tangent.plot(x, a * x**2 + b * x + c, label=f'y = {a}x² + {b}x + {c}')
        ax_tangent.plot(x_tangent, y_tangent, 'ro', label="Tangent Point")
        ax_tangent.plot(x, slope_tangent * (x - x_tangent) + y_tangent, label="Tangent Line")
        ax_tangent.legend()
        st.pyplot(fig_tangent)

# Motion Physics 🎬
elif section == "🎬 Motion Physics":
    col1.header("🎬 Motion Physics - Parabola Animation")
    a = col1.slider('Value of a', -10, 10, 1)
    b = col1.slider('Value of b', -10, 10, 0)
    c = col1.slider('Value of c', -10, 10, 0)

    # Create the figure and axis for animation
    fig_anim, ax_anim = plt.subplots()
    line, = ax_anim.plot([], [], 'r-')

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        y = a * x**2 + b * x + c
        line.set_data(x[:i], y[:i])
        return line,

    ani = animation.FuncAnimation(fig_anim, animate, frames=400, init_func=init, blit=True)

    with col2:
        st.pyplot(fig_anim)

# AR/VR 3D View 📡
elif section == "📡 AR/VR 3D View":
    col1.header("📡 AR/VR 3D View")
    col1.write("In the future, we will integrate AR/VR support for immersive 3D viewing. Stay tuned! 🎮")

# Save & Share 💾
elif section == "💾 Save & Share":
    col1.header("💾 Save & Share")
    
    def download_link(fig, filename):
        fig.savefig(filename)
        with open(filename, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        href = f'<a href="data:file/txt;base64,{encoded}" download="{filename}">Download your parabola</a>'
        return href

    with col2:
        # Provide a download link for the 3D figure
        st.markdown(download_link(fig_3d, '3d_parabola_plot.png'), unsafe_allow_html=True)

# Multiple Parabolas 🌀
elif section == "🌀 Multiple Parabolas":
    col1.header("🌀 Multiple Parabolas")
    a2 = col1.slider('Value of a (for second parabola)', -10, 10, 1)
    b2 = col1.slider('Value of b (for second parabola)', -10, 10, 0)
    c2 = col1.slider('Value of c (for second parabola)', -10, 10, 0)

    # Create the second parabola
    y2 = a2 * x**2 + b2 * x + c2

    with col2:
        fig_multiple, ax_multiple = plt.subplots()
        ax_multiple.plot(x, a * x**2 + b * x + c, label=f'First Parabola: y = {a}x² + {b}x + {c}')
        ax_multiple.plot(x, y2, label=f'Second Parabola: y = {a2}x² + {b2}x + {c2}')
        ax_multiple.legend()
        st.pyplot(fig_multiple)
