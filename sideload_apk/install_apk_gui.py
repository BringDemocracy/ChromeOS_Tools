import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def installer_apk():
    filepath = filedialog.askopenfilename(filetypes=[("Fichiers APK", "*.apk")])
    if filepath:
        try:
            result = subprocess.run(["adb", "install", filepath], capture_output=True, text=True)
            if result.returncode == 0:
                messagebox.showinfo("Succès", "APK installé avec succès.")
            else:
                messagebox.showerror("Erreur", f"Erreur lors de l'installation :\n{result.stderr}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Exception : {str(e)}")

# Création de la fenêtre
root = tk.Tk()
root.title("Installeur d'APK")

# Taille minimale
root.geometry("300x150")

# Bouton pour choisir et installer l'APK
btn_installer = tk.Button(root, text="Sélectionner et installer un APK", command=installer_apk)
btn_installer.pack(pady=40)

# Lancer la boucle principale
root.mainloop()
