def read_and_modify_file():
    filename = input("Enter the filename you want to read: ")

    try:
        # Try opening and reading the file
        with open(filename, "r") as file:
            content = file.read()  # Read content

        # Modify the content (e.g., converting text to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File modified successfully. New file: {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_and_modify_file()
