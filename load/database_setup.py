import pyodbc
import warnings

warnings.filterwarnings("ignore")  # only for this file just to ignore deprecated


class DatabaseSetup:

    def __init__(self):
        # CONNECTION SETUP
        self.server = 'localhost, 1433'
        self.database = 'final_project'
        self.username = 'SA'
        self.password = 'Porto@12'

        self.docker_final_project = pyodbc.connect(
            "DRIVER={ODBC Driver 18 for SQL Server};SERVER=" + self.server + ";DATABASE=" + self.database + ";\n"
                                                                                                            "UID=" + self.username + ";PWD=" + self.password + ";TrustServerCertificate=yes;")
        self.docker_final_project.autocommit = True  # autocommit to actually commit changes to database

        self.cursor = self.docker_final_project.cursor()

        # INITIATING METHODS
        self.create_courses()
        self.create_universities()
        self.create_degrees()
        self.create_recruiters()
        self.create_locations()
        self.create_trainers()
        self.create_students()
        self.create_student_scores()
        self.create_contact_details()
        self.create_sparta_days()
        self.create_recruiters_invitation()
        self.create_tech_skills()
        self.create_student_courses()

    # METHODS
    def create_recruiters(self):
        self.cursor.execute("CREATE TABLE recruiters ("
                            "Recruiter_id INT NOT NULL, "
                            "Recruiter_name VARCHAR(255), "
                            "PRIMARY KEY (Recruiter_id))")

    def create_recruiters_invitation(self):
        self.cursor.execute("CREATE TABLE recruiter_invitation ("
                            "Recruiter_id INT NOT NULL, "
                            "Student_id INT NOT NULL, "
                            "Invite_date DATE, "
                            "PRIMARY KEY (Recruiter_id, Student_id),"
                            "FOREIGN KEY (recruiter_id) REFERENCES recruiters(Recruiter_id),"
                            "FOREIGN KEY (Student_id) REFERENCES students(Student_id))")

    def create_students(self):
        self.cursor.execute("CREATE TABLE students ("
                            "Student_id INT NOT NULL, "
                            "First_name VARCHAR(255), "
                            "Last_name VARCHAR(255), "
                            "Gender VARCHAR(20), "
                            "Recruiter_id INT, "
                            "DOB DATE, "
                            "Geo_flex BIT, "
                            "Financial_support BIT PRIMARY KEY (Student_id), "
                            "FOREIGN KEY (recruiter_id) REFERENCES recruiters(Recruiter_id))")

    def create_contact_details(self):
        self.cursor.execute("CREATE TABLE contact_details ("
                            "Student_id INT NOT NULL, "
                            "Email VARCHAR(255), "
                            "Phone CHAR(11), "
                            "Addresses VARCHAR(255), "
                            "Post_Code VARCHAR(255), "
                            "FOREIGN KEY (Student_id) REFERENCES students(Student_id))")

    def create_tech_skills(self):
        self.cursor.execute("CREATE TABLE tech_skills ("
                            "Student_id INT NOT NULL, "
                            "Programming_language VARCHAR(255), "
                            "Results INT, "
                            "FOREIGN KEY (Student_id) REFERENCES students(Student_id))")

    def create_student_scores(self):
        self.cursor.execute("CREATE TABLE student_scores ("
                            "Student_id INT NOT NULL, "
                            "Analytical INT, "
                            "Independent INT, "
                            "Determined INT, "
                            "Professional INT, "
                            "Studious INT, "
                            "Imaginative INT, "
                            "FOREIGN KEY (Student_id) REFERENCES students(Student_id))")

    def create_degrees(self):
        self.cursor.execute("CREATE TABLE degrees ("
                            "Degree_id INT NOT NULL, "
                            "Degree VARCHAR(255), "
                            "PRIMARY KEY (Degree_id))")

    def create_locations(self):
        self.cursor.execute("CREATE TABLE locations ("
                            "Location_id INT NOT NULL, "
                            "Locations VARCHAR(255), "
                            "PRIMARY KEY (Location_id))")

    def create_courses(self):
        self.cursor.execute("CREATE TABLE courses ("
                            "Course_id INT NOT NULL, "
                            "Course_name VARCHAR(255), "
                            "PRIMARY KEY (Course_id))")

    def create_trainers(self):
        self.cursor.execute("CREATE TABLE trainers ("
                            "Trainer_id INT NOT NULL, "
                            "Trainer_name VARCHAR(255), "
                            "PRIMARY KEY (Trainer_id))")

    def create_universities(self):
        self.cursor.execute("CREATE TABLE universities ("
                            "University_id INT NOT NULL, "
                            "University VARCHAR(255), "
                            "PRIMARY KEY (University_id))")

    def create_sparta_days(self):
        self.cursor.execute("CREATE TABLE sparta_days ("
                            "Sparta_day_id INT NOT NULL, "
                            "Location_id INT NOT NULL, "
                            "Dates DATE,"
                            "PRIMARY KEY (Sparta_day_id),"
                            "FOREIGN KEY (Location_id) REFERENCES locations(Location_id))")

    def create_sparta_scores(self):
        self.cursor.execute("CREATE TABLE sparta_scores ("
                            "Student_id INT NOT NULL, "
                            "Sparta_day_id INT NOT NULL, "
                            "Psychometric DECIMAL,"
                            "Presentation DECIMAL,"
                            "PRIMARY KEY (Student_id, Sparta_day_id),"
                            "FOREIGN KEY (Student_id) REFERENCES students(Student_id),"
                            "FOREIGN KEY (Sparta_day_id) REFERENCES sparta_days(Sparta_day_id))")

    def create_student_courses(self):
        self.cursor.execute("CREATE TABLE student_courses ("
                            "Descriptions VARCHAR(255),"
                            "Trainer_id INT NOT NULL, "
                            "Degree_id INT NOT NULL, "
                            "Course_id INT NOT NULL, "
                            "Recruiter_id INT NOT NULL, "
                            "Sparta_day_id INT NOT NULL, "
                            "Location_id INT NOT NULL, "
                            "Student_id INT NOT NULL, "
                            "Course_interests VARCHAR(255),"
                            "Results BIT,"
                            "University_id INT NOT NULL, "
                            "FOREIGN KEY (Trainer_id) REFERENCES trainers(Trainer_id),"
                            "FOREIGN KEY (Degree_id) REFERENCES degrees(Degree_id),"
                            "FOREIGN KEY (Course_id) REFERENCES courses(Course_id),"
                            "FOREIGN KEY (Recruiter_id) REFERENCES recruiters(Recruiter_id),"
                            "FOREIGN KEY (Sparta_day_id) REFERENCES sparta_days(Sparta_day_id),"
                            "FOREIGN KEY (Location_id) REFERENCES locations(Location_id),"
                            "FOREIGN KEY (Student_id) REFERENCES students(Student_id),"
                            "FOREIGN KEY (University_id) REFERENCES universities(University_id))")


# Calling class and variable
project = DatabaseSetup()
project
