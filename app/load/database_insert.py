import pyodbc
import warnings

warnings.filterwarnings("ignore")  # only for this file just to ignore deprecated


class DatabaseSetup:

    def __init__(self):
        # CONNECTION SETUP
        self.server = 'server'
        self.database = 'database'
        self.username = 'username'
        self.password = 'password'

        self.docker_final_project = pyodbc.connect(
            "DRIVER={ODBC Driver 18 for SQL Server};SERVER=" + self.server + ";DATABASE=" + self.database + ";\n"
                                                                                                            "UID=" + self.username + ";PWD=" + self.password + ";TrustServerCertificate=yes;")
        self.docker_final_project.autocommit = True  # autocommit to actually commit changes to database

        self.cursor = self.docker_final_project.cursor()


    def add_courses(self, Course_id, Course_name):
        self.cursor.execute(f"INSERT INTO courses VALUES({Course_id}, '{Course_name}')")

    def add_universities(self, University_id, University):
        self.cursor.execute(f"INSERT INTO universities VALUES({University_id}, '{University}')")

    def add_degrees(self, Degree_id, Degree):
        self.cursor.execute(f"INSERT INTO degrees VALUES({Degree_id}, '{Degree}')")

    def add_recruiters(self, Recruiter_id, Recruiter_name):
        self.cursor.execute(f"INSERT INTO recruiters VALUES({Recruiter_id}, '{Recruiter_name}')")

    def add_locations(self, Location_id, Locations):
        self.cursor.execute(f"INSERT INTO locations (Location_id, Locations) VALUES({Location_id}, '{Locations}');")

    def add_trainers(self, Trainer_id, Trainer_name):
        self.cursor.execute(f"INSERT INTO trainers VALUES({Trainer_id}, '{Trainer_name}')")

    def add_students(self, Student_id, First_name, Last_name, Gender, Recruiter_id, DOB, Geo_flex, Financial_support):
        self.cursor.execute(f"INSERT INTO students VALUES({Student_id}, '{First_name}', '{Last_name}', '{Gender}', {Recruiter_id}, {DOB}, {Geo_flex}, {Financial_support})")

    def add_student_scores(self, Student_id, Analytical, Independent, Determined, Professional, Studious, Imaginative):
        self.cursor.execute(f"INSERT INTO student_scores VALUES({Student_id}, {Analytical}, {Independent}, {Determined}, {Professional}, {Studious}, {Imaginative})")

    def add_contact_details(self, Student_id, Email, Phone, Addresses, Post_Code):
        self.cursor.execute(f"INSERT INTO contact_details VALUES({Student_id}, '{Email}', '{Phone}', '{Addresses}', '{Post_Code}')")

    def add_sparta_days(self, Sparta_day_id, Location_id, Dates):
        self.cursor.execute(f"INSERT INTO sparta_days VALUES({Sparta_day_id}, {Location_id}, '{Dates}')")

    def add_recruiters_invitation(self, Recruiter_id, Student_id, Invite_date):
        self.cursor.execute(f"INSERT INTO recruiters_invitation VALUES({Recruiter_id}, {Student_id}, {Invite_date})")

    def add_tech_skills(self, Student_id, Programming_language, Results):
        self.cursor.execute(f"INSERT INTO tech_skills VALUES({Student_id}, {Programming_language, Results})")

    def add_student_courses(self, Descriptions, Trainer_id, Degree_id, Course_id, Recruiter_id, Sparta_day_id, Location_id, Student_id, Course_interests, Results, University_id):
        self.cursor.execute(f"INSERT INTO student_courses VALUES('{Descriptions}', {Trainer_id}, {Degree_id}, {Course_id}, {Recruiter_id}, {Sparta_day_id}, {Location_id}, {Student_id}, '{Course_interests}', {Results}, {University_id})")


database_data = DatabaseSetup()
