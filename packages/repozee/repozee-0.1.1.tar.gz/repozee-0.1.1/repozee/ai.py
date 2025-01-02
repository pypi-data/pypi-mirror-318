import os
from pathlib import Path
from datetime import date
import sys
import yaml

import anthropic
from jinja2 import Template

from repozee import load_definition
from repozee.projectdir import ProjectDir


class AI:

    tools = yaml.safe_load(load_definition('tools.yml'))
    system_prompt = load_definition('system.md')
    user_prompt = Template(load_definition('user.md'))

    def __init__(self, directory):

        self.directory = directory
        self.client = anthropic.Anthropic()
        self.messages = []
        self.projectdir = ProjectDir(directory)

    def ask_ai(self):
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            temperature=0,
            system=self.system_prompt,
            messages=self.messages,
            tools=self.tools)
        return message

    def loop(self):
        while True:
            print('-'*80)
            if self.messages:
                question = input("\nYou: ").strip()
                print()
            else:
                question = "List"
            self.messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": self.user_prompt.render(
                                question=question,
                                today=date.today())
                        }
                    ]
                }
            )
            message = self.ask_ai()
            while self.messages[-1]['role'] != 'assistant':
                for content in message.content:
                    if content.type == 'text':
                        print(content.text)
                        print()
                        self.messages.append({
                            "role": "assistant",
                            "content": content.text
                        })
                    elif content.type == 'tool_use':
                        if content.name == 'quit':
                            return
                        else:
                            tool = getattr(self.projectdir, content.name)
                            self.messages.append({
                                "role": "assistant",
                                "content": [dict(content)]
                            })
                            id = content.id
                            result = str(tool(**content.input))
                            self.messages.append({
                                "role": "user",
                                "content": [{
                                    "type": "tool_result",
                                    "tool_use_id": id,
                                    "content": result
                                }]
                            })
                            message = self.ask_ai()
