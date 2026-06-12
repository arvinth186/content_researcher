from dotenv import load_dotenv
from src.content_researcher.crew import ContentResearcherCrew

load_dotenv()

def run(topic: str):
    inputs = {
        "topic": topic
    }
    result = ContentResearcherCrew().crew().kickoff(inputs=inputs)
    return result


if __name__ == "__main__":
    print(run("The future of renewable energy"))