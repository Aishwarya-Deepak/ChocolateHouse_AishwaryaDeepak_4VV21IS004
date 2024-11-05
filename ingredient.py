import streamlit as st
from database import get_all_ingredients, add_ingredient
import pandas as pd

def ingredient():
    st.header("Ingredient Inventory")
    ingredient_name = st.text_input("Ingredient Name")
    quantity = st.number_input("Quantity", min_value=0)

    if st.button("Add Ingredient"):
        if len(ingredient_name) == 0:
            st.warning("Please enter a valid input")
        else:
            add_ingredient(ingredient_name, quantity)
            st.success(f"Added ingredient '{ingredient_name}' with quantity {quantity}")

    if st.button("Show Ingredients"):
        st.subheader("View Ingredients")
        ingredients = get_all_ingredients()
        
        if ingredients:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Ingredient Quantities")
                df_ingredients = pd.DataFrame(ingredients, columns=["Ingredient Name", "Quantity"])
                st.table(df_ingredients)  # Display the table of ingredients
            
            with col2:
                st.subheader("Ingredient Quantities Analysis")
                st.bar_chart(df_ingredients.set_index("Ingredient Name")["Quantity"], use_container_width=True)
        else:
            st.write("No ingredients found.")

if __name__ == "__main__":
    ingredient()
