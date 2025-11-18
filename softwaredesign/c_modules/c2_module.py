# c2 module

class Address:
    def __init__(self, street, city, area_code, country, is_home_address=False, is_post_address=False):
        self.street = street
        self.city = city
        self.area_code = area_code
        self.country = country
        self.is_home_address = is_home_address
        self.is_post_address = is_post_address
        self.person = None  # one address may have zero or one person

    def verify_as_home(self):
        # Simulate verification of the address as a home address
        self.is_home_address = True

    def print_for_post_service(self):
        # Simulate printing of the address for postal use
        return f"{self.street}, {self.city}, {self.area_code}, {self.country}"


class Person:
    def __init__(self, name, phone_number, email, address=None):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address  # one-to-one relation: person ↔ address
        if address:
            address.person = self

    def __str__(self):
        return f"{self.name} ({self.email})"


class Student(Person):
    def __init__(self, name, phone_number, email, study_id, average_grade, address=None):
        super().__init__(name, phone_number, email, address)
        self.study_id = study_id
        self.average_grade = average_grade

    def enlist_for_class(self, course_name):
        # Simulate student enrolment
        return f"{self.name} has enrolled in {course_name}."
    def __str__(self):
        return f"Student: {self.name} ({self.study_id})"

class Professor(Person):
    def __init__(self, name, phone_number, email, salary, address=None):
        super().__init__(name, phone_number, email, address)
        self.salary = salary

    def receive_salary(self):
        # Simulate salary receipt
        return f"{self.name} has received salary: €{self.salary:.2f}"


# Example usage
addr = Address("Hauptstrasse 20", "Innsbruck", "6020", "Austria")
student = Student("Inna Berger", "+43 660 1234567", "inna@gmail.com", "BWL2025", 1.4, addr)
prof = Professor("Dr. Bauern", "+43 512 334455", "bauern@mci4you.at", 4200.00)

print(student.enlist_for_class("Robotics"))
print(prof.receive_salary())
print(addr.print_for_post_service())