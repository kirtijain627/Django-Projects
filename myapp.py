import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.get(url=URL, headers= headers, data = json_data)
    response = r.json()
    print(response)

# get_data(2)

#POST

def post_data():
    data = {
        'name':'Alia',
        'roll': 105,
        'city': 'Aurangabad'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    print(json_data)

    r = requests.post(url = URL, headers=headers, data = json_data)
    print("r=", r)
    data = r.json()
    print(data)
    print(type(data))

# post_data()

def update_data():
    data = {
        'id': 1,
        'city': 'Jaipur'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL, headers= headers,data = json_data)
    data = r.json()
    print(data)

# update_data()

def delete_data():
    data = {
        'id': 4,
    }
    
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)

# delete_data()



def checking_none(id1, id = None):
    if id is not None:
        id1 = id1
        print("id=",id)
        print("id1=",id1)
    else:
        print("id is none")

checking_none(1,2)

     



