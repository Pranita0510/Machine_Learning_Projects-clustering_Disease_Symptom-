import streamlit as st
import pickle

# Load pickled disease data (DataFrame)
disease_data = pickle.load(open('Disease_Symptom.pkl', 'rb'))

# Streamlit UI setup
st.set_page_config(page_title="🩺 Disease Recommender", layout="centered")
st.title("🩺 Disease Pattern Recommendation System App")
st.write("Find disease cases that match your symptoms.")

# User input
# age = st.number_input("Age", min_value=0, max_value=120, step=1)
fever = st.slider("Fever", min_value=96, max_value=105, step=1)
cough = st.selectbox("Cough", [0, 1])
fatigue = st.selectbox("Fatigue", [0, 1])
breathlessness = st.selectbox("Breathlessness", [0, 1])
loss_of_taste = st.selectbox("Loss of Taste", [0, 1])
age = st.number_input("Age", min_value=0, max_value=120, step=1)

# Create input dictionary
symptom_input = {
    # "Age": age,
    "Fever": fever,
    "Cough": cough,
    "Fatigue": fatigue,
    "Breathlessness": breathlessness,
    "Loss of Taste": loss_of_taste,
    "Age": age
}

# Filter logic without similarity matrix
def find_matching_cases(symptom_input):
    matches = disease_data.copy()
    for key, value in symptom_input.items():
        if key in matches.columns:
            matches = matches[matches[key] == value]
    return matches.head(5)  # Return top 5 matches

# Recommend button
if st.button("Recommend Disease Cluster"):
    matches = find_matching_cases(symptom_input)
    if not matches.empty:
        st.success("Top Matching Disease Cases:")
        for i, (_, row) in enumerate(matches.iterrows(), 1):
            st.markdown(f"*Case {i}:*")
            for key, value in row.items():
                st.write(f"- {key}: {value}")
    else:
        st.error("No matching case found. Try changing symptoms.")