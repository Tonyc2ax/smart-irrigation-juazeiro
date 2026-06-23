# 1. Registramos los datos que nos dan los sensores de la finca
humedad_suelo = 32  # 32% de humedad (está seco)
temperatura = 35    # Hace mucho calor en Juazeiro (35°C)
valvula_agua = "CERRADA"

print("--- SISTEMA DE RIEGO - VALE DO SÃO FRANCISCO ---")
print(f"Humedad actual: {humedad_suelo}% | Temperatura: {temperatura}°C")

# 2. La computadora toma la decisión automática
if humedad_suelo < 40:
    valvula_agua = "ABIERTA"
    print("STATUS: Terreno seco. ¡Abriendo válvulas de agua automáticamente!")
else:
    print("STATUS: Humedad óptima. Las válvulas permanecen cerradas.")

print(f"Estado final de la manguera: {valvula_agua}")
