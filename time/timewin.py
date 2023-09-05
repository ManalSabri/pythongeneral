import tkinter as tk
from datetime import datetime
import pytz

class TimeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("World Clock")

        # Label for title
        self.title_label = tk.Label(root, text="Current time", font=('Arial', 16, 'bold'))
        self.title_label.pack(pady=10)

        self.cities_timezones = {
            'London': 'Europe/London',
            'Delhi': 'Asia/Kolkata',
            'Florida': 'US/Eastern',
            'San Diego': 'US/Pacific',
            'Singapore': 'Asia/Singapore',
            'Wuxi': 'Asia/Shanghai'
        }

        self.labels = {}

        for city in self.cities_timezones:
            label = tk.Label(root, text=f"{city}: Fetching...", font=('Arial', 14))
            label.pack(pady=5)
            self.labels[city] = label

        self.update_times()

    def get_current_time(self, timezone):
        city_time = datetime.now(pytz.timezone(timezone))
        return city_time.strftime('%Y-%m-%d %H:%M:%S')

    def update_times(self):
        for city, timezone in self.cities_timezones.items():
            time = self.get_current_time(timezone)
            self.labels[city].config(text=f"{city}: {time}")
        
        # Update the times every minute
        self.root.after(60000, self.update_times)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeApp(root)
    root.mainloop()

