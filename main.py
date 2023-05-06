import os
import openai
import json
import azure.cognitiveservices.speech as speechsdk
#--------------OPENAI CONFIG--------------------
openai.api_type = "azure"
openai.api_base = "https://gpt-playground-us.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "ce0ffef736fd4531809bceb834768d68"
#--------------------NEEDED GLOBAL VARIABLES------------------------
speechdata = "./cleaned_text.json" #cleaned data from voice input
masterjson = "data_endg.json" #master json

def talk_to_chatgpt ():
    with open('data_endg.json') as json_file:
        data = json.load(json_file)

    response = openai.ChatCompletion.create(
        engine="chatgpt", # engine = "deployment_name".
     messages=data
    )

    print(response['choices'][0]['message']['content'])


def add_speech_to_json (speechdata, masterjson):
    with open(speechdata) as json_file:
        data = json.load(json_file)
    new_data = {"role": "user", "content": data}

    def write_json(new_data, masterjson):
        with open(masterjson,'r+') as file:
          # First we load existing data into a dict.
            file_data = json.load(file)
        # Join new_data with file_data inside emp_details
            file_data.append(new_data)
        # Sets file's current position at offset.
            file.seek(0)
        # convert back to json.
            json.dump(file_data, file, indent = 4)
     
    write_json(new_data, masterjson)

add_speech_to_json(speechdata, masterjson)