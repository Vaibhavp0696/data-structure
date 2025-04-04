import streamlit as st

st.title("Calculator")
st.markdown("Welcome to my first web Calculator app!")

c1, c2 = st.columns(2)

fnum = c1.number_input("First number", value=0)
snum = c2.number_input("Second number", value=0)

options = ["Addition", "Subtraction", "Multiply", "Divide"]
choice = st.radio("Select operation", options)

# button on which after clicking an action becomes

button = st.button("Calulate")

result = 0

if button:
    if choice == "Addition":
        result = fnum + snum
    if choice == "Subtraction":
        result = fnum - snum
    if choice == "Multiply":
        result = fnum * snum
    if choice == "Divide":
        result = fnum / snum

st.warning(f"Result: {result}")
