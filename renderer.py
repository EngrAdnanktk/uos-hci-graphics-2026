"""Game-Infused Block Renderer. Turns core lecture content data into playable interface inspection missions."""
import streamlit as st

CALLOUTS = {"info": st.info, "success": st.success, "warning": st.warning, "error": st.error}

def render_blocks(blocks, key="b"):
    # Tracking score directly inside Streamlit's state context
    if "game_score" not in st.session_state:
        st.session_state.game_score = 0
    if "unlocked_nodes" not in st.session_state:
        st.session_state.unlocked_nodes = set()

    # Dynamic Game Dashboard at the top of every section block
    st.markdown(f"""
    <div style="background-color: #F3F4F6; padding: 10px; border-radius: 8px; border: 1px solid #D1D5DB; margin-bottom: 15px; text-align: center;">
        <span style="font-size: 16px; font-weight: bold; color: #1E3A8A;">🎮 HCI LAB SCORE: {st.session_state.game_score} PTS</span>
    </div>
    """, unsafe_allow_html=True)

    for i, block in enumerate(blocks):
        RENDERERS[block["type"]](block, f"{key}_{i}")

def _text(b, key):
    st.write(b["text"])

def _heading(b, key):
    st.markdown(f"### {b['text']}")

def _bullets(b, key):
    st.write("📋 **Review Checklist:**")
    for item in b["items"]:
        st.write(f"* {item}")

def _callout(b, key):
    CALLOUTS[b.get("kind", "info")](b["text"])

def _cards(b, key):
    """Turns standard information cards into a game match puzzle."""
    if b.get("title"):
        st.markdown(f"#### 🚨 Mission: Identify the definitions for '{b['title']}'")
    
    items = b["items"]
    # Create random decoy selectors out of titles
    all_titles = [item[0] for item in items]
    
    n = b.get("cols", 3)
    cols = st.columns(n)
    
    correct_matches = 0
    for i, (correct_title, description) in enumerate(items):
        with cols[i % n]:
            st.markdown(f"**Element #{i+1} Definition:**")
            st.caption(f"*{description}*")
            user_guess = st.selectbox("Assign correct label:", ["-- Select --"] + all_titles, key=f"{key}_card_{i}")
            
            if user_guess == correct_title:
                st.success(f"✅ Matched: {correct_title}!")
                correct_matches += 1
            elif user_guess != "-- Select --":
                st.error("❌ Mismatched mapping")

    if correct_matches == len(items):
        st.balloons()
        if key not in st.session_state.unlocked_nodes:
            st.session_state.game_score += 20
            st.session_state.unlocked_nodes.add(key)

def _tabs(b, key):
    """Turns structural information tabs into verification challenges."""
    st.markdown("#### ⚡ System Architecture Verification Required")
    items = b["items"]
    
    tab_names = [t[0] for t in items]
    chosen_tab = st.radio("Select an entity element to configure:", tab_names, key=f"{key}_radio")
    
    # Extract match
    idx = tab_names.index(chosen_tab)
    correct_title, description = items[idx]
    
    st.info(f"📚 **Lecture Content for {correct_title}:**\n\n{description}")
    
    # Mini challenge validation
    q = st.checkbox(f"I have studied and verified the concept requirements for {correct_title}", key=f"{key}_chk_{idx}")
    if q:
        if f"{key}_{idx}" not in st.session_state.unlocked_nodes:
            st.session_state.game_score += 10
            st.session_state.unlocked_nodes.add(f"{key}_{idx}")
            st.rerun()

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
    """Turns the 10 core principles dropdown index into a diagnostic debugging game."""
    names = [d["name"] for d in b["items"]]
    
    st.markdown("### 🛠️ HCI Bug Laboratory")
    chosen = st.selectbox(b.get("label", "Choose a module path to debug:"), names, key=f"{key}_sel")
    idx = names.index(chosen)
    
    st.warning(f"🔍 **Mission Challenge:** Inspect the data logic module for **'{chosen}'** below.")
    
    # Custom interactive challenge injector built dynamically on item indices
    if "Visibility" in chosen:
        q = st.radio("A developer hides the 'Save Profile Changes' button inside an unlabelled drop-down panel. What rule broke?", ["Affordance Mapping", "System Visibility Status", "Visibility"], key=f"{key}_game_{idx}")
        is_correct = (q == "Visibility")
    elif "Feedback" in chosen:
        q = st.radio("A user clicks submit, the site locks up completely, and gives zero updates for 2 minutes. What fixes this?", ["Change font metrics", "Provide meaningful, immediate Feedback alerts", "Delete system path"], key=f"{key}_game_{idx}")
        is_correct = (q == "Provide meaningful, immediate Feedback alerts")
    elif "Consistency" in chosen:
        q = st.radio("A website calls a button 'Sign In' on the main index page, but changes the text string to 'Logon' inside the inner panels. What metric failed?", ["Simplicity models", "Terminology Consistency", "Error Control"], key=f"{key}_game_{idx}")
        is_correct = (q == "Terminology Consistency")
    elif "Simplicity" in chosen:
        q = st.radio("What strategy keeps advanced, low-frequency framework controls out of view until explicitly needed?", ["Progressive Disclosure", "Affordance values", "Recall indices"], key=f"{key}_game_{idx}")
        is_correct = (q == "Progressive Disclosure")
    elif "Constraints" in chosen:
        q = st.radio("How should a date entry form field behave to proactively prevent typing string letters by accident?", ["Apply text constraint rules to intercept illegal inputs", "Show an alert dialog after crashing", "Do nothing"], key=f"{key}_game_{idx}")
        is_correct = (q == "Apply text constraint rules to intercept illegal inputs")
    else:
        # Catch-all backup confirmation condition for other principles
        q = st.checkbox("Decrypt and launch core lecture slide text variables", key=f"{key}_game_{idx}")
        is_correct = q
        
    if is_correct:
        st.success("🎉 Diagnostic Passed! Code Unlocked.")
        if f"detail_{idx}" not in st.session_state.unlocked_nodes:
            st.session_state.game_score += 20
            st.session_state.unlocked_nodes.add(f"detail_{idx}")
        
        st.markdown("---")
        render_blocks(b["items"][idx]["blocks"], key=f"{key}_{idx}")
    else:
        st.error("🔒 Framework Locked. Select the correct HCI principle answer to reveal the lecture insights.")

def _reveal(b, key):
    for j, (title, scenario, answer) in enumerate(b["items"]):
        with st.expander(title):
            st.write(scenario)
            guess = st.text_input("Type your diagnosed fix principle:", key=f"{key}_rev_in_{j}")
            if st.button("Verify Diagnosis", key=f"{key}_rev_btn_{j}"):
                st.write(f"💡 **Expected Criteria Includes:** {answer}")
                if f"rev_{j}" not in st.session_state.unlocked_nodes:
                    st.session_state.game_score += 15
                    st.session_state.unlocked_nodes.add(f"rev_{j}")

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
