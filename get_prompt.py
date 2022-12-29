def get_prompt ():
  # Open the file in read mode
  with open("prompts.txt", "r") as file:
      # Read the first line of the file
      first_line = file.readline()
  
  # Check if the first line is the line you want to delete
  if first_line == first_line:
      # If the first line is the line you want to delete, open the file in read mode again
      with open("prompts.txt", "r") as file:
          # Read all the lines in the file except for the first line
          lines = file.readlines()[1:]
  
      # Open the file in write mode
      with open("prompts.txt", "w") as file:
          # Write the modified lines back to the file
          file.writelines(lines)
  
  return first_line
  