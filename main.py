from Directory import Directory;
from File import File;
from commands import commands_names as commands, instructions_commands_map;
from colorama import Fore, Style;
from inputs_thread1 import commands as commands_thread1;
from inputs_thread2 import commands as commands_thread2;
from inputs_thread3 import commands as commands_thread3;
import threading
import time
import commands_to_execute as cte;


def run_command(cd):

  if(cd[0] == commands["list"]):
    cte.list();

  elif(cd[0] == commands["make_directory"]):
    cte.make_directory(cd[1:]);

  elif(cd[0] == commands["make_file"]):
    cte.make_file(cd[1:]);

  elif(cd[0] == commands["open_file"]):
    cte.open_file(cd[1:]);

  elif(cd[0] == commands["close_file"]):
    cte.close_file(cd[1:]);

  elif(cd[0] == commands["read"]):
    cte.read(cd[1:]);

  elif(cd[0] == commands["write"]):
    cte.write(cd[1:]);

  elif(cd[0] == commands["append"]):
    cte.append(cd[1:]);

  elif(cd[0] == commands["read_permission"]):
    cte.read_permission(cd[1:]);

  elif(cd[0] == commands["grant_permission"]):
    cte.grant_permission(cd[1:]);

  elif(cd[0] == commands["remove_permission"]):
    cte.remove_permission(cd[1:]);
    
  elif(cd[0] ==  commands["remove_file"]):
    cte.remove_file(cd[1:]);

  elif(cd[0] ==  commands["remove_directory"]):
    cte.remove_directory(cd[1:])

  elif(cd[0] == commands["change_directory"]):
    cte.change_directory()

  elif(cd[0] ==  commands["parent_directory"]):
    cte.parent_directory()

  elif(cd[0] ==  commands["root_directory"]):
    cte.root_directory();

  elif(cd[0] ==  commands["show_memory_map"]):
    cte.show_memory_map();
     
  elif(cd[0] ==  commands["list_commands"]):
    cte.list_commands();

  elif(cd[0] ==  commands["list_detailed_commands"]):
    cte.list_commands_with_desc();

  elif(cd[0] == commands["exit"]):
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

# for i in range(NUMBER_OF_USERS):
#   thread = threading.Thread(target=begin, args=([1]))
#   thread.start();
  
# time.sleep(2)
run_command(['mk', 'file.txt']);
run_command(['op', 'file.txt', 'w']);
run_command(['wr', 'file.txt', 'This is some content']);
run_command(['op', 'file.txt', 'r']);
run_command(['rd', 'file.txt']);





