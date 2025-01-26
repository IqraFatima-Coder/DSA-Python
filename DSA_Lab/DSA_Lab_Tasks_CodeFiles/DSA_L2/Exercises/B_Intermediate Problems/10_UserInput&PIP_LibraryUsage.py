import subprocess
def install_package(package_name):
    try:
        subprocess.check_call(["pip", "install", package_name])
        print(f"Installing {package_name}...")
        print("Installation successful.")
    except subprocess.CalledProcessError:
        print("Installation failed.")
# Input
package_name = input("Package name: ")
# Install the package
install_package(package_name)
