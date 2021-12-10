import uuid

from colorama.ansi import Fore, Style;

class Directory:
  def __init__(self, parent, name):
    self.id = uuid.uuid4().__int__().__str__()[0:6];
    self.parent = parent;
    self.name = name;
    self.size = 0;
    self.files = list();
    self.directories = list();

  # Add file and update size 
  def add_file(self, file):
    self.files.append(file);  
    self.update_size();

  # Add directory and update size 
  def add_directory(self, directory):
    self.directories.append(directory);  
    self.update_size();
  
  # @ RETURN:
  # 1 if file found and removed 
  # 0 if file not found  
  def has_file(self, name):
    for file in self.files:
      if(file.name == name):
        return 1;
    return 0;    

  def has_dir(self, name):
    for directory in self.directories:
      if(directory.name == name):
        return 1;
    return 0;    

  def remove_file(self, name):
    def check(file):
      return file.name != name;

    self.files = list(filter(check, self.files));

  # @ RETURN:
  # 1 if directory found and removed 
  # 0 if directory not found  
  def remove_directory(self, name):
    def check(directory):
      return directory.name != name;

    self.directories = list(filter(check, self.directories));
    

  def update_size(self):
    self.size = 0;
    for file in self.files:
      self.size += file.size;
    for directory in self.directories:
      self.size += directory.size;

  def empty(self):
    return len(self.files) == 0 and len(self.directories) == 0;    

  def list(self):
    for file in self.files:
      print(f'{Fore.GREEN}{file.name}{Style.RESET_ALL}', end="  ");
    for directory in self.directories:
      print(f'{Fore.YELLOW}{directory.name}{Style.RESET_ALL}', end="  ");
    print();  

  def display(self): 
    path = "";
    temp = self; 
    while (temp.parent != ""):
      path = temp.name + "/" + path;
      temp = temp.parent;
    path = temp.name + "/" + path;  
    print(f'{Fore.BLUE}==> {path}{Style.RESET_ALL}');

  # @ RETURN: 
  # child directory if found, 
  # current directory if not found
  def child_directory(self, name):      
    for directory in self.directories:
      if(directory.name == name):
        return directory;
    return self;    

  def file(self, name):      
    for file in self.files:
      if(file.name == name):
        return file;   

  def parent_directory(self):
    return self.parent;  
  
  def traverse(self, dir):
    for file in dir.files:
      print('{:<16} {:<9} {:<20}'.format(file.name, file.inode, file.size));
    # call recursively for child directries
    for directory in dir.directories:
      self.traverse(directory)  


