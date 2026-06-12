from dotenv import load_dotenv
from src.content_researcher.crew import ContentResearcherCrew
import traceback

load_dotenv()


def generate_article(topic: str):
    try:
        result = ContentResearcherCrew().crew().kickoff(
            inputs={"topic": topic}
        )

        return {
            "success": True,
            "article": str(result)
        }

    except Exception as e:
        print(traceback.format_exc())

        return {
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }















# from dotenv import load_dotenv
# from src.content_researcher.crew import ContentResearcherCrew
# import traceback

# load_dotenv()

# def generate_article(topic: str):

#     # result = (
#     #     ContentResearcherCrew()
#     #     .crew()
#     #     .kickoff(
#     #         inputs={
#     #             "topic": topic
#     #         }
#     #     )
#     # )

#     # return str(result)
    
#     try:
#         result = ContentResearcherCrew().crew().kickoff(inputs={"topic": topic})

#         return {
#             "success": True,
#             "article": str(result)
#         }

#     except Exception as e:
#          print(traceback.format_exc())
#         return {
#             "success": False,
#             "error": str(e),
#             "traceback": traceback.format_exc()
#         }
