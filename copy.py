def copy_file(source_file, destination_file):
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as source:
            # Read the content of the source file
            content = source.read()
        
        # Open the destination file in write mode
        with open(destination_file, 'w') as destination:
            # Write the content to the destination file
            destination.write(content)
        
        print("Content copied successfully from", source_file, "to", destination_file)
    
    except FileNotFoundError:
        print("One or both of the files does not exist.")

def main():
    # Specify the names of the source and destination files
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")

    # Call the function to copy the content from source to destination file
    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
