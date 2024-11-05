# Overview
A simple Chocolate house management application for a fictional chocolate house.
# Prerequisites
- python 3.9+
- docker
- Streamlit
- Streamlit-option-menu
  
## Features

- Add seasonal chocolate flavours.
- Add ingredients and quantities.
- Submit customer suggestions for new flavors along with allergy concerns.
- Display all flavours, ingredients, and suggestions on demand.
- Provide you real-time graph for statistical analysis

# Follow these steps

1.Clone the repository

2.Install the requirements from the requirements.txt file

    pip install -r requirements.txt
3.Create a virtual environment

    # Navigate to your project repo and type the following command
    python3 -m venv venv

    # Activate the virtual environment
    venv\Scripts\activate

4.Build the Docker Image

    docker build -t chocolate-house-app .
    
5.Run the Container

    docker run -p 8501:8501 chocolate-house-app
    
# Screenshot of the Application

![Uploading image.png…]()


   



   
  
  
