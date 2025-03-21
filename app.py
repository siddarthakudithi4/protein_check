# # # # # # # # # # # # # #Import libraries
# # # # # # # # # # # # # from dotenv import load_dotenv
# # # # # # # # # # # # # import os
# # # # # # # # # # # # # import google.generativeai as genai
# # # # # # # # # # # # # from PIL import Image
# # # # # # # # # # # # # import streamlit as st


# # # # # # # # # # # # # #Load API Key
# # # # # # # # # # # # # load_dotenv()
# # # # # # # # # # # # # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # # # # # # # # # # # # #Function to load Google Gemini Pro model and get response
# # # # # # # # # # # # # def get_response_diet(prompt, input):
# # # # # # # # # # # # #     model = genai.GenerativeModel('gemini-pro')
# # # # # # # # # # # # #     response = model.generate_content([prompt, input])
# # # # # # # # # # # # #     return response.text

# # # # # # # # # # # # # #Function to load Google Gemini Vision model and get response
# # # # # # # # # # # # # def get_response_nutrition(image, prompt):
# # # # # # # # # # # # #     model = genai.GenerativeModel('gemini-pro-vision')
# # # # # # # # # # # # #     response = model.generate_content([image[0], prompt])
# # # # # # # # # # # # #     return response.text

# # # # # # # # # # # # # #Preprocess image data
# # # # # # # # # # # # # def prep_image(uploaded_file):
# # # # # # # # # # # # #     #Check if there is any data
# # # # # # # # # # # # #     if uploaded_file is not None:
# # # # # # # # # # # # #         #Read the file as bytes
# # # # # # # # # # # # #         bytes_data = uploaded_file.getvalue()

# # # # # # # # # # # # #         #get the image part information
# # # # # # # # # # # # #         image_parts = [
# # # # # # # # # # # # #             {
# # # # # # # # # # # # #                 "mime_type": uploaded_file.type,
# # # # # # # # # # # # #                 "data": bytes_data
# # # # # # # # # # # # #             }
# # # # # # # # # # # # #         ]
# # # # # # # # # # # # #         return image_parts
# # # # # # # # # # # # #     else:
# # # # # # # # # # # # #         raise FileNotFoundError("No File is uploaded!")
    
# # # # # # # # # # # # # #Configuring Streamlit App
# # # # # # # # # # # # # #st.set_page_config(page_title="Health Management: Nutrition Calculator & Diet Planner")
# # # # # # # # # # # # # st.image('Nutritionist/logo.jpg', width=70)
# # # # # # # # # # # # # st.header("Health: Nutrition Calculator & Diet Planner")

# # # # # # # # # # # # # ######################################################################################
# # # # # # # # # # # # # section_choice1 = st.radio("Choose Section:", ("Nutrition Calculator","Diet Planner"))

# # # # # # # # # # # # # #If choice is nutrition calculator
# # # # # # # # # # # # # if section_choice1 == "Nutrition Calculator":
# # # # # # # # # # # # #     upload_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
# # # # # # # # # # # # #     image = ""
# # # # # # # # # # # # #     if upload_file is not None:
# # # # # # # # # # # # #         #Show the image
# # # # # # # # # # # # #         image = Image.open(upload_file)
# # # # # # # # # # # # #         st.image(image, caption="Uploaded Image", use_column_width=True)


# # # # # # # # # # # # #     #Prompt Template
# # # # # # # # # # # # #     input_prompt_nutrition = """
# # # # # # # # # # # # #     You are an expert Nutritionist. As a skilled nutritionist, you're required to analyze the food iems
# # # # # # # # # # # # #     in the image and determine the total nutrition value. 
# # # # # # # # # # # # #     Additionally, you need to furnish a breakdown of each food item along with its respective content.

# # # # # # # # # # # # #     Food item, Serving size, Tatal Cal., Protien (g), Fat,
# # # # # # # # # # # # #     Carb (g), Fiber (g), Vit B-12, Vit B-6,
# # # # # # # # # # # # #     Iron, Zinc, Mang.

# # # # # # # # # # # # #     Use a table to show above informaion.
# # # # # # # # # # # # #     """
# # # # # # # # # # # # #     ##if the button is clicked
# # # # # # # # # # # # #     submit = st.button("Calculate Nutrition value!")
# # # # # # # # # # # # #     if submit:
# # # # # # # # # # # # #         image_data = prep_image(upload_file)
# # # # # # # # # # # # #         response = get_response_nutrition(image_data, input_prompt_nutrition)
# # # # # # # # # # # # #         st.subheader("Nutrition AI: ")
# # # # # # # # # # # # #         st.write(response)

# # # # # # # # # # # # # #If choice is diet planner
# # # # # # # # # # # # # if section_choice1 == "Diet Planner":

# # # # # # # # # # # # #     #Prompt Template
# # # # # # # # # # # # #     input_prompt_diet = """
# # # # # # # # # # # # #     You are an expert Nutritionist. 
# # # # # # # # # # # # #     If the input contains list of items like fruits or vegetables, you have to give diet plan and suggest
# # # # # # # # # # # # #     breakfast, lunch, dinner wrt given item.
# # # # # # # # # # # # #     If the input contains numbers, you have to suggest diet plan for breakfast, luncg=h, dinner within
# # # # # # # # # # # # #     given number of calorie for the whole day.

# # # # # # # # # # # # #     Return the response using markdown.

# # # # # # # # # # # # #     """
# # # # # # # # # # # # #     ##if the button is clicked
# # # # # # # # # # # # #     input_diet = st.text_area(" Input the list of items that you have at home and get diet plan! OR \
# # # # # # # # # # # # #                               Input how much calorie you want to intake perday?:")
# # # # # # # # # # # # #     submit1 = st.button("Plan my Diet!")
# # # # # # # # # # # # #     if submit1:
# # # # # # # # # # # # #         response = get_response_diet(input_prompt_diet, input_diet)
# # # # # # # # # # # # #         st.subheader("Diet AI: ")
# # # # # # # # # # # # #         st.write(response)




# # # # # # # # # # # # # Import libraries
# # # # # # # # # # # # from dotenv import load_dotenv
# # # # # # # # # # # # import os
# # # # # # # # # # # # import google.generativeai as genai
# # # # # # # # # # # # from PIL import Image
# # # # # # # # # # # # import streamlit as st

# # # # # # # # # # # # # Load API Key
# # # # # # # # # # # # load_dotenv()
# # # # # # # # # # # # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # # # # # # # # # # # # Function to load Google Gemini Pro model and get response
# # # # # # # # # # # # def get_response_diet(prompt, user_input):
# # # # # # # # # # # #     model = genai.GenerativeModel('gemini-pro')
# # # # # # # # # # # #     response = model.generate_content([prompt, user_input])
# # # # # # # # # # # #     return response.text

# # # # # # # # # # # # # Function to load Google Gemini Vision model and get response
# # # # # # # # # # # # def get_response_nutrition(image_parts, prompt):
# # # # # # # # # # # #     model = genai.GenerativeModel('gemini-pro-vision')
# # # # # # # # # # # #     response = model.generate_content([prompt] + image_parts)
# # # # # # # # # # # #     return response.text

# # # # # # # # # # # # # Preprocess image data
# # # # # # # # # # # # def prep_image(uploaded_file):
# # # # # # # # # # # #     if uploaded_file is not None:
# # # # # # # # # # # #         bytes_data = uploaded_file.getvalue()
# # # # # # # # # # # #         image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
# # # # # # # # # # # #         return image_parts
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         raise FileNotFoundError("No file uploaded!")

# # # # # # # # # # # # # Configuring Streamlit App
# # # # # # # # # # # # st.image('Nutritionist/logo.jpg', width=70)
# # # # # # # # # # # # st.header("Health: Nutrition Calculator & Diet Planner")

# # # # # # # # # # # # # User selects section
# # # # # # # # # # # # section_choice1 = st.radio("Choose Section:", ("Nutrition Calculator", "Diet Planner"))

# # # # # # # # # # # # # Nutrition Calculator Section
# # # # # # # # # # # # if section_choice1 == "Nutrition Calculator":
# # # # # # # # # # # #     upload_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
# # # # # # # # # # # #     if upload_file is not None:
# # # # # # # # # # # #         image = Image.open(upload_file)
# # # # # # # # # # # #         st.image(image, caption="Uploaded Image", use_column_width=True)

# # # # # # # # # # # #     input_prompt_nutrition = """
# # # # # # # # # # # #     You are an expert Nutritionist. Analyze the food items in the image and determine the total nutritional value.
# # # # # # # # # # # #     Provide a detailed breakdown of each food item, including:

# # # # # # # # # # # #     | Food Item | Serving Size | Calories | Protein (g) | Fat (g) | Carbs (g) | Fiber (g) | Vitamin B-12 | Vitamin B-6 | Iron | Zinc | Magnesium |
# # # # # # # # # # # #     |-----------|-------------|----------|-------------|---------|----------|----------|-------------|------------|------|------|----------|

# # # # # # # # # # # #     Return the response as a formatted markdown table.
# # # # # # # # # # # #     """

# # # # # # # # # # # #     if st.button("Calculate Nutrition Value!"):
# # # # # # # # # # # #         if upload_file:
# # # # # # # # # # # #             image_data = prep_image(upload_file)
# # # # # # # # # # # #             response = get_response_nutrition(image_data, input_prompt_nutrition)
# # # # # # # # # # # #             st.subheader("Nutrition AI:")
# # # # # # # # # # # #             st.markdown(response)
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             st.error("Please upload an image first.")

# # # # # # # # # # # # # Diet Planner Section
# # # # # # # # # # # # if section_choice1 == "Diet Planner":
# # # # # # # # # # # #     input_prompt_diet = """
# # # # # # # # # # # #     You are an expert Nutritionist.

# # # # # # # # # # # #     - If the input contains a list of items like fruits or vegetables, suggest a diet plan including breakfast, lunch, and dinner based on the given items.
# # # # # # # # # # # #     - If the input contains numbers, suggest a diet plan for breakfast, lunch, and dinner within the specified calorie limit for the entire day.

# # # # # # # # # # # #     Return the response using markdown for readability.
# # # # # # # # # # # #     """

# # # # # # # # # # # #     input_diet = st.text_area("Enter the list of food items you have or specify your daily calorie goal:")

# # # # # # # # # # # #     if st.button("Plan my Diet!"):
# # # # # # # # # # # #         if input_diet.strip():
# # # # # # # # # # # #             response = get_response_diet(input_prompt_diet, input_diet)
# # # # # # # # # # # #             st.subheader("Diet AI:")
# # # # # # # # # # # #             st.markdown(response)
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             st.error("Please enter a food list or a calorie goal.")





# # # # # # # # # # Import libraries
# # # # # # # # # from dotenv import load_dotenv
# # # # # # # # # import os
# # # # # # # # # import google.generativeai as genai
# # # # # # # # # from PIL import Image
# # # # # # # # # import streamlit as st

# # # # # # # # # # Load API Key
# # # # # # # # # load_dotenv()
# # # # # # # # # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # # # # # # # # # Function to load Google Gemini Pro model and get response
# # # # # # # # # def get_response_diet(prompt, user_input):
# # # # # # # # #     model = genai.GenerativeModel('gemini-pro')
# # # # # # # # #     response = model.generate_content([prompt, user_input])
# # # # # # # # #     return response.text

# # # # # # # # # # Function to load Google Gemini Vision model and get response
# # # # # # # # # def get_response_nutrition(image_parts, prompt):
# # # # # # # # #     model = genai.GenerativeModel('gemini-pro-vision')
# # # # # # # # #     response = model.generate_content([prompt, {"image": image_parts}])
# # # # # # # # #     return response.text

# # # # # # # # # # Preprocess image data
# # # # # # # # # def prep_image(uploaded_file):
# # # # # # # # #     if uploaded_file is not None:
# # # # # # # # #         bytes_data = uploaded_file.getvalue()
# # # # # # # # #         image_parts = {"mime_type": uploaded_file.type, "data": bytes_data}
# # # # # # # # #         return image_parts
# # # # # # # # #     else:
# # # # # # # # #         return None

# # # # # # # # # # Configuring Streamlit App
# # # # # # # # # st.image('logo (1).jpg', width=70)
# # # # # # # # # st.header("Health: Nutrition Calculator & Diet Planner")

# # # # # # # # # # Initialize session state for responses
# # # # # # # # # if "nutrition_response" not in st.session_state:
# # # # # # # # #     st.session_state.nutrition_response = ""
# # # # # # # # # if "diet_response" not in st.session_state:
# # # # # # # # #     st.session_state.diet_response = ""

# # # # # # # # # # User selects section
# # # # # # # # # section_choice1 = st.radio("Choose Section:", ("Nutrition Calculator", "Diet Planner"))

# # # # # # # # # # Nutrition Calculator Section
# # # # # # # # # if section_choice1 == "Nutrition Calculator":
# # # # # # # # #     upload_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
# # # # # # # # #     if upload_file is not None:
# # # # # # # # #         image = Image.open(upload_file)
# # # # # # # # #         st.image(image, caption="Uploaded Image", use_column_width=True)

# # # # # # # # #     input_prompt_nutrition = """
# # # # # # # # #     You are an expert Nutritionist. Analyze the food items in the image and determine the total nutritional value.
# # # # # # # # #     Provide a detailed breakdown of each food item, including:

# # # # # # # # #     | Food Item | Serving Size | Calories | Protein (g) | Fat (g) | Carbs (g) | Fiber (g) | Vitamin B-12 | Vitamin B-6 | Iron | Zinc | Magnesium |
# # # # # # # # #     |-----------|-------------|----------|-------------|---------|----------|----------|-------------|------------|------|------|----------|

# # # # # # # # #     Return the response as a formatted markdown table.
# # # # # # # # #     """

# # # # # # # # #     if st.button("Calculate Nutrition Value!"):
# # # # # # # # #         if upload_file:
# # # # # # # # #             image_data = prep_image(upload_file)
# # # # # # # # #             if image_data:
# # # # # # # # #                 response = get_response_nutrition(image_data, input_prompt_nutrition)
# # # # # # # # #                 st.session_state.nutrition_response = response
# # # # # # # # #         else:
# # # # # # # # #             st.error("Please upload an image first.")

# # # # # # # # #     # Display stored response
# # # # # # # # #     if st.session_state.nutrition_response:
# # # # # # # # #         st.subheader("Nutrition AI:")
# # # # # # # # #         st.markdown(st.session_state.nutrition_response)

# # # # # # # # # # Diet Planner Section
# # # # # # # # # if section_choice1 == "Diet Planner":
# # # # # # # # #     input_prompt_diet = """
# # # # # # # # #     You are an expert Nutritionist.

# # # # # # # # #     - If the input contains a list of items like fruits or vegetables, suggest a diet plan including breakfast, lunch, and dinner based on the given items.
# # # # # # # # #     - If the input contains numbers, suggest a diet plan for breakfast, lunch, and dinner within the specified calorie limit for the entire day.

# # # # # # # # #     Return the response using markdown for readability.
# # # # # # # # #     """

# # # # # # # # #     input_diet = st.text_area("Enter the list of food items you have or specify your daily calorie goal:")

# # # # # # # # #     if st.button("Plan my Diet!"):
# # # # # # # # #         if input_diet.strip():
# # # # # # # # #             response = get_response_diet(input_prompt_diet, input_diet)
# # # # # # # # #             st.session_state.diet_response = response
# # # # # # # # #         else:
# # # # # # # # #             st.error("Please enter a food list or a calorie goal.")

# # # # # # # # #     # Display stored response
# # # # # # # # #     if st.session_state.diet_response:
# # # # # # # # #         st.subheader("Diet AI:")
# # # # # # # # #         st.markdown(st.session_state.diet_response)





# # # # # # # # # Import libraries
# # # # # # # # from dotenv import load_dotenv
# # # # # # # # import os
# # # # # # # # import google.generativeai as genai
# # # # # # # # from PIL import Image
# # # # # # # # import streamlit as st

# # # # # # # # # Load API Key
# # # # # # # # load_dotenv()
# # # # # # # # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # # # # # # # # Function to load Google Gemini 1.5 Pro model and get diet plan response
# # # # # # # # def get_response_diet(prompt, user_input):
# # # # # # # #     model = genai.GenerativeModel('gemini-1.5-pro-latest')  # Updated model name
# # # # # # # #     response = model.generate_content([prompt, user_input])
# # # # # # # #     return response.text

# # # # # # # # # Function to load Google Gemini 1.5 Pro Vision model and get nutrition analysis
# # # # # # # # def get_response_nutrition(image_parts, prompt):
# # # # # # # #     model = genai.GenerativeModel('gemini-1.5-pro-vision')  # Updated vision model
# # # # # # # #     response = model.generate_content([prompt, {"image": image_parts}])
# # # # # # # #     return response.text

# # # # # # # # # Preprocess image data
# # # # # # # # def prep_image(uploaded_file):
# # # # # # # #     if uploaded_file is not None:
# # # # # # # #         bytes_data = uploaded_file.getvalue()
# # # # # # # #         image_parts = {"mime_type": uploaded_file.type, "data": bytes_data}
# # # # # # # #         return image_parts
# # # # # # # #     else:
# # # # # # # #         return None

# # # # # # # # # Configuring Streamlit App
# # # # # # # # st.image('logo (1).jpg', width=70)
# # # # # # # # st.header("Health: Nutrition Calculator & Diet Planner")

# # # # # # # # # Initialize session state for responses
# # # # # # # # if "nutrition_response" not in st.session_state:
# # # # # # # #     st.session_state.nutrition_response = ""
# # # # # # # # if "diet_response" not in st.session_state:
# # # # # # # #     st.session_state.diet_response = ""

# # # # # # # # # User selects section
# # # # # # # # section_choice1 = st.radio("Choose Section:", ("Nutrition Calculator", "Diet Planner"))

# # # # # # # # # Nutrition Calculator Section
# # # # # # # # if section_choice1 == "Nutrition Calculator":
# # # # # # # #     upload_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
# # # # # # # #     if upload_file is not None:
# # # # # # # #         image = Image.open(upload_file)
# # # # # # # #         st.image(image, caption="Uploaded Image", use_column_width=True)

# # # # # # # #     input_prompt_nutrition = """
# # # # # # # #     You are an expert Nutritionist. Analyze the food items in the image and determine the total nutritional value.
# # # # # # # #     Provide a detailed breakdown of each food item, including:

# # # # # # # #     | Food Item | Serving Size | Calories | Protein (g) | Fat (g) | Carbs (g) | Fiber (g) | Vitamin B-12 | Vitamin B-6 | Iron | Zinc | Magnesium |
# # # # # # # #     |-----------|-------------|----------|-------------|---------|----------|----------|-------------|------------|------|------|----------|

# # # # # # # #     Return the response as a formatted markdown table.
# # # # # # # #     """

# # # # # # # #     if st.button("Calculate Nutrition Value!"):
# # # # # # # #         if upload_file:
# # # # # # # #             image_data = prep_image(upload_file)
# # # # # # # #             if image_data:
# # # # # # # #                 response = get_response_nutrition(image_data, input_prompt_nutrition)
# # # # # # # #                 st.session_state.nutrition_response = response
# # # # # # # #         else:
# # # # # # # #             st.error("Please upload an image first.")

# # # # # # # #     # Display stored response
# # # # # # # #     if st.session_state.nutrition_response:
# # # # # # # #         st.subheader("Nutrition AI:")
# # # # # # # #         st.markdown(st.session_state.nutrition_response)

# # # # # # # # # Diet Planner Section
# # # # # # # # if section_choice1 == "Diet Planner":
# # # # # # # #     input_prompt_diet = """
# # # # # # # #     You are an expert Nutritionist.

# # # # # # # #     - If the input contains a list of items like fruits or vegetables, suggest a diet plan including breakfast, lunch, and dinner based on the given items.
# # # # # # # #     - If the input contains numbers, suggest a diet plan for breakfast, lunch, and dinner within the specified calorie limit for the entire day.

# # # # # # # #     Return the response using markdown for readability.
# # # # # # # #     """

# # # # # # # #     input_diet = st.text_area("Enter the list of food items you have or specify your daily calorie goal:")

# # # # # # # #     if st.button("Plan my Diet!"):
# # # # # # # #         if input_diet.strip():
# # # # # # # #             response = get_response_diet(input_prompt_diet, input_diet)
# # # # # # # #             st.session_state.diet_response = response
# # # # # # # #         else:
# # # # # # # #             st.error("Please enter a food list or a calorie goal.")

# # # # # # # #     # Display stored response
# # # # # # # #     if st.session_state.diet_response:
# # # # # # # #         st.subheader("Diet AI:")
# # # # # # # #         st.markdown(st.session_state.diet_response)






# # # # # # # # Import libraries
# # # # # # # from dotenv import load_dotenv
# # # # # # # import os
# # # # # # # import google.generativeai as genai
# # # # # # # from PIL import Image
# # # # # # # import streamlit as st

# # # # # # # # Load API Key
# # # # # # # load_dotenv()
# # # # # # # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # # # # # # # Function to load Google Gemini 1.5 Pro model and get response
# # # # # # # def get_response_diet(prompt, user_input):
# # # # # # #     model = genai.GenerativeModel('gemini-1.5-pro')  # Updated model
# # # # # # #     response = model.generate_content([prompt, user_input])
# # # # # # #     return response.text

# # # # # # # # Function to load Google Gemini 1.5 Pro Vision model and get nutrition analysis
# # # # # # # def get_response_nutrition(image_parts, prompt):
# # # # # # #     model = genai.GenerativeModel('gemini-1.5-pro-vision')  # Updated vision model
# # # # # # #     response = model.generate_content([
# # # # # # #         prompt,
# # # # # # #         {"parts": [{"inline_data": image_parts}]}
# # # # # # #     ])
# # # # # # #     return response.text

# # # # # # # # Preprocess image data correctly
# # # # # # # def prep_image(uploaded_file):
# # # # # # #     if uploaded_file is not None:
# # # # # # #         bytes_data = uploaded_file.getvalue()
# # # # # # #         image_parts = {"mime_type": uploaded_file.type, "data": bytes_data}  # Correct format
# # # # # # #         return image_parts
# # # # # # #     else:
# # # # # # #         return None

# # # # # # # # Configuring Streamlit App
# # # # # # # st.image('logo (1).jpg', width=70)
# # # # # # # st.header("Health: Nutrition Calculator & Diet Planner")

# # # # # # # # Initialize session state for responses
# # # # # # # if "nutrition_response" not in st.session_state:
# # # # # # #     st.session_state.nutrition_response = ""
# # # # # # # if "diet_response" not in st.session_state:
# # # # # # #     st.session_state.diet_response = ""

# # # # # # # # User selects section
# # # # # # # section_choice1 = st.radio("Choose Section:", ("Nutrition Calculator", "Diet Planner"))

# # # # # # # # Nutrition Calculator Section
# # # # # # # if section_choice1 == "Nutrition Calculator":
# # # # # # #     upload_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
# # # # # # #     if upload_file is not None:
# # # # # # #         image = Image.open(upload_file)
# # # # # # #         st.image(image, caption="Uploaded Image", use_column_width=True)

# # # # # # #     input_prompt_nutrition = """
# # # # # # #     You are an expert Nutritionist. Analyze the food items in the image and determine the total nutritional value.
# # # # # # #     Provide a detailed breakdown of each food item, including:

# # # # # # #     | Food Item | Serving Size | Calories | Protein (g) | Fat (g) | Carbs (g) | Fiber (g) | Vitamin B-12 | Vitamin B-6 | Iron | Zinc | Magnesium |
# # # # # # #     |-----------|-------------|----------|-------------|---------|----------|----------|-------------|------------|------|------|----------|

# # # # # # #     Return the response as a formatted markdown table.
# # # # # # #     """

# # # # # # #     if st.button("Calculate Nutrition Value!"):
# # # # # # #         if upload_file:
# # # # # # #             image_data = prep_image(upload_file)
# # # # # # #             if image_data:
# # # # # # #                 response = get_response_nutrition(image_data, input_prompt_nutrition)
# # # # # # #                 st.session_state.nutrition_response = response
# # # # # # #         else:
# # # # # # #             st.error("Please upload an image first.")

# # # # # # #     # Display stored response
# # # # # # #     if st.session_state.nutrition_response:
# # # # # # #         st.subheader("Nutrition AI:")
# # # # # # #         st.markdown(st.session_state.nutrition_response)

# # # # # # # # Diet Planner Section
# # # # # # # if section_choice1 == "Diet Planner":
# # # # # # #     input_prompt_diet = """
# # # # # # #     You are an expert Nutritionist.

# # # # # # #     - If the input contains a list of items like fruits or vegetables, suggest a diet plan including breakfast, lunch, and dinner based on the given items.
# # # # # # #     - If the input contains numbers, suggest a diet plan for breakfast, lunch, and dinner within the specified calorie limit for the entire day.

# # # # # # #     Return the response using markdown for readability.
# # # # # # #     """

# # # # # # #     input_diet = st.text_area("Enter the list of food items you have or specify your daily calorie goal:")

# # # # # # #     if st.button("Plan my Diet!"):
# # # # # # #         if input_diet.strip():
# # # # # # #             response = get_response_diet(input_prompt_diet, input_diet)
# # # # # # #             st.session_state.diet_response = response
# # # # # # #         else:
# # # # # # #             st.error("Please enter a food list or a calorie goal.")

# # # # # # #     # Display stored response
# # # # # # #     if st.session_state.diet_response:
# # # # # # #         st.subheader("Diet AI:")
# # # # # # #         st.markdown(st.session_state.diet_response)





















# # # # # # import streamlit as st
# # # # # # import google.generativeai as genai
# # # # # # from PIL import Image
# # # # # # from io import BytesIO
# # # # # # import base64

# # # # # # # Configure Gemini API
# # # # # # API_KEY = "AIzaSyALaefBpHpZXpgA_PISFn2BITx1xup4YDo"
# # # # # # genai.configure(api_key=API_KEY)
# # # # # # model = genai.GenerativeModel("gemini-pro-vision")

# # # # # # def get_response_nutrition(image_data, input_prompt_nutrition):
# # # # # #     prompt = {"text": input_prompt_nutrition}
    
# # # # # #     # Format the image data correctly
# # # # # #     image_parts = {
# # # # # #         "mime_type": "image/jpeg",  # Ensure correct MIME type
# # # # # #         "data": image_data  # Pass the image in byte format
# # # # # #     }
    
# # # # # #     # Call the Gemini model
# # # # # #     response = model.generate_content([
# # # # # #         prompt,
# # # # # #         {"inline_data": image_parts}
# # # # # #     ])
    
# # # # # #     return response.text if response else "No response received."

# # # # # # def image_to_bytes(image):
# # # # # #     img_byte_arr = BytesIO()
# # # # # #     image.save(img_byte_arr, format='JPEG')  # Convert image to bytes
# # # # # #     return img_byte_arr.getvalue()

# # # # # # def main():
# # # # # #     st.title("AI-Powered Nutrition Analysis")
# # # # # #     st.write("Upload an image of food to get its nutritional information.")
    
# # # # # #     uploaded_file = st.file_uploader("Choose a food image...", type=["jpg", "jpeg", "png"])
# # # # # #     input_prompt_nutrition = st.text_area("Enter additional details or leave blank:")
    
# # # # # #     if uploaded_file is not None:
# # # # # #         image = Image.open(uploaded_file)
# # # # # #         st.image(image, caption="Uploaded Image", use_column_width=True)
        
# # # # # #         image_data = image_to_bytes(image)  # Convert image to bytes
        
# # # # # #         if st.button("Analyze Nutrition"):
# # # # # #             response = get_response_nutrition(image_data, input_prompt_nutrition)
# # # # # #             st.subheader("Nutrition Analysis Result")
# # # # # #             st.write(response)

# # # # # # if __name__ == "__main__":
# # # # # #     main()












# # # # # import google.generativeai as genai

# # # # # # Configure API key
# # # # # genai.configure(api_key="AIzaSyALaefBpHpZXpgA_PISFn2BITx1xup4YDo")

# # # # # # Use Gemini 1.5 Pro instead of the deprecated 1.0 Vision
# # # # # model = genai.GenerativeModel("gemini-1.5-pro")

# # # # # # Example request
# # # # # response = model.generate_content(["Describe this image:", {"image_data": image_parts}])

# # # # # # Print the response
# # # # # print(response.text)




# # # # import google.generativeai as genai
# # # # import base64

# # # # # Configure API key
# # # # genai.configure(api_key="AIzaSyALaefBpHpZXpgA_PISFn2BITx1xup4YDo")

# # # # # Function to encode image as base64
# # # # def encode_image(image_path):
# # # #     with open(image_path, "rb") as image_file:
# # # #         return base64.b64encode(image_file.read()).decode("utf-8")

# # # # # Provide the path to your image
# # # # image_path = "logo (1).jpg"

# # # # # Encode the image
# # # # image_parts = {
# # # #     "mime_type": "image/jpeg",  # Change based on image type (e.g., "image/png")
# # # #     "data": encode_image(image_path)
# # # # }

# # # # # Initialize the model
# # # # model = genai.GenerativeModel("gemini-1.5-pro")

# # # # # Generate response with the image
# # # # response = model.generate_content([
# # # #     "Describe this image:",
# # # #     {"inline_data": image_parts}  # Include image in the request
# # # # ])

# # # # # Print the response
# # # # print(response.text)







# # # import streamlit as st
# # # import google.generativeai as genai
# # # from PIL import Image
# # # from io import BytesIO
# # # import base64

# # # # Configure Gemini API
# # # API_KEY = "AIzaSyALaefBpHpZXpgA_PISFn2BITx1xup4YDo"
# # # genai.configure(api_key=API_KEY)
# # # model = genai.GenerativeModel("gemini-1.5-flash")  # Updated model

# # # def get_response_nutrition(image_data, input_prompt_nutrition):
# # #     prompt = {"text": input_prompt_nutrition}
    
# # #     # Format the image data correctly
# # #     image_parts = {
# # #         "mime_type": "image/jpeg",  # Ensure correct MIME type
# # #         "data": image_data  # Pass the image in byte format
# # #     }
    
# # #     # Call the Gemini model
# # #     response = model.generate_content([
# # #         prompt,
# # #         {"inline_data": image_parts}
# # #     ])
    
# # #     return response.text if response else "No response received."

# # # def image_to_bytes(image):
# # #     img_byte_arr = BytesIO()
# # #     image.save(img_byte_arr, format='JPEG')  # Convert image to bytes
# # #     return img_byte_arr.getvalue()

# # # def main():
# # #     st.title("AI-Powered Nutrition Analysis")
# # #     st.write("Upload an image of food to get its nutritional information.")
    
# # #     uploaded_file = st.file_uploader("Choose a food image...", type=["jpg", "jpeg", "png"])
# # #     input_prompt_nutrition = st.text_area("Enter additional details or leave blank:")
    
# # #     if uploaded_file is not None:
# # #         image = Image.open(uploaded_file)
# # #         st.image(image, caption="Uploaded Image", use_column_width=True)
        
# # #         image_data = image_to_bytes(image)  # Convert image to bytes
        
# # #         if st.button("Analyze Nutrition"):
# # #             response = get_response_nutrition(image_data, input_prompt_nutrition)
# # #             st.subheader("Nutrition Analysis Result")
# # #             st.write(response)

# # # if __name__ == "__main__":
# # #     main()






# # from dotenv import load_dotenv
# # import os
# # import google.generativeai as genai
# # from PIL import Image
# # import streamlit as st

# # # Load API Key
# # load_dotenv()
# # genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # # Function to get response from Gemini 1.5 Flash model
# # def get_response_diet(prompt, user_input):
# #     model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model
# #     response = model.generate_content([prompt, user_input])
# #     return response.text

# # # Function to get nutrition analysis using Gemini 1.5 Flash Vision model
# # def get_response_nutrition(image_parts, prompt):
# #     model = genai.GenerativeModel('gemini-1.5-flash-vision')  # Updated vision model
# #     response = model.generate_content([
# #         prompt,
# #         {"parts": [{"inline_data": image_parts}]}
# #     ])
# #     return response.text

# # # Function to preprocess image data
# # def prep_image(uploaded_file):
# #     if uploaded_file is not None:
# #         bytes_data = uploaded_file.getvalue()
# #         image_parts = {"mime_type": uploaded_file.type, "data": bytes_data}  # Correct format
# #         return image_parts
# #     return None

# # # Configuring Streamlit App
# # st.image('logo (1).jpg', width=70)
# # st.header("Health: Nutrition Calculator & Diet Planner")

# # # Initialize session state for responses
# # if "nutrition_response" not in st.session_state:
# #     st.session_state.nutrition_response = ""
# # if "diet_response" not in st.session_state:
# #     st.session_state.diet_response = ""

# # # User selects section
# # section_choice = st.radio("Choose Section:", ("Nutrition Calculator", "Diet Planner"))

# # # Nutrition Calculator Section
# # if section_choice == "Nutrition Calculator":
# #     upload_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
# #     if upload_file is not None:
# #         image = Image.open(upload_file)
# #         st.image(image, caption="Uploaded Image", use_column_width=True)

# #     input_prompt_nutrition = (
# #         "You are an expert Nutritionist. Analyze the food items in the image and determine the total nutritional value.\n"
# #         "Provide a detailed breakdown of each food item, including:\n\n"
# #         "| Food Item | Serving Size | Calories | Protein (g) | Fat (g) | Carbs (g) | Fiber (g) | Vitamin B-12 | Vitamin B-6 | Iron | Zinc | Magnesium |\n"
# #         "|-----------|-------------|----------|-------------|---------|----------|----------|-------------|------------|------|------|----------|\n\n"
# #         "Return the response as a formatted markdown table."
# #     )

# #     if st.button("Calculate Nutrition Value!"):
# #         if upload_file:
# #             image_data = prep_image(upload_file)
# #             if image_data:
# #                 response = get_response_nutrition(image_data, input_prompt_nutrition)
# #                 st.session_state.nutrition_response = response
# #         else:
# #             st.error("Please upload an image first.")

# #     if st.session_state.nutrition_response:
# #         st.subheader("Nutrition AI:")
# #         st.markdown(st.session_state.nutrition_response)

# # # Diet Planner Section
# # if section_choice == "Diet Planner":
# #     input_prompt_diet = (
# #         "You are an expert Nutritionist.\n\n"
# #         "- If the input contains a list of items like fruits or vegetables, suggest a diet plan including breakfast, lunch, and dinner based on the given items.\n"
# #         "- If the input contains numbers, suggest a diet plan for breakfast, lunch, and dinner within the specified calorie limit for the entire day.\n\n"
# #         "Return the response using markdown for readability."
# #     )

# #     input_diet = st.text_area("Enter the list of food items you have or specify your daily calorie goal:")

# #     if st.button("Plan my Diet!"):
# #         if input_diet.strip():
# #             response = get_response_diet(input_prompt_diet, input_diet)
# #             st.session_state.diet_response = response
# #         else:
# #             st.error("Please enter a food list or a calorie goal.")

# #     if st.session_state.diet_response:
# #         st.subheader("Diet AI:")
# #         st.markdown(st.session_state.diet_response)







# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
# from PIL import Image
# import streamlit as st

# # Load API Key from .env file
# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Function to get response from Gemini 1.5 Flash model (Diet Planning)
# def get_response_diet(prompt, user_input):
#     try:
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         response = model.generate_content([prompt, user_input])
#         return response.text
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Function to get nutrition analysis using Gemini 1.5 Flash Vision model
# def get_response_nutrition(image_parts, prompt):
#     try:
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         response = model.generate_content([
#             {"text": prompt},  # Ensure correct prompt format
#             {"inline_data": image_parts}  # Correctly passing image parts
#         ])
#         return response.text
#     except Exception as e:
#         return f"Error: {str(e)}"

# # Function to preprocess image data
# def prep_image(uploaded_file):
#     if uploaded_file is not None:
#         bytes_data = uploaded_file.getvalue()
#         image_parts = {"mime_type": uploaded_file.type, "data": bytes_data}
#         return image_parts
#     return None

# # Streamlit UI Configuration
# st.image('logo (1).jpg', width=70)
# st.header("🍎 Health: Nutrition Calculator & Diet Planner")

# # Initialize session state
# if "nutrition_response" not in st.session_state:
#     st.session_state.nutrition_response = ""
# if "diet_response" not in st.session_state:
#     st.session_state.diet_response = ""

# # User selects section
# section_choice = st.radio("Choose Section:", ("🥗 Nutrition Calculator", "📋 Diet Planner"))

# # 🍎 **Nutrition Calculator Section**
# if section_choice == "🥗 Nutrition Calculator":
#     upload_file = st.file_uploader("Upload an image of your meal...", type=["jpg", "jpeg", "png"])

#     if upload_file is not None:
#         image = Image.open(upload_file)
#         st.image(image, caption="Uploaded Image", use_column_width=True)

#     input_prompt_nutrition = (
#         "You are an expert Nutritionist. Analyze the food items in the image and determine the total nutritional value.\n"
#         "Provide a detailed breakdown of each food item, including:\n\n"
#         "| Food Item | Serving Size | Calories | Protein (g) | Fat (g) | Carbs (g) | Fiber (g) | Vitamin B-12 | Vitamin B-6 | Iron | Zinc | Magnesium |\n"
#         "|-----------|-------------|----------|-------------|---------|----------|----------|-------------|------------|------|------|----------|\n\n"
#         "Return the response as a formatted markdown table."
#     )

#     if st.button("Calculate Nutrition Value!"):
#         if upload_file:
#             image_data = prep_image(upload_file)
#             if image_data:
#                 response = get_response_nutrition(image_data, input_prompt_nutrition)
#                 st.session_state.nutrition_response = response
#             else:
#                 st.error("Image processing failed. Please try again.")
#         else:
#             st.error("Please upload an image first.")

#     if st.session_state.nutrition_response:
#         st.subheader("🍽️ Nutrition Breakdown:")
#         st.markdown(st.session_state.nutrition_response)

# # 📋 **Diet Planner Section**
# if section_choice == "📋 Diet Planner":
#     input_prompt_diet = (
#         "You are an expert Nutritionist.\n\n"
#         "- If the input contains a list of items like fruits or vegetables, suggest a diet plan including breakfast, lunch, and dinner based on the given items.\n"
#         "- If the input contains numbers, suggest a diet plan for breakfast, lunch, and dinner within the specified calorie limit for the entire day.\n\n"
#         "Return the response using markdown for readability."
#     )

#     input_diet = st.text_area("Enter a list of food items or your daily calorie goal:")

#     if st.button("Plan my Diet!"):
#         if input_diet.strip():
#             response = get_response_diet(input_prompt_diet, input_diet)
#             st.session_state.diet_response = response
#         else:
#             st.error("Please enter a food list or a calorie goal.")

#     if st.session_state.diet_response:
#         st.subheader("🥗 Personalized Diet Plan:")
#         st.markdown(st.session_state.diet_response)



from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image
import streamlit as st

# Load API Key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini 1.5 Flash model (Diet Planning)
def get_response_diet(prompt, user_input):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([prompt, user_input])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to get nutrition analysis using Gemini 1.5 Flash Vision model
def get_response_nutrition(image_parts, prompt):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([
            {"text": prompt},
            {"inline_data": image_parts}
        ])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to preprocess image data
def prep_image(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = {"mime_type": "image/jpeg", "data": bytes_data}
        return image_parts
    return None

# Streamlit UI Configuration
st.image('logo (1).jpg', width=70)
st.header("🍎 Health: Nutrition Calculator & Diet Planner")

# Initialize session state
if "nutrition_response" not in st.session_state:
    st.session_state.nutrition_response = ""
if "diet_response" not in st.session_state:
    st.session_state.diet_response = ""

# User selects section
section_choice = st.radio("Choose Section:", ("🥗 Nutrition Calculator", "📋 Diet Planner"))

# 🍎 **Nutrition Calculator Section**
if section_choice == "🥗 Nutrition Calculator":
    st.write("📷 **Capture an image of your meal using the camera**")
    
    # Use camera input instead of file uploader
    captured_image = st.camera_input("Take a picture of your meal")

    if captured_image is not None:
        image = Image.open(captured_image)
        st.image(image, caption="Captured Image", use_column_width=True)

    input_prompt_nutrition = (
        "You are an expert Nutritionist. Analyze the food items in the image and determine the total nutritional value.\n"
        "Provide a detailed breakdown of each food item, including:\n\n"
        "| Food Item | Serving Size | Calories | Protein (g) | Fat (g) | Carbs (g) | Fiber (g) | Vitamin B-12 | Vitamin B-6 | Iron | Zinc | Magnesium |\n"
        "|-----------|-------------|----------|-------------|---------|----------|----------|-------------|------------|------|------|----------|\n\n"
        "Return the response as a formatted markdown table."
    )

    if st.button("Calculate Nutrition Value!"):
        if captured_image:
            image_data = prep_image(captured_image)
            if image_data:
                response = get_response_nutrition(image_data, input_prompt_nutrition)
                st.session_state.nutrition_response = response
            else:
                st.error("Image processing failed. Please try again.")
        else:
            st.error("Please capture an image first.")

    if st.session_state.nutrition_response:
        st.subheader("🍽️ Nutrition Breakdown:")
        st.markdown(st.session_state.nutrition_response)

# 📋 **Diet Planner Section**
if section_choice == "📋 Diet Planner":
    input_prompt_diet = (
        "You are an expert Nutritionist.\n\n"
        "- If the input contains a list of items like fruits or vegetables, suggest a diet plan including breakfast, lunch, and dinner based on the given items.\n"
        "- If the input contains numbers, suggest a diet plan for breakfast, lunch, and dinner within the specified calorie limit for the entire day.\n\n"
        "Return the response using markdown for readability."
    )

    input_diet = st.text_area("Enter a list of food items or your daily calorie goal:")

    if st.button("Plan my Diet!"):
        if input_diet.strip():
            response = get_response_diet(input_prompt_diet, input_diet)
            st.session_state.diet_response = response
        else:
            st.error("Please enter a food list or a calorie goal.")

    if st.session_state.diet_response:
        st.subheader("🥗 Personalized Diet Plan:")
        st.markdown(st.session_state.diet_response)






