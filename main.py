from Directory import Directory;
from File import File;
from commands import commands, commands_desc;
from colorama import Fore, Style;
from inputs_thread1 import commands as commands_thread1;
import math;

# Page Size in bytes
PAGE_SIZE = 20
root = Directory('', 'root');

current_dir = root;


def create_file(name):
  return File({
    "name": name, 
    "content": "",
    "size": 1, 
    "pages": 1, 
    "starting_page_address": 0,
  });

def create_directory(name):
  return Directory(current_dir, name);

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



def run_command(cd):
  global current_dir;

  if(cd[0] == commands["list"]):
    if(current_dir.empty()):
      print(f'{Fore.RED}directory is empty!{Style.RESET_ALL}');
    else:
      current_dir.list(); 
    print();
    return; 

  if(cd[0] == commands["make_directory"]):
    if(current_dir.has_dir(cd[1])):
      print(f'{Fore.RED}directory with this name already exists.{Style.RESET_ALL}', end='\n\n');
    else:
      current_dir.add_directory(create_directory(cd[1])); 
      print(f'{Fore.GREEN}directory created.{Style.RESET_ALL}', end='\n\n');
    return;

  if(cd[0] == commands["make_file"]):
    if(current_dir.has_file(cd[1])):
      print(f'{Fore.RED}file with this name already exists.{Style.RESET_ALL}', end='\n\n');
    else:
      current_dir.add_file(create_file(cd[1])); 
      print(f'{Fore.GREEN}file created.{Style.RESET_ALL}', end='\n\n');
    return;

  if(cd[0] == commands["read"]):
    if(current_dir.has_file(cd[1])):
      current_dir.file(cd[1]).read();
      print();
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    return;

  if(cd[0] == commands["write"]):
    if(current_dir.has_file(cd[1])):
      current_dir.file(cd[1]).write(cd[2]);
      print(f'{Fore.GREEN}file updated.{Style.RESET_ALL}', end='\n\n');
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    return;

  if(cd[0] == commands["append"]):
    if(current_dir.has_file(cd[1])):
      current_dir.file(cd[1]).append(cd[2]);
      print(f'{Fore.GREEN}file updated.{Style.RESET_ALL}', end='\n\n');
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    return;

  if(cd[0] == commands["read_permission"]):
    if(current_dir.has_file(cd[1])):
      current_dir.file(cd[1]).read_permissions();
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    return;

  if(cd[0] == commands["grant_permission"]):
    if(current_dir.has_file(cd[1])):
      file = current_dir.file(cd[1]);
      permission = input('Permsission (r -> read, w -> write): ');
      file.grant_permission(permission) if(permission_valid(permission)) else print(f'{Fore.RED}invalid permission.{Style.RESET_ALL}', end='\n\n');
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    return;

  if(cd[0] == commands["remove_permission"]):

    if(current_dir.has_file(cd[1])):
      file = current_dir.file(cd[1]);
      permission = input('Permsission to remove (r -> read, w -> write): ');
      file.remove_permission(permission) if(permission_valid(permission)) else print(f'{Fore.RED}invalid permission.{Style.RESET_ALL}', end='\n\n');
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    return;

  if(cd[0] ==  commands["remove_file"]):
    if(not current_dir.has_file(cd[1])):
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    else:
      current_dir.remove_file(cd[1]); 
      print(f'{Fore.GREEN}file removed.{Style.RESET_ALL}', end='\n\n');
    return 

  if(cd[0] ==  commands["remove_directory"]):
    if(not current_dir.has_dir(cd[1])):
      print(f'{Fore.RED}no such directory.{Style.RESET_ALL}', end='\n\n');
      return;
    else:
      current_dir.remove_directory(cd[1]); 
      print(f'{Fore.GREEN}directory removed.{Style.RESET_ALL}', end='\n\n');
    return; 

  if(cd[0] == commands["change_directory"]):
    if(not current_dir.has_dir(cd[1])):
      print(f'{Fore.RED}no such directory.{Style.RESET_ALL}', end='\n\n');
    else:
      current_dir = current_dir.child_directory(cd[1]); 
    return; 

  if(cd[0] ==  commands["parent_directory"]):
    if(current_dir.parent != ""):
      current_dir = current_dir.parent; 
    return;  

  if(cd[0] ==  commands["root_directory"]):
    current_dir = root; 
    return;  

  if(cd[0] ==  commands["memory_map"]):
    if(len(root.files) > 0):
      print('{:<16} {:<9} {:<20}'.format('file', 'inode', 'size (bytes)'));
      root.traverse(root);
      print();
    else:
      print(f'{Fore.RED}nothing to show.{Style.RESET_ALL}', end='\n\n');
    return;
     
  if(cd[0] ==  commands["list_commands"]):
    list_commands();
    return; 

  if(cd[0] ==  commands["list_detailed_commands"]):
    list_commands_with_desc();
    return; 

  if(cd[0] == commands["exit"]):
    exit(0); 

  else:
    print(f'{Fore.RED}Invalid command \'{cd}\'{Style.RESET_ALL}');
  
  current_dir.display();


def start():
  # cd = "";
  # current_dir.display();


  for cd in commands_thread1:
    print("running command: ", cd);
    run_command(cd.split(" "));

start();




