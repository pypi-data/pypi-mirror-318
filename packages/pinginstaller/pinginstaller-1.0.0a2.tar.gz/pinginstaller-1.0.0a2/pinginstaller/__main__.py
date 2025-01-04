
import os, sys

# Add 'pingwizard' to the path, may not need after pypi package...
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PACKAGE_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.append(PACKAGE_DIR)

def main():

    yml = os.path.join(SCRIPT_DIR, "PINGMapper.yml")

    from pinginstaller.Install_Update_PINGMapper import install_update
    install_update(yml)

    return

if __name__ == '__main__':
    main()