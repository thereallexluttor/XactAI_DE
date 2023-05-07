# Importamos la librería Streamlit para crear aplicaciones web interactivas
import streamlit as st 

from XactAI_Libs import XactAI_Data_Collector 

proc = XactAI_Data_Collector.CleanDataframe('dataset.csv')

a = proc.csv_to_dataframe()
proc.clean_dataframe()
b = proc.name_formater()
print(b.head())
print(proc.get_column_names())
print(proc.get_columns_info())