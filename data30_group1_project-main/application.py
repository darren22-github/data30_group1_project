import pprint
import pandas as pd
from applicant import candidate
from load.database_setup import DatabaseSetup
from load.database_insert import DatabaseEdit
from Extract import Check_for_data as e
from Transform import transform_abdul as applicant_transform
from Transform import transform_weekly_csv as academy_transform

months_ab = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

applicants_files = {}
sparta_days_files = {}
courses_files = {}
candidates = []
successful_candidates = []
unsuccessful_candidates = []


def extract_clean_applicant_files():
    list_of_applicants = e.list_applicants()
    for applicant_filename in list_of_applicants:
        file_name = applicant_filename.split("/")[1]
        temp = e.extract_applicant(applicant_filename)
        applications_data = temp.read().decode('UTF-8')
        application_df = applicant_transform.read_csv(applications_data)
        applicants_files[file_name] = application_df


def extract_clean_academy_files():
    list_of_academy = e.list_courses()

    for courses in list_of_academy:
        courses_period_name = courses.split("/")[1]
        academy_df = e.extract_course(courses)
        clean_df = academy_df.fillna(0)
        new_academy_df = academy_transform.transformed_dataframe(clean_df)
        courses_files[courses_period_name] = new_academy_df


def talents_process():
    talents = e.sample_talents()
    for c in talents:
        canditate_info = e.extract_talent(c)
        canditate_info["primary_key"] = c.split("/")[1][:5]
        t_candidate = candidate(canditate_info)
        applicants_filename = f"{months_ab[int(t_candidate.get_month()) - 1]}{t_candidate.get_year()}Applicants.csv"
        get_applicants_info(applicants_filename, t_candidate)
        get_test_results(t_candidate)
        list_of_files = get_academy_files(t_candidate)
        search_candidate(list_of_files, t_candidate)
        candidates.append(t_candidate)


def get_applicants_info(filename, candidate_object):
    name = candidate_object.get_name()
    df = applicants_files[filename]
    details_list = df.query("name == @name").values.tolist()[0][1:]
    candidate_object.add_student_info(details_list)


def get_test_results(candidate_obj):
    c_name = candidate_obj.get_name().upper()
    test_info = sparta_days_files[c_name]
    candidate_obj.set_psychometrics(test_info["Psychometrics"])
    candidate_obj.set_presentation(test_info["Presentation"])
    candidate_obj.set_location(test_info["Location"])


def get_academy_details():
    list_of_academy = e.list_courses()
    new_list = []
    for i in list_of_academy:
        new_list.append(i.split("/")[1])


def get_academy_files(candidate_object):
    course_interest = candidate_object.get_course()
    str_a = f"{candidate_object.get_year()}-{candidate_object.get_month()}"
    try:
        res = [string for string in courses_files.keys() if course_interest in string]
        ss = [string for string in res if str_a in string]
        return ss
    except:
        print("Candidate didn't enroll")


def search_candidate(list_of_files, candidate_info):
    name = candidate_info.get_name()
    for file_academy in list_of_files:
        df = courses_files[file_academy]
        try:
            details_list = df.query("name == @name").values.tolist()
            candidate_info.set_trainer(details_list[0][1])
            print(f"{name} Made it")
            successful_candidates.append(candidate_info)
            add_to_performance(details_list, candidate_info)
        except:
            unsuccessful_candidates.append(candidate_info)
            return "Didn't enroll into the Academy"


def add_to_performance(list_of_performance, candidate_info):
    overall_performace = []
    for week in list_of_performance:
        overall_performace.append(week[2:])

    candidate_info.set_academy_performance(overall_performace)


def get_sparta_day_files():
    list_of_txt = e.list_spartaday()
    for sparta_day in list_of_txt:
        obj = e.extract_sparta_day(sparta_day)
        r = obj.decode().replace("\n", "")
        r = r.split("\r")
        sparta_location = r[1]
        data = r[3:]
        for i in range(len(data)):
            if len(data[i]) > 1:
                s = data[i].replace("-", ",")
                s_ = s.split(",")
                psy, pre = split_test(s_[1], s_[2])
                sparta_days_files[s_[0].rstrip()] = {"Psychometrics": psy, "Presentation": pre,
                                                     'Location': sparta_location}


def split_test(string1, string2):
    ps = ""
    pr = ""
    try:
        s = string1.split(":")
        t = string2.split(":")
        ps = s[1].replace(" ", "")
        pr = t[1].replace(" ", "")
    except:
        ps = "0/100"
        pr = "0/32"

    return ps, pr


def set_db():
    DatabaseSetup("localhost", "my_db", "sa", "Passw0rd2018")


def load_to_db():
    db = get_db()

    for candidate in successful_candidates:
        load_data(db, candidate)
        for i in range(10):
            db.add_student_scores(int(candidate.get_primary_key()), candidate.get_academy_performace()[i][0],
                                  candidate.get_academy_performace()[i][1], candidate.get_academy_performace()[i][2],
                                  candidate.get_academy_performace()[i][3], candidate.get_academy_performace()[i][4],
                                  candidate.get_academy_performace()[i][5], candidate.get_academy_performace()[i][6])

    for candidate in unsuccessful_candidates:
        load_data(db, candidate)


def load_data(db, candidate_obj):
    db.add_courses(candidate_obj.get_course())
    db.add_recruiters(candidate_obj.get_student_info()[11])
    db.add_locations(candidate_obj.get_location())
    db.add_degrees(candidate_obj.get_student_info()[8])
    db.add_trainers(candidate_obj.get_trainer())
    db.add_universities(candidate_obj.get_student_info()[7])
    key_location = db.get_key("Location_id", "locations", "Locations", candidate_obj.get_location())[0]
    db.add_sparta_days(int(key_location), candidate_obj.get_date())

    print(candidate_obj.get_student_info()[1])
    key_course = db.get_key("Course_id", "courses", "course_name", candidate_obj.get_course())[0]
    key_recruiter = db.get_key("Recruiter_ID", "recruiters", "Recruiter_name", candidate_obj.get_student_info()[11])[0]
    key_sparta_day = db.get_key("Sparta_day_id", "sparta_days", "Dates", candidate_obj.get_date())[0]
    key_trainer = db.get_key("Trainer_id", "trainers", "Trainer_name", candidate_obj.get_trainer())[0]
    key_degree = db.get_key("Degree_id", "degrees", "Degree", candidate_obj.get_student_info()[8])[0]
    key_uni = db.get_key("University_id", "universities", "University", candidate_obj.get_student_info()[7])[0]

    db.add_students(int(candidate_obj.get_primary_key()), candidate_obj.get_firstName(), candidate_obj.get_lastName(),
                    candidate_obj.get_student_info()[0], key_recruiter, str(candidate_obj.get_student_info()[1]),
                    candidate_obj.get_geo(), candidate_obj.get_financial())
    db.add_contact_details(int(candidate_obj.get_primary_key()), candidate_obj.get_student_info()[2],
                           candidate_obj.get_student_info()[6], candidate_obj.get_student_info()[4],
                           candidate_obj.get_student_info()[5])

    invited_date = candidate_obj.get_student_info()[9] + candidate_obj.get_student_info()[10]
    db.add_recruiters_invitation(int(key_recruiter), candidate_obj.get_primary_key(), str(invited_date))
    db.add_sparta_scores(int(candidate_obj.get_primary_key()), int(key_sparta_day), candidate_obj.get_psychometrics(),
                         candidate_obj.get_presentation())
    for tech_key in candidate_obj.get_score():
        db.add_tech_skills(int(candidate_obj.get_primary_key()), tech_key, candidate_obj.get_score()[tech_key])

    db.add_student_courses(candidate_obj.get_description(), int(key_trainer), int(key_degree), int(key_course),
                           int(key_recruiter), int(key_sparta_day), int(key_location),
                           int(candidate_obj.get_primary_key()), str(candidate_obj.get_course()),
                           str(candidate_obj.get_result()),
                           int(key_uni))

    db.add_courses(candidate_obj.get_course())
    db.add_recruiters(candidate_obj.get_student_info()[11])
    db.add_locations(candidate_obj.get_location())
    db.add_degrees(candidate_obj.get_student_info()[8])
    db.add_trainers(candidate_obj.get_trainer())
    db.add_universities(candidate_obj.get_student_info()[7])
    key_location = db.get_key("Location_id", "locations", "Locations", candidate_obj.get_location())[0]
    db.add_sparta_days(int(key_location), candidate_obj.get_date())

    print(candidate_obj.get_student_info()[1])
    key_course = db.get_key("Course_id", "courses", "course_name", candidate_obj.get_course())[0]
    key_recruiter = db.get_key("Recruiter_ID", "recruiters", "Recruiter_name", candidate_obj.get_student_info()[11])[0]
    key_sparta_day = db.get_key("Sparta_day_id", "sparta_days", "Dates", candidate_obj.get_date())[0]
    key_trainer = db.get_key("Trainer_id", "trainers", "Trainer_name", candidate_obj.get_trainer())[0]
    key_degree = db.get_key("Degree_id", "degrees", "Degree", candidate_obj.get_student_info()[8])[0]
    key_uni = db.get_key("University_id", "universities", "University", candidate_obj.get_student_info()[7])[0]

    db.add_students(int(candidate_obj.get_primary_key()), candidate_obj.get_firstName(), candidate_obj.get_lastName(),
                    candidate_obj.get_student_info()[0], key_recruiter, str(candidate_obj.get_student_info()[1]),
                    candidate_obj.get_geo(), candidate_obj.get_financial())
    db.add_contact_details(int(candidate_obj.get_primary_key()), candidate_obj.get_student_info()[2],
                           candidate_obj.get_student_info()[6], candidate_obj.get_student_info()[4],
                           candidate_obj.get_student_info()[5])

    invited_date = candidate_obj.get_student_info()[9] + candidate_obj.get_student_info()[10]
    db.add_recruiters_invitation(int(key_recruiter), candidate_obj.get_primary_key(), str(invited_date))
    db.add_sparta_scores(int(candidate_obj.get_primary_key()), int(key_sparta_day), candidate_obj.get_psychometrics(),
                         candidate_obj.get_presentation())
    for tech_key in candidate_obj.get_score():
        db.add_tech_skills(int(candidate_obj.get_primary_key()), tech_key, candidate_obj.get_score()[tech_key])

    db.add_student_courses(candidate_obj.get_description(), int(key_trainer), int(key_degree), int(key_course),
                           int(key_recruiter), int(key_sparta_day), int(key_location),
                           int(candidate_obj.get_primary_key()), str(candidate_obj.get_course()),
                           str(candidate_obj.get_result()),
                           int(key_uni))


def get_db():
    return DatabaseEdit("localhost", "my_db", "sa", "Passw0rd2018")


def run():
    set_db()
    extract_clean_applicant_files()
    get_sparta_day_files()
    extract_clean_academy_files()
    talents_process()
    load_to_db()

run()