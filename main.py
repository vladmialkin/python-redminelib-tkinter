from redmine import Redmine
import tkinter as tk
from tkinter import ttk

colums_list = [
        'id',
        'Проект',
        'Трекер',
        'Статус',
        'Приоритет',
        'Тема',
        'Назначена',
        'Обновлено'
]

class Interface(tk.Tk):
    """ класс интерфейса """
    __instance = None
    def __new__(cls):
        """ singleton """
        if cls.__instance == None:
            cls.__instance = super(Interface, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        super().__init__()

        self.redmine = Redmine()

        self.label_projects = tk.Label(self, width=20, text="Проект")
        self.label_projects.place(x=5, y=5)

        self.list_projects = tk.StringVar()
        self.combobox_projects = ttk.Combobox(self, textvariable=self.list_projects, state="readonly")
        self.combobox_projects.place(x=5, y=35)
        self.set_list_projects()

        self.label_authors = tk.Label(self, width=20, text="Автор")
        self.label_authors.place(x=150, y=5)

        self.list_authors = tk.StringVar()
        self.combobox_authors = ttk.Combobox(self, textvariable=self.list_authors, state="readonly")
        self.combobox_authors.place(x=150, y=35)

        self.tree = ttk.Treeview(self, height=20, show="headings", columns= colums_list)
        self.set_tree_colums()
        self.tree.place(x=5, y=400)

        self.scroll = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scroll.set)

        self.button_tree = tk.Button(self,text='Получить', width=20, command=self.get_tree_issue)
        self.button_tree.place(x=5,y=370)

        self.button_tree = tk.Button(self,text='Получить', width=20, command=self.set_list_authors)
        self.button_tree.place(x=200,y=370)

    def set_list_projects(self):
        """ функция заполняет список проектов """
        self.combobox_projects['values'] = [project for project in self.redmine.get_projects()]

    def get_project_combobox(self):
        """ функция ищет выбранный проект """
        for project in self.redmine.get_projects():
            if isinstance(project, object):
                if str(project) == self.combobox_projects.get():
                    return project

    def get_tree_issue(self):
        """ функция заполняет список задач в таблицу"""
        self.clear_tree()
        for issue in self.get_project_combobox().issues:
            if isinstance(issue, object):
                self.tree.insert("", tk.END, values=[issue.id, issue.project, issue.tracker, issue.status, issue.priority,
                                                  issue, issue.attachments, issue.updated_on])
    def clear_tree(self):
        """ удаляет все данные из таблицы при изменении работника """
        for record in self.tree.get_children():
            self.tree.delete(record)

    def set_tree_colums(self):
        """ функция заполняет названия колонок таблицы """
        count = 1
        for column in colums_list:
            self.tree.heading(f"#{count}", text=column, anchor=tk.CENTER)
            self.tree.column(f"#{count}", stretch=tk.YES, width=130)
            count += 1

    def set_list_authors(self):
        """ функция заполняет список авторов проектов """
        project = self.get_project_combobox()
        #self.combobox_authors["values"] = [author for author in self.redmine.get_author()

if __name__ == '__main__':

    window = Interface()
    window.geometry("1080x840")
    window.title("Запрос Redmine")
    window.mainloop()



