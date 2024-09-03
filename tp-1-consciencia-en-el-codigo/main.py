from codecarbon import EmissionsTracker
from draw import dibujar_espiral
import time

def tracker_emissions():
    # Inicia el tracker
    tracker = EmissionsTracker()
    tracker.start()

    # Aquí se incluye el código cuya potencia y CO2 se medira (En nuestro caso, realizamos un dibujo con la libreria Turtle)
    # El código de la funcion se incluye en el archivo draw.py
    start = time.perf_counter()
    dibujar_espiral()
    time_elapsed = time.perf_counter() - start


    # Se obtiene el resumen de las emisiones y el uso de energía; detiene el tracker
    # La funcion tracker.stop() devuelve las emisiones
    emissions = tracker.stop()
    # Utilizamos los metodos de la libreria para calcular la energia consumida
    energy = tracker.final_emissions_data.energy_consumed


    # Horas de procesamiento que compensa un arbol recien plantado (30kg por año)
    horas_proc = ( (time_elapsed/3600) / emissions ) * 30


    print("\n**********************************")
    print(f"* Emisiones de CO2 (kg): {emissions:.7f}")
    print(f"* Energía consumida (kWh): {energy:.7f}")
    print(f"* Tiempo de procesamiento (seg): {time_elapsed:.7f}")
    print(f"* Horas de procesamiento compensadas por un arbol recien plantado (hs): {horas_proc:.7f}")
    print("**********************************\n")

if __name__ == "__main__":
    tracker_emissions()