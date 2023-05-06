# Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
import json

openai.api_type = "azure"
openai.api_base = "https://gpt-playground-us.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "ce0ffef736fd4531809bceb834768d68"

# data = [
# {"role": "system", "content": "You are a helpful assistant."},
# {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
#  {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
#  {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}]

data = [
    {"role": "system",
     "content": "you will rate the response of the customer support on a scale of 1-10(10 being the highest) for the following criterias: problem-solving skills; friendliness; Professionalism; understandability. Furthermore, give some tips to improve customer support experience. Output format should be a json file as follows :{\"Problem Solving Skills\":\"\", \"Friendliness\":\"Professionalism\":\"\",\"Understandability\":\"\", \"Tips\":[]"},
    {"role": "user",
     "content": "hi thank you for calling contoso pharmacy who am i speaking with today i understand your frustration mary um can you tell me what exactly you're trying to accomplish OK uh certainly happy to check that for you one moment please i see here that you were on a generic form of lipitor is that right OK uh so i see that your doctor stopped prescribing these drugs in twenty twenty one actually OK uh yeah i'd be happy to check that for you uh because sometimes there's a gap in the system and it just doesn't get reported so let me take a look here just a moment so i'm seeing here that your doctor had these drugs prescribed to you from twenty twelve through twenty twenty one OK um yeah according to the latest records uh provided by doctor's office you're now on a different drug metformin would you like us to go ahead and fill that prescription for you for pick up a bit of form in five hundred milligrams uh you're very welcome mary please let us know if there's anything else we can do for you today."},
    {"role": "assistant",
     "content": "{\"Problem Solving Skills\":\"8\", \"Friendliness\": \"10\", \"Professionalism\": \"9\",\"Understandability\":\"9\", \"Tips\":[\"Good job!\", \"Keep up the good work!\"]"},
    {"role": "user",
     "content": "hi okay did you try resetting your password sorry i can't do that no sorry you'll have to figure it out yourself no there's no one else available right now you'll have to call back later sorry i can't do anything for you have a nice day"},
    {"role": "assistant",
     "content": "{\"Problem Solving Skills\":\"1\", \"Friendliness\": \"1\", \"Professionalism\": \"1\",\"Understandability\":\"9\", \"Tips\":[\"It can be frustrating dealing with difficult customers, but it's important to remain patient and courteous in all interactions\", \"Try to actively listen to their concerns and validate their feelings\", \"End the conversation on a positive note by thanking the customer for their time and offering any additional assistance they might need\"]"},
    {"role": "user",
     "content": "hello thank you for reaching out to our customer support team my name is john and i'll be happy to assist you today i understand you're having an issue with your account let me take a look here and see what i can do to help you based on the information you've provided it looks like your account has been temporarily suspended due to a security concern in order to reactivate your account we'll need you to go through a few security verification steps i apologize for any inconvenience this may cause but it's for the protection of your account i can guide you through the verification process step-by-step if you're ready please have your account information ready and let me know when you're ready to proceed thank you for your patience and understanding."}
]

with open("conversation.json", "w") as f:
    json.dump(data, f)

response = openai.ChatCompletion.create(
    engine="chatgpt",  # engine = "deployment_name".
    messages=data
)

# print(response)
#print(response['choices'][0]['message']['content'])

data = response['choices'][0]['message']['content']
data = data.replace('\\', '')
print(data)

with open('assessment.json', 'w') as file:
    json.dump(data, file)


