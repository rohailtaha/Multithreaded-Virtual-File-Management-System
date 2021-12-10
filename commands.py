

# Total commands =  18 
commands = {
  "list": "ls",
  "make_file": "mk",
  "make_directory": "mkdir",
  "remove_file": "rm",
  "remove_directory": "rmdir",
  "change_directory": "cd",
  "parent_directory": "cd ..",
  "root_directory": "cd /",
  "memory_map": "mm",
  "list_commands": "cmds",
  "list_detailed_commands": "cmdsd",
  "read": "rd",
  "write": "wr",
  "append": "ap",
  "read_permission": "rdpm",  
  "remove_permission": "rmpm",  
  "grant_permission": "pm",
  "exit": "ex"
}

commands_desc = [
  {
  "name": "ls",
  "description": "List all files and folders in the current directory."
}, 
  {
  "name": "rd",
  "description": "read content of a file."
}, 
  {
  "name": "wr",
  "description": "write content to a file."
}, 
  {
  "name": "ap",
  "description": "append content to a file."
}, 
{
  "name": "mk",
  "description": "Create a file in the current directory."
},
{
  "name": "mkdir",
  "description": "Create a folder in the current directory."
},
{
  "name": "cd",
  "description": "Move one directory up from the current directory."
},
{
  "name": "rm",
  "description": "Remove a file from the current directory."
},
{
  "name": "rmdir",
  "description": "Remove a directory from the current directory."
},
{
  "name": "mm",
  "description": "List details of all files in the system."
},
{
  "name": "cmds",
  "description": "List all file system commands."
},
{
  "name": "cmds_d",
  "description": "List all file system commands alongwith their description."
},
{
  "name": "cd /",
  "description": "Move to root directory."
},
{
  "name": "cd ..",
  "description": "Move to parent directory."
},
{
  "name": "pm",
  "description": "Grant permission for a file."
},
{
  "name": "rdpm",
  "description": "Read all permissions for a file"
},
{
  "name": "rmpm",
  "description": "Remove a permission for a file"
},
{
  "name": "ex",
  "description": "Exit."
},
]

