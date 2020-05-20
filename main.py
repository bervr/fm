import sys
from code import create_file, create_folder, delete_file, copy_file, save_info, get_list, change_dir
# get_list()
save_info('Начало')
command = sys.argv[1]
if command== 'list':
    get_list()
elif command == 'create_file':
    try:
        name= sys.argv[2]
    except IndexError:
        print('задайте имя файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('задайте имя папки')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('задайте имя файла')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
    except IndexError:
        print('укажите имя файла')
    else:
        try:
            new_name = sys.argv[3]
        except IndexError:
            print('задайте новое имя файла')
        else:
            copy_file(name, new_name)
elif command =='cd':
    try:
        path = sys.argv[2]
    except IndexError:
        print('укажите путь')
    else:
        change_dir(path)

elif command == 'help':
    print('list -список файлов или папок')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удаление файла или папки')
    print('copy - копирование файла или папки')
    print('cd - сменить текущую директорию')

save_info('Конец')


