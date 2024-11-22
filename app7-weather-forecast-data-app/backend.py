import requests

API_KEY = "06746051888412bb325766ff452f1c8a"

def get_data(place, forecast_days=2):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    n_values = 8 * forecast_days
    filtered_data = data["list"][:n_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data("Tokyo"))