from redmine import connect
from redmine import get_projects
from redmine import get_data_projects

if __name__ == '__main__':
    connect()
    get_data_projects(get_projects())
   # print( get_data_projects(get_projects()))

