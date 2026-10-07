"""Game Engine Renderer. Embeds a fully playable interactive HTML Canvas game block directly into Streamlit."""
import streamlit as st
import streamlit.components.v1 as components
import json

def render_blocks(blocks, key="b"):
    # 1. Setup persistent browser state mechanics for scoring metrics
    if "game_score" not in st.session_state:
        st.session_state.game_score = 0
    if "cleared_stages" not in st.session_state:
        st.session_state.cleared_stages = []

    # Calculate current slide context profile
    slide_title = blocks[0]["text"] if len(blocks) > 0 else "HCI Challenge Module"
    
    # 2. Immersive HUD Scoreboard Panel display
    st.markdown(f"""
    <div style="background-color: #0F172A; padding: 15px; border-radius: 10px; border: 2px solid #3B82F6; text-align: center; margin-bottom: 20px;">
        <span style="font-size: 18px; font-weight: bold; color: #38BDF8; font-family: monospace;">🎮 ARCADE FLOW CONTROLLER ACTIVE</span><br>
        <span style="font-size: 15px; color: #F3F4F6; font-family: monospace;">TOTAL STUDENT ACCOUNT BALANCE: <b>{st.session_state.game_score} XP</b></span>
    </div>
    """, unsafe_allow_html=True)

    # 3. Comprehensive Pure HTML5 / JavaScript Retro Canvas game script
    game_html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ margin: 0; background: #020617; font-family: 'Courier New', monospace; text-align: center; color: white; display: flex; flex-direction: column; align-items: center; justify-content: center; }}
            canvas {{ background: #1e293b; border: 4px solid #3b82f6; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); cursor: pointer; }}
            #ui-instructions {{ margin-top: 10px; font-size: 14px; color: #94a3b8; max-width: 580px; line-height: 1.4; }}
        </style>
    </head>
    <body>
        <h4 style="margin: 5px 0; color: #38bdf8;">LEVEL TARGET: {slide_title}</h4>
        <canvas id="gameCanvas" width="600" height="300"></canvas>
        <div id="ui-instructions">🎯 <b>How to Play:</b> Use your mouse cursor to click and interact. Drag the natural mapping configuration slider nodes, click invisible button frames to toggle visual highlights, or blast illegal files to keep the system safe!</div>

        <script>
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");
            
            // Game State Machine Variables
            let levelSolved = false;
            let currentScore = 0;
            let sliderX = 150; // Natural mapping game node coordinate tracker
            let isDragging = false;
            let invisibleButtonVisible = false;

            // Target Objectives Variables
            const targetX = 450; 

            // Base Core Loops Engine
            function gameLoop() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                // Draw Grid Lines (Background Environment Matrix)
                ctx.strokeStyle = "#334155";
                ctx.lineWidth = 1;
                for(let i=0; i<canvas.width; i+=40) {{
                    ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, canvas.height); ctx.stroke();
                }}
                for(let j=0; j<canvas.height; j+=40) {{
                    ctx.beginPath(); ctx.moveTo(0, j); ctx.lineTo(canvas.width, j); ctx.stroke();
                }}

                // DYNAMIC MISSION DISPATCHER CHANNELS
                if("{slide_title}".includes("Goals") || "{slide_title}".includes("Visibility")) {{
                    drawVisibilityMission();
                }} else if("{slide_title}".includes("LMS") || "{slide_title}".includes("Principles")) {{
                    drawErrorPreventionMission();
                }} else {{
                    drawMappingMission();
                }}

                if(levelSolved) {{
                    ctx.fillStyle = "rgba(16, 185, 129, 0.9)";
                    ctx.fillRect(50, 100, 500, 100);
                    ctx.fillStyle = "#ffffff";
                    ctx.font = "bold 20px Courier New";
                    ctx.fillText("MISSION CLEARED! +25 XP AWARDED", 110, 155);
                }}

                requestAnimationFrame(gameLoop);
            }}

            // MISSION 1 ENGINE: Visibility & Signifiers Level
            function drawVisibilityMission() {{
                ctx.fillStyle = "#f87171";
                ctx.font = "14px Courier New";
                ctx.fillText("BUG ALERT: The Submit button has no visual Signifier!", 30, 40);
                
                // Render the broken button based on active state parameters
                if(!invisibleButtonVisible) {{
                    ctx.fillStyle = "#334155"; // Gray blending text background box
                    ctx.fillRect(200, 120, 200, 50);
                    ctx.fillStyle = "#64748b";
                    ctx.fillText("Hidden Button Area", 225, 150);
                }} else {{
                    ctx.fillStyle = "#2563eb"; // Bright interactive blue
                    ctx.fillRect(200, 120, 200, 50);
                    ctx.strokeStyle = "#38bdf8";
                    ctx.lineWidth = 3;
                    ctx.strokeRect(200, 120, 200, 50);
                    ctx.fillStyle = "#ffffff";
                    ctx.font = "bold 16px Courier New";
                    ctx.fillText("✅ SUBMIT SYSTEM", 225, 150);
                    if(!levelSolved) triggerWin();
                }}
                ctx.fillStyle = "#e2e8f0";
                ctx.font = "12px Courier New";
                ctx.fillText("👉 CLICK THE HIDDEN RECTANGLE LAYER TO DEPLOY A SIGNIFIER", 70, 240);
            }}

            // MISSION 2 ENGINE: Natural Mapping Slider Challenge Level
            function drawMappingMission() {{
                ctx.fillStyle = "#38bdf8";
                ctx.font = "14px Courier New";
                ctx.fillText("MISSION: Align the physical knob to its target sector layout", 30, 40);
                
                // Draw target tracking terminal track
                ctx.fillStyle = "#475569";
                ctx.fillRect(100, 150, 400, 10);
                
                // Draw validation target zone
                ctx.fillStyle = "rgba(56, 189, 248, 0.3)";
                ctx.fillRect(targetX - 25, 130, 50, 50);
                ctx.fillStyle = "#38bdf8";
                ctx.fillText("TARGET ZONE", targetX - 45, 120);

                // Draw moveable slider knob element node container
                ctx.fillStyle = "#ef4444";
                ctx.beginPath();
                ctx.arc(sliderX, 155, 15, 0, Math.PI*2);
                ctx.fill();

                if(Math.abs(sliderX - targetX) < 15 && !levelSolved) triggerWin();
            }}

            // MISSION 3 ENGINE: Error Prevention Defense Level
            function drawErrorPreventionMission() {{
                ctx.fillStyle = "#fbbf24";
                ctx.font = "14px Courier New";
                ctx.fillText("CRITICAL REPAIR: Click to block hazardous illegal data packet blocks", 20, 40);
                
                ctx.fillStyle = "#ef4444";
                ctx.fillRect(150, 110, 100, 60);
                ctx.fillStyle = "#ffffff";
                ctx.fillText("MALICIOUS.EXE", 155, 145);

                ctx.fillStyle = "#10b981";
                ctx.fillRect(350, 110, 100, 60);
                ctx.fillStyle = "#ffffff";
                ctx.fillText("PROJECT.PDF", 355, 145);
                
                ctx.fillStyle = "#cbd5e1";
                ctx.font = "12px Courier New";
                ctx.fillText("👉 ACTION: CLICK ON THE INSECURE FILE FORMAT TO INTERCEPT", 60, 240);
            }}

            // Mouse Action Handlers Inside Canvas
            canvas.addEventListener("mousedown", (e) => {{
                const rect = canvas.getBoundingClientRect();
                const mouseX = e.clientX - rect.left;
                const mouseY = e.clientY - rect.top;

                // Hit validation check for Visibility level click
                if(mouseX >= 200 && mouseX <= 400 && mouseY >= 120 && mouseY <= 170) {{
                    invisibleButtonVisible = true;
                }}

                // Hit validation check for Error Prevention challenge blocks
                if(mouseX >= 150 && mouseX <= 250 && mouseY >= 110 && mouseY <= 170) {{
                    if(!levelSolved) triggerWin();
                }}

                // Slider tracking initialization bounds logic
                if(Math.abs(mouseX - sliderX) < 20 && Math.abs(mouseY - 155) < 20) {{
                    isDragging = true;
                }}
            }});

            canvas.addEventListener("mousemove", (e) => {{
                if(isDragging) {{
                    const rect = canvas.getBoundingClientRect();
                    let mx = e.clientX - rect.left;
                    if(mx >= 100 && mx <= 500) {{
                        sliderX = mx;
                    }}
                }}
            }});

            canvas.addEventListener("mouseup", () => {{ isDragging = false; }});

            function triggerWin() {{
                levelSolved = true;
                // Dispatch state response telemetry vectors back into the core Streamlit parent backend environment
                window.parent.postMessage({{type: 'streamlit:setComponentValue', value: 25}}, '*');
            }}

            gameLoop();
        </script>
    </body>
    </html>
    """

    # 4. Mount the interactive iframe block bundle inside Streamlit view framework
    game_response = components.html(game_html_code, height=400, scrolling=False)
    
    # 5. Automatically capture game events and increment Python session state values
    if game_response == 25 and key not in st.session_state.cleared_stages:
        st.session_state.game_score += 25
        st.session_state.cleared_stages.append(key)
        st.rerun()

