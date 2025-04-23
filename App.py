import streamlit as st
import joblib
import numpy as np

models = {
    'Tuned Random Forest': joblib.load('tuned_random_forest_model.pkl'),
    'Tuned Decision Tree': joblib.load('tuned_decision_tree.pkl'),
    'Logistic Regression': joblib.load('logistic_model.pkl'),
    'Naive Bayes': joblib.load('naive_bayes_model.pkl')
}


# 📂 Streamlit App UI
st.title('Heart Disease Risk Predictor')

# Model selection
model_choice = st.selectbox('Select Model for Prediction:', list(models.keys()))

st.subheader('Enter Patient Information:')

# Input fields for all 21 features

HighBP = st.selectbox('High Blood Pressure?', ['No', 'Yes'])
HighBP = 1 if HighBP == 'Yes' else 0

HighChol = st.selectbox('High Cholesterol?', ['No', 'Yes'])
HighChol = 1 if HighChol == 'Yes' else 0

CholCheck = st.selectbox('Cholesterol Check done?', ['No', 'Yes'])
CholCheck = 1 if CholCheck == 'Yes' else 0

BMI = st.slider('BMI', 10, 50, 25)

Smoker = st.selectbox('Smoker?', ['No', 'Yes'])
Smoker = 1 if Smoker == 'Yes' else 0

Stroke = st.selectbox('Had Stroke?', ['No', 'Yes'])
Stroke = 1 if Stroke == 'Yes' else 0

Diabetes = st.selectbox('Diabetes?', ['No', 'Yes', 'Borderline'])
diabetes_mapping = {'No': 0, 'Yes': 1, 'Borderline': 2}
Diabetes = diabetes_mapping[Diabetes]

PhysicalActivity = st.selectbox('Physical Activity?', ['No', 'Yes'])
PhysicalActivity = 1 if PhysicalActivity == 'Yes' else 0

Fruits = st.selectbox('Eat Fruits Daily?', ['No', 'Yes'])
Fruits = 1 if Fruits == 'Yes' else 0

Vegetables = st.selectbox('Eat Vegetables Daily?', ['No', 'Yes'])
Vegetables = 1 if Vegetables == 'Yes' else 0

HeavyAlcoholConsumption = st.selectbox('Heavy Alcohol Consumption?', ['No', 'Yes'])
HeavyAlcoholConsumption = 1 if HeavyAlcoholConsumption == 'Yes' else 0

AnyHealthcare = st.selectbox('Has Healthcare Coverage?', ['No', 'Yes'])
AnyHealthcare = 1 if AnyHealthcare == 'Yes' else 0

NoDocBecauseOfCost = st.selectbox('Skipped Doctor Visit due to Cost?', ['No', 'Yes'])
NoDocBecauseOfCost = 1 if NoDocBecauseOfCost == 'Yes' else 0

GenHlth = st.slider('General Health (1=Excellent, 5=Poor)', 1, 5, 3)

MentHlth = st.slider('Mental Health Bad Days (past month)', 0, 30, 5)

PhysHlth = st.slider('Physical Health Bad Days (past month)', 0, 30, 5)

DiffWalk = st.selectbox('Difficulty Walking?', ['No', 'Yes'])
DiffWalk = 1 if DiffWalk == 'Yes' else 0

Sex = st.selectbox('Sex?', ['Female', 'Male'])
Sex = 1 if Sex == 'Male' else 0

Age = st.slider('Age Group (1=18-24, ..., 13=80+)', 1, 13, 5)

Education = st.slider('Education Level (1=No High School, 6=College Graduate)', 1, 6, 3)

Income = st.slider('Income Level (1=Low, 8=High)', 1, 8, 4)


if st.button('Predict Heart Disease Risk'):
    features = np.array([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, Diabetes,
                          PhysicalActivity, Fruits, Vegetables, HeavyAlcoholConsumption,
                          AnyHealthcare, NoDocBecauseOfCost, GenHlth, MentHlth, PhysHlth,
                          DiffWalk, Sex, Age, Education, Income]])
    
    # Pick the selected model
    selected_model = models[model_choice]
    
    # Predict probability
    prob = selected_model.predict_proba(features)[0][1]  # probability of class 1
    thresholds = {
    'Tuned Random Forest': 0.35,
    'Tuned Decision Tree': 0.35,
    'Logistic Regression': 0.30,
    'Naive Bayes': 0.25
    }
    threshold = thresholds[model_choice]
    # Display prediction
    st.subheader('Prediction Result:')
    if prob > threshold:
        st.error(f'High Risk of Heart Disease!')
    else:
        st.success(f'Low Risk of Heart Disease!')
