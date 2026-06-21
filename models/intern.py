class Intern:

    def __init__(
        self,
        intern_id,
        name,
        email,
        domain,
        duration
    ):

        self.__intern_id = intern_id
        self.__name = name
        self.__email = email
        self.__domain = domain
        self.__duration = duration

    # Getters

    def get_intern_id(self):
        return self.__intern_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_domain(self):
        return self.__domain

    def get_duration(self):
        return self.__duration

    # Setters

    def set_intern_id(self, intern_id):
        self.__intern_id = intern_id

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_domain(self, domain):
        self.__domain = domain

    def set_duration(self, duration):
        self.__duration = duration

    def __str__(self):

        return f"""
Intern ID : {self.__intern_id}
Name      : {self.__name}
Email     : {self.__email}
Domain    : {self.__domain}
Duration  : {self.__duration} Months
"""