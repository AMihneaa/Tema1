import os;

import pandas as pd;
import matplotlib.pyplot as plt

from manager import Manager

persoane = [];

def creazaPersoana(fileLocation):
    with open(fileLocation, "r+") as fisier:
        name = fisier.readline();
        salary = fisier.readline();
        company = fisier.readline();

        pozitie_cursor = fisier.tell()

        restul_fisierului = fisier.read()

        fisier.seek(0)
        fisier.truncate()

        fisier.write(restul_fisierului)
    manager = Manager(name, salary, company);

    return manager;

def creazaCopieFisier(sourceFile, destinationFile):
    try:
        with open (sourceFile, "r") as sFile:
            data = sFile.read();

            with open (destinationFile, "w") as dFile:
                dFile.write(data);

        return destinationFile;

    except FileNotFoundError:
        return destinationFile;

def problema1():
    y = 12

    contor = y / 3;

    newLocation = creazaCopieFisier("dateProblema1.txt", "copieDate.txt");

    for x in range (int(contor)):
        manager = creazaPersoana(newLocation);
        persoane.append(manager);

    for x in persoane:
        x.display_employee();

    print(persoane[0].empCount);

    os.remove(newLocation);


def plotCsv(data, xLabel, yLabel, plotTitle):
    df = pd.DataFrame(data);
    df.plot(x = xLabel, y = yLabel, kind='line', marker='o', linestyle='-', color = 'b', label='Valori');

    plt.title = plotTitle;
    plt.xlabel = xLabel;
    plt.ylabel = yLabel;

    plt.legend();

    plt.show();
def writeCsvLine(data, x1, y1):
    try:
        data1 = data.head(x1);
        print(f"Datele pentru primele {x1} linii \n {data1} \n");
        print("Configuratia pentru tabelul 1 \n");
        xLabel = input("xLabel = ");
        yLabel = input("yLabel = ");
        plotTitle = input("plotTitle = ");

        plotCsv(data1, xLabel, yLabel, plotTitle);

        data2 = data.iloc[-y1:, :2];
        print(f"Durata si Pulsul pentru ultimele {y1} coloane: \n {data2} \n");
        print(f"Datele pentru primele {x1} linii \n {data1} \n");
        print("Configuratia pentru tabelul 2 \n");
        xLabel = input("xLabel = ");
        yLabel = input("yLabel = ");
        plotTitle = input("plotTitle = ");
        plotCsv(data2, xLabel, yLabel, plotTitle);

    except Exception as e:
        print(f"Error reading: {e}");
def problema2():
    sourceFile = "data.csv";
    data = pd.read_csv(sourceFile);

    writeCsvLine(data, 10, 12);

if __name__ == "__main__":
    problema1();
    problema2();

