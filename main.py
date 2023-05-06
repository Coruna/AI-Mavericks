#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://gpt-playground-us.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "cXXXXXXX"

response = openai.ChatCompletion.create(
    engine="chatgpt", # engine = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure Cognitive Services support this too?"},
        {"role": "assistant", "content": "Yes, other Azure Cognitive Services also support customer managed keys. Azure Cognitive Services is designed to allow you to use your own encryption keys for protecting your data at rest. By using customer managed keys, you can have greater control over the keys that are used to encrypt your data, and you can keep the keys secure in your own key vault."},
        {"role": "user", "content": "Are those managed key secured stored?"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])
