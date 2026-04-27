import psycopg2
from config import config

def connection():
    return psycopg2.connect(**config)