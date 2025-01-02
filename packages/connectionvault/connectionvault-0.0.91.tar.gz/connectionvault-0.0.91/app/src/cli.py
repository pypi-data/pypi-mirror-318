
from .connection_manager import main as conn_manage_main
import argparse
import os

# Hardcoded version information
VERSION = "0.0.91"

# Hardcoded dependencies information
DEPENDENCIES = {
    "python": "^3.11",
    "PyYAML": "^6.0.2",
    "SQLAlchemy": "^2.0.36",
    "psycopg2": "^2.9.10",
    "pandas": "^2.2.3",
    "pyodbc": "^5.2.0",
    "pylint": "^3.3.1"
}

# Hardcoded usage information
EXAMPLE = """

ENSURE YOU HAVE SET THE ENVIRONMENT VARIABLE 'conn_home' TO THE DIRECTORY WHERE YOUR connections.yaml FILE IS LOCATED.

sample usage:

from app.src.connection_utility import load_connections, choose_connection
from sqlalchemy import create_engine
import pandas as pd

def main():
    connections = load_connections()
    conn = choose_connection(connections)

    engine = create_engine(conn)
    query = input("Input your query: ")
    df = pd.read_sql_query(query, engine)
    print(df)

if __name__ == "__main__":
    main()```
"""

def main():
    parser = argparse.ArgumentParser(description='ConnectionVault CLI Tool')
    parser.add_argument('--version', action='version', version=f'ConnectionVault {VERSION}')
    parser.add_argument('--dependencies', action='store_true', help='Show project dependencies')
    parser.add_argument('--example', action='store_true', help='Show sample code syntax')
    parser.add_argument('--connections', action='store_true', help='Start connection manager utility')
    parser.add_argument('--yamldir', action='store_true', help='Show location of connection.yaml file')

    
    args = parser.parse_args()

    if args.dependencies:
        print("Project Dependencies:")
        for dep, version in DEPENDENCIES.items():
            print(f"{dep}: {version}")

    if args.example:
        print("Usage Information:\n")
        print(EXAMPLE)

    if args.connections:
        conn_manage_main()

    if args.yamldir:
        conn_home = os.getenv('conn_home')
        if conn_home:
            print(f"conn_home: {conn_home}")
        else:
            print("please set conn_home variable")

if __name__ == '__main__':
    main()



# below uses data from pyproject.toml, works well locally but needs external script to actually copy paste data while creating packages (*whl)


# import argparse
# import tomli

# def get_version():
#     with open('pyproject.toml', 'rb') as f:
#         config = tomli.load(f)
#         return config['tool']['poetry']['version']

# def get_dependencies():
#     with open('pyproject.toml', 'rb') as f:
#         config = tomli.load(f)
#         dependencies = config['tool']['poetry']['dependencies']
#         return dependencies

# def get_usage():
#     with open('README.md', 'r') as f:
#         return f.read()

# def main():
#     parser = argparse.ArgumentParser(description='ConnectionVault CLI Tool')
#     parser.add_argument('--version', action='version', version=f'ConnectionVault {get_version()}')
#     parser.add_argument('--dependencies', action='store_true', help='Show project dependencies')
#     parser.add_argument('--usage', action='store_true', help='Show usage information from README.md')
    
#     args = parser.parse_args()

#     if args.dependencies:
#         dependencies = get_dependencies()
#         print("Project Dependencies:")
#         for dep, version in dependencies.items():
#             print(f"{dep}: {version}")

#     if args.usage:
#         usage_info = get_usage()
#         print("Usage Information:\n")
#         print(usage_info)

# if __name__ == '__main__':
#     main()
