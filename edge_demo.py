#!/usr/bin/env python3
"""
Edge Computing Demo - Temperature Monitoring
From: Your Instagram @yourusername

This script demonstrates edge computing by processing
IoT sensor data locally without cloud dependency.
"""

import time
import random
from datetime import datetime

def edge_computing_demo():
    """
    Simulates an IoT temperature sensor with local processing
    This is edge computing - data processed where it's generated!
    """
    print("🔥 Edge Computing Demo Starting...")
    print("=" * 50)
    print("Simulating IoT temperature sensor...")
    print("Data processed LOCALLY (no cloud needed!)")
    print("=" * 50)
    
    alert_count = 0
    readings_count = 0
    
    try:
        while True:
            # Generate sensor data (simulating real IoT device)
            temperature = random.uniform(18, 32)
            humidity = random.uniform(40, 80)
            timestamp = datetime.now().strftime("%H:%M:%S")
            readings_count += 1
            
            # EDGE PROCESSING - happens locally!
            print(f"⏰ {timestamp} | 📊 Temp: {temperature:.1f}°C | 💧 Humidity: {humidity:.1f}%")
            
            # Local decision making (this is the "edge" part!)
            if temperature > 28:
                alert_count += 1
                print("🚨 ALERT: High temperature detected!")
                print("💡 Edge device taking local action...")
                print("   → Activating cooling system")
                print("   → Logging incident locally")
                # In real scenario: turn on fan, send notification, etc.
            elif temperature < 20:
                print("❄️  Cold temperature detected")
                print("💡 Edge device response:")
                print("   → Activating heating system")
            else:
                print("✅ Temperature normal - no action needed")
            
            # Show edge computing benefits
            if readings_count % 10 == 0:
                print("\n" + "="*50)
                print(f"📈 EDGE STATS: {readings_count} readings processed locally")
                print(f"⚡ Response time: <10ms (vs cloud: 100-500ms)")
                print(f"🔒 Privacy: All data processed on device")
                print(f"🚨 Alerts triggered: {alert_count}")
                print("="*50 + "\n")
            
            print("-" * 60)
            time.sleep(3)  # Check every 3 seconds
            
    except KeyboardInterrupt:
        print("\n\n🛑 Demo stopped by user")
        print(f"📊 Total readings processed: {readings_count}")
        print(f"🚨 Total alerts: {alert_count}")
        print("✨ Thanks for trying edge computing!")

def advanced_edge_demo():
    """
    More advanced edge computing example with data aggregation
    """
    print("🚀 Advanced Edge Computing Demo")
    print("Processing multiple sensors with local analytics...")
    
    sensor_data = {
        'temperature': [],
        'humidity': [],
        'pressure': []
    }
    
    for i in range(20):
        # Collect sensor readings
        temp = random.uniform(20, 30)
        humidity = random.uniform(40, 80)
        pressure = random.uniform(950, 1050)
        
        sensor_data['temperature'].append(temp)
        sensor_data['humidity'].append(humidity)
        sensor_data['pressure'].append(pressure)
        
        # Local analytics (edge processing)
        if len(sensor_data['temperature']) >= 5:
            avg_temp = sum(sensor_data['temperature'][-5:]) / 5
            print(f"📊 5-reading average temp: {avg_temp:.1f}°C")
            
            # Smart alerting based on trends
            if avg_temp > 27:
                print("📈 Temperature trending HIGH - preemptive cooling!")
        
        time.sleep(1)

if __name__ == "__main__":
    print("Choose demo mode:")
    print("1. Basic Edge Computing Demo")
    print("2. Advanced Edge Analytics")
    
    try:
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == "2":
            advanced_edge_demo()
        else:
            edge_computing_demo()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Try running with: python3 edge_demo.py")
