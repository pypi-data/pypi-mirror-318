import shutil
import os
import pkg_resources

def generate_program(program_number):
    # Define the name of the program file
    file_name = f"{program_number}.py"
    
    try:
        # Attempt to load the program file from the package resources
        program_code = pkg_resources.resource_string(__name__, f'programs/{file_name}')
        
        # Specify the destination file path
        destination_file = f"{program_number}.py"
        
        # Write the code to the new file
        with open(destination_file, 'wb') as f:
            f.write(program_code)
        
        print(f"{destination_file} created successfully from the package!")
    except FileNotFoundError:
        print(f"Program {file_name} does not exist in the package.")
