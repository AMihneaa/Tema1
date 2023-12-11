import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar
import pandas as pd
import matplotlib.pyplot as plt
import tkinter.simpledialog

def plotCsv(data, xLabel, yLabel, plotTitle):
    df = pd.DataFrame(data)
    df.plot(x=xLabel, y=yLabel, kind='line', marker='o', linestyle='-', color='b', label='Valori')

    plt.title(plotTitle)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    plt.legend()
    plt.show()

def writeCsvLine(data, x1, y1, xLabel, yLabel, plotTitle):
    try:
        data1 = data.head(x1)
        print(f"Datele pentru primele {x1} linii:\n{data1}\n")
        print("Configuratia pentru tabelul 1\n")

        plotCsv(data1, xLabel, yLabel, plotTitle)

        data2 = data.iloc[-y1:, :2]
        print(f"Durata si Pulsul pentru ultimele {y1} coloane:\n{data2}\n")
        print(f"Datele pentru primele {x1} linii:\n{data1}\n")
        print("Configuratia pentru tabelul 2\n")
        plotCsv(data2, xLabel, yLabel, plotTitle)

    except Exception as e:
        print(f"Error reading: {e}")

def afiseaza_grafic():
    root2 = tk.Tk()
    root2.title("Fereastră cu Intrări")

    # Adaugăm 3 câmpuri de intrare
    label1 = tk.Label(root2, text="xLabel")
    label1.grid(row=0, column=0)
    entry1 = tk.Entry(root2)
    entry1.grid(row=0, column=1)

    label2 = tk.Label(root2, text="yLabel")
    label2.grid(row=1, column=0)
    entry2 = tk.Entry(root2)
    entry2.grid(row=1, column=1)

    label3 = tk.Label(root2, text="Title")
    label3.grid(row=2, column=0)
    entry3 = tk.Entry(root2)
    entry3.grid(row=2, column=1)

    def ok_button_click():
        xLabel = entry1.get()
        yLabel = entry2.get()
        title = entry3.get()

        sourceFile = "data.csv";
        data = pd.read_csv(sourceFile);
        writeCsvLine(data, 10, 12, xLabel, yLabel, title)

        print(f"xLabel 1: {xLabel}")
        print(f"Input 2: {yLabel}")
        print(f"Input 3: {title}")

        root2.destroy()

    ok_button = tk.Button(root2, text="OK", command=ok_button_click)
    ok_button.grid(row=3, column=0, columnspan=2, pady=10)

    root2.mainloop()

def problema2_UI():
    sourceFile = "data.csv"
    data = pd.read_csv(sourceFile)

    root = tk.Tk()
    root.title("Aplicație cu UI")

    meniu = tk.Menu(root)
    root.config(menu=meniu)

    meniu_fisier = tk.Menu(meniu, tearoff=0)
    meniu_fisier.add_command(label="Deschide")
    meniu_fisier.add_command(label="Salvează")
    meniu.add_cascade(label="Fișier", menu=meniu_fisier)

    frame = ttk.Frame(root)
    frame.grid(row=0, column=0)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=(None, 10, "bold"))
    style.configure("Treeview", font=(None, 8))

    tree = ttk.Treeview(frame, columns=list(data.columns), show='headings', style="Treeview")

    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for index, row in data.iterrows():
        tree.insert("", index, values=list(row))

    tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    scrollbar = Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

    buton_actualizare = tk.Button(root, text="Afiseaza Grafic", command=afiseaza_grafic)
    buton_actualizare.grid(row=1, column=0, pady=10)

    root.mainloop()

# writeCsvLine(data, 10, 12);
