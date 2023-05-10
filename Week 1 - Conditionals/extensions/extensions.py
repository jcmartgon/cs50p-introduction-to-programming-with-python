# Jesus Carlos Martinez Gonzalez
# 09/05/2023
# File Extensions


# Figure out a given file's media type (MIME)

def main():

    # Get input from user
    file = input("File: ").strip().lower()

    # Position of dot on file
    dot = file.rfind('.')

    # File extension
    ext = file[dot + 1:]

    match ext:
        case 'gif' | 'jpg' | 'jpeg' | 'png':
            if ext == 'jpg':
                ext = 'jpeg'
            print(f'image/{ext}')
        case 'pdf' | 'zip':
            print(f'application/{ext}')
        case 'txt':
            print('text/plain')
        case _:
            print('application/octet-stream')


main()