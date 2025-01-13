import tkinter as tk
from tkinter import messagebox
from urllib.error import URLError, HTTPError
from urllib.request import urlopen


def check_internet():
    url = url_entry.get()   # Obtiene la URL ingresada por el usuario
    try:
        reponse = urlopen(url)  # Intenta abrir la URL ingresada por el usuario 
        status_code = reponse.getcode() # Obtiene el código de estado de la respuesta del servidor web 
        if status_code != 200:      # Si el código de estado no es 200, muestra un mensaje de advertencia 
            messagebox.showwarning(
                "Estado del Sitio Web",
                f"El sitio web respondió con el código: {status_code}",
            )
        else:
            messagebox.showinfo(
                "Estado del Sitio Web",
                f"El sitio web está funcionando correctamente (Código {status_code})",
            )   # Si el código de estado es 200, muestra un mensaje de información 
    
    except HTTPError as e:
        messagebox.showerror("Error HTTP", f"Error HTTP: {e.code}")
    except URLError as u:
        messagebox.showerror("No se pudo conectar al sitio web.", f"Error URL: {u.reason}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una URL válida.")


def main():
    global url_entry    # Variable global para acceder a la entrada de la URL en la función
    
    root = tk.Tk()
    root.title("Verificar Estado de un Sitio Web")
    root.geometry("500x250")
    #root.resizable(False, False)

    tk.Label(root, text="Ingrese la URL del sitio web:").pack(pady=10)
    
    url_entry = tk.Entry(root, width=50)    # Crea una entrada para que el usuario ingrese la URL del sitio web 
    url_entry.pack(pady=5) # ancho de la entrada

    check_button = tk.Button(root, text="Probar conexión", command=check_internet)
    check_button.pack(pady=20)

    root.mainloop() # Inicia el bucle principal de la aplicación tkinter 

if __name__ == "__main__":  # Si el script se ejecuta directamente, llama a la función main() 
    main()
