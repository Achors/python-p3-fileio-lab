def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)

def read_file(file_name):
    try:
        with open(f'{file_name}.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None


# def write_file(file_name, file_content):
#     with open(file_name, 'w') as file:
#         file.write(file_content)

# def append_file(file_name, append_content):
#     with open(file_name, 'a') as file:
#         file.write(append_content)

# def read_file(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             return file.read()
#     except FileNotFoundError:
#         return None 
