import requests

# function
def lambda_handler(event, context):
    x = requests.get('https://w3schools.com/python/demopage.htm')
    print(x.text)
