import serial
import serial.tools.list_ports
import time
import tkinter as tk
from tkinter import messagebox

def find_arduino():
    """Détecte automatiquement le port de l'Arduino Uno"""
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "Arduino" in port.description or "CH340" in port.description:  # CH340 pour clones Arduino
            return port.device  # Retourne le port (ex: COM3 ou /dev/ttyUSB0)
    return None  # Aucun Arduino trouvé

# Trouver le port Arduino
arduino_port = find_arduino()

if arduino_port:
    ser = serial.Serial(arduino_port, 9600, timeout=1)
    time.sleep(2)  # Attente pour l'initialisation du port
else:
    messagebox.showerror("Erreur", "Aucun Arduino détecté. Vérifiez la connexion.")
    exit()

def set_pump_speed(event=None):  # `event` ajouté pour gérer l'entrée clavier
    """Récupère la vitesse et envoie à l'Arduino"""
    try:
        speed_percent = int(speed_entry.get())  # Récupère la valeur entrée
        if 0 <= speed_percent <= 100:
            speed_us = int(500 + (speed_percent / 100) * 1000)  # Conversion en microsecondes
            ser.write(f"{speed_us}\n".encode())  # Envoi de la vitesse
            status_label.config(text=f"✔ Consigne envoyée : {speed_percent}%", fg="green")
        else:
            status_label.config(text=f"❌ Erreur : {speed_percent}% hors limite (0-100%)", fg="red")
        
        reset_status_timer()  # Réinitialise le timer de 5 secondes

    except ValueError:
        status_label.config(text="❌ Erreur : entrée invalide", fg="red")
        reset_status_timer()

def stop_pump():
    """Arrête la pompe sans quitter"""
    ser.write(b"1500\n")  # Envoie la consigne d'arrêt (1500 µs)
    speed_entry.delete(0, tk.END)  # Efface l'entrée actuelle
    speed_entry.insert(0, "0")  # Met à jour à 0%
    status_label.config(text="🔴 Pompe arrêtée (0%)", fg="orange")
    reset_status_timer()

def quit_app():
    """Arrête la pompe et ferme l'application"""
    ser.write(b"-1\n")  # Envoi de la commande d'arrêt définitif
    root.quit()  # Ferme l'interface graphique

def reset_status_timer():
    """Réinitialise le timer de 5 secondes pour effacer le message"""
    root.after_cancel(clear_status_id)  # Annule le précédent timer
    root.after(5000, clear_status)  # Redémarre le timer de 5 sec

def clear_status():
    """Efface le message de validation ou d'erreur après 5 secondes"""
    status_label.config(text="")

# Création de la fenêtre Tkinter
root = tk.Tk()
root.iconbitmap("lab-sticc.ico")
root.title("Contrôle de la Pompe")
root.geometry("350x250")
root.resizable(False, False)

# Cadre principal pour centrer le contenu
main_frame = tk.Frame(root)
main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Cadre pour la saisie et le bouton envoyer (alignés sur la même ligne)
input_frame = tk.Frame(main_frame)
input_frame.pack(pady=10)

# Champ de saisie pour la vitesse
tk.Label(input_frame, text="Vitesse (0-100%) :").pack(side=tk.LEFT, padx=5)
speed_entry = tk.Entry(input_frame, width=10)
speed_entry.pack(side=tk.LEFT, padx=5)
speed_entry.insert(0, "0")  # Par défaut à 0%
speed_entry.bind("<Return>", set_pump_speed)  # ✅ Envoi par touche "Entrée"

# Bouton Envoyer
send_button = tk.Button(input_frame, text="Envoyer", command=set_pump_speed, bg="lightblue")
send_button.pack(side=tk.LEFT, padx=5)

# Message d'état (vert ou rouge selon réussite/erreur)
status_label = tk.Label(main_frame, text="", font=("Arial", 10))
status_label.pack(pady=5)

# Bouton "Arrêt Pompe" (90% de la largeur)
stop_pump_button = tk.Button(main_frame, text="Arrêt Pompe", command=stop_pump, bg="orange", fg="black")
stop_pump_button.pack(pady=5, fill=tk.X, padx=0)  # ✅ Même largeur que STOP

# Bouton Stop (90% de la largeur)
stop_button = tk.Button(main_frame, text="STOP", command=quit_app, bg="red", fg="white")
stop_button.pack(pady=5, fill=tk.X, padx=0)

# Label signature (en bas à droite)
signature_label = tk.Label(root, text="créé par Grégory Mignot pour le Lab-STICC - 2025", font=("Arial", 8), fg="gray")
signature_label.place(relx=1.0, rely=1.0, anchor="se", x=-5, y=-5)  # Placé en bas à droite

# Timer de nettoyage des messages d'état
clear_status_id = root.after(5000, clear_status)  # Démarre le timer initial

# Lancer Tkinter
root.mainloop()
