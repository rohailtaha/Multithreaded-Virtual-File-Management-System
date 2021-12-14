s = 'write file.txt,This is some sample text,12,10';

args = s[s.index(' ')  + 1:] 

print(args.split(','))