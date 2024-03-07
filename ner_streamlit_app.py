import streamlit as st
import spacy
from spacy import displacy
import pandas as pd
import time  # For simulating a loading animation

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Set page config for a better look
st.set_page_config(page_title="Advanced NER App", page_icon="🔍", layout="wide")

def analyze_text(text):
    # Simulate a loading effect
    for percent_complete in range(100):
        time.sleep(0.01)
    doc = nlp(text)
    html = displacy.render(doc, style="ent")
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return html, entities

# Sidebar settings
st.sidebar.header("Settings")
entity_filter = st.sidebar.multiselect(
    "Entities to display",
    options=["PERSON", "ORG", "GPE", "DATE", "TIME", "MONEY", "QUANTITY", "ORDINAL", "CARDINAL"],
    default=["PERSON", "ORG", "GPE"]
)

# Adding GitHub icon with hyperlink to the sidebar
st.sidebar.markdown(
    """
    [![GitHub](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)](https://github.com/Bhavesh007Sharma)
    """,
    unsafe_allow_html=True,
)

# NLP Explainer in an expander
with st.expander("What is Named Entity Recognition (NER)?"):
    st.write("""
        Named Entity Recognition (NER) is a process in NLP that identifies named entities in text and classifies them into predefined categories, such as the names of persons, organizations, locations, expressions of times, quantities, monetary values, percentages, etc.
        This technology is key to building applications like chatbots, search engines, and systems for legal document analysis and news aggregation.
    """)

# Main app
st.title("Interactive NER with spaCy and Streamlit")
st.subheader("Type or paste your text below:")
user_input = st.text_area("", "Sam works at OpenAI in California.", height=150)

if st.button("Analyze Text"):
    with st.spinner("Analyzing text..."):
        analyzed_html, entity_list = analyze_text(user_input)
        entities_df = pd.DataFrame(entity_list, columns=["Entity", "Type"])
        filtered_df = entities_df[entities_df["Type"].isin(entity_filter)]

    st.subheader("Highlighted Entities")
    st.markdown(analyzed_html, unsafe_allow_html=True)
    
    st.subheader("Entity Details")
    st.dataframe(filtered_df)
else:
    st.info("Click the 'Analyze Text' button to start the NER process.")

# Theming and adding a simple CSS animation for text analysis
st.markdown("""
<style>
@keyframes fadeIn {
    0% {opacity: 0;}
    100% {opacity: 1;}
}
.stApp {
    background-color: #fafafa;
    animation-name: fadeIn;
    animation-duration: 1.5s;
}
</style>
""", unsafe_allow_html=True)
