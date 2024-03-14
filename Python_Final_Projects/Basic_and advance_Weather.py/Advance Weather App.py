import tkinter as tk
import requests

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather App")

        self.label = tk.Label(master, text="Enter city name:")
        self.label.pack()

        self.city_entry = tk.Entry(master)
        self.city_entry.pack()

        self.get_weather_button = tk.Button(master, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            self.result_label.config(text="Please enter your city.", fg="red")
            return

        api_key = "0f3d4a757f1a3be06786e9ee282d6961"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()
            if data["cod"] == 200:
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]
                self.result_label.config(text=f"Temperature: {temperature}°C\nDescription: {description}", fg="green")
            else:
                self.result_label.config(text="City not found. Please enter a valid city name.", fg="red")
        except Exception as e:
            self.result_label.config(text=f"An error occurred: {str(e)}", fg="red")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

