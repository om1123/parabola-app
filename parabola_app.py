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
