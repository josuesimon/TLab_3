import requests
import json
import pandas as pd

# We are setting up our inputs for our API request we will be conducting using the URL below
latitude = -21.72
longitude = -45.39
start_date = "2022-01-01"
end_date = "2023-12-31"
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"

# We are grabbing our JSON data from the API request above
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    
    # This part of the code is used to convert the JSON data into a pandas DataFrame
    with open('data/json/weather_data.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
    print("Your JSON data has now been saved.") 

    # From here we grab the data we need and save it into a CSV file called weather_data.csv, we can then use this data for further analysis later on
    # We also create else statement to handle any errors that may occur when performing the API request
    if 'hourly' in json_data:
        df = pd.DataFrame({
            'time': json_data['hourly']['time'],
            'temperature': json_data['hourly']['temperature_2m'],
            'relative_humidity': json_data['hourly']['relative_humidity_2m'],
            'precipitation': json_data['hourly']['precipitation'],
            'surface_pressure': json_data['hourly']['surface_pressure']
        })
        df.to_csv('data/csv/weather_data.csv', index=False)
        print("Your CSV data has been saved to the data/csv folder in the file weather_data.csv")
    else:
        print("No hourly data was found.")
else:
    print(f"Failed to fetch your data: {response.status_code} - {response.text}")