import os
import json
import importlib
import ttkbootstrap as tb
import tkinter as tk
from tkinter import ttk, filedialog

# Supabase SDK v2.x
from supabase import create_client, Client
from supabase.client import AuthApiError

# Importaciones de tus propios módulos
import config
from utils import log_message, log_queue
from automation import start_automation, start_exp_automation, stop_automation

# ----------------------------------------------------------------------
# CONFIGURACIÓN DE SUPABASE
# ----------------------------------------------------------------------
SUPABASE_URL = "https://wjudnxwnxlwomjyledgf.supabase.co"
SUPABASE_ANON_KEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndqdWRueHdueGx3b21qeWxlZGdmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQxODE0MzEsImV4cCI6MjA1OTc1NzQzMX0."
    "8tph6ZKywA3p_T0l7c0fRZ9YqqgvDGCEnmdI9SrPZH8"
)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# ----------------------------------------------------------------------
# AUTENTICACIÓN A SUPABASE
# ----------------------------------------------------------------------
def authenticate_user(email, password):
    """
    Autentica al usuario en Supabase usando sign_in_with_password().
    
    Retorna:
      - (True, user_obj)   si la autenticación es exitosa
      - (False, error_msg) si ocurre un error
    """
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        return True, response.user  # user = datos del usuario
    except AuthApiError as auth_err:
        return False, auth_err.message
    except Exception as e:
        return False, str(e)
    

def browse_file(entry: ttk.Entry):
    """Abre un diálogo para seleccionar un archivo y lo coloca en el Entry."""
    filepath = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Seleccione un archivo",
        filetypes=(
            ("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp"),
            ("Todos los archivos", "*.*"),
        )
    )
    if filepath:
        entry.delete(0, tk.END)
        entry.insert(0, filepath)

# ----------------------------------------------------------------------
# VENTANA DE CONFIGURACIÓN (modifica config.py y config.json)
# ----------------------------------------------------------------------
def open_config_window(root):
    config_win = tk.Toplevel(root)
    config_win.title("Configuración Personalizada")
    config_win.geometry("700x550")
    # Asignar icono a la ventana de configuración
    ico = os.path.join(os.path.dirname(__file__), 'assets', 'logo.ico')
    try:
        config_win.iconbitmap(ico)
    except Exception:
        pass

    config_win.grid_rowconfigure(0, weight=1)
    config_win.grid_rowconfigure(1, weight=0)
    config_win.grid_columnconfigure(0, weight=1)

    # Contenedor con canvas y scrollbar
    container = ttk.Frame(config_win)
    container.grid(row=0, column=0, sticky="nsew")
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    canvas = tk.Canvas(container)
    canvas.grid(row=0, column=0, sticky="nsew")
    vsb = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    vsb.grid(row=0, column=1, sticky="ns")
    canvas.configure(yscrollcommand=vsb.set)

    # Permitir scroll con rueda de ratón
    def _on_mousewheel(event):
        delta = int(-1 * (event.delta / 120))
        canvas.yview_scroll(delta, "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    inner = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=inner, anchor='nw')
    inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    notebook = ttk.Notebook(inner)
    notebook.pack(fill="both", expand=True, padx=10, pady=10)

    # --- Pestaña Controles ---
    frame_ctrl = ttk.Frame(notebook)
    notebook.add(frame_ctrl, text="Controles")
    frame_ctrl.grid_columnconfigure(1, weight=1)
    controles = [
        ("Movimiento W", "MovimientoW"), ("Movimiento A", "MovimientoA"),
        ("Movimiento S", "MovimientoS"), ("Movimiento D", "MovimientoD"),
        ("Input Hablar", "inputHablar"), ("Botón Vuelo", "botonVuelo"),
        ("Botón Bici", "botonBici"), ("Botón Caña", "botonCaña"),
        ("Botón Aroma", "botonAroma"), ("Veces Aroma", "vecesAroma")
    ]
    entradas_controles = {}
    for i, (txt, var) in enumerate(controles):
        ttk.Label(frame_ctrl, text=txt).grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        e = ttk.Entry(frame_ctrl, width=25)
        e.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
        e.insert(0, str(getattr(config, var)))
        entradas_controles[var] = e

    # --- Pestaña Imágenes y Juego ---
    frame_img = ttk.Frame(notebook)
    notebook.add(frame_img, text="Imágenes y Juego")
    frame_img.grid_columnconfigure(1, weight=1)
    frame_img.grid_columnconfigure(2, weight=0)
    items = [
        ("Check Salvaje", "check_salvaje"), ("Ciudad Ladrillo","ciudad_ladrillo"),
        ("Imagen Referencia","imagen_referencia"), ("Imagen Referencia 2","imagen_referencia2"),
        ("Imagen Ha Picado","imagen_ha_picado"), ("Imagen No Pican","imagen_no_pican"),
        ("Imagen Magikarp","imagen_magikarp"), ("Imagen Cruz","imagen_cruz"),
        ("Imagen Huir","imagen_huir"), ("Imagen Magikarp Atrapado","imagen_magikarp_atrapado"),
        ("Imagen Atentamente","imagen_atentamente"), ("Imagen Piedra","imagen_piedra"),
        ("Imagen Tirar Ball","imagen_tirarBall"), ("Imagen Enfadado","imagen_enfadado"),
        ("Imagen Huir2","imagen_huir2"), ("Imagen Magikarp Sal.","imagen_magikarSalvaje"),
        ("Imagen Ding","imagen_ding"), ("Botón Lucha","boton_lucha"),
        ("Botón Surf","boton_surf"), ("Botón Rapidash","boton_rapidash"),
        ("Revisión Salvaje","revision_salvaje"), ("Cancelar Habilidad","cancelar_habilidad"),
        ("Sí Cancelar","si_cancelar"), ("Sí Evolucionar","si_evolucionar"),
        ("Disco Terminado","disco_terminado"), ("C Ladrillo","c_ladrillo"),
        ("Disco Vacío","disco_vacio"), ("Foto Ir Fucsia","foto_irFucsia"),
        ("Nombre Juego 1","NOMBRE_JUEGO"), ("Nombre Juego 2","NOMBRE_JUEGO2"),
        ("Nombre Juego 3","NOMBRE_JUEGO3"), ("Nombre Juego 4","NOMBRE_JUEGO4")
    ]
    entradas_imagenes = {}
    for i, (txt, var) in enumerate(items):
        ttk.Label(frame_img, text=txt).grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
        e = ttk.Entry(frame_img, width=40)
        e.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
        e.insert(0, str(getattr(config, var)))
        entradas_imagenes[var] = e
        ttk.Button(frame_img, text="Examinar…", command=lambda ent=e: browse_file(ent)).grid(row=i,column=2,padx=5,pady=5)

    # Funciones guardar y reset
    def guardar_config():
        for var, e in entradas_controles.items():
            v = e.get().strip()
            setattr(config, var, int(v) if var=="vecesAroma" else v)
        for var, e in entradas_imagenes.items():
            setattr(config, var, e.get().strip())
        data = {**{k: getattr(config,k) for k in entradas_controles}, **{k: getattr(config,k) for k in entradas_imagenes}}
        path = os.path.join(os.path.dirname(__file__),"config.json")
        with open(path,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=2)
        log_message("✅ Configuración guardada.")
        config_win.destroy()

    def reset_defaults():
        cfg = os.path.join(os.path.dirname(__file__),"config.json")
        if os.path.exists(cfg):
            os.remove(cfg)
        importlib.reload(config)
        for var,e in entradas_controles.items():
            e.delete(0,tk.END)
            e.insert(0,str(getattr(config,var)))
        for var,e in entradas_imagenes.items():
            e.delete(0,tk.END)
            e.insert(0,str(getattr(config,var)))
        log_message("🔄 Valores predeterminados restaurados.")

    # Botones
    btn_frame = ttk.Frame(config_win)
    btn_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
    tb.Button(btn_frame, text="💾 Guardar", bootstyle="success", command=guardar_config).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
    tb.Button(btn_frame, text="🔄 Reset Predeterminado", bootstyle="warning", command=reset_defaults).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

# ----------------------------------------------------------------------
# MANEJO DEL LOG EN TIEMPO REAL
# ----------------------------------------------------------------------
def update_log_text(log_text, root):
    while not log_queue.empty():
        msg = log_queue.get()
        log_text.config(state=tk.NORMAL)
        log_text.insert(tk.END, msg + "\n")
        log_text.see(tk.END)
        log_text.config(state=tk.DISABLED)
    root.after(100, update_log_text, log_text, root)

# ----------------------------------------------------------------------
# PANTALLA DE LOGIN (Toplevel)
# ----------------------------------------------------------------------
def login_screen(parent):
    login_win = tk.Toplevel(parent)
    login_win.title("Inicio de Sesión")
    login_win.geometry("400x300")
    # Asignar icono a la ventana de login
    ico = os.path.join(os.path.dirname(__file__), 'assets', 'logo.ico')
    try:
        login_win.iconbitmap(ico)
    except Exception:
        pass
    login_win.option_add("*Font", ("Segoe UI", 10))

    authenticated = tk.BooleanVar(value=False)
    frame = tb.Frame(login_win, padding=10)
    frame.pack(expand=True, fill="both")
    ttk.Label(frame, text="Email:").pack(pady=5)
    email_entry = ttk.Entry(frame)
    email_entry.pack(pady=5)
    ttk.Label(frame, text="Contraseña:").pack(pady=5)
    password_entry = ttk.Entry(frame, show="*")
    password_entry.pack(pady=5)
    error_label = ttk.Label(frame, text="", foreground="red")
    error_label.pack(pady=5)

    def attempt_login():
        success, result = authenticate_user(email_entry.get().strip(), password_entry.get().strip())
        if success:
            authenticated.set(True)
            login_win.destroy()
        else:
            error_label.config(text=f"Error: {result}")

    tb.Button(frame, text="Iniciar Sesión", bootstyle="success", command=attempt_login).pack(pady=10)
    parent.wait_window(login_win)
    return authenticated.get()

# ----------------------------------------------------------------------
# CONSTRUCCIÓN DE LA VENTANA PRINCIPAL
# ----------------------------------------------------------------------
def build_main_gui(root):
    current_dir = os.path.dirname(__file__)
    ico_path = os.path.join(current_dir, 'assets', 'logo.ico')
    try:
        root.iconbitmap(ico_path)
    except Exception:
        pass
    # También asignar logo como PhotoImage para dark mode
    try:
        logo_img = tk.PhotoImage(file=os.path.join(current_dir, 'assets', 'logo.png'))
        root.iconphoto(False, logo_img)
        root.logo_image = logo_img
    except Exception:
        pass

    frame_buttons = tb.Frame(root, padding=10)
    frame_buttons.pack(pady=10)
    tb.Button(frame_buttons, text="▶ Iniciar Magikarp", bootstyle="success", command=lambda: start_automation(root)).pack(side=tk.LEFT, padx=5)
    tb.Button(frame_buttons, text="✨ Iniciar EXP",     bootstyle="warning", command=lambda: start_exp_automation(root)).pack(side=tk.LEFT, padx=5)
    tb.Button(frame_buttons, text="■ Detener",          bootstyle="danger",  command=stop_automation).pack(side=tk.LEFT, padx=5)
    tb.Button(frame_buttons, text="⚙ Configurar",       bootstyle="info",    command=lambda: open_config_window(root)).pack(side=tk.LEFT, padx=5)

    frame_log = tb.Frame(root, padding=10)
    frame_log.pack(fill=tk.BOTH, expand=True)
    log_text = tk.Text(frame_log, wrap=tk.WORD, state=tk.DISABLED, bg="#1e1e1e", fg="#f8f8f2", insertbackground="white")
    log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = ttk.Scrollbar(frame_log, command=log_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    log_text.config(yscrollcommand=scrollbar.set)
    update_log_text(log_text, root)

# ----------------------------------------------------------------------
# FUNCIÓN PRINCIPAL DE LA APP
# ----------------------------------------------------------------------
def main_app():
    root = tb.Window(themename="darkly")
    root.title("PokeFarm")
    root.geometry("700x500")
    root.option_add("*Font", ("Segoe UI", 10))
    root.withdraw()
    if login_screen(root):
        root.deiconify()
        build_main_gui(root)
        root.mainloop()
    else:
        root.destroy()
