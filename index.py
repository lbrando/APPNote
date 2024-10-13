import customtkinter as ctk

# Funzione chiamata dal pulsante
def funzione_chiamata():
    print("Chiamata")

# Definizione della finestra
window = ctk.CTk()

# Titolo della finestra
window.title("Titolo")

# Dimensione della finestra
window.geometry("500x200")

# Do un peso uguale alle colonne definite nella tupla in modo che queste siano identiche come grandezza
window.grid_columnconfigure((0, 1), weight=1)

# Definizione del bottone
button = ctk.CTkButton(window, text="Testo Bottone", command=funzione_chiamata)
# Inserisco il bottone nella griglia con padding 20 in entrambi gli assi
# Dando l'attributo 'sticky="ew"' (che significa east e west) faccio in modo che prenda tutto lo spazio orizzontale disponibile
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

# Definizione del bottone
button2 = ctk.CTkButton(window, text="Testo", command=funzione_chiamata)
# Inserisco il bottone nella griglia con padding 20 in entrambi gli assi
button2.grid(row=0, column=1, padx=20, pady=20)

# Definizione del bottone
button3 = ctk.CTkButton(window, text="Testone", command=funzione_chiamata)
# Inserisco il bottone nella griglia con padding 20 in entrambi gli assi
# Dando l'attributo 'sticky="ew"' (che significa east e west) faccio in modo che prenda tutto lo spazio orizzontale disponibile
# Con columnspan=2 definisco che questa riga si "espande" su 2 colonne, posso fare lo stesso con le righe tramite 'rawspan'
button3.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

# Definizione della checkbox
checkbox_1 = ctk.CTkCheckBox(window, text="checkbox 1")
# Inserisco la checkbox nella griflia, facendola "attaccare" sul lato a est, il padding y ha come valore una tupla, in modo da averlo solo sotto
checkbox_1.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="e")
# Definizione della checkbox
checkbox_2 = ctk.CTkCheckBox(window, text="checkbox 2")
# Inserisco la checkbox nella griflia, facendola "attaccare" sul lato a ovest (west), il padding y ha come valore una tupla, in modo da averlo solo sotto
checkbox_2.grid(row=2, column=1, padx=20, pady=(0, 20), sticky="w")

# Messa in loop la finestra
window.mainloop()