# MeLi Application - Lautaro Diana

## Overview
This is an application done as a response to the MeLi test, for consideration on Level 2. The app was conceived in two stages

- The first stage was the offline app (the `mutant.py` in the Git repository), which consists in a script that contains the `is_mutant` function. Given a list of strings that have only the letters 'A', 'T', 'C' and 'G' (for the sake of the test example, called `dna`, noting that if the list has a N length, every string should have N elements, making an array of NxN dimensions), our function returns a boolean value, which is `True` in the case of having four or more letters in line, in any direction, and `False` in any other case.
- The second stage was the deployment of the app, which can be found in this link: http://18.117.99.231:5000/. Our online app was built with Flask, a Python microframework to build web apps. For the deploy, AWS EC2 was used.

## How to use it

Our MeLiApp has two routes:

- `'/'`, which is the default route, which displays only the message "Meli Application - Lautaro Diana"
- `'/mutant/'`, which is the endpoint where, through a POST request, we can send a JSON object `dna` which should have this structure:
```
{
    "dna" : ['ATGCGA', 'CAGTGC', 'TTATTT', 'AGACGG', 'GCGTCA', 'TCACTG']
}
```
In the case that, for the sake of the example, the dna requested belongs to a mutant (that is, in the case that we have at least four or more equal letter in line in any direction), the request will return a `Response [200]`. In opposite case, it'll return a `Response [403]`.

### Python example

Here we have a little Python script, which it was used to test the application:
```
import requests, json

url = 'http://18.117.99.231:5000/mutant'

response = requests.post(
    url, 
    json = {"dna" : #Example array }
)

print(response)
```

For a `True` example, we can send:
```
import requests, json

url = 'http://18.117.99.231:5000/mutant'

response = requests.post(
    url, 
    json = {"dna" : ['ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG']}
)

print(response)
```
That will print on console:
```
<Response [200]>
```
Now, for a `False` case:
```
import requests, json

url = 'http://18.117.99.231:5000/mutant'

response = requests.post(
    url, 
    json = {"dna" : ['ATGCGA', 'CAGTGC', 'TTATTT', 'AGACGG', 'GCGTCA', 'TCACTG']}
)

print(response)
```
Which return:
```<Response [403]>```
