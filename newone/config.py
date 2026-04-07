from dotenv import load_dotenv
import os

load_dotenv()

SHOP_URL = os.getenv("SHOP_URL")
ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")