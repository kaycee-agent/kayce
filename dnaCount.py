import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

image = Image.open('DNA.png')
st.image(image, use_column = True, height= 150, width=300)


st.header('Enter DNA sequence')
sequence_input = ">DNA Query 2\nGAACACGTGAGCTCATGGGAAATTTAACCCACCCAATTTAAAGGGATCATGAC \n ATCTTTGACATTTAGACCATAACTACCAATACCATACCATACTACGGGATAAGATAG \n TGATGAACATTGACCAGTAGGAACAGATAGAGATAGATAGATA"
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence
sequence = sequence[1:]
sequence = ''.join(sequence)
sequence
st.write("""
         ***
         """)
st.header('INPUT(DNA Query)')
sequence
st.header('OUTPUT(DNA Nucleotide Count)')
st.subheader('1. Print Count')
def DNA_counter(x):
    d = dict([
        ('A',x.count('A')),
        ('C',x.count('C')),
        ('G',x.count('G')),
        ('T',x.count('T'))
    ])
    return d
count = DNA_counter(sequence)
count_labels = list(count)
count_values = list(count.values())

count
st.header('2. Print text')
st.write('There are ' + str(count['A']) + ' adenine (A) in the DNA sequence')
st.write('There are ' + str(count['C']) + ' cytosine (C) in the DNA sequence')
st.write('There are ' + str(count['G']) + ' guanine (G) in the DNA sequence')
st.write('There are ' + str(count['T']) + ' thyminee (T) in the DNA sequence')
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(count, orient='index')
df = df.rename({0: 'count'}, axis = 'columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x = 'nucleotide',y='count'
)
p = p.properties(
    width =alt.Step(80)
)
st.write(p)
