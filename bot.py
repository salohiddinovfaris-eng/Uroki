from dotenv import load_dotenv
import os

load_dotenv()

vk_token = os.getenv('VK_TOKEN')

if vk_token:
    print('Токен есть')

else:
    print('Токена нет')