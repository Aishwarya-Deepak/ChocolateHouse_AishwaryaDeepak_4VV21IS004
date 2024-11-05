import streamlit as st
from db import init_db, yourflavour, youringredient, yoursuggestion, displayflavours, displayingredients,displaysuggestions
init_db()
st.title("CHOCOLATE HOUSE")
st.header("Add SEASONAL FLAVOURS")
fname=st.text_input("YOUR FLAVOUR")
season=st.selectbox("Season",["Summer","Winter","Rainy","Autumn","Spring"])
if st.button("ADD FLAVOUR"):
    yourflavour(fname,season)
    st.success(f"'{fname}'for {season} added")
st.header("Add INGREDIENTS")
igname=st.text_input("YOUR INGREDIENT")
quantity=st.number_input("AMOUNT",min_value=0)
if st.button("ADD INGREDIENT"):
    youringredient(igname,quantity)
    st.success(f"'{igname}'for {quantity} added")
st.header("DROP YOUR SUGGESTIONS")
suggestion=st.text_input("YOUR SUGGESTION")
allergy=st.text_area("ANY ALLERGY SPECIFICATION")
if st.button("ADD SUGGESTION"):
    yoursuggestion(suggestion,allergy)
    st.success(f"Suggestion added")

if st.button("Show Flavours"):
    st.subheader("View Flavours")
    flavours = displayflavours()
    if flavours:
        for flavour in flavours:
            st.write(f"Flavour: {flavour[0]}, Season: {flavour[1]}")
    else:
        st.write("No flavours to display.")


if st.button("Show Ingredients"):
    st.subheader("View Ingredients")
    ingredients = displayingredients()
    if ingredients:
        for ingredient in ingredients:
            st.write(f"Ingredient: {ingredient[0]}, Quantity: {ingredient[1]}")
    else:
        st.write("No ingredients to display.")


if st.button("Show Suggestions"):
    st.subheader("View Suggestions")
    suggestions = displaysuggestions()
    if suggestions:
        for suggestion in suggestions:
            st.write(f"Suggested Flavor: {suggestion[0]}, Allergy Concern: {suggestion[1]}")
    else:
        st.write("No suggestions to display.")