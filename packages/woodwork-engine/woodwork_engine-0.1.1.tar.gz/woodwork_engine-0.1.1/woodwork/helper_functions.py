import importlib
import os

from woodwork.globals import global_config as config


def set_globals(**kwargs) -> None:
    for key, value in kwargs.items():
        config[key] = value


def print_debug(*args: any) -> None:
    if config["mode"] == "debug":
        print(*args)


def import_all_classes(package_name: str) -> bool:
    # Get the package path
    package = importlib.import_module(package_name)
    package_path = package.__path__[0]

    # Traverse directories and import all .py files as modules
    imported_all = True
    for root, _, files in os.walk(package_path):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                # Derive the full module path
                relative_path = os.path.relpath(root, package_path)
                print("RELPATH =", relative_path)
                module_name = os.path.splitext(file)[0]

                if relative_path == ".":
                    full_module_name = f"{package_name}.{module_name}"
                else:
                    full_module_name = f"{package_name}.{relative_path.replace(os.path.sep, '.')}.{module_name}"

                # Import the module
                try:
                    importlib.import_module(full_module_name)
                except ImportError as e:
                    print(f"Could not import {full_module_name}: {e}")
                    imported_all = False

    return imported_all
