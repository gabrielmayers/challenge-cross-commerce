import requests
import json
import numpy as np


def get_all_numbers():
    URL = "http://challenge.dienekes.com.br/api/numbers?page="
    all_numbers = []    
        
    i = 0

    while True:
        i += 1
        URL = URL + str(i)
        response = requests.get(URL)

        if response.text == '{"numbers":null}':
            break

        else:
            # transforme response in json to extract numbers:
            response = json.loads(response.text)

            # get numbers, put in array and store in a list
            all_numbers.append(np.array(response))
    
    return all_numbers
        


result = get_all_numbers()

print(result)

print(len(result))

# def val():
#     v = requests.get("http://challenge.dienekes.com.br/api/numbers?page=2")

#     print(type(v.text))


# val()