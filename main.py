from manager import Manager
persoane = [];

def creazaPersoana():
    name = input("Enter your name: ");
    salary = input("Enter your salary: ");
    company = input("Enter your company: ");
    manager = Manager(name, salary, company);

    return manager;

if __name__ == "__main__":
    y = 12

    contor = y / 3;

    for x in range (int(contor)):
        manager = creazaPersoana();
        persoane.append(manager);

    for x in persoane:
        x.display_employee();

    print(persoane[0].empCount);

