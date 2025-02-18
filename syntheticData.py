import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_realistic_synthetic_data(num_devices=5, hours=24):
    np.random.seed(42)
    timestamps = pd.date_range(end=datetime.now(), periods=hours*60, freq='T')
    device_ids = [f"SRV-{i:03d}" for i in range(1, num_devices+1)]
    rack_locations = ["RACK-A", "RACK-B", "RACK-C"]

    #data generation
    data = []
    for ts in timestamps:
        for device in device_ids:
            
            hour_of_day = ts.hour
            daily_pattern = np.sin(2 * np.pi * hour_of_day / 24)

            
            cpu_base = 20 + 30 * daily_pattern + np.random.normal(0, 5)
            cpu_spike = 80 + np.random.uniform(0, 20) if np.random.rand() < 0.02 else 0  
            cpu = np.clip(cpu_base + cpu_spike, 10, 95)

            
            mem_base = 40 + 0.3 * cpu + np.random.normal(0, 5)
            mem = np.clip(mem_base, 15, 90)

            
            disk_base = np.random.poisson(200 + 100 * daily_pattern)
            disk = disk_base + np.random.randint(-50, 100) if cpu > 70 else disk_base

            
            temp_base = 20 + 0.1 * cpu + 2 * daily_pattern
            temp_anomaly = 35 + np.random.uniform(0, 5) if np.random.rand() < 0.01 else 0  
            temp = np.clip(temp_base + temp_anomaly, 18, 38)

            
            if 9 <= hour_of_day < 18:  # Business hours
                net_traffic = np.random.weibull(1.5) * 400  
            else:
                net_traffic = np.random.exponential(100)
            net_traffic = np.clip(net_traffic, 50, 800)

            
            power = 150 + 2 * cpu + 0.5 * disk + np.random.normal(0, 20)

            
            status = "normal"
            if cpu > 90 and temp > 32:
                status = "critical"
            elif cpu > 80 or temp > 28:
                status = "warning"

            data.append({
                "timestamp": ts,
                "device_id": device,
                "rack_location": np.random.choice(rack_locations),
                "cpu_utilization": round(cpu, 1),
                "memory_usage": round(mem, 1),
                "disk_io": int(disk),
                "temperature": round(temp, 1),
                "network_traffic": int(net_traffic),
                "power_usage": round(power, 1),
                "status": status
            })

    df = pd.DataFrame(data)

    
    mask = np.random.rand(*df.shape) < 0.005
    df = df.mask(mask).ffill()  

    return df


synthetic_data = generate_realistic_synthetic_data(num_devices=5, hours=24)

# Save to CSV
synthetic_data.to_csv("realistic_data_center_metrics.csv", index=False) #change name to test_realistic_data_center_metrics.csv to generate test data


print("Sample data:")
print(synthetic_data.sample(10).sort_index())