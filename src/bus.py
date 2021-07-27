

class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.destination = destination
        self.capacity = capacity
        self.price = price
        self.passengers = []
        self.total_cash = 0

    def drive(self):
        return 'Brum brum'

    def passenger_count(self):
        return len(self.passengers)

    def remaining_capacity(self):
        return self.capacity - len(self.passengers)

    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty(self):
        self.passengers.clear()

    def payment(self, passenger):
        """TODO"""
        passenger.cash -= self.price
        self.total_cash += self.price
    
    def pick_up_from_stop(self, bus_stop):
        full_queue = bus_stop.queue.copy()
        for person in full_queue:
            if not person.destination and (self.remaining_capacity() > 0): 
                self.passengers.append(person)               
            elif person.destination != self.destination or person.cash <= self.price or self.remaining_capacity() == 0:
                continue
            else:
                self.payment(person)
                self.passengers.append(person) 
                bus_stop.remove_passanger(person)
    
        

        
    