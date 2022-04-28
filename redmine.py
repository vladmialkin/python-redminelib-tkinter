import redminelib as rdm
from local_settings import redmine_site
from local_settings import redmine_key

class Redmine:
    """ класс взаимодействия с Redmine через API"""
    def __init__(self):
        self.redmine = rdm.Redmine(redmine_site, key=redmine_key)

    def connect(self):
        """функция подключается к redmine"""
        try:
            self.redmine
        except BaseException as e:
            print(f"Ошибка подключения: {e}")


    def get_projects(self)-> list:
        """функция полючает список всех проектов"""
        try:
            return self.redmine.project.all()
        except Exception as e:
            print(f"Ошибка проектов: {e}")

    def get_data_projects(self) -> list:
        """функция получает данные проектов"""
        try:
            return [list(project) for project in self.get_projects()]
        except Exception as e:
            print(f"Ошибка: {e}")