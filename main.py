import streamlit as st

st.title('Largest Number Finder')

# Input from the user
num1 = st.number_input('Enter the first number')
num2 = st.number_input('Enter the second number')
num3 = st.number_input('Enter the third number')

# Function to find the largest number
def find_largest(n1, n2, n3):
    return max(n1, n2, n3)

# Button to perform the action
if st.button('Find Largest Number'):
    result = find_largest(num1, num2, num3)
    st.success(f'The largest number is {result}')
