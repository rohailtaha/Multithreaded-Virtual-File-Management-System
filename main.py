from Directory import Directory;
from File import File;
from util_structures import commands_names as commands, instructions_commands_map;
from colorama import Fore, Style;
import threading
import commands_to_execute as user;
import time;
from commands_to_execute import User;

def run_command(cd, user):

  if(cd[0] == commands["list"]):
    user.list();

  elif(cd[0] == commands["make_directory"]):
    user.make_directory(cd[1:]);

  elif(cd[0] == commands["make_file"]):
    user.make_file(cd[1:]);

  elif(cd[0] == commands["open_file"]):
    user.open_file(cd[1:]);

  elif(cd[0] == commands["close_file"]):
    user.close_file(cd[1:]);

  elif(cd[0] == commands["read"]):
    user.read(cd[1:]);

  elif(cd[0] == commands["write"]):
    user.write(cd[1:]);

  elif(cd[0] == commands["append"]):
    user.append(cd[1:]);

  elif(cd[0] == commands["truncate_file"]):
    user.truncate_file(cd[1:]);

  elif(cd[0] == commands["move_file"]):
    user.move_file(cd[1:]);

  elif(cd[0] == commands["read_permission"]):
    user.read_permission(cd[1:]);

  elif(cd[0] == commands["grant_permission"]):
    user.grant_permission(cd[1:]);

  elif(cd[0] == commands["remove_permission"]):
    user.remove_permission(cd[1:]);
    
  elif(cd[0] ==  commands["remove_file"]):
    user.remove_file(cd[1:]);

  elif(cd[0] ==  commands["remove_directory"]):
    user.remove_directory(cd[1:])

  elif(cd[0] == commands["change_directory"]):
    user.change_directory(cd[1:])

  elif(cd[0] ==  commands["show_memory_map"]):
    user.show_memory_map();
     
  elif(cd[0] ==  commands["list_commands"]):
    user.list_commands();

  elif(cd[0] ==  commands["list_detailed_commands"]):
    user.list_commands_with_desc();

  elif(cd[0] == commands["exit"]):
    exit(0); 

  else:
    print(f'{Fore.RED}Invalid command \'{cd}\'{Style.RESET_ALL}');


def begin(thread_num):
  user = User();
  print (user.current_dir);

  def getInstruction(line):
    return line.split(' ')[0].strip();
  def getInstructionArguments(line):
    # remove new line charauserr from line; 
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
    user.display_current_directory();
    line = input_file.readline();
    if(line == ''):
      break;
    command = instructions_commands_map[getInstruction(line)];
    command_arguments = getInstructionArguments(line);

    print('thread:', thread_num ,", command:", get_command(line), "\n");
    output_file.write("running command: " + get_command(line) + "\n");
    run_command([command] + command_arguments, user);

NUMBER_OF_USERS = 1;

for i in range(NUMBER_OF_USERS):
  thread = threading.Thread(target=begin, args=([2]))
  thread.start();
  
# time.sleep(1)
# run_command(['mkdir', 'dir1']);``
# run_command(['cd', 'dir1']);
# run_command(['mk', 'file.txt']);
# run_command(['ls']);
# run_command(['cd', '/']);
# run_command(['ls']);



