# Heart Disease Health Indicators

This repository contains a dataset and code for analyzing and predicting heart disease and related health indicators. The dataset, obtained from the Behavioral Risk Factor Surveillance System (BRFSS) 2015, includes various health features that can be used to predict whether an individual has heart disease or has experienced a heart attack.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Models and Results](#models-and-results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to create a predictive model that can determine whether an individual has heart disease or has had a heart attack based on their health indicators. We explore multiple machine learning models, such as **Support Vector Machine (SVM)**, to achieve maximum accuracy.

## Dataset

The dataset consists of various health indicators such as:

- **HeartDiseaseorAttack**: Target variable (0 = No, 1 = Yes)
- **HighBP**: Whether the individual has high blood pressure (0 = No, 1 = Yes)
- **HighChol**: Whether the individual has high cholesterol (0 = No, 1 = Yes)
- **BMI**: Body Mass Index
- **Smoker**: Whether the individual is a smoker (0 = No, 1 = Yes)
- **Stroke**: Whether the individual has had a stroke (0 = No, 1 = Yes)
- **Diabetes**: Whether the individual has diabetes (0 = No, 1 = Yes)
- **PhysActivity**: Whether the individual engages in physical activity (0 = No, 1 = Yes)
- **Fruits**: Whether the individual consumes fruits regularly (0 = No, 1 = Yes)
- And other relevant health indicators...

The data is stored in CSV format.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vidhipalan/Heart_disease_health_indicators.git
   cd Heart_disease_health_indicators
