# A multi-agent private LLM from scratch, without any pre-built agentic workflow libraries 

#First go to https://ollama.com/download to be able to use llama3 model. 
#then open a terminal and run this command, which takes time to downlaod the llama3 model, the 8B parameters (4.7G) version:
# https://ollama.com/library/llama3 

## ollama run llama3 

# Then after the download is completed, run the following command in anaconda prompt terminal to install ollama

## pip install ollama

import ollama 

with open('sensitive_info.txt', 'r') as file:
    data = file.read()
print()


if data:
    print("File loaded successfully.")
else: 
    print("Loading failed.")
print()
 

#### The point is that different form GPT models of OpenAI which sends every single of our promts to the OpenAI servres an will be used for future 
# training/fine-tuning their models, we are now running an LLM locally, so this is going to be a private agent. 


# set the first prompt for the first private agent 
prompt_01 = f"{data} #### from this text, extract two main items in the provided text."
print("<agent_01> is generating the response...")
print()


#response = ollama.chat(model = "llama3", messages = [
#    {
#        "role": "user",
#        "content": "I want to know more about private AI Agents",
#
#    }
#])

response_01 = ollama.chat(model = "llama3", messages = [
    {
        "role": "user",
        "content": prompt_01,
    }
])

print(response_01["message"]["content"])



####### now the second agent: 

prompt_02 = f"{response_01['message']['content']} #### Explain this in a simple, clear way. Be concise." 
# this mimics the role of a teacher agent :) 
 
  
#print("<agent_02> Prompt: " + prompt_02)
#print()
print("<agent_02> is generating the response...")
print()

response_02 = ollama.chat(model = "llama3", messages = [
    {
        "role": "user",
        "content": prompt_02,
    }
])

print("<agent_02> Response: " + response_02['message']['content']) 