"""
Simple try of the agent.

@dev You need to add OPENAI_API_KEY to your environment variables.
"""

from browser_use_akimoto import Agent
from langchain_openai import ChatOpenAI
import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


llm = ChatOpenAI(model='gpt-4o')
agent = Agent(
    task='Give me top 3 favorite videos from youtube in Japan, this week',
    llm=llm,
)


async def main():
    await agent.run(max_steps=3)
    # agent.create_history_gif()


asyncio.run(main())
