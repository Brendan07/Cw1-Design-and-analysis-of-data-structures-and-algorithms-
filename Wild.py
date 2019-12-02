class Wild:
    def __init__(self, wild_id, wild_type, vaccinated, admission_reason, arrival,
                 departure, destination, destination_address):
        self.wild_id = wild_id
        self.wild_type = wild_type
        self.vaccinated = vaccinated
        self.admission_reason = admission_reason
        self.arrival = arrival
        self.departure = departure
        self.destination = destination
        self.destination_address = destination_address

    def __str__(self):
        return_str = "Sanctuary Identification: " + self.wild_id + "|"
        return_str += "Type: " + self.wild_type + "|"
        return_str += "Vaccinated: " + self.vaccinated + "|"
        return_str += "Reason for admission: " + self.admission_reason + "|"
        return_str += "Date of Arrival: " + self.arrival + "|"
        return_str += "Date of Departure: " + self.departure + "|"
        return_str += "Destination: " + self.destination + "|"
        return_str += "Destination Address: " + self.destination_address + "|"
        return return_str

    def __lt__(self, other):
        return self.wild_id < other.wild_id

    def __gt__(self, other):
        return self.wild_id > other.wild_id
