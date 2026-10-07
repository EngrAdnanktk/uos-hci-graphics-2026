"""Generic block renderer. Lecture files describe content as data; this turns it into Streamlit UI."""
import streamlit as st

CALLOUTS = {"info": st.info, "success": st.success, "warning": st.warning, "error": st.error}


def render_blocks(blocks, key="b"):
    for i, block in enumerate(blocks):
        RENDERERS[block["type"]](block, f"{key}_{i}")


def _text(b, key):
    st.write(b["text"])


def _heading(b, key):
    st.markdown(f"### {b['text']}")


def _bullets(b, key):
    for item in b["items"]:
        st.write(f"* {item}")


def _callout(b, key):
    CALLOUTS[b.get("kind", "info")](b["text"])


def _cards(b, key):
    if b.get("title"):
        st.markdown(f"### {b['title']}")
    n = b.get("cols", 3)
    cols = st.columns(n)
    for i, (title, text) in enumerate(b["items"]):
        with cols[i % n]:
            st.markdown(f"**{title}**")
            st.caption(text)


def _tabs(b, key):
    items = b["items"]
    for tab, (title, text) in zip(st.tabs([t for t, _ in items]), items):
        with tab:
            st.markdown(f"### **{title}**")
            st.write(text)


def _steps(b, key):
    if b.get("title"):
        st.markdown(f"### {b['title']}")
    for i, (title, text) in enumerate(b["items"], start=1):
        st.markdown(f"**{i}. {title}**")
        st.caption(text)


def _compare(b, key):
    left, right = st.columns(2)
    for col, side in ((left, b["left"]), (right, b["right"])):
        with col:
            CALLOUTS[side.get("kind", "info")](
                f"**{side['title']}**\n" + "\n".join(f"* {x}" for x in side["items"])
            )


def _detail(b, key):
    """Selectbox that reveals a block list for the chosen entry."""
    names = [d["name"] for d in b["items"]]
    chosen = st.selectbox(b.get("label", "Choose one:"), names, key=f"{key}_sel")
    render_blocks(b["items"][names.index(chosen)]["blocks"], key=f"{key}_{names.index(chosen)}")


def _reveal(b, key):
    """Scenario expanders with a show-answer checkbox."""
    for j, (title, scenario, answer) in enumerate(b["items"]):
        with st.expander(title):
            st.write(scenario)
            if st.checkbox(b.get("label", "Reveal answer"), key=f"{key}_{j}"):
                st.success(answer)


def _discussion(b, key):
    for i, (task, prompt) in enumerate(b["items"], start=1):
        st.markdown(f"**{i:02d}. {task}**")
        st.caption(prompt)


def _answer_box(b, key):
    st.text_area(b.get("label", "Your answer (not saved):"), key=f"{key}_ans")


RENDERERS = {
    "text": _text, "heading": _heading, "bullets": _bullets, "callout": _callout,
    "cards": _cards, "tabs": _tabs, "steps": _steps, "compare": _compare,
    "detail": _detail, "reveal": _reveal, "discussion": _discussion, "answer_box": _answer_box,
}
