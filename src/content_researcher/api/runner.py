from dotenv import load_dotenv
from src.content_researcher.crew import ContentResearcherCrew
import traceback
import time

load_dotenv()

def generate_article(topic: str, max_retries: int = 3):
    for attempt in range(max_retries):
        try:
            result = ContentResearcherCrew().crew().kickoff(
                inputs={"topic": topic}
            )
            return {
                "success": True,
                "article": str(result)
            }
        except Exception as e:
            error_str = str(e)
            # If rate limited, wait and retry
            if "rate_limit_exceeded" in error_str and attempt < max_retries - 1:
                wait_time = 60  # wait 60 seconds for TPM window to reset
                print(f"Rate limited. Waiting {wait_time}s before retry {attempt + 2}/{max_retries}...")
                time.sleep(wait_time)
                continue
            # Any other error, return immediately
            print(traceback.format_exc())
            return {
                "success": False,
                "error": error_str,
                "traceback": traceback.format_exc()
            }
