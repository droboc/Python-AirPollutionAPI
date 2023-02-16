import requests
import datetime
import json

def get_pollution_data(start_date, end_date, latitude, longitude, api_key, save_to_file=False):
    # Convierte las fechas de entrada en formato timestamp
    start_timestamp = int(datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S').timestamp())
    end_timestamp = int(datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S').timestamp())

    # Realiza la solicitud a la API
    url = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={latitude}8&lon={longitude}&start={start_timestamp}&end={end_timestamp}&appid={api_key}"
    response = requests.get(url)

    # Comprueba si la solicitud se ha realizado correctamente
    if response.status_code == 200:
        # Convierte la respuesta en un objeto JSON
        data = response.json()

        # Convierte el parámetro dt al formato datetime
        for item in data["list"]:
            item["dt"] = datetime.datetime.fromtimestamp(item["dt"]).strftime('%Y-%m-%d %H:%M:%S')

        if save_to_file:
           # Guarda los datos JSON en un archivo
            with open("pollution_data.json", "w") as f:
                json.dump(data, f)

        return data
    else:
        raise Exception(f"Request failed with status code: {response.status_code}")

#Salida en consola
start_date = input("Ingrese fecha inicial (YYYY-MM-DD hh:00:00): ")
end_date = input("Ingrese fecha final (YYYY-MM-DD hh:00:00): ")
longitude = float(input("Ingrese longitud: "))
latitude = float(input("Ingrese latitud: "))
api_key = "1adda074324bc90d82d31352ca137afc"


pollution_data = get_pollution_data(start_date, end_date, latitude, longitude, api_key, save_to_file=True)
