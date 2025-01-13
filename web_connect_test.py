import tkinter as tk
from tkinter import messagebox
from urllib.error import URLError, HTTPError
from urllib.request import urlopen


def check_internet():
    url = url_entry.get()
    try:
        reponse = urlopen(url)
        status_code = reponse.getcode()
        if status_code != 200:
            messagebox.showwarning(
                "Estado del Sitio Web",
                f"El sitio web respondió con el código: {status_code}",
            )
        else:
            messagebox.showinfo(
                "Estado del Sitio Web",
                f"El sitio web está funcionando correctamente (Código {status_code})",
            )
    except HTTPError as e:
        messagebox.showerror("Error HTTP", f"Error HTTP: {e.code}")
    except URLError as u:
        messagebox.showerror(
            "No se pudo conectar al sitio web.", f"Error URL: {u.reason}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una URL válida.")


def main():
    global url_entry
    
    root = tk.Tk()
    root.title("Verificar Estado de un Sitio Web")
    root.geometry("500x250")
    #root.resizable(False, False)

    tk.Label(root, text="Ingrese la URL del sitio web:").pack(pady=10)
    
    url_entry = tk.Entry(root, width=50)
    url_entry.pack(pady=5) # ancho de la entrada

    check_button = tk.Button(root, text="Probar conexión", command=check_internet)
    check_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
