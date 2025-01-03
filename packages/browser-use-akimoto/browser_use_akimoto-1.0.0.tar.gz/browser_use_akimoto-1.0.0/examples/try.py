"""
Simple try of the agent.

@dev You need to add ANTHROPIC_API_KEY to your environment variables.
"""

import os
import sys

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse
import asyncio

from browser_use_akimoto import Agent
from browser_use_akimoto.browser.browser import Browser, BrowserConfig
from browser_use_akimoto.controller.service import Controller


def get_llm(provider: str):
	if provider == 'anthropic':
		return ChatAnthropic(
			model_name='claude-3-5-sonnet-20240620', timeout=25, stop=None, temperature=0.0
		)
	elif provider == 'openai':
		return ChatOpenAI(model='gpt-4o', temperature=0.0)
	else:
		raise ValueError(f'Unsupported provider: {provider}')


task = 'Show the solution of y"(z) + sin(y(z)) = 0 from wolframalpha https://www.wolframalpha.com/'


parser = argparse.ArgumentParser()
parser.add_argument('--query', type=str, help='The query to process', default=task)
parser.add_argument(
	'--provider',
	type=str,
	choices=['openai', 'anthropic'],
	default='openai',
	help='The model provider to use (default: openai)',
)

args = parser.parse_args()

# llm = get_llm(args.provider)
llm = get_llm('anthropic')


browser = Browser(
	config=BrowserConfig(
		# chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)

# hard code here for debuggability
# task = """以下の作業を順番に行ってください。
# 				1 Google Mapを開く。
# 				2 妙蓮寺駅周辺の歯医者を日本語で検索する。
# 				3 結果の歯医者の名前をすべて赤文字に変更する。
# 				"""

task = "次のULRを開いて、一覧のリストを一番下までスクロールしてください。 https://www.google.com/maps/search/%E5%A6%99%E8%93%AE%E5%AF%BA%E9%A7%85+%E6%AD%AF%E5%8C%BB%E8%80%85/@35.4975744,139.640832,14z?hl=ja&entry=ttu&g_ep=EgoyMDI0MTIxMS4wIKXMDSoASAFQAw%3D%3D"

agent = Agent(
	task=task, llm=llm, controller=Controller(), browser=browser, validate_output=True
)




async def main():
	await agent.run(max_steps=25)

	await browser.close()


asyncio.run(main())
