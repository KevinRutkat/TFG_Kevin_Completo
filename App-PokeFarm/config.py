# config.py

import json
import os

# Ruta al archivo JSON de configuración
_CFG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

# Carga los valores desde config.json, si existe
try:
    with open(_CFG_PATH, encoding="utf-8") as _f:
        _data = json.load(_f)
except FileNotFoundError:
    _data = {}

# — Teclas de control —
MovimientoW = _data.get("MovimientoW", "W")
MovimientoA = _data.get("MovimientoA", "A")
MovimientoS = _data.get("MovimientoS", "S")
MovimientoD = _data.get("MovimientoD", "D")
inputHablar  = _data.get("inputHablar", "Z")
botonVuelo   = _data.get("botonVuelo", "9")
botonBici    = _data.get("botonBici", "1")
botonCaña    = _data.get("botonCaña", "5")
botonAroma   = _data.get("botonAroma", "7")
vecesAroma   = int(_data.get("vecesAroma", 6))

# — Rutas de imágenes y otros recursos —
check_salvaje            = _data.get("check_salvaje",            "assets/checkSalvaje.png")
ciudad_ladrillo          = _data.get("ciudad_ladrillo",          "assets/ciudadLadrillo.png")
imagen_referencia        = _data.get("imagen_referencia",        "assets/identificadorFucsia.png")
imagen_referencia2       = _data.get("imagen_referencia2",       "assets/identificadorLadrillo.png")
imagen_ha_picado         = _data.get("imagen_ha_picado",         "assets/haPicado.png")
imagen_no_pican          = _data.get("imagen_no_pican",          "assets/noPican.png")
imagen_magikarp          = _data.get("imagen_magikarp",          "assets/magikarp.png")
imagen_cruz              = _data.get("imagen_cruz",              "assets/cruz.png")
imagen_huir              = _data.get("imagen_huir",              "assets/huir.png")
imagen_magikarp_atrapado = _data.get("imagen_magikarp_atrapado", "assets/magikarpAtrapado.png")
imagen_atentamente       = _data.get("imagen_atentamente",       "assets/atentamente.png")
imagen_piedra            = _data.get("imagen_piedra",            "assets/tirarPiedra.png")
imagen_tirarBall         = _data.get("imagen_tirarBall",         "assets/ball.png")
imagen_enfadado          = _data.get("imagen_enfadado",          "assets/enfadado.png")
imagen_huir2             = _data.get("imagen_huir2",             "assets/huir2.png")
imagen_magikarSalvaje    = _data.get("imagen_magikarSalvaje",    "assets/magikarpSalvaje.png")
imagen_ding              = _data.get("imagen_ding",              "assets/ddon.png")
boton_lucha              = _data.get("boton_lucha",              "assets/luchaButton.png")
boton_surf               = _data.get("boton_surf",               "assets/surfButton.png")
boton_rapidash           = _data.get("boton_rapidash",           "assets/rapidash.png")
revision_salvaje         = _data.get("revision_salvaje",         "assets/revisionSalvaje.png")
cancelar_habilidad       = _data.get("cancelar_habilidad",       "assets/cancelarHabilidad.png")
si_cancelar              = _data.get("si_cancelar",              "assets/siCancelar.png")
si_evolucionar           = _data.get("si_evolucionar",           "assets/revisionEvolucion.png")
disco_terminado          = _data.get("disco_terminado",          "assets/discoFinal.png")
c_ladrillo               = _data.get("c_ladrillo",               "assets/cLadrillo.png")
disco_vacio              = _data.get("disco_vacio",              "assets/discovacio.png")
foto_irFucsia            = _data.get("foto_irFucsia",            "assets/fotoirFucsia.png")

# — Nombres de juegos —
NOMBRE_JUEGO  = _data.get("NOMBRE_JUEGO",  "PokeMMO")
NOMBRE_JUEGO2 = _data.get("NOMBRE_JUEGO2", "РokeМMO")
NOMBRE_JUEGO3 = _data.get("NOMBRE_JUEGO3", "PokeMМO")
NOMBRE_JUEGO4 = _data.get("NOMBRE_JUEGO4", "PokеMМO")
