#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://gpt-playground-us.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "xxxxxx"

response = openai.ChatCompletion.create(
    engine="chatgpt", # engine = "deployment_name".
   # messages=[
   #     {"role": "system", "content": "You are an assistant designed to analyze sentiment from speech data. Users will paste in a string of text and you will answer 'positive', 'negative', or 'neutral' depending on the mood of the statement."},
   #     {"role": "user", "content": " I should post some photos of my robots  ok - offline for 4 hours now. ttfn (oh, so IM...)"},
   #     {"role": "assistant", "content": "neutral"},
   #     {"role": "user", "content": " hahahah of course  they have such a nasty display picture :`)"},
   #     {"role": "assistant", "content": "negative"},
   #     {"role": "user", "content": "the fact my room is so hot is making me feel sick"},
   #     {"role": "assistant", "content": "negative"},
   #     {"role": "user", "content": " I LLLOOOVVVEEE ICARLY"},
   #     {"role": "assistant", "content": "positive"},
   #     {"role": "user", "content": "  hope your day gets better soon!!"},
   #     {"role": "assistant", "content": "positive"},
   #     {"role": "user", "content": "melissa_leah: my car wont start......."},
    #]
    messages=["data/messages.json"]
)

#print(response)
print(response['choices'][0]['message']['content'])
print(type(messages))