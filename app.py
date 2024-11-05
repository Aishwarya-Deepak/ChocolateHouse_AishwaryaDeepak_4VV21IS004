import streamlit as st
from streamlit_option_menu import option_menu

from season import season
from ingredient import ingredient
from suggest import suggest

PAGES = {
    "Seasonal Flavours": season,
    "Ingredient Inventory": ingredient,
    "Customer Suggestions": suggest
}

def main():

    selected = option_menu(
            menu_title="Chocolate House !",  
            options=["Seasonal Flavours", "Ingredient Inventory", "Customer Suggestions"], 
            icons=["snow", "box", "smile"],
            menu_icon="cast",  
            default_index=0,  
            orientation="horizontal",
        )

    if selected == "Seasonal Flavours":
        season()
    elif selected == "Ingredient Inventory":
        ingredient()
    elif selected == "Customer Suggestions":
        suggest()
             
if __name__ == "__main__":
    main()
