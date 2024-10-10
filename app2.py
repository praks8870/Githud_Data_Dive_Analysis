import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



def fetch_data():
    data = pd.read_csv('github_repos.csv')
    data['Creation_Date'] = pd.to_datetime(data['Creation_Date'])
    data['Last_Updated_Date'] = pd.to_datetime(data['Last_Updated_Date'])
    return data


st.set_page_config(page_title="GitHub Data Dive", layout="wide")


st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/GitHub_logo_White.svg/1024px-GitHub_logo_White.svg.png");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


tab1, tab2 = st.tabs(["$\huge Repositories$", "$\huge Analysis$"])

with tab1:
    st.sidebar.header("Filters")

    repos_data = fetch_data()

    languages = repos_data['Programming_Language'].unique().tolist()
    selected_language = st.sidebar.multiselect("Select Programming Language", options=languages, default=languages)
    
    filtered_data = repos_data[repos_data['Programming_Language'].isin(selected_language)]

    st.write("Filtered Repositories:", filtered_data)

    top_users = filtered_data.groupby('Owner')['Number_of_Stars'].sum().reset_index()
    top_users = top_users.sort_values(by='Number_of_Stars', ascending=False).head(10)

    fig = px.bar(top_users, x='Owner', y='Number_of_Stars', title="Top Users by Stars", color='Number_of_Stars')
    st.plotly_chart(fig)

with tab2:
    st.header("Analysis")

    # Select box for analysis questions
    question = st.selectbox(
        "Choose a question to analyze:",
        [
            "Top 10 repositories by number of stars",
            "Top 10 repositories by number of forks",
            "Top 10 programming languages used in repositories",
            "Monthly trend of repository creation and updates",
            "Top 5 licenses with the most repositories",
            "Top 5 programming languages with the most stars",
            "Top 10 months with the highest number of repositories created",
            "Distribution of repositories by programming language",
            "Comparison of stars vs. forks",
            "Top 5 repositories with the most open issues",
        ]
    )



    if question == "Top 10 repositories by number of stars":
        top_stars = repos_data.nlargest(10, 'Number_of_Stars')
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Number_of_Stars', y='Repository_Name', data=top_stars, palette='viridis')
        plt.title('Top 10 Repositories by Number of Stars')
        plt.xlabel('Number of Stars')
        plt.ylabel('Repository Name')
        st.pyplot(plt)

    elif question == "Top 10 repositories by number of forks":
        top_forks = repos_data.nlargest(10, 'Number_of_Forks')
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Number_of_Forks', y='Repository_Name', data=top_forks, palette='plasma')
        plt.title('Top 10 Repositories by Number of Forks')
        plt.xlabel('Number of Forks')
        plt.ylabel('Repository Name')
        st.pyplot(plt)

    elif question == "Top 10 programming languages used in repositories":
        top_languages = repos_data['Programming_Language'].value_counts().head(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_languages.values, y=top_languages.index, palette='magma')
        plt.title('Top 10 Programming Languages Used in Repositories')
        plt.xlabel('Number of Repositories')
        plt.ylabel('Programming Language')
        st.pyplot(plt)

    elif question == "Monthly trend of repository creation and updates":
        creation_trend = repos_data['Creation_Date'].dt.to_period("M").value_counts().sort_index()
        update_trend = repos_data['Last_Updated_Date'].dt.to_period("M").value_counts().sort_index()

        combined_trend = pd.DataFrame({
            'Created': creation_trend,
            'Updated': update_trend
        }).fillna(0)

        fig = px.line(combined_trend, x=combined_trend.index.astype(str), y=combined_trend.columns,
                       labels={'value': 'Count', 'index': 'Month'}, title='Monthly Trend of Repository Creation and Updates')
        st.plotly_chart(fig)

    elif question == "Top 5 licenses with the most repositories":
        license_counts = repos_data['License_Type'].value_counts().head(5)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=license_counts.values, y=license_counts.index, palette='cividis')
        plt.title('Top 5 Licenses with the Most Repositories')
        plt.xlabel('Number of Repositories')
        plt.ylabel('License Type')
        st.pyplot(plt)

    elif question == "Top 5 programming languages with the most stars":
        stars_by_lang = repos_data.groupby('Programming_Language')['Number_of_Stars'].sum().nlargest(5)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=stars_by_lang.values, y=stars_by_lang.index, palette='crest')
        plt.title('Top 5 Programming Languages with the Most Stars')
        plt.xlabel('Total Stars')
        plt.ylabel('Programming Language')
        st.pyplot(plt)

    elif question == "Top 10 months with the highest number of repositories created":
        creation_trend = repos_data['Creation_Date'].dt.to_period("M").value_counts().sort_values(ascending=False).head(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=creation_trend.values, y=creation_trend.index.astype(str), palette='viridis')
        plt.title('Top 10 Months with the Highest Number of Repositories Created')
        plt.xlabel('Number of Repositories')
        plt.ylabel('Month')
        st.pyplot(plt)

    elif question == "Distribution of repositories by programming language":
        language_distribution = repos_data['Programming_Language'].value_counts()
        fig, ax = plt.subplots(figsize=(10, 6))
        wedges, texts, autotexts = ax.pie(language_distribution, autopct='%1.1f%%', startangle=90)
        ax.legend(wedges, language_distribution.index, title="Programming Languages", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        ax.axis('equal')  
        st.pyplot(fig)

    elif question == "Comparison of stars vs. forks":
        comparison = repos_data[['Number_of_Stars', 'Number_of_Forks']].sum()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=comparison.values, y=comparison.index, palette='dark')
        plt.title('Comparison of Stars vs. Forks')
        plt.xlabel('Count')
        plt.ylabel('Type')
        st.pyplot(plt)

    elif question == "Top 5 repositories with the most open issues":
        top_issues = repos_data.nlargest(5, 'Number_of_Open_Issues')
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Number_of_Open_Issues', y='Repository_Name', data=top_issues, palette='pastel')
        plt.title('Top 5 Repositories with the Most Open Issues')
        plt.xlabel('Number of Open Issues')
        plt.ylabel('Repository Name')
        st.pyplot(plt)
