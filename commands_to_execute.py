from colorama.ansi import Fore, Style
from Directory import Directory
from File import File
from commands import commands_desc;

root = Directory('', 'root');

current_dir = root;

def create_file(name):
  return File({
    "name": name, 
    "content": "",
    "size": 0, 
    "pages": 0, 
    "starting_page_address": 0,
  });

def create_directory(name):
  return Directory(current_dir, name);

def display_current_directory():
  current_dir.display();

def move_to_parent_directory():
  global current_dir;
  current_dir = current_dir.move_to_parent_directory();

def list_commands():
  print("List of all commands:");
  for command in commands_desc:
    print(command['name'], end="  ");
  print("");  

def list_commands_with_desc():
  print("Details of all commands:");
  for command in commands_desc:
    print('{:<8} {:<70}'.format(command['name'] + ": ", command['description']));
  print("");  

def permission_valid(permission):  
  return permission in ['r', 'w'];

def list():
  if(current_dir.empty()):
      print(f'{Fore.RED}directory is empty!{Style.RESET_ALL}');
  else:
    current_dir.list(); 
  print();

def make_directory(args):
  if(current_dir.has_dir(args[0])):
    print(f'{Fore.RED}directory with this name already exists.{Style.RESET_ALL}', end='\n\n');
  else:
    current_dir.add_directory(create_directory(args[0])); 
    print(f'{Fore.GREEN}directory created.{Style.RESET_ALL}', end='\n\n');

def make_file(args):
  if(current_dir.has_file(args[0])):
      print(f'{Fore.RED}file with this name already exists.{Style.RESET_ALL}', end='\n\n');
  else:
    current_dir.add_file(create_file(args[0])); 
    print(f'{Fore.GREEN}file created.{Style.RESET_ALL}', end='\n\n');

def open_file(args):
  if(current_dir.has_file(args[0])):
    current_dir.file(args[0]).open(args[1]);
    print(f'{Fore.GREEN}file opened.{Style.RESET_ALL}', end='\n\n');
  else:
    print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');

def close_file(args):
  if(current_dir.has_file(args[0])):
    current_dir.file(args[0]).close();
    print(f'{Fore.GREEN}file closed.{Style.RESET_ALL}', end='\n\n');
  else:
    print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
  return;


def read(args):
  file = current_dir.file(args[0]);
  if(not file):
    print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
  elif(file.opened == False):
    print(f'{Fore.RED}file is not opened.{Style.RESET_ALL}', end='\n\n');
  elif(file.mode != 'r'):
    print(f'{Fore.RED}file is not opened in read mode.{Style.RESET_ALL}', end='\n\n');
  elif(not file.read_permission()):
    print(f'{Fore.RED}you do not have permission to read this file.{Style.RESET_ALL}', end='\n\n');
  else:
    file.read(args[1], args[2]);
    print();


def write(args):
  file = current_dir.file(args[0]);
  if(not file):
    print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
  elif(file.opened == False):
    print(f'{Fore.RED}file is not opened.{Style.RESET_ALL}', end='\n\n');
  elif(file.mode != 'w'):
    print(f'{Fore.RED}file is not opened in write mode.{Style.RESET_ALL}', end='\n\n');
  elif(not file.write_permission()):
    print(f'{Fore.RED}you do not have permission to write to this file.{Style.RESET_ALL}', end='\n\n');
  else:
    file.write(args[1]) if len(args) == 2 else file.write(args[1], args[2], args[3])
    print(f'{Fore.GREEN}file updated.{Style.RESET_ALL}', end='\n\n');


def append(args):
  file = current_dir.file(args[0]);
  if(not file):
    print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
  elif(file.opened == False):
    print(f'{Fore.RED}file is not opened.{Style.RESET_ALL}', end='\n\n');
  elif(file.mode != 'a'):
    print(f'{Fore.RED}file is not opened in append mode.{Style.RESET_ALL}', end='\n\n');
  elif(not file.write_permission()):
    print(f'{Fore.RED}you do not have permission to write to this file.{Style.RESET_ALL}', end='\n\n');
  else:
    file.append(args[1]);
    print(f'{Fore.GREEN}file updated.{Style.RESET_ALL}', end='\n\n');

def move_file(args):
  file = current_dir.file(args[0]);
  if(not file):
    print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    return;
  file.name = args[1];  
  print(f'{Fore.GREEN}file moved.{Style.RESET_ALL}', end='\n\n');

def truncate_file(args):
  file = current_dir.file(args[0]);
  if(not file):
    print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    return;
  file.truncate(args[1]);
  print(f'{Fore.GREEN}file truncated.{Style.RESET_ALL}', end='\n\n');

def show_memory_map():
  if(len(root.files) > 0):
    print();
    print('{:<16} {:<9} {:<16} {:<12}'.format('file', 'inode', 'size (bytes)', 'total pages'));
    root.traverse(root);
    print();
  else:
    print(f'{Fore.RED}nothing to show.{Style.RESET_ALL}', end='\n\n');

def read_permission(args):
  if(current_dir.has_file(args[1])):
    current_dir.file(args[1]).read_permissions();
  else:
    print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');

def grant_permission(args):
  if(current_dir.has_file(args[1])):
    file = current_dir.file(args[1]);
    permission = input('Permsission (r -> read, w -> write): ');
    file.grant_permission(permission) if(permission_valid(permission)) else print(f'{Fore.RED}invalid permission.{Style.RESET_ALL}', end='\n\n');
  else:
    print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');

def remove_permission(args):
  if(current_dir.has_file(args[1])):
    file = current_dir.file(args[1]);
    permission = input('Permsission to remove (r -> read, w -> write): ');
    file.remove_permission(permission) if(permission_valid(permission)) else print(f'{Fore.RED}invalid permission.{Style.RESET_ALL}', end='\n\n');
  else:
    print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');

def remove_file(args):
  if(not current_dir.has_file(args[1])):
    print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
  else:
    current_dir.remove_file(args[1]); 
    print(f'{Fore.GREEN}file removed.{Style.RESET_ALL}', end='\n\n');

def remove_directory(args):
  if(not current_dir.has_dir(args[1])):
    print(f'{Fore.RED}no such directory.{Style.RESET_ALL}', end='\n\n');
  else:
    current_dir.remove_directory(args[1]); 
    print(f'{Fore.GREEN}directory removed.{Style.RESET_ALL}', end='\n\n');

def change_directory(args):
  global current_dir;
  # check if user wants to go to previous directory
  if(args[0] == '..'):
    if(current_dir.parent != ""):
      current_dir = current_dir.parent; 
    return;

  if(args[0] == '/'):
    current_dir = root;  
    return;

  if(not current_dir.has_dir(args[0])):
    print(f'{Fore.RED}no such directory.{Style.RESET_ALL}', end='\n\n');
  else:
    current_dir = current_dir.child_directory(args[0]); 








