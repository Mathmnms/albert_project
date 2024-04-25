# Project: PredictVote

## Overview

PredictVote is designed to analyze public French datasets and scrape various sources, such as the French National Institute of Statistics and Economic Studies (INSEE) and other websites. The objective is to compile a comprehensive dataset that includes a range of features by municipality, highlighting voting trends from 2017 to 2021.

### Data Features

The dataset includes the following features for each municipality:

- Department code (`code_dep`)
- Department name (`lib_dep`)
- Municipality code (`code_commune`)
- Municipality name (`lib_commune`)
- Registered voters (`Inscrits`)
- Actual voters (`Votants`)
- Candidate name (`Nom`)
- Percentage of votes/expression (`% Voix/Exp`)
- Number of mosque (`mosquee`)
- Year of election data (`year`)
- INSEE code for the commune (`code_commune_INSEE`)
- Postal code (`code_postal`)
- Latitude (`latitude`)
- Longitude (`longitude`)
- Population size (`POP`)
- Number of victims (`victimes`)
- Number of infractions (`infractions`)

## Project Steps

### Step 1: Data Aggregation

Aggregate all datasets to create a comprehensive training dataset. This step involves data cleaning, integration, and preparation for analysis.

### Step 2: Model Testing

Test multiple machine learning models to identify the best performer based on predefined metrics. This step

## Dataset Access

The dataset is available for download via the following Google Drive link:

[Download Dataset](https://drive.google.com/drive/folders/1bSHFMVzuUL2KWNdyiowYFEcjuPng7V04?usp=sharing)


## Objectives 

We aim to give a prediction of the EU french representives vote using municipality features.    