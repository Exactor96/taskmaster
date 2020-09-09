import os


class Config:
    MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb+srv://root:root@localhost/')
