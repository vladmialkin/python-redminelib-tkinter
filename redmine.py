import redminelib as rdm
from local_settings import redmine_site
from local_settings import redmine_key


def connect():
    """функция подключается к redmine"""
    try:
        rdm.Redmine(redmine_site, key=redmine_key)
    except BaseException as e:
        print(f"Ошибка подключения: {e}")


def get_projects()-> list:
    """функция полючает список всех проектов"""
    try:
        redmine = rdm.Redmine(redmine_site, key=redmine_key)
        projects = redmine.project.all()
        return projects
    except Exception as e:
        print(f"Ошибка проектов: {e}")


def get_data_projects(projects: list):
    """функция получает данные проектов"""
    try:
        return [list(project) for project in projects]
    except Exception as e:
        print(f"Ошибка: {e}")