class candidate:
    def __init__(self, dict_values):
        self.name = dict_values['name']
        self.date = dict_values['date']
        self.course = dict_values['course_interest']
        self.financial = dict_values['financial_support_self']
        self.geo = dict_values['geo_flex']
        self.primary_key = dict_values['primary_key']
        self.result = dict_values['result']
        self.development = dict_values['self_development']
        self.strengths = dict_values.get('strengths',[])
        self.weakness = dict_values.get('weaknesses',[])
        self.score = dict_values.get('tech_self_score',{})
        self.student_info = []
        self.psychometrics = ""
        self.presentation = ""
        self.sparta_location = ""
        self.trainer = ""
        self.academy_perfomance = []

    def set_academy_performance(self, value):
        self.academy_perfomance = value

    def get_academy_performace(self):
        return self.academy_perfomance

    def set_trainer(self, value):
        self.trainer = value

    def get_trainer(self):
        return self.trainer
    def get_firstName(self):
        return self.get_name().split(" ")[0]

    def get_lastName(self):
        return self.get_name().split(" ")[1]
    def get_location(self):
        return self.sparta_location

    def set_location(self, location_value):
        self.sparta_location = location_value

    def set_psychometrics(self, s_value):
        self.psychometrics = s_value

    def set_presentation(self, p_value):
        self.presentation = p_value

    def get_psychometrics(self):
        return self.psychometrics

    def get_presentation(self):
        return self.presentation

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_day(self):
        return self.date.split("/")[0]

    def get_month(self):
        return self.date.split("/")[1]

    def get_year(self):
        return self.date.split("/")[2]

    def get_financial(self):
        return self.financial

    def get_score(self):
        return self.score

    def get_geo(self):
        return self.geo

    def get_primary_key(self):
        return self.primary_key

    def get_description(self):
        string_s = ""
        string_w = ""
        for strenght in self.strengths:
            string_s += strenght
        for weakness in self.weakness:
            string_w += weakness
        return f"Strength - {string_s} , Weakness - {string_w}"

    def add_student_info(self, list_info):
        self.student_info = list_info

    def get_student_info(self):
        return self.student_info

    def get_course(self):
        return self.course

    def get_result(self):
        return self.result
