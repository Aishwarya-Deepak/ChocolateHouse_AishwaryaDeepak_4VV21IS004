import streamlit as st
from database import get_all_suggestions, add_customer_suggestion
import pandas as pd
def suggest():
    st.header("Customer Flavor Suggestions")
    suggested_flavor = st.text_input("Flavor Suggestion")
    allergy_concern = st.text_area("Allergy Concern (optional)")
    if st.button("Submit Suggestion"):
        if len(suggested_flavor) == 0:
            st.warning("Please enter a valid input")
        else:
            add_customer_suggestion(suggested_flavor, allergy_concern)
            st.success("Suggestion submitted!")
    
    if st.button("Show Suggestions"):
        st.subheader("View Suggestions")
        suggestions = get_all_suggestions()
        if suggestions:
            df_suggestions = [(suggestion[0], suggestion[1]) for suggestion in suggestions]
            st.table(pd.DataFrame(df_suggestions, columns=["Flavor Suggestion", "Allergy Concern"]))
        else:
            st.write("No suggestions found.")
    
if __name__ == "__main__":
    suggest()
