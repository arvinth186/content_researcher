from dotenv import load_dotenv
from src.content_researcher.crew import ContentResearcherCrew

load_dotenv()

def generate_article(topic: str):

    # result = (
    #     ContentResearcherCrew()
    #     .crew()
    #     .kickoff(
    #         inputs={
    #             "topic": topic
    #         }
    #     )
    # )

    # return str(result)
    
    try:
        result = ContentResearcherCrew().crew().kickoff(inputs={"topic": topic})

        return {
            "success": True,
            "article": str(result)
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
