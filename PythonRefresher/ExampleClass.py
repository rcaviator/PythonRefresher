import os
import shutil

#example class
class MyClass:
    """A simple example class"""

    #constructor
    def __init__(self, path):
        self.__path_name = path
        self.__file_list = []
        
        #set up file list
        for file in os.listdir():
            if file.endswith(".txt"):
                self.__file_list.append(file)

    #gets a list of files in the directory
    def get_files(self):
        return self.__file_list

    #copyies the files into into a new folder
    def copy_and_move_files(self, path):
        
        #if the folder does not exist, create it
        if not os.path.exists(self.__path_name + path):
            #create folder
            os.makedirs(self.__path_name + path)

        #copy files over to new folder
        for x in self.__file_list:
            shutil.copy2(x, self.__path_name + path)

    #deletes the coppied files from folder
    def delete_copied_files(self, path):
        
        #if the folder does not exist, exit
        if not os.path.exists(self.__path_name + path):
            print("Folder does not exist.")
            return

        #get any text file if there are text files
        self.__text_files = []
        for file in os.listdir(self.__path_name + path):
            if file.endswith(".txt"):
                self.__text_files.append(file)

        #check if the list is greater than 0
        if len(self.__text_files) > 0:
            for file in self.__text_files:
                os.remove(self.__path_name + path + "\\" + file)
        else:
            print("No text files to delete")