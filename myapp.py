import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Page title
image = Image.open('dna_count.png')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA

***
""")

# Input text box
st.header("Enter DNA sequence")

sequence_input = ">DNA Query\nAATCCGCTAG\nAAACCCTTAG\nCGCGAATTCGCG"

sequence = st.text_area("Sequence inut", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] #skip first line
sequence = ''.join(sequence)

st.write("""
***
""")

# Print the input DNA sequence
st.header("Input (DNA Query)")
sequence

# DNA nucleotide count
st.header("Output (DNA Nucleotide Count)")


def DNA_nucleotide_count(seq):
    dna_count_dict = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return dna_count_dict

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

st.subheader("1. Print text")
st.write("There are " + str(X['A']) + " adenine (A)")
st.write("There are " + str(X['T']) + " thymine (T)")
st.write("There are " + str(X['G']) + " guanine (G)")
st.write("There are " + str(X['C']) + " cytosine (C)")

# Display Dataframe
st.subheader("3. Display DataFrame")
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)

# Display Bar chart
st.subheader("4. Display Bar Chart")
bar_chart = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

bar_chart = bar_chart.properties(
    width=alt.Step(80)
)

st.write(bar_chart)


