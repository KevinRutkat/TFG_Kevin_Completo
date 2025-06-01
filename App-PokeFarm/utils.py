# utils.py

import queue
import pygetwindow as gw
from constants import CYRILLIC_TO_LATIN

# Cola para mensajes de log (útil para mostrar en la GUI)
log_queue = queue.Queue()

def log_message(message):
    log_queue.put(message)
    print(message)

def normalizar_texto(texto):
    """Reemplaza caracteres cirílicos por sus equivalentes latinos."""
    return ''.join(CYRILLIC_TO_LATIN.get(c, c) for c in texto)

def encontrar_ventana_juego(nombre_esperado):
    """Busca y retorna la ventana que contenga el nombre esperado."""
    nombre_normalizado = normalizar_texto(nombre_esperado).lower()
    ventanas = gw.getAllTitles()
    for titulo in ventanas:
        if nombre_normalizado in normalizar_texto(titulo).lower():
            return gw.getWindowsWithTitle(titulo)[0]
    return None
