import streamlit as st
from persistent_q import PersistentQSQLite

def app():
    queue = PersistentQSQLite()
    st.title("Persistent Queue")
    st.write(f"Queue size: {queue.size()}")
    job = st.text_input("Add job")
    if st.button("Add"):
        queue.put(job)

if __name__ == "__main__":
    app()