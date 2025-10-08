# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 00:40:13 2025

@author: Krishnakant lodhi
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

def prediction_system(input_data,model):
    input_data=np.asarray(input_data,dtype=float)
    input_data=input_data.reshape(1,-1)
    output=model.predict(input_data)
    return output

heart_model=pickle.load(open("head_model.sav",'rb'))
diabetes_model=pickle.load(open("diabetes_model.sav",'rb'))
#house_price_model = pickle.load(open("house_price_model.sav", "rb"))

with st.sidebar:
    
    selection=option_menu("multiple deasease prediction system", 
                          ["Diabetes prediction",
                           "heart prediction ",
                           "House price prediction"],
                          icons=["hospital","clipboard2-pulse","house-door"],
                          default_index=0)
    
if(selection=="Diabetes prediction"):
    st.title("Diabetes prediction")
    
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input("Pregnancies")
    with col2:
        Glucose=st.text_input("Glucose")
    with col3:
        BloodPressure=st.text_input("BloodPressure")
    with col1:
        SkinThickness=st.text_input("SkinThickness")
    with col2:
        Insulin=st.text_input("Insulin")
    with col3:
        BMI=st.text_input("BMI")
    with col1:
        DiabetesPedigreeFunction=st.text_input("DiabetesPedigreeFunction")
    with col2:
        Age=st.text_input("Age")
                                                    
    # getting input data form user
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    # predict result
    dianosis=""
    
    # button for predict
    if st.button("test result"):
        dianosis_result=prediction_system([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age],diabetes_model)
        if(dianosis_result==1):
            dianosis="result is positive"
        else:
            dianosis="result is negative"
    st.success(dianosis)


if(selection=="heart prediction "):
    st.title("heart prediction ")

    
    
    col1,col2,col3=st.columns(3)

    with col1:
        age=st.text_input("age")
    with col2:
        sex=st.text_input("sex")
    with col3:
        cp=st.text_input("cp")
    with col1:
        trestbps=st.text_input("trestbps")
    with col2:
        chol=st.text_input("chol")
    with col3:
        fbs=st.text_input("fbs")
    with col1:
        restecg=st.text_input("restecg")
    with col2:
        thalach=st.text_input("thalach")
    with col3:
        exang=st.text_input("exang")
    with col1:
        oldpeak=st.text_input("oldpeak")
    with col2:
        slope=st.text_input("slope")
    with col3:
        ca=st.text_input("ca")
    with col1:
        thal=st.text_input("thal")
                                       
    # getting input data form user
    
    # predict result
    dianosis=""
    
    # button for predict
    if st.button("test result"):
        dianosis_result=prediction_system([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal],heart_model)
        if(dianosis_result==1):
            dianosis="result is positive"
        else:
            dianosis="result is negative"
    st.success(dianosis)

    
if(selection=="House price prediction"):
    st.title("House price prediction")
    
    

    
    
    col1,col2,col3=st.columns(3)

    with col1:
        crim=st.text_input("crim")
    with col2:
        zn=st.text_input("zn")
    with col3:
        indus=st.text_input("indus")
    with col1:
        chas=st.text_input("chas")
    with col2:
        nox=st.text_input("nox")
    with col3:
        rm=st.text_input("rm")
    with col1:
        age=st.text_input("age")
    with col2:
        dis=st.text_input("dis")
    with col3:
        rad=st.text_input("rad")
    with col1:
        tax=st.text_input("tax")
    with col2:
        ptratio=st.text_input("ptratio")
    with col3:
        b=st.text_input("b")
    with col1:
        lstat=st.text_input("lstat")
                                       
    # getting input data form user
    
    # predict result
    dianosis=""
    
    # button for predict
    if st.button("test result"):
        result=prediction_system([crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat],house_price_model)

    st.success(result)





