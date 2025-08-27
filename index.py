def read_file(filename):
    """Reads the content of a file."""
    with open(filename, 'r') as f:
        return f.read()

def write_file(filename, content):
    """Writes the given content to a file."""
    with open(filename, 'w') as f:
        f.write(content)

def transform_content(content):
    """Example transformation: uppercase everything."""
    return content.upper()

def main():
    # Step 1: Ask the user for an input file
    input_file = input("Enter the file name to read: ")

    try:
        # Step 2: Read the file
        original_content = read_file(input_file)

        # Step 3: Transform the content
        modified_content = transform_content(original_content)

        # Step 4: Generate output file name
        output_file = "modified_" + input_file

        # Step 5: Write the modified content
        write_file(output_file, modified_content)

        print(f"✅ Success! '{output_file}' has been created.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"❌ Error: Permission denied for '{input_file}'.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    main()
