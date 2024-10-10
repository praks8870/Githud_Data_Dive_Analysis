# GitHub Data Dive

## Overview

The **GitHub Data Dive** project analyzes and visualizes data from GitHub repositories, providing insights into programming languages, repository trends, and other key metrics. This project utilizes Streamlit for the web application, alongside libraries like Pandas, Matplotlib, Seaborn, and Plotly for data manipulation and visualization.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Analysis Questions](#analysis-questions)
- [Visualizations](#visualizations)

## Technologies Used

- **Python**: The primary programming language used for data analysis and web development.
- **Streamlit**: A library for creating web apps for machine learning and data science projects.
- **Pandas**: Used for data manipulation and analysis.
- **Psycopg2**: PostgreSQL database adapter for Python.
- **Matplotlib**: A plotting library for creating static, interactive, and animated visualizations.
- **Seaborn**: A statistical data visualization library based on Matplotlib.
- **Plotly**: A graphing library for interactive visualizations.

## Installation

To run this project, follow these steps:

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd github_data_dive

2. Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

pip install -r requirements.txt

4. Set up your PostgreSQL database and ensure the github_repositories table is created with the appropriate schema.

## Usage

To run the Streamlit application, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where your `app.py` file is located.

3. Install the required packages (if not already done) by running:
   ```bash
   pip install -r requirements.txt


### To run the Streamlit application, execute the following command in your terminal:

streamlit run app.py

This will start a local server, and you can view the app in your web browser at http://localhost:8501.

## Project Structure

github_data_dive/
│
├── app.py                # Main Streamlit application file
├── requirements.txt      # Dependencies required for the project
└── README.md             # Documentation for the project

## Analysis Questions

The project addresses the following analytical questions:

1. **Top 10 repositories by number of stars**: Visualizes the top 10 repositories sorted by the number of stars received, displayed as a horizontal bar chart.

2. **Top 10 repositories by number of forks**: Displays the top 10 repositories based on the number of forks, using a horizontal bar chart for comparison.

3. **Top 10 programming languages used in repositories**: Analyzes the top 10 programming languages used across the repositories and presents the data as a horizontal bar chart.

4. **Monthly trend of repository creation and updates**: Provides a line chart illustrating the monthly trend of repositories created and updated over time.

5. **Top 5 licenses with the most repositories**: Shows the top 5 license types based on the number of repositories, visualized in a horizontal bar chart.

6. **Top 5 programming languages with the most stars**: Analyzes which programming languages have the highest total stars across repositories and visualizes the data in a horizontal bar chart.

7. **Top 10 months with the highest number of repositories created**: Displays the months with the highest counts of newly created repositories using a horizontal bar chart.

8. **Distribution of repositories by programming language**: Illustrates the distribution of repositories across different programming languages using a pie chart with a legend for clarity.

9. **Comparison of stars vs. forks**: Compares the total counts of stars and forks for all repositories, displayed as a horizontal bar chart.

10. **Top 5 repositories with the most open issues**: Highlights the top 5 repositories that have the most open issues, visualized using a horizontal bar chart.


## Visualizations

The visualizations are created using Matplotlib, Seaborn, and Plotly, providing various types of charts including:

Horizontal Bar Charts: For comparing the number of stars, forks, and open issues across repositories and programming languages.
Pie Chart: To show the distribution of repositories by programming language.
Doughnut Chart: To illustrate the percentage of repositories under different license types.
Line Charts: To represent trends in repository creation and updates over time.

