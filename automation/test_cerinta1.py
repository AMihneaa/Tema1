import os
import pytest
from manager import Manager
from Cerinta1 import creazaPersoana, creazaCopieFisier, problema1, persoane


@pytest.fixture
def test_file():
    file_name = 'dateProblema1.txt'
    with open(file_name, 'w') as file:
        file.writelines('John \n');
        file.writelines('50000 \n');
        file.writelines("CompanyA \n");
    yield file_name

    os.remove(file_name)

def test_creazaPersoana(test_file):
    manager = creazaPersoana(test_file)
    assert isinstance(manager, Manager)
    assert manager.name == 'John \n'
    assert manager.salary == '50000 \n'
    assert manager.departament == 'CompanyA \n'

def test_creazaCopieFisier(test_file):
    copy_name = 'copieDate.txt'
    destination_file = creazaCopieFisier(test_file, copy_name)
    assert os.path.exists(destination_file)
    with open(destination_file, 'r') as file:
        content = file.read()
    with open(test_file, 'r') as original_file:
        original_content = original_file.read()
    assert content == original_content
    # Clean up: delete the copy after the test
    os.remove(copy_name)

def test_problema1(test_file):
    new_location = creazaCopieFisier(test_file, 'copieDate.txt')

    for x in range(4):
        manager = creazaPersoana(new_location)
        persoane.append(manager);

    os.remove(new_location)
