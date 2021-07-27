

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
        """TODO"""
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
        travelers = []
        for person in bus_stop.queue:
            if not person.destination: 
                self.passengers.append(person)                
            elif person.destination != self.destination or person.cash >= self.price:
                continue
            else:
                travelers.append(person)
                self.payment(person)

        if len(travelers) <= self.remaining_capacity():
                self.passengers.extend(travelers)
        else:
            self.passengers.extend(travelers[0:self.remaining_capacity()])

    # def bus_journey(self):
    #     self.pick_up_from_stop()

            

        
    