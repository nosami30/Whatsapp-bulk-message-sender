import subprocess
import sys

def check_and_install(package):
    try:
        # Check if the package is installed
        subprocess.check_output([sys.executable, '-m', 'pip', 'show', package])
        print(f'{package} is already installed.')
    except subprocess.CalledProcessError:
        print(f'{package} is not installed. Installing...')
        # Install the package using pip
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f'{package} has been installed.')

def main():
    # List of packages to check and install
    packages = ['selenium', 'streamlit']

    for package in packages:
        check_and_install(package)
    print("Run the Web Page . . . ")
    execute_command = 'streamlit run .\\WebApp.py'
    subprocess.run(execute_command)

if __name__ == "__main__":
    main()
