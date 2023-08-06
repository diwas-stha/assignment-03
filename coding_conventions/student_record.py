import json


class StudentManager:
    """
    A class to manage student records.

    Attributes:
    ----------
        file_path (str): The path to the JSON file to store the records.
        records (list): A list of dictionaries representing student records.

    """

    def __init__(self, file_path):
        """
        Initialize the StudentManager class.

        Parameters:
        ----------
            file_path (str): The path to the JSON file to store the records.

        """
        self.file_path = file_path
        self.records = self.load_records()

    def load_records(self):
        """
        Load student records from the JSON file.

        Returns:
        -------
            list: A list of dictionaries representing student records.

        """
        try:
            with open(self.file_path, "r") as file:
                data = file.read()
                if data:
                    return json.loads(data)
                else:
                    return []
        except FileNotFoundError:
            return []

    def save_records(self):
        """
        Save student records to the JSON file.

        """
        with open(self.file_path, "w") as file:
            json.dump(self.records, file)

    def add_student(self, student_id, name, age, grade):
        """
        Add a new student record to the records.

        Parameters:
        ----------
            student_id (int): The student ID.
            name (str): The student's name.
            age (int): The student's age.
            grade (str): The student's grade.

        """
        if not isinstance(student_id, int) or not isinstance(name, str) or not isinstance(age, int) or not isinstance(grade, str):
            raise TypeError(
                "Invalid data types. Please provide valid integer for student_id and age, and string for name and grade.")

        for student in self.records:
            if student_id == student["student_id"] or name == student["name"]:
                print("Student with the same ID or name already exists. Skipping")
                return
        student = {
            "student_id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
        }
        self.records.append(student)
        self.save_records()

    def search_student(self, keyword):
        """
        Search for a student by student_id or name.

        Parameters:
        ----------
            keyword (str or int): The student ID or name to search for.

        Returns:
        -------
            dict or None: A dictionary containing the student's information if found, None otherwise.

        """
        for student in self.records:
            if keyword in (str(student["student_id"]), student["name"]):
                return {
                    "age": student["age"],
                    "grade": student["grade"],
                }
        return None

    def update_student_info(self, keyword, attribute, value):
        """
        Update a student's information by using student_id or name (age or grade).

        Parameters:
        ----------
            keyword (str or int): The student ID or name to search for.
            attribute (str): The attribute to update ("age" or "grade").
            value (str or int): The new value for the attribute.

        Returns:
        -------
            bool: True if the update is successful, False if the student is not found.

        """
        if not isinstance(keyword, (int, str)):
            raise TypeError(
                "Invalid data type for keyword. Please provide a valid integer for student_id or a string for name.")

        if attribute not in ("age", "grade"):
            raise ValueError(
                "Invalid attribute. Please provide either 'age' or 'grade' as the attribute.")

        if attribute == "age" and not isinstance(value, int):
            raise TypeError(
                "Invalid data type for age. Please provide a valid integer.")

        if attribute == "grade" and not isinstance(value, str):
            raise TypeError(
                "Invalid data type for grade. Please provide a valid string.")

        for student in self.records:
            if str(keyword) in (str(student["student_id"]), student["name"]):
                student[attribute] = value
                self.save_records()
                return True
        return False


# Example usage:
if __name__ == "__main__":
    manager = StudentManager("student_records.json")

    manager.add_student(101, "John Doe", 20, "A")
    manager.add_student(102, "Jane Smith", 22, "B")
    manager.add_student(103, "Alice Johnson", 21, "B")
    manager.add_student(104, "Bob Smith", 19, "A")
    manager.add_student(105, "Eva Martinez", 20, "B+")
    manager.add_student(106, "Michael Brown", 22, "A-")

    search_result = manager.search_student("John Doe")
    if search_result:
        print(f"Age: {search_result['age']}, Grade: {search_result['grade']}")

    else:
        print("Student not found")

    manager.update_student_info(105, "age", 25)
    manager.update_student_info(101, "grade", "C")
