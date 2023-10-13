#!/usr/bin/python3
'''Console of Airbnb'''

 
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    class_dict = {"BaseModel": BaseModel
                  ,"User": User,
                  "Place": Place,
                  "State": State,
                  "City": City,
                  "Amenity": Amenity,
                  "Review": Review
                  }
    
    obj_dict = models.storage.all()

    

    def emptyline(self):
        """Do nothing when an empty line is input"""
        pass

    def do_classes(self, arg):
        """Prints the available classes when user tape classes """
        print("BaseModel . User.Place.State . City .Amenity . Review")

    def do_create(self, class_name):
        """
        Creates a new instance of an  Class
        classes to see available classes\n
        """
        if class_name == "":
            print("** class name missing **")

        elif self.class_dict[class_name]:
            obj = self.class_dict[class_name]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints  string representation of an instance.

        Usage:  <class name> <id> forme
        """

        if arg == "":
            print("** class name missing **")

        elif (arg.split())[0] not in self.class_dict:
            print("** class doesn't exist **")

        elif len(arg.split()) == 1:
            print("** instance id missing **")

        else:
            key_str = str(arg.replace(" ", "."))
            try:
                obj_dict = models.storage.all()
                print(obj_dict[key_str])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        destroy or delete an instance based on the class name and id

        Type classes to see available classes
        """

        if arg == "":
            print("** class name missing **")

        elif (arg.split())[0] not in self.class_dict:
            print("** class doesn't exist **")

        elif len(arg.split()) == 1:
            print("** instance id missing **")

        else:
            key_str = str(arg.replace(" ", "."))
            try:
                obj_dict = models.storage.all()
                del obj_dict[key_str]
                models.storage.save()
            except KeyError:
                print("** no instance found **")        

    def do_all(self, arg):
        """
        Prints instances as a string represtentation.

        Usage: all
        """

        if len(arg.split()) == 0 or (arg.split())[0] in self.class_dict :
            obj_dict = models.storage.all()
            list_str = []
            for key, value in obj_dict.items():
                list_str.append(str(value))
            print(list_str)
        else:
            print("** class doesn't exist **")   

    def do_update(self, arg):

        """
        Updates an instance based on the class <name and id
        and attributes

        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        list_arg = arg.split()
        if arg == "":
            print("** class name missing **")

        elif (list_arg[0] not in self.class_dict):
            print("** class doesn't exist **")

        elif len(list_arg) == 1:
            print("** instance id missing **")

        elif len(list_arg) == 2:
            print("** attribute name missing **")

        elif len(list_arg) == 3:
            print("** value missing **")
        else:
            list_arg = arg.split()
            cast_int = [
                "number_rooms",
                "number_bathrooms",
                "max_guest",
                "price_by_night"
                ]

            float_cast = ["latitude", "longitude"]
            key_str = list_arg[0] + "." + list_arg[1]
            obj_dict = models.storage.all()

            if key_str in obj_dict:
                name_attribute = list_arg[2]
                atribute_value = list_arg[3].replace('"', "")
                if name_attribute in cast_int:
                    atribute_value = int(atribute_value)
                if name_attribute in float_cast:
                    atribute_value = float(atribute_value)
                setattr(obj_dict[key_str], name_attribute, atribute_value)
                obj_dict[key_str].save()
            else:
                print("** no instance found **")  

    def do_BaseModel(self, arg):
        """BaseModel method

           arg:class of  object
        """
        if len(arg.split()) > 1:
            if arg[:7] == ".update" and arg.split()[1][0] != "{":
                values = arg.split()
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "BaseModel." + id
                atrribu_name = values[1].replace('"', "")[0:-1]
                attr_value = values[2].replace('"', "")[0:-1]
                if string in self.obj_dict:
                    setattr(self.obj_dict[string], atrribu_name, attr_value)
                    self.obj_dict[string].save()
                else:
                    print("** no instance found **")
            else:
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "BaseModel." + id
                my_string = ""
                for i in range(1, len(arg.split())):
                    my_string += arg.split()[i]
                new_dic = eval(my_string.replace(")", ""))
                if string in self.obj_dict:
                    for key, value in new_dic.items():
                        setattr(self.obj_dict[string], key, value)
                        self.obj_dict[string].save()
                else:
                    print("** no instance found **")
        elif arg.split()[0] == ".all()":
            for i in self.obj_dict.values():
                if type(i) == BaseModel:
                    print(i)
        elif arg.split()[0] == ".count()":
            count = 0
            for i in self.obj_dict.values():
                if type(i) == BaseModel:
                    count += 1
            print(count)
        elif arg.split()[0][:5] == ".show":
            id = arg.split()[0].replace('"', "")[6:-1]
            string = "BaseModel." + id
            try:
                print(self.obj_dict[string])
            except:
                print("** no instance found **")
        elif arg.split()[0][:8] == ".destroy":
            id = arg.split()[0].replace('"', "")[9:-1]
            string = "BaseModel." + id
            try:
                del self.obj_dict[string]
                models.storage.save()
            except:
                print("** no instance found **")

    def do_User(self, arg):
        """user method

        Args:
    
        """
        if len(arg.split()) > 1:
            if arg[:7] == ".update" and arg.split()[1][0] != "{":
                values = arg.split()
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "User." + id
                atrribu_name = values[1].replace('"', "")[0:-1]
                attr_value = values[2].replace('"', "")[0:-1]
                if string in self.obj_dict:
                    setattr(self.obj_dict[string], atrribu_name, attr_value)
                    self.obj_dict[string].save()
                else:
                    print("** no instance found **")
            else:
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "User." + id
                my_string = ""
                for i in range(1, len(arg.split())):
                    my_string += arg.split()[i]
                new_dic = eval(my_string.replace(")", ""))
                if string in self.obj_dict:
                    for key, value in new_dic.items():
                        setattr(self.obj_dict[string], key, value)
                        self.obj_dict[string].save()
                else:
                    print("** no instance found **")

        elif arg.split()[0] == ".all()":
            for i in self.obj_dict.values():
                if type(i) == User:
                    print(i)
        elif arg.split()[0] == ".count()":
            count = 0
            for i in self.obj_dict.values():
                if type(i) == User:
                    count += 1
            print(count)
        elif arg.split()[0][:5] == ".show":
            id = arg.split()[0].replace('"', "")[6:-1]
            string = "User." + id
            try:
                print(self.obj_dict[string])
            except:
                print("** no instance found **")
        elif arg.split()[0][:8] == ".destroy":
            id = arg.split()[0].replace('"', "")[9:-1]
            string = "User." + id
            try:
                del self.obj_dict[string]
                models.storage.save()
            except:
                print("** no instance found **")

    def do_Place(self, arg):
        """Place method

        
        """
        if len(arg.split()) > 1:
            if arg[:7] == ".update" and arg.split()[1][0] != "{":
                values = arg.split()
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "Place." + id
                atrribu_name = values[1].replace('"', "")[0:-1]
                attr_value = values[2].replace('"', "")[0:-1]
                if string in self.obj_dict:
                    setattr(self.obj_dict[string], atrribu_name, attr_value)
                    self.obj_dict[string].save()
                else:
                    print("** no instance found **")
            else:
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "Place." + id
                my_string = ""
                for i in range(1, len(arg.split())):
                    my_string += arg.split()[i]
                new_dic = eval(my_string.replace(")", ""))
                if string in self.obj_dict:
                    for key, value in new_dic.items():
                        setattr(self.obj_dict[string], key, value)
                        self.obj_dict[string].save()
                else:
                    print("** no instance found **")
        elif arg.split()[0] == ".all()":
            for i in self.obj_dict.values():
                if type(i) == Place:
                    print(i)
        elif arg.split()[0] == ".count()":
            count = 0
            for i in self.obj_dict.values():
                if type(i) == Place:
                    count += 1
            print(count)
        elif arg.split()[0][:5] == ".show":
            id = arg.split()[0].replace('"', "")[6:-1]
            string = "Place." + id
            try:
                print(self.obj_dict[string])
            except:
                print("** no instance found **")
        elif arg.split()[0][:8] == ".destroy":
            id = arg.split()[0].replace('"', "")[9:-1]
            string = "Place." + id
            try:
                del self.obj_dict[string]
                models.storage.save()
            except:
                print("** no instance found **")

    def do_State(self, arg):
        """State method

        Args:
            
        """
        if len(arg.split()) > 1:
            if arg[:7] == ".update" and arg.split()[1][0] != "{":
                values = arg.split()
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "State." + id
                atrribu_name = values[1].replace('"', "")[0:-1]
                attr_value = values[2].replace('"', "")[0:-1]
                if string in self.obj_dict:
                    setattr(self.obj_dict[string], atrribu_name, attr_value)
                    self.obj_dict[string].save()
                else:
                    print("** no instance found **")
            else:
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "State." + id
                my_string = ""
                for i in range(1, len(arg.split())):
                    my_string += arg.split()[i]
                new_dic = eval(my_string.replace(")", ""))
                if string in self.obj_dict:
                    for key, value in new_dic.items():
                        setattr(self.obj_dict[string], key, value)
                        self.obj_dict[string].save()
                else:
                    print("** no instance found **")
        elif arg.split()[0] == ".all()":
            for i in self.obj_dict.values():
                if type(i) == State:
                    print(i)
        elif arg.split()[0] == ".count()":
            count = 0
            for i in self.obj_dict.values():
                if type(i) == State:
                    count += 1
            print(count)
        elif arg.split()[0][:5] == ".show":
            id = arg.split()[0].replace('"', "")[6:-1]
            string = "State." + id
            try:
                print(self.obj_dict[string])
            except:
                print("** no instance found **")
        elif arg.split()[0][:8] == ".destroy":
            id = arg.split()[0].replace('"', "")[9:-1]
            string = "State." + id
            try:
                del self.obj_dict[string]
                models.storage.save()
            except:
                print("** no instance found **")

    def do_City(self, arg):
        """City method

        Args:
            class of the object
        """
        if len(arg.split()) > 1:
            if arg[:7] == ".update" and arg.split()[1][0] != "{":
                values = arg.split()
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "City." + id
                atrribu_name = values[1].replace('"', "")[0:-1]
                attr_value = values[2].replace('"', "")[0:-1]
                if string in self.obj_dict:
                    setattr(self.obj_dict[string], atrribu_name, attr_value)
                    self.obj_dict[string].save()
                else:
                    print("** no instance found **")
            else:
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "City." + id
                my_string = ""
                for i in range(1, len(arg.split())):
                    my_string += arg.split()[i]
                new_dic = eval(my_string.replace(")", ""))
                if string in self.obj_dict:
                    for key, value in new_dic.items():
                        setattr(self.obj_dict[string], key, value)
                        self.obj_dict[string].save()
                else:
                    print("** no instance found **")
        elif arg.split()[0] == ".all()":
            for i in self.obj_dict.values():
                if type(i) == City:
                    print(i)
        elif arg.split()[0] == ".count()":
            count = 0
            for i in self.obj_dict.values():
                if type(i) == City:
                    count += 1
            print(count)
        elif arg.split()[0][:5] == ".show":
            id = arg.split()[0].replace('"', "")[6:-1]
            string = "City." + id
            try:
                print(self.obj_dict[string])
            except:
                print("** no instance found **")
        elif arg.split()[0][:8] == ".destroy":
            id = arg.split()[0].replace('"', "")[9:-1]
            string = "City." + id
            try:
                del self.obj_dict[string]
                models.storage.save()
            except:
                print("** no instance found **")

    def do_Amenity(self, arg):
        """Amenity method

        Args:
            arg 
        """
        if len(arg.split()) > 1:
            if arg[:7] == ".update" and arg.split()[1][0] != "{":
                values = arg.split()
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "Amenity." + id
                atrribu_name = values[1].replace('"', "")[0:-1]
                attr_value = values[2].replace('"', "")[0:-1]
                if string in self.obj_dict:
                    setattr(self.obj_dict[string], atrribu_name, attr_value)
                    self.obj_dict[string].save()
                else:
                    print("** no instance found **")
            else:
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "Amenity." + id
                my_string = ""
                for i in range(1, len(arg.split())):
                    my_string += arg.split()[i]
                new_dic = eval(my_string.replace(")", ""))
                if string in self.obj_dict:
                    for key, value in new_dic.items():
                        setattr(self.obj_dict[string], key, value)
                        self.obj_dict[string].save()
                else:
                    print("** no instance found **")
        elif arg.split()[0] == ".all()":
            for i in self.obj_dict.values():
                if type(i) == Amenity:
                    print(i)
        elif arg.split()[0] == ".count()":
            count = 0
            for i in self.obj_dict.values():
                if type(i) == Amenity:
                    count += 1
            print(count)
        elif arg.split()[0][:5] == ".show":
            id = arg.split()[0].replace('"', "")[6:-1]
            string = "Amenity." + id
            try:
                print(self.obj_dict[string])
            except:
                print("** no instance found **")
        elif arg.split()[0][:8] == ".destroy":
            id = arg.split()[0].replace('"', "")[9:-1]
            string = "Amenity." + id
            try:
                del self.obj_dict[string]
                models.storage.save()
            except:
                print("** no instance found **")

    def do_Review(self, arg):
        """Review method

        Args:
            arg :class of the object]
        """
        if len(arg.split()) > 1:
            if arg[:7] == ".update" and arg.split()[1][0] != "{":
                values = arg.split()
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "Review." + id
                atrribu_name = values[1].replace('"', "")[0:-1]
                attr_value = values[2].replace('"', "")[0:-1]
                if string in self.obj_dict:
                    setattr(self.obj_dict[string], atrribu_name, attr_value)
                    self.obj_dict[string].save()
                else:
                    print("** no instance found **")
            else:
                id = arg.split()[0].replace('"', "")[8:-1]
                string = "Review." + id
                my_string = ""
                for i in range(1, len(arg.split())):
                    my_string += arg.split()[i]
                new_dic = eval(my_string.replace(")", ""))
                if string in self.obj_dict:
                    for key, value in new_dic.items():
                        setattr(self.obj_dict[string], key, value)
                        self.obj_dict[string].save()
                else:
                    print("** no instance found **")
        elif arg.split()[0] == ".all()":
            for i in self.obj_dict.values():
                if type(i) == Review:
                    print(i)
        elif arg.split()[0] == ".count()":
            count = 0
            for i in self.obj_dict.values():
                if type(i) == Review:
                    count += 1
            print(count)
        elif arg.split()[0][:5] == ".show":
            id = arg.split()[0].replace('"', "")[6:-1]
            string = "Review." + id
            try:
                print(self.obj_dict[string])
            except:
                print("** no instance found **")
        elif arg.split()[0][:8] == ".destroy":
            id = arg.split()[0].replace('"', "")[9:-1]
            string = "Review." + id
            try:
                del self.obj_dict[string]
                models.storage.save()
            except:
                print("** no instance found **")               

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print()
        return True
     
    def do_quit(self, arg):
        """Quit command to exit """
        return True   
if __name__ == '__main__':
    HBNBCommand().cmdloop()

