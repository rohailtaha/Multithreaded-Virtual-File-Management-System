from os import read
from Directory import Directory;
from File import File;
from commands import commands, commands_desc, instructions_commands_map;
from colorama import Fore, Style;
from inputs_thread1 import commands as commands_thread1;
from inputs_thread2 import commands as commands_thread2;
from inputs_thread3 import commands as commands_thread3;
import threading
import time

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

  if(cd[0] == commands["open"]):
    if(current_dir.has_file(cd[1])):
      current_dir.file(cd[1]).open(cd[2]);
      print(f'{Fore.GREEN}file opened.{Style.RESET_ALL}', end='\n\n');
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    return;

  if(cd[0] == commands["close"]):
    if(current_dir.has_file(cd[1])):
      current_dir.file(cd[1]).close();
      print(f'{Fore.GREEN}file closed.{Style.RESET_ALL}', end='\n\n');
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    return;

  if(cd[0] == commands["read"]):
    if(current_dir.has_file(cd[1])):
      current_dir.file(cd[1]).read();
      print();
    elif(current_dir.file(cd[1]).opened == False or current_dir.file(cd[1]).mode != 'r'):
      print(f'{Fore.RED}file is not opened for reading.{Style.RESET_ALL}', end='\n\n');
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    return;

  if(cd[0] == commands["write"]):
    if(current_dir.has_file(cd[1])):
      content  = ' '.join(word for word in cd[2:]);
      current_dir.file(cd[1]).write(content);
      print(f'{Fore.GREEN}file updated.{Style.RESET_ALL}', end='\n\n');
    elif(current_dir.file(cd[1]).opened == False or current_dir.file(cd[1]).mode != 'w'):
      print(f'{Fore.RED}file is not opened for writing.{Style.RESET_ALL}', end='\n\n');
    else:
      print(f'{Fore.RED}no such file.{Style.RESET_ALL}', end='\n\n');
    return;

  if(cd[0] == commands["append"]):
    if(current_dir.has_file(cd[1])):
      content  = ' '.join(word for word in cd[2:]);
      current_dir.file(cd[1]).append(content);
      print(f'{Fore.GREEN}file updated.{Style.RESET_ALL}', end='\n\n');
    elif(current_dir.file(cd[1]).opened == False or current_dir.file(cd[1]).mode != 'a'):
      print(f'{Fore.RED}file is not opened for appending.{Style.RESET_ALL}', end='\n\n');
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
      print('{:<16} {:<9} {:<16} {:<12}'.format('file', 'inode', 'size (bytes)', 'total pages'));
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


  

def begin(thread_num):

  def getInstruction(line):
    return line.split(' ')[0].strip();
  def getInstructionArguments(line):
    # remove new line character from line; 
    line = line.strip();
    # check if intruction has any arguments: 
    if(len(line.split(' ')) > 1):
      return line.split(' ')[1].split(',');
    return [''];

  def get_command(line):
    command = instructions_commands_map[getInstruction(line)];
    command_arguments = getInstructionArguments(line);
    return ' '.join(s for s in [command] + command_arguments);

  input_file = open('input_thread' + str(thread_num) + '.txt');
  output_file = open('output_thread' + str(thread_num) + '.txt', 'a');
  while(True):
    line = input_file.readline();
    if(line == ''):
      break;
    command = instructions_commands_map[getInstruction(line)];
    command_arguments = getInstructionArguments(line);

    print('thread:', thread_num ,", command:", get_command(line));
    output_file.write("running command: " + get_command(line) + "\n");
    run_command([command] + command_arguments);

NUMBER_OF_USERS = 1;

for i in range(NUMBER_OF_USERS):
  thread = threading.Thread(target=begin, args=([1]))
  thread.start();
  
# time.sleep(2)
# run_command(['mm']);



