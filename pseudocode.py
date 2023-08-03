if in_path and out_path:
    # Get files from the input directory
    files = os.listdir(in_path)
    
    # Sort files by their creation date
    files.sort(key=lambda x: os.stat(os.path.join(in_path, x)).st_mtime)
    
    # Initialize a counter for renaming files
    count = 0
    
    # Loop through each file in the input directory
    for file in files:
        # Get the full path of the current file
        old_file_path = os.path.join(in_path, file)
        
        # Get the base name of the file (without the directory)
        file_name = os.path.basename(old_file_path)
        
        # Create a new file name with a prefix and the current count
        new_file_name = "__" + str(count) + "__" + file_name
        
        # Combine the new file name with the output directory to get the new file path
        new_file_path = os.path.join(out_path, new_file_name)
        
        # Copy the file from the input directory to the output directory with the new name
        shutil.copy(old_file_path, new_file_path)
        
        # Increment the counter for the next file
        count += 1
