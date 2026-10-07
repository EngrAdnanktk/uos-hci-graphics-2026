import streamlit as st

import importlib
import sys
from pathlib import Path

from renderer import render_blocks

APP_DIR = Path(__file__).resolve().parent
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))


def load_lectures():
    """Finds every lecture_XX.py next to app.py that defines a LECTURE dict."""
    found = []
    for path in sorted(APP_DIR.glob("lecture_*.py")):
        found.append(importlib.import_module(path.stem).LECTURE)
    return sorted(found, key=lambda lec: lec["number"])


st.set_page_config(page_title="HCI Lectures", page_icon="🎨", layout="centered")

st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; color: #1E3A8A; margin-bottom: 0px; }
    .sub-title { font-size: 18px; color: #4B5563; margin-bottom: 20px; }
    .section-header { font-size: 24px; font-weight: bold; color: #1E3A8A; border-bottom: 2px solid #E5E7EB; padding-bottom: 8px; margin-top: 30px; }
    </style>
""", unsafe_allow_html=True)

lectures = load_lectures()
if not lectures:
    st.error("No lectures found. Add a file such as lecture_03.py next to app.py.")
    st.stop()

# Sidebar: choose lecture, then section
st.sidebar.title("📚 HCI Lectures")
labels = {f"Lecture {l['number']:02d}: {l['title']}": l for l in lectures}
lecture = labels[st.sidebar.selectbox("Choose a lecture:", list(labels))]

st.sidebar.divider()
st.sidebar.subheader("Lecture Navigation")
section_titles = [f"{i:02d} • {s['title']}" for i, s in enumerate(lecture["sections"], start=1)]
choice = st.sidebar.radio("Go to Section:", section_titles, key=f"nav_{lecture['number']}")
section = lecture["sections"][section_titles.index(choice)]

# Header
st.markdown('<div class="main-title">BS COMPUTER SCIENCE • UNIVERSITY OF SWABI</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="sub-title"><b>Lecture {lecture["number"]:02d}:</b> {lecture["subtitle"]}</div>',
    unsafe_allow_html=True,
)

# Section body
st.markdown(f'<div class="section-header">{choice}</div>', unsafe_allow_html=True)
render_blocks(section["blocks"], key=f"L{lecture['number']}_{section_titles.index(choice)}")

if section.get("is_last") and lecture.get("next"):
    st.success(f"**Next lecture:** {lecture['next']}")
