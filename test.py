import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"name": "palinca", "grade": 55},
#     {"name": "whiskey", "grade": 40},
#     {"name": "vodka", "grade": 40},
#     {"name": "tequila", "grade": 36},
#     {"name": "tatra-tea", "grade": 80},
#     {"name": "absinthe", "grade": 65},
# ]
#
# for i in range(len(data)):
#     response = requests.put(BASE +"drink/" + str(i), data[i])
#     print(response.json())
# input()

response = requests.patch(BASE + "drink/2", {"name":"tuica", "grade": 42})
print(response)