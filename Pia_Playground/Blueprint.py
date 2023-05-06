import os
import requests
import json
import openai

openai.api_key = "XXXX"
openai.api_base =  "https://gpt-playground-us.openai.azure.com/" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2022-12-01' # this may change in the future

deployment_name='chatgpt' #This will correspond to the custom name you chose for your deployment when you deployed a model.

# Send a completion call to generate an answer
print('Ask your question, fellow!')
while True:
    start_phrase = "Give me a list of cute dog breeds i can look up on the internet"
    stop = input()
    #start_phrase = input()
    response = openai.Completion.create(engine=deployment_name, prompt=start_phrase, max_tokens=100, temperature=1)
    answer = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
    #answer = response
    print(answer)
