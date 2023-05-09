from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, data: str):
        self.data = data

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        temperaturas = []
        humedades = []
        presiones = []
        velocidades_viento = []
        direcciones_viento = []

        with open(self.data) as f:
            for linea in f:
                if linea.startswith("Temperatura"):
                    temperatura = float(linea.split(": ")[1])
                    temperaturas.append(temperatura)
                elif linea.startswith("Humedad"):
                    humedad = float(linea.split(": ")[1])
                    humedades.append(humedad)
                elif linea.startswith("Presion"):
                    presion = float(linea.split(": ")[1])
                    presiones.append(presion)
                elif linea.startswith("Viento"):
                    velocidad_viento, direccion_viento = linea.split(": ")[1].split(",")
                    velocidades_viento.append(float(velocidad_viento))
                    direcciones_viento.append(direccion_viento.strip())

        temperatura_promedio = sum(temperaturas) / len(temperaturas)
        humedad_promedio = sum(humedades) / len(humedades)
        presion_promedio = sum(presiones) / len(presiones)
        velocidad_promedio_viento = sum(velocidades_viento) / len(velocidades_viento)

        direcciones_grados = {
            "N": 0,
            "NNE": 22.5,
            "NE": 45,
            "ENE": 67.5,
            "E": 90,
            "ESE": 112.5,
            "SE": 135,
            "SSE": 157.5,
            "S": 180,
            "SSW": 202.5,
            "SW": 225,
            "WSW": 247.5,
            "W": 270,
            "WNW": 292.5,
            "NW": 315,
            "NNW": 337.5
        }

        direcciones_grados_promedio = sum([direcciones_grados[direccion] for direccion in direcciones_viento]) / len(direcciones_viento)

        direcciones_grados_diferencias = {direccion: abs(direcciones_grados[direccion] - direcciones_grados_promedio) for direccion in direcciones_grados}

        direccion_predominante_viento = min(direcciones_grados_diferencias, key=direcciones_grados_diferencias.get)

        return temperatura_promedio, humedad_promedio, presion_promedio, velocidad_promedio_viento, direccion_predominante_viento

datos = DatosMeteorologicos("Data.txt")
temperatura_promedio, humedad_promedio, presion_promedio, velocidad_promedio_viento, direccion_predominante_viento = datos.procesar_datos()

print(f"Temperatura promedio: {temperatura_promedio:.2f}°C")
print(f"Humedad promedio: {humedad_promedio:.2f}%")
print(f"Presión promedio: {presion_promedio:.2f} hPa")
print(f"Velocidad promedio del viento: {velocidad_promedio_viento:.2f} km/h")
print(f"Dirección predominante del viento: {direccion_predominante_viento}")