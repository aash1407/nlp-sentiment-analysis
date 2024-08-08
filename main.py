from io import StringIO

import plotly.express as px
import streamlit as st
import utils
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s '
                                               '- %(message)s')

DIARY_PATH = "diary/*.txt"


def main():

    st.set_page_config(page_title="Diary Sentiment Analysis",
                       page_icon="📊")

    st.header("Diary Sentiment Analysis")
    st.write("Upload your diary files in simple txt format to analyze the "
             "sentiment over time (find sample txts in git project).")

    uploaded_files = st.file_uploader("Choose diary files...",
                                      accept_multiple_files=True, type=["txt"])
    positivity = []
    negativity = []
    dates = []

    try:
        for uploaded_file in uploaded_files:
            content = StringIO(uploaded_file.getvalue().decode("utf-8")).read()
            score = utils.get_sentiment(content)
            positivity.append(score["pos"])
            negativity.append(score["neg"])
            dates.append(uploaded_file.name.strip(".txt"))
        if uploaded_files:
            st.subheader("Positivity")
            pos_graph = px.line(x=dates, y=positivity,
                                labels={"x": "Date", "y": "Positivity"})
            neg_graph = px.line(x=dates, y=negativity,
                                labels={"x": "Date", "y": "Negativity"})

            st.plotly_chart(pos_graph)
            st.subheader("Negativity")
            st.plotly_chart(neg_graph)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
