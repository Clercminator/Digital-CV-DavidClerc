from pathlib import Path
import streamlit as st
from PIL import Image

#--PATH SETTINGS--
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file1 = current_dir / "assets" / "CV Spanish.pdf"
resume_file2 = current_dir / "assets" / "CV English.pdf"
profile_pic = current_dir / "assets" / "David profile circulo.png"


#--GENERAL SETTINGS--
PAGE_TITLE = "Digital CV | David Clerc"
PAGE_ICON = ":wave:"
NAME = "David Clerc"
DESCRIPTION = """
Commercial Engineer, Entrepreneur, Asset Manager
"""
EMAIL = "dclerc@fen.uchile.cl"
SOCIAL_MEDIA = {
    "Youtube":"https://www.youtube.com/watch?v=ghbR94UgKUo",
    "LinkedIn":"https://www.linkedin.com/in/david-clerc/",
    "GitHub":"https://github.com/Clercminator",
    "Twitter":"https://twitter.com/edmundoclerc7",
}
PROJECTS = {
    "Founder of **BeChange**: Crowdfunding platform to fund sustainable startups.": "https://pitch.com/public/b4952581-658c-49ed-8b19-f22ba5863c0a",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


#---LOAD CSS, PDF & PROFILE PIC---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file1,"rb") as pdf_file:
    PDFbyte1 = pdf_file.read()
with open(resume_file2,"rb") as pdf_file:
    PDFbyte2 = pdf_file.read()
profile_pic = Image.open(profile_pic)


#---HERO SECTION---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="🗳 Download Spanish CV",
        data=PDFbyte1,
        file_name=resume_file1.name,
        mime="application/octet-stream",
    )
    st.download_button(
        label="🗳 Download English CV",
        data=PDFbyte2,
        file_name=resume_file2.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


#---SOCIAL LINKS---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#---EXPERIENCE & QUALIFICATIONS
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✅ 2.5 years of internships at great companies like **P&G**, **Dadneo**, and **LiderBCI**
    - ✅ Strong hands on experience and knowledge in Python, R, and Excel.
    - ✅ Good understanding of financial investments and management.
    - ✅ Excellent team-player and always willing to go the extra mile.
    """
)

#---SKILLS---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 💻 Programming: Python, R, Visual Basic.
    - 📊 Data Visualization: PowerBI, Excel.
    - 📈 Modeling: Logistic Regression, Linear Regression, Decision Trees, Neural Networks.
    - 📁 Databases: Azure, Access
    - 💰 Valuation: MonteCarlo Simulation.
    """
)


#---WORK HISTORY---
st.write("#")
st.subheader("Work History")
st.write("---")

#---JOB 1---
st.write("**F&A Intern | Procter & Gamble**")
st.write("07/2022 - 02/2023")
st.write(
    """
    - ♦︎ Plan & execute the Legal Entity Risk Factor project for Chile, where the goal is to better manage risk (operational, reputational, financial) that faces the organization. 
    - ♦︎ Plan & execute the Backup project for Pacific (Colombia, Peru, and Chile), where the goal is to make sure the organization is in compliance with its key processes, as a part of a Business Continuity Plan. 
    - ♦︎ Monthly analysis of P&G Chile's financial statements to improve awareness and make better decisions
    """
)
#---JOB 2---
st.write("**Intern & Consultant | Dadneo**")
st.write("08/2021 - 03/2022")
st.write(
    """
    - ♦︎ Advise startups in how to define their market, adjust their value proposition and improve their pitch, among others. 
    - ♦︎ Valuation through different methods and tools. 
    - ♦︎ Optimize process within the organization using Macros and creating automated reports.
    """
)
#---JOB 3---
st.write("**Sales Analyst Intern | LiderBCI**")
st.write("06/2021 - 08/2021")
st.write(
    """
    - ♦︎ Update and consolidate databases to present sales results to then analyze these numbers and create reports with PowerBI.
    """
)
#---JOB 4---
st.write("**Marketing Intern | Travolution Travel**")
st.write("08/2020 - 12/2020")
st.write(
    """
    - ♦︎  Improve brand's website to better transmit their value proposition. Readjust target client segments and optimize SEO. 
    """
)

#---PROJECTS & ACCOMPLISHMENTS---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")