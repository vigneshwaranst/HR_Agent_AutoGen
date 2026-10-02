from dotenv import load_dotenv
load_dotenv()

import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Set up the OpenAI model client
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini") 

# Create the AssistantAgent with the exact system message
agent = AssistantAgent(
    name="hr_assistant", 
    model_client=model_client,
    system_message="You are an HR assistant."
)

async def main():
    # We specify "five bullet points" so the model clearly understands what "5 lines" means
    task_prompt = "Write a 5-line job description for a Junior Python Developer. Please format it as exactly five bullet points."
    
    # Run the agent and stream the output to the console
    await Console(agent.run_stream(task=task_prompt))
    
    # Close the model client when done so the script doesn't hang
    await model_client.close()

# Run the async function
asyncio.run(main())