import streamlit as st
#header
st.header("Welcome to the Streamlit App")

st.divider()

#title
st.title("welcome to student Application")

st.divider()

#subheader
st.subheader("This is a subheader for additional context")

st.divider()

#text
st.text("This is a simple text element in the Streamlit app.")

st.divider()

#markdown
st.markdown("### ------------ Markdown Section ------------")
st.markdown("This is a **bold** text and this is an *italic* text in markdown.")
st.markdown("*italic text*")
st.markdown("**bold text**")
st.markdown("- item 1\n- item 2")
st.markdown("<h3 style='color:red;'>red text</h3>", unsafe_allow_html=True)

st.divider()

#write method to provide additional details
st.write("hello streamlit")
st.write(123)
st.write([1,2,3,4,5])
st.write({"name":"streamlit","type":"library"})
st.write((10,20,30))

st.divider()

#code
st.code("""
        def add(a,b):
            return a+b
        """, language='python')

st.divider()

#latex
st.latex(r'''
    a^2 + b^2 = c^2
    ''')
#divider method to separate sections or horizontal line
st.divider()

#caption method to add descriptive text below elements
st.caption("This is a caption providing additional information about the content above.")

st.divider()

#button
if st.button("Click Me"):
    st.write("Button Clicked!")
    st.success("You have successfully clicked the button.")
    st.balloons()
else:
    st.write("Button Not Clicked Yet.")
    st.error("connection error")

st.divider()

#text input
name = st.text_input("Enter your name:")
if name=="":
    st.warning("name cannot be empty")
elif not name.isalpha():
    st.error("name should only contain alphabets")  
else:    
    st.success(f"Hello, {name}!")

st.divider()

#number input
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
st.write(f"You are {age} years old.")

st.divider()

#text area
address = st.text_area("Enter your address:")
st.write("Your address is:", address)

st.divider()

#checkbox
if st.checkbox("I agree to the terms and conditions"):
    st.write("Thank you for agreeing!") 
else:
    st.write("You must agree to proceed.")

st.divider()

#radio button method to create radio button options
gender = st.radio("Select your gender:", ("Male", "Female", "Other"))
st.write(f"You selected: {gender}") 

st.divider()

#selectbox
country = st.selectbox("Select your country:", ["India", "USA", "Canada", "UK", "Australia"])
st.write(f"You selected: {country}")

st.divider()

#multiselect
skills = st.multiselect("Select your skills:", ["Python", "Java", "C++", "JavaScript", "HTML", "CSS"])
st.write("You selected:", skills)

st.divider()

#slider
rating = st.slider("Rate your experience:", 0, 10, 5)
st.write(f"You rated: {rating}")

st.divider()

#file uploader
uploaded_file = st.file_uploader("Upload a file:")
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write("Filename:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)
else:
    st.write("No file uploaded yet.")

st.divider()

#form method to create a form for user input
with st.form("student_form"):
    st.write("Please fill out the form:")
    student_name = st.text_input("Student Name:")
    student_age = st.number_input("Student Age:", min_value=0, max_value=120, step=1)
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        st.success("Form submitted successfully!")
        st.write("Name:", student_name)
        st.write("Age:", student_age)

st.divider()

#form submit button method to submit the form data
with st.form("login"):
    st.write("Login Form:")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    login_button = st.form_submit_button("Login")
    if login_button:
        st.success("Login successful!")
        st.write("Welcome,", username)

st.divider()

#columns method to create multiple columns for layout
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Column 1")
    st.write("This is the first column.")
with col2:
    st.header("Column 2")
    st.write("This is the second column.")
with col3:
    st.header("Column 3")
    st.write("This is the third column.")    

st.divider()

#container method to create a container
container = st.container()
container.write("This is inside the container.")
container.button("Container Button")
container.success("Container Success Message")

st.divider()

#table method to display data in tabular format
data = {
    'Name': ['nikhil','nani','varun'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)

st.divider()

#sidebar method to create a sidebar for navigation or additional options
st.sidebar.title("Sidebar Menu")
option=st.sidebar.selectbox("Choose an option:", 
                            ["Home", "About", "contact"])
st.sidebar.write(f"You selected: {option}")

#cache data
@st.cache_data
def load_data():
    return [1,2,3,4]
data = load_data()
st.write("Cached Data:", data)

st.divider()
