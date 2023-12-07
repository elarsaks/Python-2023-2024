#!/usr/bin/env python3

def file_extensions(filename):
    # Lists to store filenames without extensions and a dictionary for those with extensions
    no_extension = []
    extensions_dict = {}

    # Open and read the file
    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace from the end of the line
            line = line.strip()

            # Check if there is a period in the filename (indicating an extension)
            if '.' in line:
                # Extract the extension and add the filename to the corresponding list in the dictionary
                extension = line.split('.')[-1]
                extensions_dict.setdefault(extension, []).append(line)
            else:
                # If no period, add the filename to the no_extension list
                no_extension.append(line)

    return no_extension, extensions_dict


def main():
    # Call the file_extensions function with a specific file
    no_ext, ext_dict = file_extensions("src/filenames.txt")

    # Print the number of files without an extension
    print(f"{len(no_ext)} files with no extension")

    # Iterate through the extensions dictionary in alphabetical order
    for ext in sorted(ext_dict.keys()):
        # Print the extension and the number of files with that extension
        print(f"{ext} {len(ext_dict[ext])}")


if __name__ == "__main__":
    main()
