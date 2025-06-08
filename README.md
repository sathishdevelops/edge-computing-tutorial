# 🚀 Edge Computing Tutorial: Raspberry Pi Basics

Welcome to a beginner-friendly guide to **edge computing**! Learn how to process data *locally* on a Raspberry Pi, mimicking smart devices like self-driving cars or security cameras. Perfect for your first IoT project! 🔌

## What is Edge Computing?
Edge computing processes data right where it’s created (e.g., on your smartwatch or thermostat) instead of sending it to a distant cloud server. Why? It’s:
- **Faster**: Instant decisions (no cloud lag).
- **Efficient**: Saves bandwidth.
- **Private**: Keeps sensitive data local.

**Example**: Smart traffic lights analyze traffic data on the spot to reduce congestion.

## What You’ll Need
- **Raspberry Pi**: Any model (e.g., Pi 3 or 4).
- **Software**: Raspberry Pi OS with Python (pre-installed).
- **Optional**: A sensor like DHT11 for real data (this tutorial uses simulated data).
- A computer to access the Pi (via terminal or SSH).

## Step-by-Step Tutorial
1. **Set Up Your Raspberry Pi**:
   - Download and install [Raspberry Pi OS](https://www.raspberrypi.org/software/).
   - Boot your Pi and open a terminal (or connect via SSH).
2. **Save the Code**:
   - Copy the Python script below to a file named `edge_computing.py` (or download it from this repo).
   - This script simulates a temperature sensor processing data locally, like an IoT device.

```python
import time
import random  # Simulates sensor data
while True:
    temp = random.uniform(20, 30)  # Fake temperature data
    print(f"Edge Device Temp: {temp:.1f}°C")
    if temp > 28:  # Process locally
        print("Alert: High temp detected!")
    time.sleep(5)
