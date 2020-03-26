
class Department:
    def __init__(self, name, code):
        self._name = name
        self._code = code


class Employee:
    hours = 8

    def __init__(self, code, name, salary):
        if type(self) == Employee:
            raise TypeError()
        self._code = code
        self._name = name
        self._salary = salary

    @classmethod
    def calc_bonus(cls):
        pass

    @classmethod
    def get_hours(cls):
        return cls.hours


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('managers', 1)

    def calc_bonus(self):
        return self._salary * 0.15

    def get_department(self):
        return self._departament._name

    def set_department(self, name):
        self._departament._name = name


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('sellers', 2)
        self._sales = 0

    def get_sales(self):
        return self._sales

    def put_sales(self, sale):
        self._sales += sale

    def get_department(self):
        return self._departament._name

    def set_department(self, name):
        self._departament._name = name

    def calc_bonus(self):
        return self._sales * 0.15
