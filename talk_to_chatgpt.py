import os
import requests
import json
import openai

openai.api_key = "XXXXXX"
openai.api_base =  "https://XXXX.openai.azure.com/" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
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
    with open("output.txt", "a") as f:
        print(answer, file=f)



#It is always a number between 0 and 1.
#A temperature of 0 means the responses will be very straightforward, almost deterministic (meaning you almost always get the same response to a given prompt)
#A temperature of 1 means the responses can vary wildly.
