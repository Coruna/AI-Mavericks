#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://gpt-playground-us.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "ce0ffef736fd4531809bceb834768d68"

response = openai.ChatCompletion.create(
    engine="chatgpt", # engine = "deployment_name".
    max_tokens=10,
    temperature=0,
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
    messages=[
    {"role": "system", "content": "You are an assistant designed to analyze sentiment from speech data. Users will paste in a string of text nd you will respond with a number on a scale of 1-10 (10 being the best) for each of the following attributes: 'problem-solving competence', 'friendliness' and 'comprehensibility'."},
    {"role": "user", "content": "Customer: Hello, I'm having trouble connecting to the company's VPN. Can you help me? IT Support: Hi there, I'd be happy to assist you. Let's start by checking your network connection. Are you currently connected to the internet? Customer: Yes, I am connected to the internet. IT Support: Okay, next let's check if the VPN client is properly installed on your computer. Can you confirm that you have installed the VPN client? Customer: Yes, I have installed the VPN client.IT Support: Great, let's try restarting the VPN client and see if that helps. Can you please close the VPN client and open it again .Customer: Sure, let me do that. IT Support: Alright, now try to connect to the VPN. Are you able to connect now? Customer: Yes, it's working now! Thank you so much for your help. IT Support: You're welcome! I'm glad I could assist you. Is there anything else you need help with? Customer: No, that's all for now. Thank you again."},
    {"role": "assistant", "content": "Rating 5 - The IT support representative was incredibly helpful and patient in resolving my VPN connection issue. Thank you!"},
    {"role": "user", "content": "Customer: Hi, I'm having trouble with my printer. It's not working and I'm not sure what to do. IT Support: Hi there, I can assist you with that. Let's start by checking the printer's connection to your computer. Is the printer connected to your computer with a USB cable or is it a wireless printer? Customer: It's a wireless printer. IT Support: Alright, let's make sure the printer is connected to your Wi-Fi network. Can you check if the printer is connected to the Wi-Fi network? Customer: Yes, the printer is connected to the Wi-Fi network. IT Support: Okay, let's try uninstalling and reinstalling the printer driver. Can you please go to the manufacturer's website and download the latest driver for your printer model? Customer: Sure, let me do that. IT Support: Once you've downloaded the driver, please run the installation process. Let me know if you encounter any issues. Customer: The installation process is taking longer than I expected. Is this normal? IT Support: Yes, it can take a few minutes to install the driver, depending on your computer's specifications. Please be patient and let the installation process complete. Customer: Okay, it's finally done. The printer is working now. Thank you for your help. IT Support: You're welcome! Is there anything else you need assistance with?"},
    #{"role": "assistant", "content": "Rating 3 - The IT support was able to fix my printer issue, but it took longer than I expected. Communication could have been clearer."},
  #  {"role": "user", "content": "Customer: Hi, I am having trouble accessing the company software. Whenever I try to open it, it just keeps crashing. IT Support: Hi there, I'm sorry to hear that. Let's start by checking if your computer meets the system requirements for the software. Can you confirm that your computer meets the minimum system requirements for the software? Customer: Yes, my computer meets the minimum system requirements. IT Support: Okay, let's try uninstalling and reinstalling the software. Can you please uninstall the software and then download and install the latest version from the company's website? Customer: I have uninstalled and reinstalled the software multiple times, but it's still not working. IT Support: I'm sorry to hear that. In that case, let's try using an alternative solution. Can you try accessing the software from a different computer or from a different internet connection? Customer: I have tried accessing the software from a different computer and a different internet connection, but it's still not working. IT Support: I'm sorry to hear that the alternative solution did not work for you. Is there anything else I can do to assist you? Customer: No, I think I'll have to contact the software vendor for further assistance.?"},
   # {"role": "assistant", "content": "Rating 2 - The IT support person was not able to fix my issue, and the alternative solution provided was not helpful either."},
   # {"role": "user", "content": "Customer Hi, I'm having trouble with my email program. Every time I try to send an email, I get an error message saying that it can't be sent. IT Support: Have you tried restarting your computer? Customer: Yes, I've restarted my computer multiple times. It's still not working. IT Support: Okay, can you try deleting and re-adding your email account in the program? Customer: I've tried that too, and it didn't work. IT Support: Well, have you checked your internet connection? Customer: Yes, my internet connection is working fine. I can access other websites and programs without any problems. IT Support: Hmm, I'm not sure what else to try. Maybe you should just switch to a different email program. Customer: That's not a helpful solution. I need to use this program for work. IT Support: Well, I don't know what else to tell you. Maybe you should just try again later."},
]
)
#print(response)
print(response['choices'][0]['message']['content'])


#You are an assistant designed to analyze sentiment from speech data. Users will paste in a string of text and you will respond with an assessment of the response of the speaker. Rate on a scale of 1-10 (10 being highest). Explain why this rating was given.