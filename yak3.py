import streamlit as st

# Initialize session state for storing input
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Function to handle button clicks
def click_button(value):
    st.session_state.expression += str(value)

# Function to clear input
def clear_display():
    st.session_state.expression = ""

# Function to calculate result
def calculate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except Exception:
        st.session_state.expression = "Error"

# Streamlit UI
st.title("Calculator")

# Display current expression
st.text_input("Display", value=st.session_state.expression, key="display", disabled=True)

# Button layout (Ensuring operators render properly)
buttons = [
    ["7", "8", "9", "➕"],  # + symbol fixed
    ["4", "5", "6", "➖"],  # - symbol fixed
    ["1", "2", "3", "✖"],  # * symbol fixed
    ["C", "0", "=", "➗"]   # / symbol fixed
]

# Creating buttons dynamically
for row in buttons:
    cols = st.columns(4)
    for i, text in enumerate(row):
        if text == "C":
            cols[i].button(text, on_click=clear_display)
        elif text == "=":
            cols[i].button(text, on_click=calculate)
        else:
            cols[i].button(text, on_click=click_button, args=(text,))

# Mapping correct operator symbols to eval-compatible versions
operator_map = {"➕": "+", "➖": "-", "✖": "*", "➗": "/"}

# Convert operators before evaluation
if any(op in st.session_state.expression for op in operator_map):
    for unicode_op, actual_op in operator_map.items():
        st.session_state.expression = st.session_state.expression.replace(unicode_op, actual_op)
