import os
import re

# ==========================================
# 1. CONFIGURACIÓN: PEGA AQUÍ TU NUEVA CONFIGURACIÓN
# Copia esto tal cual te lo da Firebase (entre las comillas triples)
# ==========================================
NUEVA_CONFIG_FIREBASE = """const firebaseConfig = {
apiKey: "AIzaSyCY8V_P7m8lZUvGbMVlGaa-GVhbmyikmag",
  authDomain: "gad-alicante-v4.firebaseapp.com",
  databaseURL: "https://gad-alicante-v4-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "gad-alicante-v4",
  storageBucket: "gad-alicante-v4.firebasestorage.app",
  messagingSenderId: "119727545224",
  appId: "1:119727545224:web:36880c50d196c456cdb83d"
};"""

# ==========================================
# 2. RUTA DE TU CARPETA
# Pon "." si este script está en la misma carpeta que los HTML.
# O pon la ruta completa ejemplo: "C:/Usuarios/TuNombre/Proyecto"
# ==========================================
CARPETA_PROYECTO = "." 

def reemplazar_configuracion():
    # Esta expresión regular busca cualquier variable llamada firebaseConfig
    # que empiece por const, var o let y capture todo lo que hay entre llaves { }
    patron_regex = r"(const|var|let)\s+firebaseConfig\s*=\s*\{[\s\S]*?\};"
    
    contador = 0
    archivos_modificados = []

    print(f"--- Iniciando búsqueda en: {os.path.abspath(CARPETA_PROYECTO)} ---")

    # Recorremos todas las carpetas y subcarpetas
    for raiz, directorios, archivos in os.walk(CARPETA_PROYECTO):
        for archivo in archivos:
            if archivo.endswith(".html") or archivo.endswith(".js"):
                ruta_completa = os.path.join(raiz, archivo)
                
                try:
                    with open(ruta_completa, 'r', encoding='utf-8') as f:
                        contenido = f.read()
                    
                    # Busamos si existe la configuración antigua
                    match = re.search(patron_regex, contenido)
                    
                    if match:
                        print(f"--> Encontrado en: {archivo}")
                        
                        # Reemplazamos el bloque antiguo por el nuevo
                        nuevo_contenido = re.sub(patron_regex, NUEVA_CONFIG_FIREBASE, contenido)
                        
                        # Guardamos el archivo
                        with open(ruta_completa, 'w', encoding='utf-8') as f:
                            f.write(nuevo_contenido)
                        
                        contador += 1
                        archivos_modificados.append(archivo)
                except Exception as e:
                    print(f"Error leyendo {archivo}: {e}")

    print("-" * 30)
    print(f"¡PROCESO TERMINADO! Se actualizaron {contador} archivos.")
    if contador > 0:
        print("Archivos modificados:", archivos_modificados)
    else:
        print("No se encontró ninguna configuración de Firebase para reemplazar.")
        print("Asegúrate de que en tus HTML dice 'const firebaseConfig = { ... };'")

if __name__ == "__main__":
    reemplazar_configuracion()