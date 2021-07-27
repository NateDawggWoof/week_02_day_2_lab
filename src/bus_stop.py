class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_to_queue(self, passenger):
        self.queue.append(passenger)

    def clear(self):
        self.queue.clear()

    def queue_length(self):
        return len(self.queue)
    
