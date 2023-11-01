from pathlib import Path

import streamlit as st
from PIL import Image

from streamlit_extras.colored_header import colored_header

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Cristian Femenia"
PAGE_ICON = ":wave:"
NAME = "Cristian Femenia"
DESCRIPTION = """
**Data scientist** from Argentina 🇦🇷 🧉.
"""
EMAIL = "cristianfemenia77@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/cristian-femenia-80b943200",
    # "GitHub": "https://github.com",

}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

    # "light-blue-70",
    # "orange-70",
    # "blue-green-70",
    # "blue-70",
    # "violet-70",
    # "red-70",
    # "green-70",
    # "yellow-80",

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns((1,2))#, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.markdown(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("🇦🇷")


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA), gap='small')
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[:blue[{platform}]]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
# st.subheader("Experience & Qulifications")

colored_header(
    label="Experience & Qualifications",
    description=None,
    color_name="light-blue-70",
)
st.write(
    """
- ✔️ 3 Years expirience extracting actionable insights from data
- ✔️ Proficient in Python with 5+ years of expirience
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS --r-
st.write('\n')
# st.subheader("Hard Skills")
colored_header(
    label="Hard Skills",
    description=None,
    color_name="light-blue-70",
)
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Selenium), SQL
- 📊 Data Visualization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Databases: Postgres, MySQL, SQL Server
"""
)


# --- WORK HISTORY ---
st.write('\n')
# st.subheader("Work History")
colored_header(
    label="Work History",
    description=None,
    color_name="red-70",
)
# st.write("---")

# --- JOB 1
st.write('\n')
st.write("🚧", "**Data Analyst | Banco San Juan SA**")
st.write("August 2018 - Present")
st.write(
    """
- ► Leverage Python and Selenium to automate tasks, such as downloading files from various URLs and processing them efficiently.
- ► Successfully integrated Windows tasks with the Solaris OS banking core environment SFB/SCB using Python..
- ► Designed and implemented a monitoring dashboard using Python and SQL to oversee automated tasks for Probatch (Unisys).
- ► Developed a web application with Streamlit, Python, and SQL, enabling the creation of interactive dashboards and reports for Veeam.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Core Banking Operator | Banco San Juan SA**")
st.write("May 2016 - August 2018")
st.write(
    """
- ► Devised menu structures with batch files to streamline and organize operators' tasks, resulting in increased operational efficiency.
- ► Automated repetitive tasks and batch processes using batch files, reducing task completion times by 25%.
"""
)


# # --- Projects & Accomplishments ---
# st.write('\n')
# # st.subheader("Projects & Accomplishments")
# colored_header(
#     label="Projects & Accomplishments",
#     description=None,
#     color_name="green-70",
# )
# # st.write("---")
# # for project, link in PROJECTS.items():
# #     st.write(f"[{project}]({link})")
