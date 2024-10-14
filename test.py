import tkinter as tk

class App(tk.Tk):
    def __init__(self, window_width, window_height):
        super().__init__()
        
        # Titolo della finestra
        self.title("Titolo")
        # Dimensione della finestra
        self.geometry(f"{window_width}x{window_height}")

        # Do un peso uguale alle colonne definite nella tupla in modo che queste siano identiche come grandezza
        self.grid_columnconfigure((0, 1), weight=1)

        # Definizione del bottone
        # Inserisco il bottone nella griglia con padding 20 in entrambi gli assi
        # Dando l'attributo 'sticky="ew"' (che significa east e west) faccio in modo che prenda tutto lo spazio orizzontale disponibile
        self.button = tk.Button(self, text="Testo Bottone", command=self.funzione_chiamata).grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Definizione del bottone
        # Inserisco il bottone nella griglia con padding 20 in entrambi gli assi
        self.button2 = tk.Button(self, text="Testo", command=self.funzione_chiamata).grid(row=0, column=1, padx=20, pady=20)

        # Definizione del bottone
        # Inserisco il bottone nella griglia con padding 20 in entrambi gli assi
        # Dando l'attributo 'sticky="ew"' (che significa east e west) faccio in modo che prenda tutto lo spazio orizzontale disponibile
        # Con columnspan=2 definisco che questa riga si "espande" su 2 colonne, posso fare lo stesso con le righe tramite 'rawspan'
        self.button3 = tk.Button(self, text="Testone", command=self.funzione_chiamata).grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        # Definizione della checkbox
        # Inserisco la checkbox nella griflia, facendola "attaccare" sul lato a est, il padding y ha come valore una tupla, in modo da averlo solo sotto
        self.checkbox_1 = tk.Checkbutton(self, text="checkbox 1").grid(row=2, column=0, padx=20, pady=(0, 20), sticky="e")

        # Definizione della checkbox
        # Inserisco la checkbox nella griflia, facendola "attaccare" sul lato a ovest (west), il padding y ha come valore una tupla, in modo da averlo solo sotto
        self.checkbox_2 = tk.Checkbutton(self, text="checkbox 2").grid(row=2, column=1, padx=20, pady=(0, 20), sticky="w")

    # Funzione chiamata dal pulsante
    def funzione_chiamata(self):
        print("Chiamata")

root = App(500, 200)
# Messa in loop la finestra
root.mainloop()