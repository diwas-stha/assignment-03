'''
Create a Python class to represent a University. The university should have
attributes like name, location, and a list of departments.
Implement encapsulation to
protect the internal data of the University class. Create a Department
class that
inherits from the University class. The Department class should have attributes
 like
department name, head of the department, and a list of courses offered.
 Implement
polymorphism by defining a common method for both the University and
Department classes to display their details.

'''


class University:
    '''
        A class representing a University.

        Attributes:
            name (str): The name of the university.
            location (str): The location of the university.
            departments (list): A list of Department objects.

    '''

    def __init__(self, name, location):
        '''
        Initialize a new University object.

        Parameters:
            name (str): The name of the university.
            location (str): The location of the university.
        '''
        self._name = name
        self._location = location
        self._departments = []

    def add_department(self, department):
        """
        Add a new Department to the university.

        Parameters:
            department (Department): The Department object to add.
        """
        self._departments.append(department)

    def display_details(self):
        """
        Display details of the university and its departments.
        """
        print(f"University Name: {self._name}")
        print(f"Location: {self._location}")
        print("Departments:")
        for department in self._departments:
            print(f" - {department.get_department_name()}")


class Department(University):
    '''
    A class representing deparment of university.

    Attributes:
        name (str): The name of the university.
        location (str): The location of the university.
        department_name (str): The name of the department.
        head_of_department (str): The head of the department.

    '''

    def __init__(self, name, location, department_name, head_of_department):
        '''
        Initialize a new Department object.

        Parameters:
            name (str): The name of the university.
            location (str): The location of the location.
            department_name (str): The name of department
            head_of_department (str): The head of the department.

        '''
        super().__init__(name, location)
        self._department_name = department_name
        self._head_of_department = head_of_department
        self._courses_offered = []

    def add_course(self, course):
        '''
        Add a new course to the department's list of courses offered.

        Parameters:
            course (str): The name of the course to add.
        '''
        self._courses_offered.append(course)

    def get_department_name(self):
        '''
        Get the name of the department

        Return:
            str: The name of the department
        '''
        return f"{self._department_name} Department"

    def display_details(self):
        """
        Display details of the department.
        """
        super().display_details()
        print(f"Department Name: {self._department_name}")
        print(f"Head of Department: {self._head_of_department}")
        print("Courses Offered:")
        for course in self._courses_offered:
            print(f" - {course}")


if __name__ == "__main__":
    university = University("Kathmandu University", "Dhulikhel")
    department1 = Department("Kathmandu University",
                             "Block 9", "Computer Science", "Bal Krishna Bal")
    department2 = Department("Kathmandu University", "Block 8",
                             "Electrical Engineering", "Prof. Hari Shyam Hari")

    department1.add_course("Python Programming")
    department1.add_course("Data Structures")
    department2.add_course("Digital Electronics")
    department2.add_course("Power Systems")

    university.add_department(department1)
    university.add_department(department2)

    university.display_details()
    print("\n")
    department1.display_details()
    print("\n")
    department2.display_details()


"""
Output
University Name: Kathmandu University
Location: Dhulikhel
Departments:
 - Computer Science Department
 - Electrical Engineering Department


University Name: Kathmandu University
Location: Block 9
Departments:
Department Name: Computer Science
Head of Department: Bal Krishna Bal
Courses Offered:
 - Python Programming
 - Data Structures


University Name: Kathmandu University
Location: Block 8
Departments:
Department Name: Electrical Engineering
Head of Department: Prof. Hari Shyam Hari
Courses Offered:
 - Digital Electronics
 - Power Systems
"""
