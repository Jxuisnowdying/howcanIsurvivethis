import streamlit as st
import pandas as pd
import csv
from itertools import accumulate, repeat
from operator import mul
from my_Sidebar import Sidebar

st.set_page_config(
    page_title="Binary Decimal Converter",
    page_icon="🪄",)

#Sidebar
Sidebar.Decorate()
Sidebar.mail()

#Function
def bin2dec(bin_str):
    return sum(
        int(n) * m for n, m in zip(
            str(bin_str)[::-1],
            accumulate((repeat(2)), func=mul, initial=1)))

def remove_commas(x):
    return str(x).replace(',', '')

def add_historydec2bin():
    columns = ['Decimal', 'Binary']
    with open('my_csv/dectobin_data.csv', 'a') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(columns)
        writer.writerow([dec_int, bin_str])

def add_historybin2dec():
    columns = ['Binary', 'Decimal']
    with open('my_csv/bintodec_data.csv', 'a') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(columns)
        writer.writerow([bin_str, dec])

def clear_history():
    empty_df = pd.DataFrame(columns=['Decimal', 'Binary'])
    empty_df.to_csv('my_csv/dectobin_data.csv', index=False)
    empty_df = pd.DataFrame(columns=['Binary', 'Decimal'])
    empty_df.to_csv('my_csv/bintodec_data.csv', index=False)
    st.success('History cleared successfully! Please refresh the page.')

#Converter
st.title('Binary-Decimal Converter')
col1, col2 = st.columns(2)
with col1:
    form = st.form(key='form')
    dec_int = form.text_input('Enter Decimal:')
    submitdec = form.form_submit_button('Convert')
if submitdec:
    bin_str = '{:08b}'.format(int(dec_int))
    form.write(f'Binary of {dec_int}: {bin_str}')
    add_historydec2bin()
with col2:
    form = st.form(key='my')
    bin_str = form.text_input('Enter Binary:')
    submitbin = form.form_submit_button('Convert')
if submitbin:
    dec = bin2dec(bin_str)
    form.write(f'Decimal of {bin_str}: {dec}')
    add_historybin2dec()

#History
st.header('Converter History')
cl1, cl2 = st.columns(2)
with cl1:
    all_data = pd.read_csv('my_csv/dectobin_data.csv')
    if len(all_data) <= 10000000:
        all_data['Binary'] = all_data['Decimal'].apply(lambda x: '{:08b}'.format(x))
    else:
        all_data['Binary'] = all_data['Decimal'].apply(remove_commas(bin_str))
    st.dataframe(all_data, use_container_width=True)
with cl2:
    all_data = pd.read_csv('my_csv/bintodec_data.csv')
    if len(all_data) <= 10000000:
        all_data['Binary'] = all_data['Decimal'].apply(lambda x: '{:08b}'.format(x))
    else:
        all_data['Binary'] = all_data['Decimal'].apply(remove_commas(bin_str))
    st.dataframe(all_data, use_container_width=True)
if st.button('Clear History'):
    clear_history()
