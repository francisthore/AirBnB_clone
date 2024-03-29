#!/usr/bin/python3
# entry file
"""this is a console program"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """class for hbnb command line"""
    class_names = ['BaseModel', 'User',
                   'Amenity', 'City', 'Place', 'Review', 'State']
    __all_objects = []
    prompt = '(hbnb)'

    def do_quit(self, line):
        """function to quit the program"""
        return True

    def do_EOF(self, line):
        """function to quit the program"""
        return True

    def emptyline(self):
        """handle empty line"""
        pass

    def do_create(self, line):
        """function to create an instance """
        if len(line) == 0:
            print('** class name missing **')
        elif line not in self.class_names:
            print("** class doesn't exist **")
        else:
            new_model = globals()[line]()
            new_model.save()
            print("{}".format(new_model.id))

    def do_show(self, line):
        """to print the string repressentation"""
        line_arr = line.split(' ')
        if len(line) == 0:
            print('** class name missing **')
        elif line_arr[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(line_arr) != 2:
            print('** instance id missing **')
        else:
            name = line_arr[0] + '.' + line_arr[1]
            if name in storage.reload():
                my_new_model = globals()[line_arr[0]](**storage.reload()[name])
                print(my_new_model)
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance"""
        line_arr = line.split(' ')
        if len(line) == 0:
            print('** class name missing **')
        elif line_arr[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(line_arr) != 2:
            print('** instance id missing **')
        else:
            name = line_arr[0] + '.' + line_arr[1]
            if name in storage.reload():
                del storage.reload()[name]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints string represantation of all instances"""
        if line:
            if line in self.class_names:
                for key, value in storage.reload().items():
                    if key.split('.')[0] == line:
                        object = str(globals()[line](**value))
                        self.__all_objects.append(object)
                print(self.__all_objects)
            else:
                print("** class doesn't exist **")
        else:
            for key, value in storage.reload().items():
                object = str(globals()[key.split('.')[0]](**value))
                self.__all_objects.append(object)
            print(self.__all_objects)
        self.__all_objects = []

    def do_update(self, line):
        """updates an instance based on the
        class name and id"""
        line_arr = line.split(' ')
        if len(line) == 0:
            print('** class name missing **')
        elif line_arr[0] not in self.class_names:
            print("** class doesn't exist **")
        elif len(line_arr) < 2:
            print('** instance id missing **')
        else:
            name = line_arr[0] + '.' + line_arr[1]
            if name not in storage.reload():
                print("** no instance found **")
            elif len(line_arr) < 3:
                print("** attribute name missing **")
            elif len(line_arr) < 4:
                print("** value missing **")
            else:
                storage.reload()[name][line_arr[2]] = line_arr[3]
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
