

p_number_of_line = 54
u_number_of_line = 84
number_of_lines_remove = u_number_of_line - p_number_of_line

context = {
  'stats':{
    "p_no":p_number_of_line,
    "u_no": u_number_of_line,
    "no_removed": number_of_lines_remove
  },
}

print(context)