"""Game Engine Renderer. Transforms regular lecture slide data arrays into playable inspection stages."""
import streamlit as st

CALLOUTS = {"info": st.info, "success": st.success, "warning": st.warning, "error": st.error}

def _text(b, key):
    st.markdown(f"📜 **Mission Log Context:** *{b['text']}*")

def _heading(b, key):
    st.markdown(f"### 🛡️ Objective: {b['text']}")

def _bullets(b, key):
    st.markdown("🔍 **Decoded Manual Data:**")
    for item in b["items"]:
        st.markdown(f"🔹 *{item}*")

def _callout(b, key):
    st.markdown(f"💡 **Intel Data:** `{b['text']}`")

def _cards(b, key):
    st.markdown("<div style='color: #2563EB; font-weight: bold; font-size: 18px;'>🧩 TASK: Memory Matrix Match</div>", unsafe_allow_html=True)
    items = b["items"]
    
    labels_pool = [item[0] for item in items]
    correct_matches = 0
    
    for idx, (correct_title, description) in enumerate(items):
        st.markdown(f"📎 **Definition Hint:** *{description}*")
        guess = st.selectbox("Identify the matching concept component:", ["-- SELECT LABEL --"] + labels_pool, key=f"{key}_card_game_{idx}")
        if guess == correct_title:
            correct_matches += 1

    if correct_matches == len(items):
        st.success("🎯 MATRIX MATCHED COMPLETE! +20 XP UNLOCKED.")
        if key not in st.session_state.unlocked_stages:
            st.session_state.game_score += 20
            st.session_state.unlocked_stages.add(key)
    else:
        st.info("🔒 Match all definitions above correctly to clear this matrix node.")

def _tabs(b, key):
    st.markdown("<div style='color: #D97706; font-weight: bold; font-size: 18px;'>🔓 SYSTEM GATE: Data Verification Code</div>", unsafe_allow_html=True)
    items = b["items"]
    
    titles = [t[0] for t in items]
    target_select = st.radio("Choose a database file sector to clear:", titles, key=f"{key}_tab_radio")
    
    idx = titles.index(target_select)
    selected_title, original_desc = items[idx]
    
    st.markdown(f"⚙️ *Analyzing encrypted architecture definition sector for: `{selected_title}`...*")
    
    if "GUI" in selected_title:
        q = st.selectbox("GUI stands for Graphical User Interface. What core design metric summarizes its primary look?", ["-- Select --", "Command line lines text terminal style code", "Visual elements like windows, menus, icons, and buttons"], key=f"{key}_tab_q_{idx}")
        success_cond = "Visual elements" in q
    elif "UI" in selected_title:
        q = st.selectbox("What components form the complete scope framework of a traditional User Interface?", ["-- Select --", "The hardware processing speeds only", "The set of elements and controls through which a person communicates with a system"], key=f"{key}_tab_q_{idx}")
        success_cond = "set of elements" in q
    elif "UX" in selected_title:
        q = st.selectbox("User Experience (UX) focuses on which phase timeline of the student or user flow?", ["-- Select --", "The broader experience and perceptions before, during, and after interactions", "The database backup compression layout parameters"], key=f"{key}_tab_q_{idx}")
        success_cond = "broader experience" in q
    else:
        q = st.checkbox("Toggle decrypt switch connector matrix parameters", key=f"{key}_tab_q_{idx}")
        success_cond = q

    if success_cond:
        st.markdown(f"""
        <div style="background-color: #ECFDF5; border-left: 5px solid #10B981; padding: 15px; border-radius: 4px; margin-top: 10px;">
            <b style="color: #047857;">🔓 SECTOR DECRYPTED SUCCESSFUL:</b><br>
            <p style="color: #065F46; font-style: normal; margin-top: 5px;">{original_desc}</p>
        </div>
        """, unsafe_allow_html=True)
        if f"{key}_tab_clear_{idx}" not in st.session_state.unlocked_stages:
            st.session_state.game_score += 15
            st.session_state.unlocked_stages.add(f"{key}_tab_clear_{idx}")
    else:
        st.error("🔒 ACCESS DENIED. Select the correct conceptual response to clear this node pipeline.")

def _steps(b, key):
    st.markdown(f"#### 🪜 Quest Progression Timeline: {b.get('title', 'Steps')}")
    for idx, (title, description) in enumerate(b["items"], start=1):
        st.markdown(f"**Stage {idx}: {title}** — *{description}*")

def _compare(b, key):
    st.markdown("⚖️ **HCI Comparative Analysis Framework:**")
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**{b['left']['title']}**\n" + "\n".join(f"* {item}" for item in b['left']['items']))
    with col2:
        st.error(f"**{b['right']['title']}**\n" + "\n".join(f"* {item}" for item in b['right']['items']))

def _detail(b, key):
    st.markdown("<div style='color: #DC2626; font-weight: bold; font-size: 18px;'>🚨 HARDWARE REPAIR TERMINAL: Clean the Bugs</div>", unsafe_allow_html=True)
    names = [d["name"] for d in b["items"]]
    
    selected_module = st.selectbox("Choose a lecture section to debug and unlock:", ["-- CHOOSE CORE PRINCIPLE MODULE --"] + names, key=f"{key}_detail_select")
    
    if selected_module != "-- CHOOSE CORE PRINCIPLE MODULE --":
        idx = names.index(selected_module)
        st.info(f"🛠️ **Diagnostic Bug Scenario Report for: `{selected_module}`**")
        
        if "Visibility" in selected_module:
            ans = st.radio("A system developer hid the main 'Download Admit Card' action inside a nested secondary configuration panel. What design rule failed?", ["Mapping", "Visibility", "Consistency"], key=f"{key}_puz_{idx}")
            is_valid = (ans == "Visibility")
        elif "Feedback" in selected_module:
            ans = st.radio("A student presses 'Submit Assignment', the interface completely freezes without showing any confirmation indicator. What rules fixes this?", ["Feedback", "Simplicity", "Visual size"], key=f"{key}_puz_{idx}")
            is_valid = (ans == "Feedback")
        elif "Consistency" in selected_module:
            ans = st.radio("An LMS names a function 'Gradebook' on one page but renames the same interface table to 'Marks Portal' on another page. What failed?", ["Constraints", "Consistency", "Affordance"], key=f"{key}_puz_{idx}")
            is_valid = (ans == "Consistency")
        elif "Simplicity" in selected_module:
            ans = st.radio("What principle hides advanced configurations until explicitly called by the user?", ["Progressive Disclosure", "System Recall", "Natural Mapping"], key=f"{key}_puz_{idx}")
            is_valid = (ans == "Progressive Disclosure")
        elif "Constraints" in selected_module:
            ans = st.radio("A text input area meant strictly for registration ID numbers lets users enter random letters, causing server crashes. What should be applied?", ["Input Constraints", "System Status Indicators", "Visual contrast"], key=f"{key}_puz_{idx}")
            is_valid = (ans == "Input Constraints")
        else:
            ans = st.checkbox("Override console system locking connectors manually", key=f"{key}_puz_{idx}")
            is_valid = ans

        if is_valid:
            st.success("🎉 CORE LAB BUG FIXED! DATA STREAM UNLOCKED.")
            if f"puz_ok_{idx}" not in st.session_state.unlocked_stages:
                st.session_state.game_score += 25
                st.session_state.unlocked_stages.add(f"puz_ok_{idx}")
            st.markdown("---")
            render_blocks(b["items"][idx]["blocks"], key=f"{key}_nested_{idx}")
        else:
            st.error("🔒 SECURITY FIREWALL BLOCKED: Solve the conceptual bug challenge above to launch the slide insights.")

def _reveal(b, key):
    st.markdown("### 🎭 Interactive Application Scenarios")
    for j, (title, context_scenario, expected_fix) in enumerate(b["items"]):
        with st.expander(f"📋 Mission Target Scenario: {title}"):
            st.write(context_scenario)
            user_input = st.text_input("Diagnose and type the solution framework required:", key=f"{key}_rev_input_{j}")
            if st.button("Submit Diagnostics Log", key=f"{key}_rev_action_{j}"):
                st.success(f"🔓 Node cleared. Core evaluation criteria: {expected_fix}")
                if f"rev_node_{j}" not in st.session_state.unlocked_stages:
                    st.session_state.game_score += 15
                    st.session_state.unlocked_stages.add(f"rev_node_{j}")

def _discussion(b, key):
    st.markdown("### 🗣️ Classroom Combat Mode Challenges:")
    for idx, (question, evaluation_prompt) in enumerate(b["items"], start=1):
        st.markdown(f"**Question {idx}: {question}**")
        st.caption(f"🎯 *Inspection Challenge Prompt:* {evaluation_prompt}")

def _answer_box(b, key):
    st.text_area(b.get("label", "Enter your field research data notes here:"), key=f"{key}_text_game_box")

# Dictionary mapping placed clearly before execution functions run
RENDERERS = {
    "text": _text, "heading": _heading, "bullets": _bullets, "callout": _callout,
    "cards": _cards, "tabs": _tabs, "steps": _steps, "compare": _compare,
    "detail": _detail, "reveal": _reveal, "discussion": _discussion, "answer_box": _answer_box,
}

def render_blocks(blocks, key="b"):
    if "game_score" not in st.session_state:
        st.session_state.game_score = 0
    if "unlocked_stages" not in st.session_state:
        st.session_state.unlocked_stages = set()

    st.markdown(f"""
    <div style="background-color: #111827; padding: 15px; border-radius: 10px; border: 2px solid #3B82F6; text-align: center; margin-bottom: 25px;">
        <span style="font-size: 20px; font-weight: bold; color: #38BDF8; font-family: monospace; letter-spacing: 2px;">🕹️ INTRUDER DETECTION SYSTEM ACTIVE</span><br>
        <span style="font-size: 16px; color: #F3F4F6; font-family: monospace;">CURRENT ACADEMIC SCORE: <b>{st.session_state.game_score} XP</b></span>
    </div>
    """, unsafe_allow_html=True)

    for i, block in enumerate(blocks):
        b_type = block["type"]
        if b_type in RENDERERS:
            RENDERERS[b_type](block, f"{key}_{i}")
