from PrintOnScreen import DisplayMsg

dsp = DisplayMsg("PrintVariable")
dsp.see("Hello World")

def calculate_age(birth_year, current_year):
    current_age = current_year - birth_year
    return current_age


class biodata:
    def __init__(self, name, birth_year, current_year):
        self.name = name
        self.birth_year = birth_year
        self.current_year = current_year

    def display_data(self):
        msg = "Hello My name is " + self.name
        dsp.see(msg)

    def get_age(self):
        age = calculate_age(self.birth_year, self.current_year)
        dsp.see(f"You Current Age is " + str(age))
        return age


# data = biodata("Stephan", 1997, 2023)
# data.display_data()
# data.get_age()
