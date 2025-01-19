import streamlit as st
import numpy as np
import plotly.graph_objects as go
import re
import matplotlib.pyplot as plt

# Header
st.markdown(
    """
    <div style="text-align: center; font-size: 24px; font-weight: bold; color: blue;">
        Developed by Om
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar for section selection
section = st.sidebar.selectbox(
    "Choose the Section",
    ("📈 2D Parabola", "🕶️ 3D Parabola", "📐 Tangents & Derivatives"),
)

# Function to plot 2D Parabola
def plot_2d_parabola(a):
    x = np.linspace(-10, 10, 400)
    y = np.sqrt(4 * a * x)
    y_neg = -np.sqrt(4 * a * x)  # Lower branch for visualization

    focus_x, focus_y = (a, 0)
    directrix_x = -a
    axis_of_symmetry = "x = 0"
    directrix_equation = f"x = {-a}"
    latus_rectum_length = 4 * a

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Parabola", line=dict(color="deepskyblue", width=3)))
    fig.add_trace(
        go.Scatter(x=x, y=y_neg, mode="lines", name="Lower Branch", line=dict(color="deepskyblue", width=3, dash="dot"))
    )
    fig.add_trace(go.Scatter(x=[focus_x], y=[focus_y], mode="markers", name="Focus", marker=dict(color="red", size=12, symbol="x")))
    fig.add_trace(
        go.Scatter(x=[directrix_x, directrix_x], y=[-10, 10], mode="lines", name="Directrix", line=dict(color="gold", dash="dash", width=2))
    )

    fig.update_xaxes(
        showgrid=True,
        gridwidth=2,
        gridcolor="white",
        zeroline=True,
        zerolinewidth=3,
        zerolinecolor="red",
        range=[-10, 10],
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=2,
        gridcolor="white",
        zeroline=True,
        zerolinewidth=3,
        zerolinecolor="red",
        range=[-10, 10],
    )

    fig.update_layout(
        title="2D Parabola",
        xaxis_title="X-Axis",
        yaxis_title="Y-Axis",
        template="plotly_dark",
        height=600,
        width=800,
        margin=dict(l=20, r=20, t=50, b=20),
    )
    return fig, focus_x, focus_y, directrix_x, axis_of_symmetry, directrix_equation, latus_rectum_length


# Function to plot 3D Paraboloid with resolution control
def plot_3d_parabola(a, b, resolution=100):
    x = np.linspace(-10, 10, resolution)
    y = np.linspace(-10, 10, resolution)
    x, y = np.meshgrid(x, y)

    z = a * x**2 + b * y**2

    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale="Viridis", cmin=-100, cmax=100)])

    fig.update_layout(
        title="3D Paraboloid",
        scene=dict(xaxis_title="X-Axis", yaxis_title="Y-Axis", zaxis_title="Z-Axis"),
        template="plotly_dark",
        height=600,
        width=800,
        margin=dict(l=20, r=20, t=50, b=20),
    )
    return fig


# 2D Parabola Section
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

        # Call the plot function
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


# 3D Parabola Section
elif section == "🕶️ 3D Parabola":
    st.header("🕶️ Interactive 3D Parabola")
    col1, col2 = st.columns([1, 2])

    with col1:
        # Inputs for 3D parabola equation (z = ax^2 + by^2)
        a = st.number_input("Enter value for 'a'", value=1.0, step=0.1)
        b = st.number_input("Enter value for 'b'", value=1.0, step=0.1)

        # Resolution slider to control plot responsiveness
        resolution = st.slider(
            "Resolution", min_value=50, max_value=200, value=100, step=10, help="Higher values may decrease responsiveness."
        )

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
        a = st.slider("Value of a", -10, 10, 1)
        b = st.slider("Value of b", -10, 10, 0)
        c = st.slider("Value of c", -10, 10, 0)

        # Derivative calculation
        def derivative(x, a, b):
            return 2 * a * x + b

        # Select x-coordinate for the tangent
        x_tangent = st.slider("Select x-value for tangent", -10, 10, 0)
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
        ax_tangent.plot(x, a * x**2 + b * x + c, label=f"y = {a}x² + {b}x + {c}")
        ax_tangent.plot(x_tangent, y_tangent, "ro", label="Tangent Point")
        ax_tangent.plot(x, slope_tangent * (x - x_tangent) + y_tangent, label="Tangent Line")
        ax_tangent.legend()
        st.pyplot(fig_tangent)
