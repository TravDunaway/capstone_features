class Currentlocation:
    def __init__(self, customer_id, time_of_day, number_of_times_used, location_id):
        self.customer_id = customer_id
        self.time_of_day = time_of_day
        self.number_of_times_used = number_of_times_used
        self.location_id = location_id

class Home:
    def __init__(self, home_id, customer_id, fastest_route, alternatives, time_of_day, number_of_times_used, location_id):
        self.home_id = home_id
        self.customer_id = customer_id
        self.fastest_route = fastest_route
        self.alternatives = alternatives
        self.time_of_day = time_of_day
        self.number_of_times_used = number_of_times_used
        self.location_id = location_id

class Work:
    def __init__(self, home_id, customer_id, fastest_route, alternatives, time_of_day, number_of_times_used, location_id):
        self.home_id = home_id
        self.customer_id = customer_id
        self.fastest_route = fastest_route
        self.alternatives = alternatives
        self.time_of_day = time_of_day
        self.number_of_times_used = number_of_times_used
        self.location_id = location_id

class School:
    def __init__(self, home_id, customer_id, fastest_route, alternatives, time_of_day, number_of_times_used, location_id):
        self.home_id = home_id
        self.customer_id = customer_id
        self.fastest_route = fastest_route
        self.alternatives = alternatives
        self.time_of_day = time_of_day
        self.number_of_times_used = number_of_times_used
        self.location_id = location_id
