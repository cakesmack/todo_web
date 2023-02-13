import streamlit as st
import functions

def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo) 
    functions.write_file(todos)

todos = functions.read_file()

st.title('My Todo App Biy')
st.subheader('Silly little todo list making app.')
st.write(f'This will 100% definitely increase your productivity.')

for index, i in enumerate(todos):
    checkbox = st.checkbox(i, key=i)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[i]
        st.experimental_rerun()

st.text_input(label='Add an item', on_change=add_todo, key='new_todo')