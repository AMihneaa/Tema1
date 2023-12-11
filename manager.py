from employee import Employee;

class Manager(Employee):
    def __init__(self, name, salary, departamnet):
        super().__init__(name, salary);
        self.departament = departamnet;

    # def __del__(self):
    #     super().__del__(self);

    def display_employee(self):
        print(self.salary);



