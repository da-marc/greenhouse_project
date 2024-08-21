import tkinter as tk
from tkinter import ttk
import random
import time

# Global variables for sensor data
sensor_data = {
    "temperature": 17.4,
    "humidity": 40.0,
    "moisture": 47.4,
    "light_intensity": 45.0,
    "crop_growth": 1.3
}

class GreenhouseUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Greenhouse System")
        self.configure(bg="#D0E9F5")

        # Layout configuration
        self.geometry("800x600")
        self.resizable(False, False)

        # Create the interface
        self.create_widgets()

    def create_widgets(self):
        # Greenhouse Area
        self.canvas = tk.Canvas(self, width=500, height=300, bg="#B2C7DA")
        self.canvas.create_rectangle(50, 50, 450, 250, fill="#D3D3D3", outline="black")
        self.canvas.create_oval(350, 20, 380, 50, fill="yellow", outline="black", tags="light")  # Light
        self.canvas.create_rectangle(300, 90, 350, 140, fill="red", outline="black", tags="heater")  # Heater
        self.canvas.create_rectangle(150, 200, 200, 250, fill="blue", outline="black", tags="water_pump")  # Water Pump
        self.canvas.create_rectangle(370, 50, 400, 80, fill="grey", outline="black", tags="window")  # Window
        self.canvas.create_polygon(150, 90, 130, 150, 170, 150, fill="green", outline="black", tags="fan")  # Fan
        self.canvas.create_oval(220, 150, 270, 200, fill="yellow", outline="black", tags="temp_sensor")  # Temp Sensor
        self.canvas.pack(pady=20)

        # Sensor Data Labels
        self.temp_label = ttk.Label(self, text=f"Temperature: {sensor_data['temperature']} °C", font=('Helvetica', 12))
        self.humidity_label = ttk.Label(self, text=f"Humidity: {sensor_data['humidity']} %", font=('Helvetica', 12))
        self.moisture_label = ttk.Label(self, text=f"Moisture: {sensor_data['moisture']} %", font=('Helvetica', 12))
        self.light_label = ttk.Label(self, text=f"Light Intensity: {sensor_data['light_intensity']} %", font=('Helvetica', 12))
        self.crop_label = ttk.Label(self, text=f"Crop Growth: {sensor_data['crop_growth']} %", font=('Helvetica', 12))

        self.temp_label.pack(pady=5)
        self.humidity_label.pack(pady=5)
        self.moisture_label.pack(pady=5)
        self.light_label.pack(pady=5)
        self.crop_label.pack(pady=5)

        # Control Buttons
        button_frame = tk.Frame(self, bg="#D0E9F5")
        button_frame.pack(pady=10)

        self.temp_button = ttk.Button(button_frame, text="Increase Temperature", command=self.increase_temperature)
        self.light_button = ttk.Button(button_frame, text="Increase Light Intensity", command=self.increase_light)
        self.moisture_button = ttk.Button(button_frame, text="Increase Moisture", command=self.increase_moisture)
        self.window_button = ttk.Button(button_frame, text="Toggle Window", command=self.toggle_window)
        self.fan_button = ttk.Button(button_frame, text="Toggle Fan", command=self.toggle_fan)

        self.temp_button.grid(row=0, column=0, padx=5, pady=5)
        self.light_button.grid(row=0, column=1, padx=5, pady=5)
        self.moisture_button.grid(row=0, column=2, padx=5, pady=5)
        self.window_button.grid(row=1, column=0, padx=5, pady=5)
        self.fan_button.grid(row=1, column=1, padx=5, pady=5)

        # Start real-time updates
        self.update_time()

    def increase_temperature(self):
        sensor_data["temperature"] += random.uniform(0.5, 1.5)
        self.update_labels()

    def increase_light(self):
        sensor_data["light_intensity"] += random.uniform(5.0, 10.0)
        self.update_labels()

    def increase_moisture(self):
        sensor_data["moisture"] += random.uniform(2.0, 5.0)
        self.update_labels()

    def toggle_window(self):
        window_state = self.canvas.itemcget("window", "fill")
        new_state = "grey" if window_state == "white" else "white"
        self.canvas.itemconfig("window", fill=new_state)

    def toggle_fan(self):
        fan_state = self.canvas.itemcget("fan", "fill")
        new_state = "green" if fan_state == "black" else "black"
        self.canvas.itemconfig("fan", fill=new_state)

    def update_labels(self):
        self.temp_label.config(text=f"Temperature: {sensor_data['temperature']:.2f} °C")
        self.humidity_label.config(text=f"Humidity: {sensor_data['humidity']:.2f} %")
        self.moisture_label.config(text=f"Moisture: {sensor_data['moisture']:.2f} %")
        self.light_label.config(text=f"Light Intensity: {sensor_data['light_intensity']:.2f} %")
        self.crop_label.config(text=f"Crop Growth: {sensor_data['crop_growth']:.2f} %")

    def update_time(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.canvas.create_text(400, 290, text=f"Time: {current_time}", font=('Helvetica', 12), fill="black", tags="time")
        self.after(1000, self.update_time)  # update time every second

if __name__ == "__main__":
    app = GreenhouseUI()
    app.mainloop()
