def split_and_join(line):
   line = line.split(" ")
   line = "-".join(line)
   return line 

if _name_ == '_main_':
    line = input()
    result = split_and_join(line)
    print(result)
