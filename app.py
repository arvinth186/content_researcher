import streamlit as st
from dotenv import load_dotenv
import sys

sys.path.insert(0, "src/content_researcher")
load_dotenv()

from crew import ContentResearcherCrew

st.set_page_config(
    page_title="Content Researcher AI",
    page_icon="📰",
    layout="wide"
)

st.title("📰 Multi-Agent Content Research & Writing")
st.caption("Research Agent → Fact Check Agent → Writer Agent → Editor Agent")
st.divider()

topic = st.text_input(
    "Enter a topic to research",
    placeholder="e.g. Impact of AI on healthcare in 2025"
)

if st.button("🔍 Research & Write", type="primary", use_container_width=True):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        with st.spinner("🤖 Agents working..."):
            status = st.empty()

            status.info("🔍 Research Agent gathering sources...")
            try:
                result = ContentResearcherCrew().crew().kickoff(
                    inputs={"topic": topic}
                )
                status.success("✅ Article ready!")
                st.divider()
                st.subheader(f"📄 {topic}")
                st.caption(f"~{len(str(result).split())} words")
                st.markdown(str(result))
                st.download_button(
                    "⬇️ Download Article",
                    data=str(result),
                    file_name=f"{topic[:30].replace(' ','_')}.md",
                    mime="text/markdown"
                )
            except Exception as e:
                status.error(f"Error: {str(e)}")

st.divider()
st.caption("Built with CrewAI + Streamlit")