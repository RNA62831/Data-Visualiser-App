import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title = "Data Visualiser",
                   layout ="centered",
                    page_icon="📊")

#title
#st.title("📊 Data Visualiser")
st.markdown("<h1 style='text-align: center;'>📊 Data Visualiser</h1>", unsafe_allow_html=True)

downloads_folder = "C:/Users/ASUS/Downloads"
csv_files = [f for f in os.listdir(downloads_folder) if f.endswith(".csv")]
#selected_file = st.selectbox("Select a file", csv_files, index=None)
uploaded_file = st.file_uploader("Choose a file", type=["csv"])

# if selected_file:
#     #get complete path of the file
#     file_path = os.path.join(downloads_folder, selected_file)
#     #reading the file
#     df = pd.read_csv(file_path)
#
#     col1, col2 = st.columns(2)
#     with col1:
#         st.write("")
#         st.write(df.head())

if uploaded_file:
    # Read the uploaded file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    col1, col2 = st.columns(2)

    columns = df.columns.tolist()
    with col1:
        st.write(df.head())

    with col2:
        #user selction of cols
        x_axis = st.selectbox("Select the x axis", options = columns + ["None"], index=None)
        y_axis = st.selectbox("Select the y axis", options=columns + ["None"], index=None)

        plot_list = ["Line Plot", "Bar Chart", "Scatter Plot", "Distribution Plot", "Count Plot"]

        selected_plot = st.selectbox("Select a plot", options=plot_list, index=None)


#button to generat plots
    if st.button("Generate Plot"):
        fig, ax =plt.subplots(figsize = (6,4))
        if selected_plot == "Line Plot":
            sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
        elif selected_plot == "Bar Chart":
            sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
        elif selected_plot == "Scatter Plot":
            sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
        elif selected_plot == "Distribution Plot":
            sns.histplot(df[x_axis], kde=True, ax=ax)
        elif selected_plot == "Count Plot":
            sns.countplot(x=df[x_axis], ax=ax)

        #adjust label sizes
        ax.tick_params(axis="x", labelsize=10)
        ax.tick_params(axis="y", labelsize=10)

        #title
        plt.title(f"{selected_plot} of {y_axis} vs {x_axis}", fontsize=12)
        plt.xlabel(x_axis, fontsize=10)
        plt.ylabel(y_axis, fontsize=10)

        st.pyplot(fig)