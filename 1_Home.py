import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojies here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Tommy's Projects", page_icon=":construction:", layout="wide")

# Function to make API request to the lottieurl to retrieve the animation.
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/fcdaf5c1-6ee2-4f27-aea4-6c45f2e4c63c/8Ter1PFE9B.json")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I'm Tommy :wave:")
    st.title("A Security Professional from Minnesota")
    st.write("I'm passionate about all things Cyber Security and Information Technology.")
    st.write("[LinkedIn >](https://www.linkedin.com/in/thomas-gagliardi-92bbb8192/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column, = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            In my professional work I'm focused currently on:
            - Strengthening policies and procedures to better align with industry standards.
            - Automating repetitive processes using PowerShell.
            - Creating TTPs for compliance related tasks.
            - Responding to customer risk assessments as they relate to our cloud-hosted applications.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

    # ---- PROJECTS ----
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        st.write(
            """
            My most recent projects demonstrate API use best practices:
            - Virus Total Integration into Streamlit
            - ChatGPT Integration into Discord
            """
        )
        if st.button("Projects"):
            st.switch_page("pages/2_ChatGPT Discord Bot.py")

    # ---- PROJECTS ----
    with st.container():
        st.write("---")
        st.header("Certifications")
        st.write(
            """
            - AZ-900
            - CompTIA Security+ CE
            - DoD Secret Security Clearance
            - Army PKI Trusted Agent Training v2
            - Army PKI Enhanced Trusted Agent Training v2
            - DISA ACAS Version 5.3 (2016)
            - DISA HBSS 201 ePO5.1
            - DISA HBSS 301 ePO5.1
            """
        )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Contact Me!")
    st.write("##")

    # Documentation: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/vannilla7788@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
