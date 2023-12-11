import os
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

