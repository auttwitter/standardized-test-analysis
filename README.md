# Problem Statement

    General Assembly Academy is planning to launch a new institution focused on standardized test preparation, specifically the ACT and SAT. The goal is to identify the best states to establish the institution and determine which subjects should be included in an intensive program.

# Background

    The ACT is a standardized test that consists of four main sections: English, Math, Reading, and Science. Each section is scored on a scale of 1 to 36, and the composite score, which represents each tester, is the average of the four section scores, rounded to the nearest whole number. The maximum composite score is 36. Additionally, there is an optional Writing section, which is scored separately on a scale of 2 to 12.

    In contrary, the SAT is a standardized test that consists of three main sections: Evidence-Based Reading and Writing, and Math. Each section has a maximum score of 800, making the total maximum score 1600. The score representing each tester is called the total score, which is the sum of the scores from the Evidence-Based Reading and Writing section and the Math section. There is an optional Essay section, which is scored separately on a scale of 2 to 8.

    In the U.S., different states tend to favor either the ACT or the SAT based on their educational policies; however, students from specific states have the flexibility to choose their preferred test.

# Datasets

The datasets used in this analysis are:

- [`act_2017.csv`](./data/act_2017.csv): 2017 ACT scores by states, has columns State, Participation, English, Math, Reading, Science and Composite
- [`sat_2017.csv`](./data/sat_2017.csv): 2017 SAT scores by states, has columns State, Participation, Evidence-Based Reading and Writing, Math, Total

# Analysis

## Import Essential Libraries

pandas, numpy, matplotlib.pyplot, matplotlib.patches, seaborn, math

## Data Cleaning Step

- Check the key for merging 2 DataFrames together, i.e., states
- Convert data types of each columns to appropiate types
- Handling NaNs by patching the data to reasonable values
- Adding the abbreviations of each state and adding the coordinate for making graph

## Methodology

- The ideal states for establishing the institution should have many students taking both the ACT and SAT. This can be determined by examining the participation rates of both tests, using the median as a guide. If the participation rates for both tests are greater than the median, then those states are considered ideal.
- To determine which subjects should be included in an intensive program, we can compare the scores between the ideal states and other states.

## Findings

- There are four states—Hawaii, Florida, North Carolina, and South Carolina—that have participation rates greater than the median for both tests.
- When comparing the scores of these four states with those of other states, the difference in ACT English scores is the highest among all subjects.
