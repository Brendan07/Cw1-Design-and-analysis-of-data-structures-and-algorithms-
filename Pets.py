class Pets:
    def __init__(self, pet_id, pet_type, breed, vaccinated, neutered, micro_chip, admission_reason, arrival,
                 departure, destination, destination_address):
        self.pet_id = pet_id
        self.pet_type = pet_type
        self.breed = breed
        self.vaccinated = vaccinated
        self.neutered = neutered
        self.micro_chip = micro_chip
        self.admission_reason = admission_reason
        self.arrival = arrival
        self.departure = departure
        self.destination = destination
        self.destination_address = destination_address

    def __str__(self):
        return_str = "Sanctuary Identification " + self.pet_id + "|"
        return_str += "Type: " + self.pet_type + "|"
        return_str += "Breed: " + self.breed + "|"
        return_str += "Vaccinated: " + self.vaccinated + "|"
        return_str += "Neutered: " + self.neutered + "|"
        return_str += "Microchip Number: " + self.micro_chip + "|"
        return_str += "Reason for admission: " + self.admission_reason + "|"
        return_str += "Date of Arrival: " + self.arrival + "|"
        return_str += "Date of Departure: " + self.departure + "|"
        return_str += "Destination: " + self.destination + "|"
        return_str += "Destination Address: " + self.destination_address + "|"
        return return_str

    # DO FOR OTHER wild etc

    def __lt__(self, other):
        return self.pet_id < other.pet_id

    def __gt__(self, other):
        return self.pet_id > other.pet_id
