# Project: PredictVote

## Overview

PredictVote is designed to analyze public French datasets and scrape various sources, such as the French National Institute of Statistics and Economic Studies (INSEE) and other websites. The objective is to compile a comprehensive dataset that includes a range of features by municipality, highlighting voting trends from 2017 to 2021.

### Data Features

The dataset includes the following features for each municipality:

code_dep - Department code.
lib_commune - Name of the commune.
Inscrits - Number of registered voters.
Votants - Number of actual voters.
Nom - Name (possibly of candidates or relevant entities).
% Voix/Exp - Percentage of votes/expression.
year - Year of the data entry or event.
code_commune_INSEE - INSEE code of the commune.
code_postal - Postal code of the commune.
latitude - Latitude coordinate of the commune.
longitude - Longitude coordinate of the commune.
victimes_par_hab - Number of victims per inhabitant.
infractions_par_hab - Number of infractions per inhabitant.
mosquee_par_hab - Number of mosques per inhabitant.
NB_Pers_par_Foyer_Alloc_par_hab - Number of persons per household receiving allowances per inhabitant.
statut_commune_uu2020 - Status of the commune in 2020.
revenu_imposable_par_habitant - Taxable income per inhabitant.
rural - Indicator of whether the commune is rural.
montagne - Indicator of whether the commune is in a mountainous area.
touristique - Indicator of whether the commune is a tourist area.
ptot_n - Total population (nomenclature not specified).
dep_inv_hor_remb_par_hab - Expenditure on unremunerated investments per inhabitant.
dot_glo_fonc_par_hab - Global functional endowment per inhabitant.
conso_ind_par_hab - Industrial consumption per inhabitant.
cons_agr_par_hab - Agricultural consumption per inhabitant.
conso_ter_par_hab - Tertiary (service sector) consumption per inhabitant.
conso_res_par_hab - Residential consumption per inhabitant.

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