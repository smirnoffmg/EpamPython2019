"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:
> print(folder1)
V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1
А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True
"""
import os


class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.base_level = content[0][0].count(os.sep)

    def __str__(self):

        def string_editor(str, _level):
            for i in range(_level):
                str[i] = '|'
                if i > 0:
                    str[i] = '\t|'

        dir_tree = ''
        for roots, dirs, files in self.content:
            level = roots.replace(self.name, '').count(os.sep) - self.base_level
            indent = '\t' * (level-1)
            if level > 0:
                temp_str = list('{}|-> V {}\n'.format(indent, os.path.basename(roots)))
                string_editor(temp_str, level)
                dir_tree += ''.join(temp_str)

            else:
                dir_tree += '{}V {}\n'.format(indent, os.path.basename(roots))
            indent = '\t' * level
            for f in files:
                temp_str = list('|{}{}\n'.format(indent, PrintableFile(f)))
                string_editor(temp_str, level+1)
                dir_tree += ''.join(temp_str)
        return dir_tree

    def __contains__(self, item):
        for _, _, files in self.content:
            for f in files:
                if f == item.name:
                    return True
        return False


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'-> {self.name}'


path = '/home/fury/studying/EpamPython2019/06-advanced-python'
basename = os.path.basename(path)
content = []
for root, dirs, files in os.walk(path):
    content.append((root, dirs, files))

folder_test = PrintableFolder(basename, content)
print(folder_test)
print(PrintableFile('task4.py') in folder_test)