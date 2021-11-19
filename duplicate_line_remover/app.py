

from pathlib import Path 


#def unique_path(directory, name_pattern):
#    counter = 0
#    while True:
#        counter += 1
#        path = directory / name_pattern.format(counter)
#        if not path.exists():
#            return path

   

def duplicate_text_remover(pathstrings): 

  pathstring=Path(pathstrings).resolve()

  with open(pathstring) as file: 
    readfile= file.readlines() 
    
    # Use file to refer to the file object
  

  my_data=[]

  for line in readfile:
      if line in my_data:
          pass
      else:
          my_data.append(line)
    
         
  my_str=" ".join(my_data)
 

  with open('py-drills\\vs-extension3.txt',"w") as to_file: 
    to_file.write(my_str)

    
     # Use file to refer to the file object
  


pathstring=Path("styles.css").resolve()



#path1 = unique_path(pathlib.Path.cwd(), 'repeatremoved{:03d}.txt')
