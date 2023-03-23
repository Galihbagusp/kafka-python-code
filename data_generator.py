import requests
import random

list_id = list(range(1,30))
def get_message_product():
    random_id = random.choice(list_id)
    # get data from dummyjson    
    url = f'https://dummyjson.com/products/{random_id}'
    response = requests.get(url)
    data = response.json()
    # only return 'id', 'title', and 'description' 
    return {
        'id' : data['id'],
        'title' : data['title'],
        'description': data['description']
    }

def get_message_users():
    random_id = random.choice(list_id)
    # get data from dummyjson
    url = f'https://dummyjson.com/users/{random_id}'
    response = requests.get(url)
    data = response.json()
    # only return 'first name', 'last_name'
    return {
        'firstName': data['firstName'],
        'lastName': data['lastName'],
        'age': data['age'],
        'gender': data['gender'],
        'email' : data['email']
    }