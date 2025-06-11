"""Example: RAG-powered research agent."""

from praison import Agent
from praison.tools import document_search

agent = Agent(
    name='rag_researcher',
    role='Document Analyst',
    goal='Answer questions using provided documents',
    tools=[document_search],
    memory=True
)

# Load documents
agent.load_documents('./research_papers/')

# Query
result = agent.run('Summarize the key findings across all papers')
print(result)
