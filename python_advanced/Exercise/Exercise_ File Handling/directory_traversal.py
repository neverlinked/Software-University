from os import listdir, path


def traverse_dir(current_path, files_by_ext):
    for element in listdir(current_path):
        if path.isdir(path.join(current_path, element)):
            traverse_dir(path.join(current_path, element))
        else:
            extension = element.split('.')[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(element)


files_by_extension = {}
traverse_dir('.', files_by_extension)

for extension, files in sorted(files_by_extension.items()):
    print(f'.{extension}')
    for file in sorted(files):
        print(f'- - - {file}')
