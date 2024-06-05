This repo showcases a multi-agent private LLM from scratch, without using any of the pre-built agentic workflow libraries, such as CrewAI, AutoGen, etc. 

The LLM agents employ the 8B Llama3 model. Different form pre-built agentic workflows such as crewai with GPT models, which sends every single prompt to the OpenAI servres an will be used for future training/fine-tuning their models, we are now running LLM agents locally, so this is going to be a private agentic workflow.  

In this example, two agents are programmed, working as a writer agent which extrcats the private information from a sensitive file (a text file is fed into the agent as an example of a sensitive file) and a teacher agent, which explains the response of the first agent.  
