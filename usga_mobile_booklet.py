import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="USGA U.S. Open Player Memo", layout="wide", page_icon="https://idss-proxy.imgix.net/https%3A%2F%2Ffiles.idss.com%2FC32%2F0efcbc6c-d7cc-4aa2-9ee5-ca7e854a3fe3.png?auto=compress%2Cformat&fit=max&h=1080&q=80&w=1920&s=25f63e35e4c282d2d2a004f9827045c7")

# --- Floating Top-Right Toggle Button with Emoji ---
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False

query_params = st.experimental_get_query_params()
if "toggle_theme" in query_params:
    st.session_state["dark_mode"] = not st.session_state["dark_mode"]
    st.experimental_set_query_params()  # Clear params after use

toggle_code = f"""
<style>
#theme-toggle {{
    position: fixed;
    top: 1rem;
    right: 1rem;
    z-index: 9999;
}}
</style>
<div id="theme-toggle">
    <form>
        <button name="toggle_theme" type="submit" style="font-size:1.2rem; padding:0.4rem 0.75rem; border-radius:10px; border:none; background:#005BAC; color:white;">
            {'☀️' if st.session_state["dark_mode"] else '🌙'}
        </button>
    </form>
</div>
"""
st.markdown(toggle_code, unsafe_allow_html=True)

# --- Apply Dark/Light Mode Styling with Animation ---
if st.session_state["dark_mode"]:
    st.markdown("""
        <style>
        .main, .block-container {
            background-color: #111111 !important;
            color: #f0f0f0 !important;
            transition: background-color 0.4s ease, color 0.4s ease;
        }
        .title, .subtitle, .content {
            color: #f0f0f0 !important;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .main, .block-container {
            background-color: #ffffff !important;
            color: #222222 !important;
            transition: background-color 0.4s ease, color 0.4s ease;
        }
        .title, .subtitle, .content {
            color: #222222 !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- Style Override ---
st.markdown("""
    <style>
    .main {background-color: #f9f9f9; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;}
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    .title {font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem; color: #002664;}
    .section {margin-top: 2rem; margin-bottom: 2rem;}
    .subtitle {font-size: 1.25rem; font-weight: 600; color: #005BAC; margin-top: 1rem;}
    .content {font-size: 1rem; line-height: 1.6; color: #333333;}
    .button {background-color: #002664; color: white; border-radius: 12px; padding: 0.6rem 1rem; border: none; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# --- Header ---
" "
st.image("https://idss-proxy.imgix.net/https%3A%2F%2Ffiles.idss.com%2FC32%2F0efcbc6c-d7cc-4aa2-9ee5-ca7e854a3fe3.png?auto=compress%2Cformat&fit=max&h=1080&q=80&w=1920&s=25f63e35e4c282d2d2a004f9827045c7", width=150)
st.markdown("<div class='title'>2025 U.S. Open Player Memo</div>", unsafe_allow_html=True)

# --- Navigation ---
section = st.selectbox("Jump to Section", [
    "Welcome Message",
    "Schedule Overview",
    "Player Services",
    "Dining Options",
    "Transportation Info",
    "Contact & Emergency Info"
])

# --- Content Sections ---
if section == "Welcome Message":
    st.markdown("""
    <div class='section'>
        <div class='subtitle'>Welcome to Oakmont!</div>
        <div class='content'>
        We are thrilled to host you at the 2025 U.S. Open Championship. This interactive booklet is your digital hub for everything from schedules to dining to transportation. Swipe through and tap the menu to jump around.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif section == "Schedule Overview":
    st.markdown("""
    <div class='section'>
        <div class='subtitle'>Key Championship Dates</div>
        <div class='content'>
        - Mon, June 9: Player registration & practice rounds<br>
        - Tue, June 10: Practice rounds & media day<br>
        - Wed, June 11: Final practice day<br>
        - Thu–Sun, June 12–15: Championship rounds
        </div>
    </div>
    """, unsafe_allow_html=True)

elif section == "Player Services":
    st.markdown("""
    <div class='section'>
        <div class='subtitle'>On-Site Amenities</div>
        <div class='content'>
        - Locker rooms with full amenities<br>
        - Massage therapists on-call (book via Player App)<br>
        - Daily laundry pickup & return<br>
        - Physio & athletic training staff available daily
        </div>
    </div>
    """, unsafe_allow_html=True)

elif section == "Dining Options":
    st.markdown("""
    <div class='section'>
        <div class='subtitle'>Cafeteria & Grab-and-Go</div>
        <div class='content'>
        Located near the clubhouse entrance, open 6:00 AM – 8:00 PM.<br>
        Options include smoothies, protein bowls, and fresh sandwiches. Special dietary needs can be flagged via the app.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif section == "Transportation Info":
    st.markdown("""
    <div class='section'>
        <div class='subtitle'>Shuttles & Parking</div>
        <div class='content'>
        Complimentary player shuttle runs every 15 minutes from hotels.<br>
        Player parking available at Gate 3 with credential.<br>
        Caddies should use designated lot at Gate 2.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif section == "Contact & Emergency Info":
    st.markdown("""
    <div class='section'>
        <div class='subtitle'>Key Contacts</div>
        <div class='content'>
        - Player Services: +1 (555) 123-4567<br>
        - Medical Emergency: Dial 911<br>
        - On-site security: +1 (555) 765-4321<br>
        - Lost & Found: Locker Room Services Desk
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<hr style='border: 0; border-top: 1px solid #ccc;'>
<p style='text-align:center; font-size: 0.8rem;'>© 2025 United States Golf Association. All Rights Reserved.</p>
""", unsafe_allow_html=True)
