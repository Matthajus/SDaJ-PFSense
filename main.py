from dotenv import load_dotenv
import os
from pfsense.service.w3sa_convertor import parse_w3sa_json_file


def load_credential():
    # Load environment variables from .env file
    load_dotenv()

    # Access the environment variables
    print(os.getenv('DB_HOST'))
    print(os.getenv('DB_USER'))
    print(os.getenv('DB_PASSWORD'))
    print(os.getenv('DB_SCHEMA'))

    print(os.getenv('PF_HOST'))
    print(os.getenv('PF_USER'))
    print(os.getenv('PF_PASSWORD'))
    print(os.getenv('PF_VERIFY'))


if __name__ == '__main__':

    load_credential()
    w3sa_data = parse_w3sa_json_file('w3sa_priklad_pre_vlan196.json')

    for item in w3sa_data:
        print(item)
