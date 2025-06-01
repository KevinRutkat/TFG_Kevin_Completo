# automation.py

import time
import threading
import keyboard
import cv2
import numpy as np
import mss
import pyautogui

import config
from utils import log_message, encontrar_ventana_juego

# Variable de control global para la ejecución de automatizaciones
running = False


def sleep_check(duration):
    """
    Duerme en pequeños intervalos, verificando en cada paso que 'running' sea True.
    Si se cambia a False, retorna inmediatamente.
    """
    end_time = time.time() + duration
    while time.time() < end_time:
        if not running:
            return False
        time.sleep(0.05)
    return True

# Función que se dedica a abrir el mapa e ir a la ciudad indicada
def irFucsia():
    ventana_juego = encontrar_ventana_juego(config.NOMBRE_JUEGO)
    if not ventana_juego:
        log_message("❌ El juego no está abierto o el nombre es incorrecto.")
        return False

    # 1) Restaurar si está minimizada
    # 2) Activar siempre para traerla al frente
    try:
        if ventana_juego.isMinimized:
            ventana_juego.restore()
            if not sleep_check(0.5):
                return False

        ventana_juego.activate()
        if not sleep_check(1):
            return False
    except Exception as e:
        log_message(f"⚠ Error al restaurar/activar la ventana: {e}")
        return False

    # 3) Verificar que realmente obtuvo el foco
    if not ventana_juego.isActive:
        log_message("❌ La ventana del juego no está activa después de activate().")
        return False

    # Damos un pequeño margen antes de empezar
    if not sleep_check(1):
        return False

    # Ya con la ventana en primer plano, enviamos el click inicial
    pyautogui.leftClick()
    if not sleep_check(1):
        return False

    # Pulsar tecla de vuelo y movernos
    keyboard.press_and_release(config.botonVuelo)
    log_message(f"✅ Tecla '{config.botonVuelo}' enviada al juego.")
    if not sleep_check(0.3):
        return False

    keyboard.press(config.MovimientoW)
    keyboard.press(config.MovimientoA)
    if not sleep_check(2):
        return False
    keyboard.release(config.MovimientoW)
    keyboard.release(config.MovimientoA)
    if not sleep_check(0.2):
        return False

    log_message("🔍 Buscando ciudad fucsia")
    click_imagen(config.foto_irFucsia, 0.6)

    keyboard.press_and_release(config.inputHablar)
    if not sleep_check(5.5):
        return False

    if detectar_imagen(config.imagen_referencia, 0.8):
        log_message("✅ Estamos en la ciudad correcta.")
    log_message("✅ Movimiento completado.")
    return True


# Envía todos los inputs necesarios para movernos hasta la zona safari
def movimientoSafari():
    if not running:
        return
    if not sleep_check(1):
        return

    keyboard.press_and_release(config.botonBici)
    if not sleep_check(0.2):
        return

    keyboard.press(config.MovimientoD)
    if not sleep_check(0.6):
        return
    keyboard.release(config.MovimientoD)

    if not sleep_check(1):
        return
    keyboard.press(config.MovimientoW)
    if not sleep_check(1.4):
        return
    keyboard.release(config.MovimientoW)

    if not sleep_check(0.2):
        return
    keyboard.press(config.MovimientoD)
    if not sleep_check(0.5):
        return
    keyboard.press(config.MovimientoS)
    if not sleep_check(0.1):
        return
    keyboard.release(config.MovimientoS)
    if not sleep_check(0.9):
        return
    keyboard.release(config.MovimientoD)

    if not sleep_check(0.2):
        return
    keyboard.press(config.MovimientoW)
    if not sleep_check(1.3):
        return
    keyboard.release(config.MovimientoW)

    if not sleep_check(0.2):
        return
    keyboard.press(config.MovimientoA)
    if not sleep_check(1.5):
        return
    keyboard.release(config.MovimientoA)

    keyboard.press(config.MovimientoS)
    if not sleep_check(0.1):
        return
    keyboard.release(config.MovimientoS)

    if not sleep_check(0.2):
        return
    keyboard.press(config.MovimientoA)
    if not sleep_check(0.4):
        return
    keyboard.release(config.MovimientoA)

    if not sleep_check(0.2):
        return
    keyboard.press(config.MovimientoW)
    if not sleep_check(3.5):
        return
    keyboard.release(config.MovimientoW)

# Entra dentro del safari
def entrarSafari():
    if not running:
        return
    if not sleep_check(0.5):
        return
    keyboard.press(config.inputHablar)
    if not sleep_check(11):
        return
    keyboard.release(config.inputHablar)

# Va a la posición del safari elegida para pescar
def posicionSafari():
    if not running:
        return
    keyboard.press_and_release(config.botonBici)
    if not sleep_check(0.2):
        return
    keyboard.press(config.MovimientoW)
    if not sleep_check(1):
        return
    keyboard.release(config.MovimientoW)
    if not sleep_check(0.2):
        return
    keyboard.press(config.MovimientoD)
    if not sleep_check(0.52):
        return
    keyboard.release(config.MovimientoD)
    if not sleep_check(0.2):
        return
    keyboard.press(config.MovimientoW)
    if not sleep_check(0.5):
        return
    keyboard.release(config.MovimientoW)

# Función genérica para detección de imagen en pantalla
def detectar_imagen(imagen_ref, umbral):
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        img_pantalla = np.array(screenshot)
        img_pantalla_gris = cv2.cvtColor(img_pantalla, cv2.COLOR_BGRA2GRAY)
        img_ref_gris = cv2.imread(imagen_ref, cv2.IMREAD_GRAYSCALE)
        if img_ref_gris is None:
            log_message(f"❌ Error: No se encontró la imagen {imagen_ref}")
            return False
        resultado = cv2.matchTemplate(img_pantalla_gris, img_ref_gris, cv2.TM_CCOEFF_NORMED)
        loc = np.where(resultado >= umbral)
        if len(loc[0]) > 0:
            log_message(f"✅ Imagen detectada: {imagen_ref}")
            return True
        else:
            return False

# Función para hacer click sobre la imagen
def click_imagen(ruta_imagen, umbral=0.8):
    with mss.mss() as sct:
        while running:
            screenshot = sct.grab(sct.monitors[1])
            pantalla = np.array(screenshot)
            pantalla = cv2.cvtColor(pantalla, cv2.COLOR_RGB2GRAY)
            plantilla = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)
            if plantilla is None:
                log_message(f"❌ Error: No se pudo cargar '{ruta_imagen}'")
                return None
            resultado = cv2.matchTemplate(pantalla, plantilla, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(resultado)
            if max_val >= umbral:
                x, y = max_loc
                x += plantilla.shape[1] // 2
                y += plantilla.shape[0] // 2
                pyautogui.moveTo(x, y)
                if not sleep_check(0.5):
                    return None
                pyautogui.click()
                log_message(f"✅ Click en imagen en posición ({x}, {y})")
                return (x, y)
            log_message("🔍 Imagen no encontrada, reintentando...")
            if not sleep_check(0.2):
                return None
        return None

# Detecta si el Pokémon ha picado
def detectarPicado():
    while running:
        if detectar_imagen(config.imagen_ha_picado, 0.8):
            log_message("✅ Ha picado")
            return True
        elif detectar_imagen(config.imagen_no_pican, 0.8):
            log_message("❌ No picaron")
            return False
        log_message("🔍 Buscando imagen de picar")
        if not sleep_check(0.5):
            return False
    return False

# Lanza una piedra
def tirarPiedra():
    while running:
        if click_imagen(config.imagen_piedra, 0.8):
            log_message("🪨 Tirando piedra…")
            return enfado()
        log_message("❌ No se encuentra botón Tirar Piedra")
        if not sleep_check(0.5):
            return False
    return False

# Revisa si el Pokémon se enfadó
def enfado():
    for _ in range(15):
        if not running:
            return False
        if detectar_imagen(config.imagen_enfadado, 0.8):
            log_message("😡 Se encontró enfado")
            return True
        log_message("😕 No se encuentra enfado")
        if not sleep_check(0.2):
            return False
    return False

# Lanza una Poké Ball
def tirarBall():
    while running:
        if click_imagen(config.imagen_tirarBall, 0.8):
            log_message("⚽ Tirando pelota")
            return True
        log_message("❌ No se encuentra tirar pelota")
        if not sleep_check(0.5):
            return False
    return False

# Cierra el popup después de la captura
def cerrarPopup():
    while running:
        if click_imagen(config.imagen_cruz, 0.9):
            log_message("❎ Cerrando popup…")
            return True
        log_message("❌ No se encuentra popup…")
        if not sleep_check(0.5):
            return False
    return False

# Revisa si se han acabado las Poké Balls en el safari
def dingdong():
    for _ in range(15):
        if not running:
            return False
        if detectar_imagen(config.imagen_ding, 0.8):
            log_message("🔔 Ding Dong! Se acabó! Reiniciando…")
            keyboard.press(config.inputHablar)
            if not sleep_check(4):
                return False
            keyboard.release(config.inputHablar)
            keyboard.press(config.MovimientoW)
            if not sleep_check(1):
                return False
            keyboard.release(config.MovimientoW)
            entrarSafari()
            if not sleep_check(3):
                return False
            posicionSafari()
            return True
        else:
            log_message("🔍 No se encontró ding dong")
            if not sleep_check(0.2):
                return False
    return False

# Flujo completo de pesca
def pescar():
    while running:
        if not sleep_check(2):
            return
        keyboard.press_and_release(config.botonCaña)
        if not running:
            return
        if detectarPicado():
            log_message("🎣 Pokémon ha picado, lanzando piedra…")
            if not sleep_check(1):
                return
            keyboard.press_and_release(config.inputHablar)
            if not sleep_check(0.2):
                return
            if tirarPiedra():
                log_message("✅ Piedra lanzada, intentando tirar ball")
                if not sleep_check(0.2):
                    return
                if tirarBall():
                    log_message("✅ Ball lanzada, cerrando popup")
                    if cerrarPopup():
                        log_message("🔄 Revisando Ding Dong…")
                        if dingdong():
                            log_message("🔔 Ding Dong")
                            continue
                        else:
                            log_message("🔄 Ding dong no encontrado. Reiniciando ciclo…")
                            continue
                    else:
                        log_message("❌ Error cerrando popup")
                else:
                    log_message("❌ Error al tirar Ball")
            else:
                log_message("🔄 Revisando Ding Dong…")
                if dingdong():
                    log_message("🔔 Ding Dong")
                else:
                    log_message("🔄 Ding dong no encontrado. Reiniciando ciclo…")
                    continue
        else:
            log_message("❌ No ha picado, reiniciando proceso…")
            if not sleep_check(0.2):
                return
            keyboard.press_and_release(config.inputHablar)
            if not sleep_check(0.2):
                return
            continue

# Función para volar a Ciudad Ladrillo
def irLadrillo():
    ventana_juego = encontrar_ventana_juego(config.NOMBRE_JUEGO)
    if not ventana_juego:
        log_message("❌ El juego no está abierto o el nombre es incorrecto.")
        return False

    # Restaurar/activar igual que en irFucsia
    try:
        if ventana_juego.isMinimized:
            ventana_juego.restore()
            if not sleep_check(0.5):
                return False

        ventana_juego.activate()
        if not sleep_check(1):
            return False
    except Exception as e:
        log_message(f"⚠ Error al restaurar/activar la ventana: {e}")
        return False

    if not ventana_juego.isActive:
        log_message("❌ La ventana del juego no está activa después de activate().")
        return False

    if not sleep_check(1):
        return False

    pyautogui.leftClick()
    if not sleep_check(1):
        return False

    keyboard.press_and_release(config.botonVuelo)
    log_message(f"✅ Tecla '{config.botonVuelo}' enviada al juego.")
    if not sleep_check(0.3):
        return False

    keyboard.press(config.MovimientoW)
    keyboard.press(config.MovimientoA)
    if not sleep_check(4):
        return False
    keyboard.release(config.MovimientoW)
    keyboard.release(config.MovimientoA)
    if not sleep_check(0.2):
        return False

    click_imagen(config.c_ladrillo, 0.8)
    if not sleep_check(0.2):
        return False

    keyboard.press_and_release(config.inputHablar)
    if not sleep_check(5.5):
        return False

    if detectar_imagen(config.imagen_referencia2, 0.8):
        log_message("✅ Estamos en la ciudad correcta.")
    log_message("✅ Movimiento completado.")
    return True

# Mueve al personaje dentro de Ciudad Ladrillo para recuperar PP
def moverHierba():
    log_message("➡️ Moviendo a hierba")
    if not sleep_check(0.5):
        return
    keyboard.press_and_release(config.botonBici)
    if not sleep_check(0.8):
        return
    keyboard.press(config.MovimientoA)
    if not sleep_check(2.65):
        return
    keyboard.release(config.MovimientoA)
    if not sleep_check(0.2):
        return
    keyboard.press(config.MovimientoW)
    if not sleep_check(0.3):
        return
    keyboard.release(config.MovimientoW)
    sleep_check(0.2)

# Revisa si sale un Pokémon no deseado al entrar en hierba
def checkSalvaje():
    log_message("🔍 Revisando salvaje")
    time.sleep(0.5)
    for _ in range(20):
        if not running:
            return
        if detectar_imagen(config.revision_salvaje, 0.8):
            if not sleep_check(5):
                return
            click_imagen(config.check_salvaje)
            log_message("🏃 Huyendo de Pokémon no deseado…")
            if not sleep_check(0.5):
                return
        else:
            log_message("✅ Ningún salvaje no deseado, comenzando farmeo…")

# Maneja subida de nivel y posible evolución
def revisionNivel():
    log_message("🔄 Revisando subida de nivel")
    if not sleep_check(8):
        return
    seguir = True
    while seguir and running:
        if not sleep_check(8):
            return
        if detectar_imagen(config.si_evolucionar, 0.7):
            log_message("✨ Pokémon evolucionado, esperando…")
            if not sleep_check(15):
                return
        elif detectar_imagen(config.cancelar_habilidad, 0.7):
            click_imagen(config.cancelar_habilidad)
            if not sleep_check(0.2):
                return
            click_imagen(config.si_cancelar)
        else:
            log_message("✅ No hay subida de nivel")
            seguir = False

# Farmeo de experiencia con Dulce Aroma
def farmeoExp():
    log_message("⚡ Farmeo EXP")
    if not sleep_check(3):
        return
    keyboard.press_and_release(config.botonAroma)
    if not sleep_check(10):
        return
    click_imagen(config.boton_lucha)
    if not sleep_check(0.2):
        return
    click_imagen(config.boton_surf)
    if not sleep_check(0.2):
        return
    click_imagen(config.boton_rapidash)
    sleep_check(2)

# Recupera PP en Ciudad Ladrillo
def recuperar():
    log_message("💧 Recuperando PP")
    irLadrillo()
    if not sleep_check(0.2):
        return
    keyboard.press(config.MovimientoW)
    if not sleep_check(4.5):
        return
    keyboard.release(config.MovimientoW)
    if not sleep_check(0.2):
        return
    keyboard.press(config.inputHablar)
    if not sleep_check(12):
        return
    keyboard.release(config.inputHablar)
    if not sleep_check(0.2):
        return
    keyboard.press(config.MovimientoS)
    if not sleep_check(2.8):
        return
    keyboard.release(config.MovimientoS)

# Secuencia principal de automatización de pesca
def automation_sequence(root):
    global running
    running = True
    root.iconify()
    log_message("▶️ Iniciando automatización…")
    if not sleep_check(1):
        running = False
        root.deiconify()
        return

    if irFucsia():
        movimientoSafari()
        entrarSafari()
        posicionSafari()
        pescar()
    else:
        log_message("❌ Juego no abierto")

    running = False
    log_message("✅ Automatización finalizada.")
    root.deiconify()

def start_automation(root):
    """Inicia la automatización en un hilo separado."""
    global running
    if not running:
        t = threading.Thread(target=automation_sequence, args=(root,), daemon=True)
        t.start()

# Secuencia de farmeo de EXP
def automation_exp_sequence(root):
    global running
    running = True
    root.iconify()
    log_message("▶️ Iniciando farmeo de EXP…")
    if not sleep_check(1):
        running = False
        root.deiconify()
        return

    if irLadrillo():
        while running:
            log_message("➡️ Nuevo ciclo de farmeo EXP…")
            moverHierba()
            checkSalvaje()
            for _ in range(config.vecesAroma):
                farmeoExp()
                revisionNivel()
                if not running:
                    break
            recuperar()
            if not sleep_check(2):
                break
    else:
        log_message("❌ Juego no abierto")

    running = False
    log_message("✅ Farmeo de EXP finalizado.")
    root.deiconify()

def start_exp_automation(root):
    """Inicia la automatización de EXP en un hilo separado."""
    global running
    if not running:
        t = threading.Thread(target=automation_exp_sequence, args=(root,), daemon=True)
        t.start()

def stop_automation():
    """Detiene la automatización."""
    global running
    running = False
    log_message("⏹️ Se solicitó detener la automatización.")
