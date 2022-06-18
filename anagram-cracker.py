#!/usr/bin/python3
#Author: IRISON
#Date: 18-06-2022
from itertools import permutations
import requests

url = "https://twinword-word-graph-dictionary.p.rapidapi.com/definition/"
headers = {
	"X-RapidAPI-Key": "your_own_API_KEY",
	"X-RapidAPI-Host": "twinword-word-graph-dictionary.p.rapidapi.com"
}
word = input("what is the word you want to form combinations from\n")
permList = permutations(word)
for perm in list(permList):
    new_word = ''.join(perm)
    querystring = {"entry": new_word}
    response = requests.request("GET", url, headers=headers, params=querystring)
    jsonresponse = response.json()
    if "Entry word not found" not in jsonresponse["result_msg"]:
        print(new_word + " = " + jsonresponse["meaning"]['noun'].split("(nou)")[1].split(";")[0])
