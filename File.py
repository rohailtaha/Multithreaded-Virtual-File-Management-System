import uuid
import math

from colorama.ansi import Fore, Style;

# Page Size in bytes
PAGE_SIZE = 40

class File:
  def __init__(self, file):
    self.inode = uuid.uuid4().__int__().__str__()[0:6];
    self.name = file['name'];
    self.size = file['size'];
    self.pages = file['pages'];
    self.content = file['content'];
    self.starting_page_address = file['starting_page_address'];
    # permissions = ['r', 'w'] for read, write.
    self.permissions= ['r', 'w'];
    self.mode = 'r';
    self.opened = False;

  def update_size(self):
    self.size = len(self.content) + 1;
    self.pages = math.ceil(self.size / PAGE_SIZE);   

  def write_permission(self):
    return 'w' in self.permissions;

  def read_permission(self):
    return 'r' in self.permissions;  

  def open(self, mode):
    self.opened = True;
    self.mode = mode;

  def close(self):
    self.opened = False;
    self.mode = 'r';

  def read(self, startLocation, size):
    if(self.open and self.mode == 'r' and self.read_permission()):
      print(self.content[startLocation: startLocation + size]);      

  def append(self, content):  
    if(self.open and self.mode == 'a' and self.write_permission()):
      self.content += (" " + content);
      self.update_size();

  def replace(self, text, startLocation, size):
    if(int(size) > len(text)): 
      print(f'{Fore.RED}number of bytes to write are greater than the text size.{Style.RESET_ALL}', end='\n\n');
      return False;

    if(startLocation > len(self.content) or startLocation < -1):
      print(f'{Fore.RED}invalid start location.{Style.RESET_ALL}', end='\n\n');
      return False;

    if(startLocation == -1):
      return text[:size] + self.content;
    return self.content[: startLocation] + text[:size] + self.content[startLocation  + size:];    

  def write(self, content, startLocation = None, size = None):
    if(self.open and self.mode == 'w'  and self.write_permission()):
      if(startLocation is None and size is None):
        self.content = content;
      else:
        replaced_content = self.replace(content, startLocation, size);
        if replaced_content:
          self.content = replaced_content;
      self.update_size();

  def truncate(self, maxSize):
    self.content = self.content[:maxSize];
    self.update_size();

  def read_permissions(self):
    permissions = "Permissions: ";
    for permission in self.permissions:
      permissions += (permission + " ");
    print(permissions); 

  def grant_permission(self, permission):
    if(permission not in self.permissions):
      self.permissions.append(permission);

  def remove_permission(self, permission):
    def check(apermission):
      return apermission != permission

    self.permissions = list(filter(check, self.permissions));
    


