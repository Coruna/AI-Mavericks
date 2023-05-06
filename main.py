#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
import json
openai.api_type = "azure"
openai.api_base = "https://gpt-playground-us.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "ce0ffef736fd4531809bceb834768d68"




data = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
    {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
    {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}
]

with open("conversation.json", "w") as f:
    json.dump(data, f)

response = openai.ChatCompletion.create(
    engine="chatgpt", # engine = "deployment_name".
    messages=data
)

print(response)
print(response['choices'][0]['message']['content'])
