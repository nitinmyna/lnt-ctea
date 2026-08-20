import plotly.express as px

time = [1, 2, 3, 4, 5]
temperature = [25, 28, 31, 35, 30]

fig = px.line(
    x = time,
    y = temperature,
    markers = True,
    title = "Machine Temperature Monitoring"
) 
fig.update_xaxes(title="Time (hours)")
fig.update_yaxes(title="Temperature (°C)")
fig.show()