import urllib.parse
import requests
import time

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "7GO2QDiwVi82joz7BM9CnKLhH8GzITsj"

# Obtener la hora actual
current_time = time.strftime("%H:%M")

print("¡Bienvenido al programa de direcciones!")
print("Hora actual:", current_time)

while True:
    orig = input("Ubicación de partida: ")
    if orig == "exit" or orig == "exit":
        break
    dest = input("Destino: ")
    if dest == "exit" or dest == "exit":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest, "locale": "es_ES"})
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("Estado de la API: " + str(json_status) + " = Llamada de ruta exitosa.\n")
        print("=============================================")
        print("Indicaciones desde " + orig + " hasta " + dest)
        print("Duración del viaje: " + json_data["route"]["formattedTime"])
        print("Millas: " + str(round(json_data["route"]["distance"], 4)))
        print("Kilómetros: " + str(round(json_data["route"]["distance"] * 1.61, 4)))
        # print("Combustible (Gal): " + str(json_data["route"]["fuelUsed"]))
        # print("Combustible (Ltr): " + str(json_data["route"]["fuelUsed"] * 3.78))
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " (" + str(round(each["distance"] * 1.61, 4)) + " km)")
        print("=============================================")
        if json_status == 402:
            print("**********************************************")
            print("Código de estado: " + str(json_status) + "; Entradas de usuario no válidas para una o ambas ubicaciones.")
            print("**********************************************\n")
        elif json_status == 611:
            print("**********************************************")
            print("Código de estado: " + str(json_status) + "; Falta una entrada para una o ambas ubicaciones.")
            print("**********************************************\n")
        else:
            print("************************************************************************")
            print("Para el código de estado: " + str(json_status) + "; Consulta:")
            print("https://developer.mapquest.com/documentation/directions-api/status-codes")
            print("************************************************************************\n")