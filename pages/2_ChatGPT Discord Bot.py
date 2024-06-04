import requests
import streamlit as st
from streamlit_lottie import st_lottie

# ---- PAGE CONFIGURATION ----
st.set_page_config(page_title="Discord ChatGPT Bot", page_icon=":robot:", layout="wide")

# Function to make API request to the lottieurl to retrieve the animation.
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/26f56764-92bd-4956-81ac-a0e27bbb286d/mAMeXV5J1R.json")
lottie_coding2 = load_lottieurl("https://lottie.host/d71645e6-3fd3-4f45-8d1f-0a89c50e78bb/ff283qERvA.json")
lottie_coding3 = load_lottieurl("https://lottie.host/7f8bd565-6af9-4f5d-a979-4987746d04c9/2yrc2HMbDK.json")

# ---- INTRODUCTION ----
with st.container():
    st.title("Discord ChatGPT Bot Integration")
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    with col1:
        st.header("Introduction")
        st.write("""
                This page contains instructions to build a fully functional Discord chat bot in Python.
                Here you can learn how to create and host a Discord chat bot:
                - from a virtual machine
                - as a container
                - and from the cloud (Azure)

                """
                )
        st.write("""
                This comprehensive guide provides insight into development best practices, API usage in Python,
                 building containers with Docker, and finally using Kubernetes to build infrastructure in the Azure
                 cloud to support our Discord bot.
                 """)
    with col2:
        st_lottie(lottie_coding, height=300, key="python")
    with col3:
        st_lottie(lottie_coding2, height=300, key="docker")
    with col4:
        st_lottie(lottie_coding3, height=300, key="cloud")
st.write("---")

# ---- USE CASE ----
with st.container():
        st.header("Use Case")
        col1, col2= st.columns([1, 1.5])
        with col1:
                st.write("""
                        Initially, the primary use case of this excercise was to demonstrate how API requests should be handled with Python; however, this project
                        evolved and now serves as a great way to better understand hosting web applications from different environments.
                        """)
        st.write("---")
        
# ---- INSTRUCTIONS ----
with st.container():
     st.header("Hosting a Discord bot from a Linux Virtual Machine")
     st.subheader("Requirements")
     st.write("""
        - A CPU/Computer capable of virtualization [How to check?](https://shaileshjha.com/how-to-find-out-if-intel-vt-x-or-amd-v-virtualization-technology-is-supported-in-windows-10-windows-8-windows-vista-or-windows-7-machine/)
        - Virtualization software such as VMware or VirtualBox
        - An [OpenAI](https://openai.com/blog/openai-api) account
        - A [Discord Developer](https://discord.com/developers/docs/intro) account
        """)
     st.write("---")
     st.subheader("Building a Virtual Machine")
     st.write("""
              - Choose a hypervisor. In this guide we will be using [VMware Workstation Pro](https://www.vmware.com/products/workstation-pro.html).
              - Choose an operating system. In my case I chose to use Kali Linux, but you may choose to use any Debian-based linux distribution.
              - To download Kali Linux: navigate to the following directory and download the zip file associated with your hypervisor software: https://www.kali.org/get-kali/#kali-virtual-machines.
              - Extract the downloaded zip file, you may need to download WinRAR to do so.
              - Open VMware Workstation Pro.
              - Select "Open a Virtual Machine".
              - Navigate to the newly extracted zip files and locate the vmdk file.
              - You should now see an option to power on the virtual machine.
              """)
     st.write("---")
     st.subheader("Creating the Python Files")
     st.write("""
              - Power on the virtual machine
              - Download Visual Studio Code (VS Code).
              - Install VS Code.
              - Navigate to your preferred working directory, in our case it will be the Documents folder.
              - Create a folder within the Documents folder, or wherever you please, and name it “Your Project Name”.
              - Launch VS Code, select the “Explorer” icon, and choose the new folder you just created as your working directory.
              """)
     st.write("##")

     # Create a select box to allow users to choose which Python file to view.
     pythoncode = st.selectbox(
          "Python scripts",
          ("main.py", "keep_alive.py", ".env"),
          index=None,
          placeholder="Select a Python script...")
     st.write("Selected: ", pythoncode)
     
     st.code("""
        '''
        Create GusBot in Discord. Leverage both openai and Discord APIs to do so.
        '''

        # import libraries
        from openai import OpenAI
        import discord
        from discord.ext import commands
        import os
        from dotenv import load_dotenv
        from keep_alive import keep_alive

        # functions
        # Create function to make API request to openAI
        def generate_response(prompt):

        client = OpenAI()

        completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                {"role": "system", "content": "You are a helpful Gusbot."},
                {"role": "user", "content": prompt}
                ]
        )

        message = completion.choices[0].message
        return message.content

        # Main function, where the magic happens.
        def main():

        print("Running...")

        # Load environment variable
        load_dotenv()

        # Initialize openai client object
        client = OpenAI()

        # Initialize the API keys from environment
        client.api_key = os.getenv("OPENAI_API_KEY")
        discord_api_key = os.getenv("DISCORD_API_KEY")

        # Run the webserver.
        keep_alive()

        # Create a class for the discord bot
        class BingBot(discord.Client):
                # Override the on_ready method
                async def on_ready(self):
                print("We have logged in as {0.user}".format(self))

                # Override the on_message method
                async def on_message(self, message):
                # Ignore messages from the bot itself
                if message.author == self.user:
                        return
                else:
                        # Generate a response using the message content as prompt
                        response = generate_response(message.content)

                        # Send the response to the same channel as the message
                        await message.channel.send(response)

        # Create an instance of the bot with all intents enabled
        botclient = BingBot(intents=discord.Intents.all())

        # Run the bot with the token
        botclient.run(discord_api_key)

        # Run the main function if "main.py" is executed directly.
        if __name__ == "__main__":
        main()
                """)

# Detailed instructions for enabling virtualization: (https://www.virtualmetric.com/blog/how-to-enable-hardware-virtualization#:~:text=Open%20your%20task%20manager%20by,mentioned%20in%20the%20task%20manager.)