# Quick Start Guide

## Installation
```bash
pip install praison
```

## Create Your First Agent
```python
from praison import Agent

agent = Agent(
    name='researcher',
    role='Research Assistant',
    goal='Find and summarize information',
    llm='gpt-4'
)

result = agent.run('What are the latest developments in multi-agent AI?')
print(result)
```

## Multi-Agent Example
```python
from praison import Agent, Team

researcher = Agent(name='researcher', role='Research')
writer = Agent(name='writer', role='Content Writer')

team = Team(agents=[researcher, writer])
output = team.run('Write a blog post about autonomous AI agents')
```
