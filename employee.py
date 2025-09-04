class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


class PartTimeEmployee(Employee):
    def __init__(self, name, age, hourly_rate):
        super().__init__(name, age)
        self.hourly_rate = hourly_rate

    def daily_wage(self, hours):
        return self.hourly_rate * hours


class FullTimeEmployee(Employee):
    def __init__(self, name, age, monthly_rate):
        super().__init__(name, age)
        self.monthly_rate = monthly_rate

    def yearly_salary(self):
        return self.monthly_rate * 12


if __name__ == "__main__":
    pt = PartTimeEmployee("Ali", 22, 15)
    ft = FullTimeEmployee("Sara", 30, 2000)

    print(pt.get_name(), "Daily Wage:", pt.daily_wage(8))
    print(ft.get_name(), "Yearly Salary:", ft.yearly_salary())
