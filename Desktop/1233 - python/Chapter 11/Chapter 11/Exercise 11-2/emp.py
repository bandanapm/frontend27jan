# Programming Exercise 11-2

class Employee:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_name(self):
        return self.__name
        
    def get_id_number(self):
        return self.__id_number
        
class ProductionWorker(Employee):
    def __init__(self, name, id_number, shift_number, pay_rate):
        # Call superclass __init__ method.
        Employee.__init__(self, name, id_number)

        # Initialize the shift_number and pay_rate attributes.
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate

    # Mutator functions for shift_number and pay_rate.
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    # Accessor functions for shift_number and pay_rate.
    def get_shift_number(self):
        return self.__shift_number

    def get_pay_rate(self):
        return self.__pay_rate

class ShiftSupervisor(Employee):
    def __init__(self, name, id_number, salary, bonus):
        # Call superclass __init__ method.
        Employee.__init__(self, name, id_number)

        # Initialize the salary and bonus attributes.
        self.__salary = salary
        self.__bonus = bonus

    # Mutator functions for salary and bonus.
    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    # Accessor functions for salary and bonus.
    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus




