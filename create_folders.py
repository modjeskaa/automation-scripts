import os

def create_folders():
    input_path = input("Folder destination:\n(for example: C:\\Users\\AgataPC\\DesC:\ktop)\n")
    base_path = input_path.replace("\\", "\\\\")

    choice = int(input("1. Create x number of folders\n2. Create folders with names\nEnter 1 or 2: "))

    if choice == 1:
        num_folders = int(input("Number of folders to create: "))
        folder_list = [f"folder_{i}" for i in range(1, num_folders + 1)]

        for folder_name in folder_list:
            folder_path = os.path.join(base_path, folder_name)
            os.mkdir(folder_path)
        
        print("Folders created")

    elif choice == 2:
        folder_names_input = input("Folder names (comma-separated): ")
        folder_names = [name.strip() for name in folder_names_input.split(',')]

        for folder_name in folder_names:
            folder_path = os.path.join(base_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)
        
        print("Folders created")

create_folders()
