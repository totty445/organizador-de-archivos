import os
import shutil

# Pedir la ruta de forma interactiva en la terminal
ruta_destino = input("Ingresa la ruta de la carpeta que quieres organizar (ej. C:\\Users\\TuUsuario\\Downloads): ").strip('"') 

def organizar_carpeta():
    if not os.path.exists(ruta_destino):
        print("❌ La ruta no existe o está mal escrita. Inténtalo de nuevo.")
        return

    # Diccionario de extensiones y carpetas
    extensiones = {
        "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Instaladores": [".exe", ".msi", ".zip", ".rar"]
    }

    contador = 0
    for archivo in os.listdir(ruta_destino):
        ruta_archivo = os.path.join(ruta_destino, archivo)
        
        # Ignorar si es una carpeta
        if os.path.isdir(ruta_archivo):
            continue

        _, extension = os.path.splitext(archivo)
        
        for carpeta, exts in extensiones.items():
            if extension.lower() in exts:
                carpeta_destino = os.path.join(ruta_destino, carpeta)
                
                # Crear la carpeta si no existe
                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)
                
                # Mover el archivo
                shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                print(f"📦 Movido: {archivo} -> {carpeta}/")
                contador += 1
                break

    print(f"\n¡Listo! Se organizaron {contador} archivos con éxito.")

if __name__ == "__main__":
    organizar_carpeta()