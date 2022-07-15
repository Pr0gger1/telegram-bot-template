from dotenv import load_dotenv
import os

__env_file = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(__env_file):
    load_dotenv(__env_file)

TOKEN = os.environ.get("TOKEN")