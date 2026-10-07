LECTURE = {
    "number": 2,
    "title": "UI Design Principles",
    "subtitle": "Designing Interfaces for People",
    "next": "Usability: Effectiveness, Efficiency & Satisfaction",
    "sections": [
        {"title": "Lecture Goals", "blocks": [
            {"type": "text", "text": "By the end of this lecture, students should be able to explain and apply the fundamental principles used to design effective user interfaces."},
            {"type": "callout", "text": """**Students will be able to:**
* **Define UI:** Explain what a user interface is and distinguish between UI, GUI, and UX.
* **Explain Principles:** Describe why visibility, feedback, consistency, simplicity, and other principles matter.
* **Recognize Problems:** Identify common UI problems such as clutter, ambiguity, inconsistency, and poor feedback.
* **Understand Human Use:** Connect interface decisions with user perception, attention, memory, and expectations.
* **Evaluate Interfaces:** Use design principles to discuss whether an interface supports users effectively.
* **Prepare for Practice:** Apply the principles later in the HCI lab through interface design and evaluation."""},
        ]},
        {"title": "Foundations: What is UI?", "blocks": [
            {"type": "text", "text": "A **User Interface (UI)** is the set of elements and interaction mechanisms through which a person communicates with and controls a computing system."},
            {"type": "cards", "title": "🔁 The UI Communication Loop", "items": [
                ("📥 Input", "Buttons, fields, keyboard, touch, voice, and gestures used to provide commands."),
                ("⚙️ Process & State", "The system interprets actions, changes internal states, and determines next steps."),
                ("📤 Output & Feedback", "Communicates results through text, graphics, sound, animation, or status messages."),
            ]},
            {"type": "callout", "kind": "warning", "text": "💡 **Core Takeaway:** UI is not only what a screen looks like; it is also how users interact with the system."},
        ]},
        {"title": "Clarification: UI vs GUI vs UX", "blocks": [
            {"type": "text", "text": "Let's break down the boundaries of design terminology:"},
            {"type": "tabs", "items": [
                ("UI", "The interface through which users interact with a system. It includes controls, information presentation, and interaction behavior."),
                ("GUI", "A graphical user interface uses visual elements such as windows, menus, icons, buttons, and pointers. GUI is one type of UI."),
                ("UX", "Broader than UI. It concerns the user's overall experience, perceptions, and outcomes before, during, and after interaction."),
            ]},
            {"type": "callout", "text": "**Academic Context:** HCI is the broader discipline; UI is one major part of designing the interaction."},
            {"type": "cards", "title": "✅ What Makes a Good UI?", "items": [
                ("Understandable", "Users quickly grasp the purpose of the screen, available actions, and current system state."),
                ("Predictable", "Similar actions behave consistently, so users form reliable expectations."),
                ("Efficient", "Tasks are completed without unnecessary steps or mental effort."),
                ("Forgiving", "The design prevents avoidable errors and provides ways to recover."),
                ("Accessible", "Information and controls can be perceived and operated by users with different abilities and contexts."),
                ("Visually organized", "Hierarchy, spacing, typography, and contrast help users locate and interpret information."),
            ]},
        ]},
        {"title": "Core Ideas: 10 Design Principles", "blocks": [
            {"type": "text", "text": "Select a principle below to reveal its lecture details and real-world examples:"},
            {"type": "detail", "label": "Choose a design principle:", "items": [
                {"name": "1. Visibility", "blocks": [
                    {"type": "heading", "text": "👀 Principle 1: Visibility"},
                    {"type": "text", "text": "Important information and available actions should be easy for users to notice when they need them."},
                    {"type": "bullets", "items": ["**What users need to see:** Current status, available actions, important options, progress, and relevant information at the appropriate time."]},
                    {"type": "callout", "kind": "error", "text": "**Poor Visibility example:** A hidden Save action, unclear current page, or invisible system status forces users to guess or search."},
                    {"type": "callout", "kind": "success", "text": "**Design Response:** Use clear labels, visual hierarchy, meaningful placement, and status indicators. Do not hide critical information without a reason. (e.g., an upload button should be obvious when submitting a file)."},
                ]},
                {"name": "2. Feedback", "blocks": [
                    {"type": "heading", "text": "🔄 Principle 2: Feedback"},
                    {"type": "text", "text": "Feedback tells users what happened after they perform an action and helps them understand the system's current state."},
                    {"type": "bullets", "items": [
                        "**Immediate:** Prompt responses tell users the system received their input.",
                        "**Meaningful:** Communicate results, don't just show activity. A loader/spinner alone doesn't prove success.",
                        "**Appropriate:** Match the form of feedback to the importance of the event: subtle for routine actions, clear for errors or critical states."]},
                    {"type": "callout", "kind": "success", "text": "**Example:** After submitting an assignment, show a clear confirmation message with submission status."},
                ]},
                {"name": "3. Consistency", "blocks": [
                    {"type": "heading", "text": "🧩 Principle 3: Consistency"},
                    {"type": "text", "text": "Similar elements, actions, and terminology should behave and appear in similar ways."},
                    {"type": "bullets", "items": [
                        "**Visual:** Use related typography, colors, spacing, icons, and control styles for related functions.",
                        "**Behavioral:** A gesture, button, or shortcut should not change its meaning in different areas.",
                        "**Terminology:** Use the same words for the exact same concept throughout."]},
                    {"type": "callout", "text": "Consistency reduces learning effort because users can transfer previous knowledge to new parts of the interface."},
                ]},
                {"name": "4. Simplicity", "blocks": [
                    {"type": "heading", "text": "🍃 Principle 4: Simplicity"},
                    {"type": "text", "text": "Presenting what users need without unnecessary complexity, not simply removing features."},
                    {"type": "bullets", "items": [
                        "**Reduce Clutter:** Remove decorative or irrelevant elements competing with task-relevant information.",
                        "**Focus the Task:** Prioritize the primary user goal and make the most important actions easy to find.",
                        "**Progressive Disclosure:** Keep advanced or infrequent options available without presenting every choice at once."]},
                    {"type": "callout", "kind": "warning", "text": "**Important:** Simple does not mean empty. The interface should contain the information users actually need."},
                ]},
                {"name": "5. Affordance & Signifiers", "blocks": [
                    {"type": "heading", "text": "🛎️ Principle 5: Affordance & Signifiers"},
                    {"type": "bullets", "items": [
                        "**Affordance:** A possible action provided by an object (e.g., a button affords clicking; a text field affords entering information).",
                        "**Signifier:** Communicates *where* and *how* an action can be performed (labels, borders, icons, cursor changes, familiar shapes)."]},
                    {"type": "callout", "kind": "error", "text": "**Design Problem:** If something is interactive but looks like ordinary text, or looks clickable but is not, users form the wrong expectation."},
                    {"type": "callout", "text": "Good signifiers help users understand what they can do before they act."},
                ]},
                {"name": "6. Mapping", "blocks": [
                    {"type": "heading", "text": "🗺️ Principle 6: Mapping"},
                    {"type": "text", "text": "The relationship between controls and their effects."},
                    {"type": "bullets", "items": [
                        "**Natural Mapping:** The arrangement of controls corresponds directly to the things they control (e.g., a row of switches arranged in the same order as the lights they operate).",
                        "**Poor Mapping:** When the relationship is unclear, users must experiment or remember arbitrary associations.",
                        "**UI Examples:** Volume sliders, temperature controls, and dashboard controls are easier to use when movement and layout match expected outcomes."]},
                ]},
                {"name": "7. Constraints & Error Prevention", "blocks": [
                    {"type": "heading", "text": "🛡️ Principle 7: Constraints & Error Prevention"},
                    {"type": "text", "text": "Limits invalid actions or guides users toward valid choices, preventing predictable errors before they happen."},
                    {"type": "bullets", "items": [
                        "**Input Constraints:** A date field accepts a valid date format; a numeric field rejects alphabetic characters when appropriate.",
                        "**Choice Constraints:** Disable unavailable options or present only valid choices when the system can determine them safely.",
                        "**Dangerous Actions:** For destructive actions, use clear wording, appropriate confirmation, and where feasible an undo or recovery mechanism."]},
                    {"type": "callout", "kind": "success", "text": "Prevention is usually better than forcing users to fix avoidable errors later."},
                ]},
                {"name": "8. User Control & Freedom", "blocks": [
                    {"type": "heading", "text": "🔓 Principle 8: User Control & Freedom"},
                    {"type": "text", "text": "Users should feel that they control the interaction rather than being trapped by the system's workflow."},
                    {"type": "bullets", "items": [
                        "**Undo / Redo:** Where appropriate, let users reverse actions instead of recovering manually.",
                        "**Cancel / Back:** Users should be able to leave or cancel an operation when the context permits.",
                        "**Clear State:** Show where the user is, what is happening, and what choices are available next."]},
                    {"type": "callout", "text": "Control is especially important when actions are irreversible, costly, or time-consuming."},
                ]},
                {"name": "9. Recognition Rather than Recall", "blocks": [
                    {"type": "heading", "text": "🧠 Principle 9: Recognition Rather than Recall"},
                    {"type": "text", "text": "Interfaces should make relevant information and choices visible when practical, reducing the amount users must remember."},
                    {"type": "bullets", "items": [
                        "**Recognition:** Users choose from visible options, labels, examples, or recently used items.",
                        "**Recall:** Users must retrieve information from memory without seeing it, such as command syntax.",
                        "**Balance:** Experienced users may benefit from shortcuts, while visible controls support learning and recognition."]},
                    {"type": "callout", "kind": "success", "text": "**Example:** Autocomplete suggestions reduce the need to remember an exact search term."},
                ]},
                {"name": "10. Visibility of System Status", "blocks": [
                    {"type": "heading", "text": "📊 Principle 10: Visibility of System Status"},
                    {"type": "text", "text": "Keep users informed about what the system is doing through appropriate, timely, and understandable feedback."},
                    {"type": "bullets", "items": [
                        "**Idle / Ready:** Make it clear the system is ready for the next action.",
                        "**Processing:** For operations that take time, show progress or another indication that the request is being handled.",
                        "**Completed / Failed:** Clearly communicate success, failure, or required next steps."]},
                    {"type": "callout", "kind": "success", "text": "**UI Example:** Displaying *'Uploading 3 of 5 files...'* is more informative than leaving the screen unchanged."},
                ]},
            ]},
        ]},
        {"title": "Visual Design & Hierarchy", "blocks": [
            {"type": "text", "text": "Visual hierarchy organizes information so users can quickly distinguish primary content, secondary information, and actions."},
            {"type": "cards", "title": "🔝 Helping Users See What Matters", "items": [
                ("📏 Size", "Larger elements usually attract attention and can communicate importance."),
                ("🌗 Contrast", "Differences in color, weight, or brightness make important elements easier to notice."),
                ("↔️ Spacing", "Whitespace and grouping separate related content and prevent visual clutter."),
                ("📐 Alignment", "Consistent alignment creates structure and makes content easier to scan."),
                ("🔤 Typography", "Font size, weight, and style create levels of importance and improve readability."),
                ("🎨 Color", "Color can emphasize status or categories, but should not be the only way to communicate meaning."),
            ]},
            {"type": "heading", "text": "🎛️ Color, Contrast, Typography & Icons"},
            {"type": "tabs", "items": [
                ("Color", "Use color to communicate meaningful states or categories. Do not rely on color alone because users may have different visual abilities."),
                ("Contrast", "Text and controls need sufficient contrast against their background so users can perceive them clearly."),
                ("Typography", "Choose readable type, appropriate sizes, and clear hierarchy. Avoid decorative styles that reduce legibility."),
                ("Icons", "Icons can save space and support recognition, but unfamiliar icons should have labels or other supporting cues."),
            ]},
            {"type": "callout", "text": "Visual design is functional: it affects perception, attention, interpretation, and task performance."},
        ]},
        {"title": "Practical Case Study & Activity", "is_last": True, "blocks": [
            {"type": "heading", "text": "Good UI vs Poor UI"},
            {"type": "compare",
             "left": {"title": "✅ Good UI", "kind": "success", "items": [
                 "Clear purpose and hierarchy", "Consistent controls and terminology", "Visible system status",
                 "Meaningful feedback", "Appropriate constraints", "Easy recovery from errors", "Readable text and adequate contrast"]},
             "right": {"title": "⚠️ Poor UI", "kind": "error", "items": [
                 "Cluttered information", "Inconsistent labels or controls", "Hidden actions or status",
                 "Ambiguous icons", "No feedback after actions", "Preventable errors", "Difficult recovery"]}},
            {"type": "text", "text": "The goal is not decoration; the goal is to support users in accomplishing their tasks."},
            {"type": "heading", "text": "Case Study: University LMS"},
            {"type": "text", "text": "Imagine a student opening an LMS to submit an assignment. Identify which principles should guide the interface."},
            {"type": "reveal", "items": [
                ("Screen 1: Find the course and assignment", "The student must find the correct course and assignment.", "Visibility, visual hierarchy, consistency, and recognition."),
                ("Screen 2: Upload a file", "The student uploads a file.", "Affordance, constraints, feedback, and visibility of system status."),
                ("Screen 3: Wrong file selected", "The student accidentally selects the wrong file.", "Error prevention, user control, undo/cancel, and clear recovery."),
            ]},
            {"type": "text", "text": "**Class question:** Which principle would you prioritize first, and why?"},
            {"type": "answer_box", "label": "Your answer (for discussion only, not saved):"},
            {"type": "heading", "text": "Class Activity"},
            {"type": "discussion", "items": [
                ("Find one UI you use every day.", "Identify one design principle it follows well."),
                ("Find one confusing interface element.", "Which principle is violated and what could be changed?"),
                ("Think about a delete button.", "What feedback, constraints, and recovery should be provided?"),
                ("Compare two login screens.", "Which one reduces cognitive effort? Explain using at least two principles."),
            ]},
            {"type": "heading", "text": "Lecture Summary"},
            {"type": "callout", "text": "* Good UI makes interaction **understandable, predictable, and controllable**.\n* Make important information visible and provide clear feedback.\n* Use consistency, simplicity, affordances, mapping, and constraints to reduce user effort and errors.\n* Support recognition, visual hierarchy, accessibility, and recovery from mistakes."},
        ]},
    ],
}
