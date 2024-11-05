import streamlit as st
from database import init_db, add_flavor, get_all_flavors
import pandas as pd

def season():
    init_db()
    
    st.header("Seasonal Flavors")
    flavor_name = st.text_input("Flavor Name")
    selected_season = st.selectbox("Season", ["Spring", "Summer", "Fall", "Winter"])
    
    if st.button("Add Flavor"):
        if len(flavor_name) == 0:
            st.warning("Please enter a valid input")
        else:
            add_flavor(flavor_name, selected_season)
            st.success(f"Added flavor '{flavor_name}' for {selected_season}")
    
    if st.button("Show Seasonal Flavors"):
        st.subheader("View Seasonal Flavors")
        flavors = get_all_flavors()
        
        if flavors:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Seasonal Flavor")

                df_flavors = pd.DataFrame(flavors, columns=["Flavor", "Season"])
                st.table(df_flavors)             
                season_counts = df_flavors['Season'].value_counts()
                
            
            with  col2:
                st.subheader("Seasonal Flavor Analysis")
                st.line_chart(season_counts, use_container_width=True)
        else:
            st.write("No flavors found.")

if __name__ == "__main__":
    season()
