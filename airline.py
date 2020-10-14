class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.pesangers = []

    def add_passengers(self, name):
        if not self.open_sits():
            return False
        else:
            self.pesangers.append(name)
            return True

    def open_sits(self):
        return self.capacity-len(self.pesangers)


flight = Flight(3)
passengers = ['Dipu', 'Ramiza', 'Simran', 'MOni']


for persons in passengers:
    if flight.add_passengers(persons):
        print(f'Added {persons} to flight Succesfully')
    else:
        print(f"No availabe seats for {persons}")
