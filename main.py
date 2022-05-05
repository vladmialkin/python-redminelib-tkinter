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
    def __init__(self):
        super().__init__()

        self.redmine = Redmine()

        self.label_projects = tk.Label(self, width=20, text="Проекты")
        self.label_projects.place(x=5, y=5)

        self.list_projects = tk.StringVar()
        self.combobox_projects = ttk.Combobox(self, textvariable=self.list_projects, state="readonly")
        self.combobox_projects.place(x=5, y=35)
        self.set_list_projects()

        self.tree = ttk.Treeview(self, height=20, show="headings", columns= colums_list)
        self.set_tree_colums()
        self.tree.place(x=5, y=400)

        self.scroll = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scroll.set)

        self.but = tk.Button(self, width=20, command=self.get_tree_issue)
        self.but.place(x=5,y=200)

    def set_list_projects(self):
        """ функция заполняет список проектов """
        self.combobox_projects['values'] = [project for project in self.redmine.get_projects()]

    def get_project_combobox(self):
        for project in self.redmine.get_projects():
            if str(project) == self.combobox_projects.get():
                return project

    def get_tree_issue(self):
        """ функция заполняет список задач """
        self.clear_tree()
        for issue in self.get_project_combobox().issues:
            self.tree.insert("", tk.END, values= [issue.id, issue.project, issue.tracker])

    def clear_tree(self):
        """ удаляет все данные из таблицы при изменении работника """
        for record in self.tree.get_children():
            self.tree.delete(record)

    def set_tree_colums(self):
        """ функция заполняет названия колонок таблицы """
        count = 1
        for column in colums_list:
            self.tree.heading(f"#{count}", text=column, anchor=tk.CENTER)
            self.tree.column(f"#{count}", stretch=tk.YES, width=120)
            count += 1

if __name__ == '__main__':

    window = Interface()
    window.geometry("1024x840")
    window.title("Запрос Redmine")
    window.mainloop()



