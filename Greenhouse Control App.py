import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os
import random
from datetime import datetime

# Function to clear content

def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

def show_monitor():
    clear_content()

    # Title for Contor Panel
    monitor_title = tk.Label(content_frame, text="Control Panel", font=("Arial", 24, "bold"), bg="#e7f9e7")
    monitor_title.pack(pady=20)

    def save_settings():
        name = simpledialog.askstring("Save Settings", "Enter a name for this save:")
        if name:
            settings = {
                "air_temperature": air_temp_entry.get(),
                "air_humidity": air_hum_entry.get(),
                "soil_humidity": soil_hum_entry.get(),
            }
            with open(f"{name}_greenhouse_settings.json", "w") as f:
                json.dump(settings, f)
            messagebox.showinfo("Success", f"Settings '{name}' saved successfully!")

    def load_settings():
        files = [f for f in os.listdir() if f.endswith("_greenhouse_settings.json")]
        if not files:
            messagebox.showwarning("Error", "No settings files found!")
            return

        name = simpledialog.askstring("Load Settings", "Enter the name of the save to load:")
        file_name = f"{name}_greenhouse_settings.json"
        if name and file_name in files:
            with open(file_name, "r") as f:
                settings = json.load(f)
                air_temp_entry.delete(0, tk.END)
                air_hum_entry.delete(0, tk.END)
                soil_hum_entry.delete(0, tk.END)
                air_temp_entry.insert(0, settings["air_temperature"])
                air_hum_entry.insert(0, settings["air_humidity"])
                soil_hum_entry.insert(0, settings["soil_humidity"])
                messagebox.showinfo("Success", f"Settings '{name}' loaded successfully!")
        else:
            messagebox.showwarning("Error", "Save not found!")

    # Labels and entries
    air_temp_label = tk.Label(content_frame, text="Desired Air Temperature (°C):", bg="#e7f9e7")
    air_temp_label.pack(pady=5)
    air_temp_entry = tk.Entry(content_frame)
    air_temp_entry.pack(pady=5)

    air_hum_label = tk.Label(content_frame, text="Desired Air Humidity (%):", bg="#e7f9e7")
    air_hum_label.pack(pady=5)
    air_hum_entry = tk.Entry(content_frame)
    air_hum_entry.pack(pady=5)

    soil_hum_label = tk.Label(content_frame, text="Desired Soil Humidity (%):", bg="#e7f9e7")
    soil_hum_label.pack(pady=5)
    soil_hum_entry = tk.Entry(content_frame)
    soil_hum_entry.pack(pady=5)

    # Buttons
    save_button = tk.Button(content_frame, text="Save Settings", command=save_settings, bg="#a8e6a8")
    save_button.pack(pady=5)

    load_button = tk.Button(content_frame, text="Load Settings", command=load_settings, bg="#a8e6a8")
    load_button.pack(pady=5)

def show_control_panel():
    clear_content()

    # Title for Monitor
    control_panel_title = tk.Label(content_frame, text="Monitor", font=("Arial", 24, "bold"), bg="#e7f9e7")
    control_panel_title.pack(pady=20)

    def get_sensor_data():
        """Simulate getting data from Arduino. Replace with actual data fetching logic."""
        air_temperature = random.uniform(18, 35)  # Replace with Arduino value
        air_humidity = random.uniform(40, 80)     # Replace with Arduino value
        soil_humidity = random.uniform(20, 60)    # Replace with Arduino value
        water_level = random.uniform(50, 90)
        return air_temperature, air_humidity, soil_humidity, water_level

    def update_sensor_data():
        """Update sensor data displayed on the app."""
        air_temp, air_hum, soil_hum, wat_lvl = get_sensor_data()
        lbl_air_temp_value.config(text=f"{air_temp:.1f} °C")
        lbl_air_hum_value.config(text=f"{air_hum:.1f} %")
        lbl_soil_hum_value.config(text=f"{soil_hum:.1f} %")
        lbl_wat_lvl_value.config(text=f"{wat_lvl:.1f} %")
        lbl_last_updated.config(text=f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Frame for sensor data
    data_frame = ttk.Frame(content_frame, padding="10")
    data_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    # Air Temperature
    air_temp_frame = ttk.Frame(data_frame)
    air_temp_frame.grid(row=0, column=0, padx=10, pady=10)

    lbl_air_temp = tk.Label(air_temp_frame, text="Air Temperature", font=("Helvetica", 12), anchor="center")
    lbl_air_temp.pack()

    lbl_air_temp_value = tk.Label(air_temp_frame, text="-- °C", font=("Helvetica", 14, "bold"), fg="#2A9D8F")
    lbl_air_temp_value.pack()

    # Air Humidity
    air_hum_frame = ttk.Frame(data_frame)
    air_hum_frame.grid(row=1, column=0, padx=10, pady=10)

    lbl_air_hum = tk.Label(air_hum_frame, text="Air Humidity", font=("Helvetica", 12), anchor="center")
    lbl_air_hum.pack()

    lbl_air_hum_value = tk.Label(air_hum_frame, text="-- %", font=("Helvetica", 14, "bold"), fg="#2A9D8F")
    lbl_air_hum_value.pack()

    # Soil Humidity
    soil_hum_frame = ttk.Frame(data_frame)
    soil_hum_frame.grid(row=2, column=0, padx=10, pady=10)

    lbl_soil_hum = tk.Label(soil_hum_frame, text="Soil Humidity", font=("Helvetica", 12), anchor="center")
    lbl_soil_hum.pack()

    lbl_soil_hum_value = tk.Label(soil_hum_frame, text="-- %", font=("Helvetica", 14, "bold"), fg="#2A9D8F")
    lbl_soil_hum_value.pack()

    # Water Level
    wat_lvl_frame = ttk.Frame(data_frame)
    wat_lvl_frame.grid(row=3, column=0, padx=10, pady=10)

    lbl_wat_lvl = tk.Label(wat_lvl_frame, text="Water Level", font=("Helvetica", 12), anchor="center")
    lbl_wat_lvl.pack()

    lbl_wat_lvl_value = tk.Label(wat_lvl_frame, text="-- %", font=("Helvetica", 14, "bold"), fg="#2A9D8F")
    lbl_wat_lvl_value.pack()

    # Last Updated Label
    lbl_last_updated = tk.Label(content_frame, text="Last updated: --", font=("Helvetica", 10), bg="#DFF5E3", fg="#555")
    lbl_last_updated.pack(pady=5)

    # Refresh Buttons
    btn_refresh = ttk.Button(content_frame, text="Refresh Now", command=update_sensor_data)
    btn_refresh.pack(pady=10)

    # Initial Data Update
    update_sensor_data()

# Main window setup
root = tk.Tk()
root.title("Smart Greenhouse")
root.geometry("1000x600")
root.configure(bg="#e7f9e7")

# Layout frames
menu_frame = tk.Frame(root, bg="#c8e6c9", width=200)
menu_frame.pack(side=tk.LEFT, fill=tk.Y)

content_frame = tk.Frame(root, bg="#e7f9e7")
content_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# Title
menu_title = tk.Label(content_frame, text="Smart Greenhouse", font=("Arial", 40, "bold"), bg="#e7f9e7")
menu_title.pack(pady=90)

# Menu buttons
menu_label = tk.Label(menu_frame, text="Menu", font=("Arial", 18, "bold"), bg="#c8e6c9")
menu_label.pack(pady=20)

monitor_button = tk.Button(menu_frame, text="Control Panel", command=show_monitor, bg="#a8e6a8", font=("Arial", 14))
monitor_button.pack(pady=10, fill=tk.X)

control_panel_button = tk.Button(menu_frame, text="Monitor", command=show_control_panel, bg="#a8e6a8", font=("Arial", 14))
control_panel_button.pack(pady=10, fill=tk.X)

# Footer
footer_label = tk.Label(root, text="Created by: \n Igor Redko ", font=("Arial", 10, "italic"), bg="#e7f9e7")
footer_label.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

root.mainloop()