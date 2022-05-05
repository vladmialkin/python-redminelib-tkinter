import redminelib as rdm
from local_settings import redmine_site
from local_settings import redmine_key

class Redmine:
    """ класс взаимодействия с Redmine через API"""
    def __init__(self):
        self.redmine = rdm.Redmine(redmine_site, key=redmine_key)
        self.connect()

    def connect(self):
        """функция подключается к redmine"""
        try:
            self.redmine
        except BaseException as e:
            print(f"Ошибка подключения: {e}")


    def get_projects(self):
        """функция полючает список всех проектов"""
        return self.redmine.project.all()
