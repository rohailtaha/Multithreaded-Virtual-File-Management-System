# List of commands in input_thread1.txt

commands = [
  'mk file1.txt',
  'wr file1.txt abcd',
  'mk file2.txt',
  'wr file2.txt 123',
  'mm',
  'wr file1.txt xyz',
  'mm'
];


# create file1.txt
# open file1.txt,w
# write_to_file file1.txt,"abcd"
# create file2.txt
# open file2.txt,w
# show_memory_map
# write_to_file file2.txt,"123"
# write_to_file file1.txt,"xyz"
# close file1.txt
# close fil2.txt
# show_memory_map
