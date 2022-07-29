import pyodbc
import warnings

warnings.filterwarnings("ignore")  # only for this file just to ignore deprecated


class DatabaseEdit:

    def __init__(self, server, database, username, password):
        # CONNECTION SETUP
        self.server = server
        self.database = database
        self.username = username
        self.password = password

        self.docker_final_project = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + self.server + ";DATABASE=" + self.database + ";\n"
                                                                                                            "UID=" + self.username + ";PWD=" + self.password + ";TrustServerCertificate=yes;")
        self.docker_final_project.autocommit = True  # autocommit to actually commit changes to database

        self.cursor = self.docker_final_project.cursor()

    def add_courses(self, Course_name):
        self.cursor.execute(f"IF NOT EXISTS (SELECT * FROM courses WHERE Course_Name = '{Course_name}')BEGIN "
                            f" INSERT INTO courses (Course_name) VALUES('{Course_name}')"
                            f"END")

    def add_sparta_scores(self, Student_ID, Sparta_Day_ID, psy, presentation):
        self.cursor.execute(f"IF NOT EXISTS (SELECT * FROM sparta_scores WHERE Student_id = {Student_ID} and Sparta_day_id = {Sparta_Day_ID})BEGIN "
                            f" INSERT INTO sparta_scores (Student_id,Sparta_day_id,Psychometric,Presentation) VALUES({Student_ID},{Sparta_Day_ID},'{psy}','{presentation}')"
                            f"END")

    def add_universities(self, University):
        self.cursor.execute(f"IF NOT EXISTS (SELECT * FROM universities WHERE University = '{University}')BEGIN"
                            f" INSERT INTO universities (University) VALUES('{University}')"
                            f"END")

    def add_degrees(self, Degree):
        self.cursor.execute(f"IF NOT EXISTS (SELECT * FROM degrees WHERE Degree = '{Degree}')BEGIN"
                            f" INSERT INTO degrees (Degree) VALUES('{Degree}')"
                            f"END")

    def add_recruiters(self, Recruiter_name):
        self.cursor.execute(f"IF NOT EXISTS (SELECT * FROM recruiters WHERE Recruiter_name = '{Recruiter_name}')BEGIN "
                            f" INSERT INTO recruiters (Recruiter_name) VALUES('{Recruiter_name}')"
                            f"END")

    def add_locations(self, Locations):
        self.cursor.execute(f"IF NOT EXISTS (SELECT * FROM locations WHERE Locations = '{Locations}')BEGIN"
                            f" INSERT INTO locations (Locations) VALUES('{Locations}');"
                            f"END")

    def add_trainers(self, Trainer_name):
        self.cursor.execute(f"IF NOT EXISTS (SELECT * FROM trainers WHERE Trainer_name = '{Trainer_name}')BEGIN"
                            f" INSERT INTO trainers (Trainer_name) VALUES('{Trainer_name}')"
                            f"END")

    def add_students(self, Student_id, First_name, Last_name, Gender, Recruiter_id, DOB, Geo_flex, Financial_support):
        self.cursor.execute(
            f"IF NOT EXISTS (SELECT * FROM students WHERE Student_ID = {Student_id})BEGIN"
            f" INSERT INTO students(Student_ID,First_name,Last_name,Gender,Recruiter_ID,DOB,Geo_flex,Financial_support)"
            f" VALUES({Student_id}, '{First_name}', '{Last_name}', '{Gender}', {Recruiter_id},'{DOB}', '{Geo_flex}', '{Financial_support}')"
            f"END")

    def get_key(self, column_name, table_name, column_query, value):
        query = self.cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE {column_query} = '{value}' ")
        return query.fetchone()

    def add_student_scores(self, Student_id, week, Analytical, Independent, Determined, Professional, Studious,
                           Imaginative):
        self.cursor.execute(
            f"INSERT INTO student_scores VALUES({Student_id},{week}, {Analytical}, {Independent}, {Determined}, {Professional}, {Studious}, {Imaginative})")

    def add_contact_details(self, Student_id, Email, Phone, Addresses, Post_Code):
        self.cursor.execute(
            f"INSERT INTO contact_details VALUES({Student_id}, '{Email}', '{Phone}', '{Addresses}', '{Post_Code}')")

    def add_sparta_days(self, Location_id, Dates):
        self.cursor.execute(f"IF NOT EXISTS (SELECT * FROM sparta_days WHERE Dates = '{Dates}')BEGIN"
                            f" INSERT INTO sparta_days (Location_id,Dates) VALUES({Location_id}, '{Dates}')"
                            f"END")

    def add_recruiters_invitation(self, Recruiter_id, Student_id, Invite_date):
        self.cursor.execute(f"IF NOT EXISTS (SELECT * FROM recruiter_invitation WHERE Recruiter_id = {Recruiter_id} and Student_id = {Student_id})BEGIN"
                            f" INSERT INTO recruiter_invitation VALUES({Recruiter_id}, {Student_id}, '{Invite_date}')"
                            f"END")

    def add_tech_skills(self, Student_id, Programming_language, Results):
        self.cursor.execute(f"INSERT INTO tech_skills VALUES({Student_id}, '{Programming_language}', '{Results}')")

    def add_student_courses(self, Descriptions, Trainer_id, Degree_id, Course_id, Recruiter_id, Sparta_day_id,
                            Location_id, Student_id, Course_interests, Results, University_id):
        self.cursor.execute(
            f"INSERT INTO student_courses "
            f"(Descriptions,Trainer_id,Degree_id,Course_id,Recruiter_id,Sparta_day_id,Location_id,Student_id,Course_interests,Results,University_id) "
            f"VALUES ( '{Descriptions}', {Trainer_id} ,{Degree_id}, {Course_id}, {Recruiter_id}, {Sparta_day_id},{Location_id},{Student_id},'{Course_interests}','{Results}', {University_id});")
