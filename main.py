from redmine import Redmine
import tkinter as tk
from tkinter import ttk

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

        self.tree = ttk.Treeview(self, height=20, show="headings", columns='ID')
        self.set_tree_colums()

        self.tree.place(x=5, y=400)

        self.scroll = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scroll.set)

    def set_list_projects(self):
        """ функция заполняет список проектов """
        self.combobox_projects['values'] = [project for project in self.redmine.get_projects()]

    def set_tree_colums(self):
        """ функция заполняет колонки таблицы """
        self.tree.heading("#1", text='id')
        self.tree.column("#1", stretch=tk.YES)

    def insert_data_tree(self):
        pass

if __name__ == '__main__':

    window = Interface()
    window.geometry("1024x840")
    window.title("Запрос Redmine")
    window.mainloop()



