from crewai_tools import SerperDevTool

# CrewAI handles SerperDevTool internally
# Just reads SERPER_API_KEY from .env automatically
search_tool = SerperDevTool()