import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.exceptions import NotFittedError
import pickle
from my_Sidebar import Sidebar

st.set_page_config(
    page_title="Animal Classification",
    page_icon="🔍",)

#Sidebar
Sidebar.Decorate()
Sidebar.mail()

df = pd.read_csv('my_csv/zoo.csv')
X = df.drop(['animal_name', 'class_type'], axis=1)
y = df['animal_name']

#Function
def create_model():
    model = RandomForestClassifier()
    model.fit(X, y)
    with open('zoo_model.pkl', 'wb')as f:
        pickle.dump(model, f)
    return model

def save_model(model):
    with open('zoo_model.pkl', 'wb') as f:
        pickle.dump(model, f)

def load_model():
    with open('zoo_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def predict_animal_type(model, hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize):
    animal = [[hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize]]
    prediction = model.predict(animal)
    return prediction[0]


#Classifier
st.title('Animal Classification')
st.caption('Predict the classification of the animals by their attribute information')
model = create_model()
col1, col2, col3 = st.columns([3.5, 3, 2])
with col1:
    create = st.button('Create Model')
with col2:
    load = st.button('Load Model')
with col3:
    save = st.button('Save Model')
with st.empty():
    if create:
        st.success('Model has been created')
    if load:
        load_model()
        st.success('Model has been loaded')
    if save:
        save_model(model)
        st.success('Model has been saved')

#UserInput
cl1, cl2 = st.columns(2)
with cl1:
    hair = st.selectbox('Does the animal have hair?', options=[True, False])
    feathers = st.selectbox('Does the animal have feathers?', options=[True, False])
    eggs = st.selectbox('Does the animal lay eggs?', options=[True, False])
    milk = st.selectbox('Does the animal produce milk?', options=[True, False])
    airborne = st.selectbox('Is the animal airborne?', options=[True, False])
    aquatic = st.selectbox('Is the animal aquatic?', options=[True, False])
    predator = st.selectbox('Is the animal a predator?', options=[True, False])
    toothed = st.selectbox('Does the animal have teeth?', options=[True, False])
with cl2:
    backbone = st.selectbox('Does the animal have a backbone?', options=[True, False])
    breathes = st.selectbox('Does the animal breathe?', options=[True, False])
    venomous = st.selectbox('Is the animal venomous?', options=[True, False])
    fins = st.selectbox('Does the animal have fins?', options=[True, False])
    legs = st.slider('How many legs does the animal have?', min_value=0, max_value=8, step=1)
    tail = st.selectbox('Does the animal have a tail?', options=[True, False])
    domestic = st.selectbox('Is the animal domestic?', options=[True, False])
    catsize = st.selectbox('Is the animal cat-sized?', options=[True, False])


if st.button('Predict'):
    try:
        loaded_model = load_model()
        animal_type = predict_animal_type(loaded_model, hair, feathers, eggs, milk, airborne, aquatic, predator, toothed, backbone, breathes, venomous, fins, legs, tail, domestic, catsize)
        st.success(f'The animal is: {animal_type}')
    except NotFittedError:
        st.error('Model has not been trained yet. Please create or load a trained model.')
    except FileNotFoundError:
        st.error('Model has not been created yet. Please create model.')
