import requests
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

USERNAME = "riadvai"

url = f"https://github-contributions-api.jogruber.de/v4/{riadvai}"
data = requests.get(url).json()

days = []
counts = []

for week in data["contributions"]:
    for day in week["days"]:
        days.append(day["date"][-2:])
        counts.append(day["count"])

x = np.arange(len(days))
y = counts

fig, ax = plt.subplots(figsize=(10,4))
line, = ax.plot([], [], color='#00f7ff', marker='o')

ax.set_xlim(0, len(x))
ax.set_ylim(0, max(y)+5)

ax.set_facecolor('#0d1117')
fig.patch.set_facecolor('#0d1117')

ax.tick_params(colors='white')
ax.set_title("GitHub Contribution Graph", color='cyan')

def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=len(x), interval=30)

ani.save("graph.gif", writer="pillow")
