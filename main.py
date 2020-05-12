import sys
from code import create_file, create_folder, delete_file, copy_file, save_info, get_list
# get_list()
command = sys.argv[1]
if command== 'list':
    get_list()
elif command == 'create_file':
    pass
elif command == 'create_folder':
    pass
elif command == 'delete':
    pass
elif command == 'copy':
    pass
elif command == 'help':
    print(' Ну что, помогло?')

