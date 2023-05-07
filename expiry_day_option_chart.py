import plotly.graph_objects as go
from datetime import datetime

# Sample data in the format [timestamp, open, high, low, close, volume]
data = [
        [
            1683106800,
            175.6,
            185.6,
            174.35,
            184.6,
            4185150
        ],
        [
            1683107100,
            184.8,
            185.7,
            179.55,
            181.1,
            4270450
        ],
        [
            1683107400,
            182.0,
            183.9,
            178.7,
            178.7,
            4348000
        ],
        [
            1683107700,
            179.05,
            180.5,
            172.6,
            175.5,
            4442050
        ]
    ]

# Extract the individual data arrays
timestamps = [datetime.fromtimestamp(point[0]) for point in data]
opens = [point[1] for point in data]
highs = [point[2] for point in data]
lows = [point[3] for point in data]
closes = [point[4] for point in data]

# Create a candlestick chart
fig = go.Figure(
    data=[
        go.Candlestick(
            x=timestamps,
            open=opens,
            high=highs,
            low=lows,
            close=closes,
        )
    ]
)

# Set the title and labels
fig.update_layout(
    title="Candlestick Chart",
    xaxis_title="Time",
    yaxis_title="Price",
)

# Show the plot
fig.show()

