from Directory import Directory;
from File import File;
from commands import commands, commands_desc;
from colorama import Fore, Style;
import math;

# Page Size in bytes
PAGE_SIZE = 20
root = Directory('', 'root');

current_dir = root;

def file_name():
  return input("File name: ");

def dir_name():
  return input("Directory name: ");


def create_file(name):
  return File({
    "name": name, 
    "content": "",
    "size": 1, 
    "pages": 0, 
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
    current_dir.display();
    return; 

  if(cd == commands["make_directory"]):
    name = dir_name();
    if(current_dir.has_dir(name)):
      print(f'{Fore.RED}directory with this name already exists.{Style.RESET_ALL}', end='\n\n');
    else:
      current_dir.add_directory(create_directory(name)); 
      print(f'{Fore.GREEN}directory created.{Style.RESET_ALL}', end='\n\n');
    current_dir.display();
    return;

  if(cd[0] == commands["make_file"]):
    # name = file_name();
    if(current_dir.has_file(cd[1])):
      print(f'{Fore.RED}file with this name already exists.{Style.RESET_ALL}', end='\n\n');
    else:
      current_dir.add_file(create_file(cd[1])); 
      print(f'{Fore.GREEN}file created.{Style.RESET_ALL}', end='\n\n');
    current_dir.display();
    return;

  if(cd == commands["read"]):
    name = file_name();
    if(current_dir.has_file(name)):
      current_dir.file(name).read();
      print();
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    current_dir.display();
    return;

  if(cd == commands["write"]):
    name = file_name();
    if(current_dir.has_file(name)):
      current_dir.file(name).write(input("Content: "));
      print(f'{Fore.GREEN}file updated.{Style.RESET_ALL}', end='\n\n');
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    current_dir.display();
    return;

  if(cd == commands["append"]):
    name = file_name();
    if(current_dir.has_file(name)):
      current_dir.file(name).append(input("Content: "));
      print(f'{Fore.GREEN}file updated.{Style.RESET_ALL}', end='\n\n');
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    current_dir.display();
    return;

  if(cd == commands["read_permission"]):
    name = file_name();
    if(current_dir.has_file(name)):
      current_dir.file(name).read_permissions();
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    current_dir.display();
    return;

  if(cd == commands["grant_permission"]):
    name = file_name();
    if(current_dir.has_file(name)):
      file = current_dir.file(name);
      permission = input('Permsission (r -> read, w -> write): ');
      file.grant_permission(permission) if(permission_valid(permission)) else print(f'{Fore.RED}invalid permission.{Style.RESET_ALL}', end='\n\n');
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    current_dir.display();
    return;

  if(cd == commands["remove_permission"]):
    name = file_name();
    if(current_dir.has_file(name)):
      file = current_dir.file(name);
      permission = input('Permsission to remove (r -> read, w -> write): ');
      file.remove_permission(permission) if(permission_valid(permission)) else print(f'{Fore.RED}invalid permission.{Style.RESET_ALL}', end='\n\n');
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    current_dir.display();
    return;

  if(cd ==  commands["remove_file"]):
    name = file_name();
    if(not current_dir.has_file(name)):
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    else:
      current_dir.remove_file(name); 
      print(f'{Fore.GREEN}file removed.{Style.RESET_ALL}', end='\n\n');
    current_dir.display();
    return 

  if(cd ==  commands["remove_directory"]):
    name = dir_name();
    if(not current_dir.has_dir(name)):
      print(f'{Fore.RED}no such directory.{Style.RESET_ALL}', end='\n\n');
      return;
    else:
      current_dir.remove_directory(name); 
      print(f'{Fore.GREEN}directory removed.{Style.RESET_ALL}', end='\n\n');
    current_dir.display();
    return; 

  if(cd == commands["change_directory"]):
    name = dir_name();
    if(not current_dir.has_dir(name)):
      print(f'{Fore.RED}no such directory.{Style.RESET_ALL}', end='\n\n');
    else:
      current_dir = current_dir.child_directory(name); 
    current_dir.display();
    return; 

  if(cd ==  commands["parent_directory"]):
    if(current_dir.parent != ""):
      current_dir = current_dir.parent; 
    current_dir.display();
    return;  

  if(cd ==  commands["root_directory"]):
    current_dir = root; 
    current_dir.display();
    return;  

  if(cd ==  commands["memory_map"]):
    if(len(root.files) > 0):
      print('{:<16} {:<9} {:<20}'.format('file', 'inode', 'size (bytes)'));
      root.traverse(root);
      print();
    else:
      print(f'{Fore.RED}nothing to show.{Style.RESET_ALL}', end='\n\n');
    current_dir.display();
    return;
     
  if(cd ==  commands["list_commands"]):
    list_commands();
    current_dir.display();
    return; 

  if(cd ==  commands["list_detailed_commands"]):
    list_commands_with_desc();
    current_dir.display();
    return; 

  if(cd == commands["exit"]):
    exit(0); 

  else:
    print(f'{Fore.RED}Invalid command \'{cd}\'{Style.RESET_ALL}');
    current_dir.display();


def start():
  cd = "";
  current_dir.display();
  f = open("input_thread1.txt");
  while(cd != commands['exit']):
    # cd = f.readline();
    # if(cd == ''):
    #   break; 
    # print(cd);
    cd = input();
    run_command(cd.split(" "));

start();




