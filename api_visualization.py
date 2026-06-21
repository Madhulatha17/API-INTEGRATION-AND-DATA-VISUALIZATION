import requests
import matplotlib.pyplot as plt

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
CITY = "Hyderabad"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

dates = []
temps = []

for item in data["list"][:10]:
    dates.append(item["dt_txt"])
    temps.append(item["main"]["temp"])

plt.figure(figsize=(10,5))
plt.plot(dates, temps, marker="o")
plt.title(f"Temperature Forecast - {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("dashboard.png")
plt.show()
