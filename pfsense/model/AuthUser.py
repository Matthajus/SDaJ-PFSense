from dotenv import load_dotenv
import os


def get_auth_user():
    load_dotenv()
    return {
        'host': os.getenv('PF_HOST'),
        'user': os.getenv('PF_USER'),
        'password': os.getenv('PF_PASSWORD'),
        'verify': os.getenv('PF_VERIFY'),
        'port': os.getenv('PF_PORT')
    }
