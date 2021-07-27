import unittest
from src.bus import Bus
from src.bus_stop import BusStop
from src.person import Person

class TestBus(unittest.TestCase):
    def setUp(self):
        self.bus = Bus(22, "Ocean Terminal", 2, 5)

    # @unittest.skip("Delete this line to run the test")
    def test_has_route_number(self):
        self.assertEqual(22, self.bus.route_number)


    # @unittest.skip("Delete this line to run the test")
    def test_has_destination(self):
        self.assertEqual("Ocean Terminal", self.bus.destination)

    # @unittest.skip("Delete this line to run the test")
    def test_has_price(self):
        self.assertEqual(2, self.bus.price)

    # @unittest.skip("Delete this line to run the test")
    def test_has_capacity(self):
        self.assertEqual(5, self.bus.capacity)

    # @unittest.skip("Delete this line to run the test")
    def test_can_drive(self):
        self.assertEqual("Brum brum", self.bus.drive())

    # @unittest.skip("Delete this line to run the test")
    def test_starts_with_no_passengers(self):
        self.assertEqual(0, self.bus.passenger_count())

    # @unittest.skip("Delete this line to run the test")
    def test_can_pick_up_passenger(self):
        person = Person("Guido van Rossum", 64)
        self.bus.pick_up(person)
        self.assertEqual(1, self.bus.passenger_count())

    # @unittest.skip("Delete this line to run the test")
    def test_can_drop_off_passenger(self):
        person = Person("Guido van Rossum", 64)
        self.bus.pick_up(person)
        self.bus.drop_off(person)
        self.assertEqual(0, self.bus.passenger_count())

    # @unittest.skip("Delete this line to run the test")
    def test_can_empty_bus(self):
        person = Person("Guido van Rossum", 64)
        self.bus.pick_up(person)
        self.bus.empty()
        self.assertEqual(0, self.bus.passenger_count())

    # @unittest.skip("Delete this line to run the test")
    def test_can_pick_up_passenger_from_bus_stop(self):
        person_1 = Person("Guido van Rossum", 64)
        person_2 = Person("Carol Willing", 50)
        bus_stop = BusStop("Waverly Station")
        bus_stop.add_to_queue(person_1)
        print(bus_stop.queue)
        bus_stop.add_to_queue(person_2)
        print(bus_stop.queue)

        self.bus.pick_up_from_stop(bus_stop)
        self.assertEqual(2, self.bus.passenger_count())


    # @unittest.skip("Delete this line to run the test")
    def test_can_pick_up_passenger_from_bus_stop_extended(self):
        person_1 = Person("Guido van Rossum", 64, 100, "Ocean Terminal")
        person_2 = Person("Carol Willing", 50, 75, "Gyle")
        bus_stop = BusStop("Waverly Station")
        bus_stop.add_to_queue(person_1)
        print(bus_stop.queue)
        bus_stop.add_to_queue(person_2)
        print(bus_stop.queue)

        self.bus.pick_up_from_stop(bus_stop)
        self.assertEqual(1, self.bus.passenger_count())

    def test_can_pick_up_passenger_from_bus_stop_extended_part2(self):
        person_1 = Person("Guido van Rossum", 64, 100, "Ocean Terminal")
        person_2 = Person("Carol Willing", 50, 75, "Gyle")
        bus_stop = BusStop("Waverly Station")
        bus_stop.add_to_queue(person_1)
        bus_stop.add_to_queue(person_2)

        self.bus.pick_up_from_stop(bus_stop)
        self.assertEqual(1, self.bus.passenger_count())

        person_3 = Person("Guido van Rossum", 64, 100, "Ocean Terminal")
        person_4 = Person("Carol Willing", 50, 75, "Ocean Terminal")
        person_5 = Person("Guido van Rossum", 64, 100, "Ocean Terminal")
        person_6 = Person("Carol Willing", 50, 75, "Ocean Terminal")
        person_7 = Person("Guido van Rossum", 64, 100, "Ocean Terminal")
        person_8 = Person("Carol Willing", 50, 75, "Ocean Terminal")
        bus_stop.add_to_queue(person_3)
        bus_stop.add_to_queue(person_4)
        bus_stop.add_to_queue(person_5)
        bus_stop.add_to_queue(person_6)
        bus_stop.add_to_queue(person_7)
        bus_stop.add_to_queue(person_8)


        self.bus.pick_up_from_stop(bus_stop)
        self.assertEqual(5, self.bus.passenger_count())
        
        

        
                