import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import base64
import matplotlib.animation as animation

# Title
st.title("Parabola Explorer 🚀")

# 2D Parabola Section
st.header("🎛️ 2D Parabola Features")
a = st.slider('Value of a', -10, 10, 1)
b = st.slider('Value of b', -10, 10, 0)
c = st.slider('Value of c', -10, 10, 0)

# Function to plot parabola
x = np.linspace(-10, 10, 400)
y = a * x**2 + b * x + c

fig, ax = plt.subplots()
ax.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
st.pyplot(fig)

# 3D Parabola Section
st.header("🕶️ 3D Parabola Features")
fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111, projection='3d')

# Parametric equations for a 3D parabola
u = np.linspace(-10, 10, 400)
v = np.linspace(-10, 10, 400)
U, V = np.meshgrid(u, v)
Z = a * U**2 + b * V + c

ax_3d.plot_surface(U, V, Z, cmap='viridis')
st.pyplot(fig_3d)

# Sketch Mode Section ✏️
st.header("✏️ Sketch Mode")
fig = go.Figure()
fig.add_trace(go.Scatter(x=[], y=[], mode='markers', marker=dict(size=12, color='blue')))
fig.update_layout(title="Draw Your Parabola", clickmode='event+select')
st.plotly_chart(fig)

# Tangents & Derivatives Section 📐
st.header("📐 Tangents & Derivatives")
def derivative(x, a, b):
    return 2 * a * x + b

x_tangent = st.slider('Select x-value for tangent', -10, 10, 0)
y_tangent = a * x_tangent**2 + b * x_tangent + c
slope_tangent = derivative(x_tangent, a, b)

fig_tangent, ax_tangent = plt.subplots()
ax_tangent.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
ax_tangent.plot(x_tangent, y_tangent, 'ro', label="Tangent Point")
ax_tangent.plot(x, slope_tangent * (x - x_tangent) + y_tangent, label="Tangent Line")
ax_tangent.legend()
st.pyplot(fig_tangent)

# Motion Physics Section 🎬
st.header("🎬 Motion Physics - Parabola Animation")
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
st.pyplot(fig_anim)

# Save & Share Section 💾
st.header("💾 Save & Share")
def download_link(fig, filename):
    fig.savefig(filename)
    with open(filename, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    href = f'<a href="data:file/txt;base64,{encoded}" download="{filename}">Download your parabola</a>'
    return href

# Provide a download link
st.markdown(download_link(fig_3d, '3d_parabola_plot.png'), unsafe_allow_html=True)

# Multiple Parabolas Comparison 🌀
st.header("🌀 Multiple Parabolas")
a2 = st.slider('Value of a (for second parabola)', -10, 10, 1)
b2 = st.slider('Value of b (for second parabola)', -10, 10, 0)
c2 = st.slider('Value of c (for second parabola)', -10, 10, 0)

y2 = a2 * x**2 + b2 * x + c2

fig_multiple, ax_multiple = plt.subplots()
ax_multiple.plot(x, y, label=f'First Parabola: y = {a}x² + {b}x + {c}')
ax_multiple.plot(x, y2, label=f'Second Parabola: y = {a2}x² + {b2}x + {c2}')
ax_multiple.legend()
st.pyplot(fig_multiple)
