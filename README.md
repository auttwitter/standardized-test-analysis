# Standardized Test Analysis
This repository contains Project 1: Standardized Test Analysis, assigned by Mr. James Larkin for class DSI-04.

# Problem Statement
General Assembly Academy is planning to launch a new institution focused on ACT and SAT standardized test preparation. The goal is to identify the best states to establish the institution and determine which subjects to emphasize in an intensive study program.

# Background
About the Tests
The ACT is a standardized test that consists of four main sections: English, Math, Reading, and Science. Each section is scored on a scale of 1 to 36, and the composite score, which represents each tester, is the average of the four section scores, rounded to the nearest whole number. The maximum composite score is 36. Additionally, there is an optional Writing section, which is scored separately on a scale of 2 to 12.

In contrary, the SAT is a standardized test that consists of three main sections: Evidence-Based Reading and Writing, and Math. Each section has a maximum score of 800, making the total maximum score 1600. The score representing each tester is called the total score, which is the sum of the scores from the Evidence-Based Reading and Writing section and the Math section. There is an optional Essay section, which is scored separately on a scale of 2 to 8.
About the States and Tests
In the U.S., different states tend to lean toward either the ACT or SAT based on their policies. Nevertheless, students from specific states can choose their preferred tests.

# Datasets

The datasets used in this analysis are:

- [`act_2017.csv`](./data/act_2017.csv): 2017 ACT scores by states, has columns State, Participation, English, Math, Reading, Science and Composite
- [`sat_2017.csv`](./data/sat_2017.csv): 2017 SAT scores by states, has columns State, Participation, Evidence-Based Reading and Writing, Math, Total

# Prepare DataFrame

## Import Essential Libraries

pandas, numpy, matplotlib.pyplot, seaborn

## Data Cleaning Step

- Check the key for merging 2 DataFrames together, i.e., states
- Convert data types of each columns to appropiate types
- Handling NaNs by patching the data to reasonable values
- Adding the abbreviations of each state and adding the coordinate for making graph

# Analysis
## Goals and How to achieve

- To identify the best states to establish the institution, we analyzed the participation rates of both tests.
- To determine which subjects to emphasize in an intensive study program, we compared the scores between the group of states and the nationwide.

