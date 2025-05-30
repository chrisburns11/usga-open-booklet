import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="USGA U.S. Open Player Memo",
    layout="wide",
    page_icon="https://idss-proxy.imgix.net/https%3A%2F%2Ffiles.idss.com%2FC32%2F0efcbc6c-d7cc-4aa2-9ee5-ca7e854a3fe3.png?auto=compress%2Cformat&fit=max&h=1080&q=80&w=1920&s=25f63e35e4c282d2d2a004f9827045c7"
)

components.html("""
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-69MWYNCENJ"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-69MWYNCENJ', {
        send_page_view: true,
        page_path: window.location.pathname,
        page_title: document.title
      });
      gtag('event', 'page_view', {
        page_location: window.location.href,
        page_path: window.location.pathname,
        page_title: document.title
      });
    </script>
""", height=0)

col1, = st.columns([1])

with col1:
    dark_mode = st.toggle("🌙", value=False, label_visibility="visible")

# Apply dark or light mode styles
def apply_theme(is_dark):
    if is_dark:
        st.markdown(
            """
            <style>
            html, body, .stApp {
                background-color: #1e1e1e;
                color: #f5f5f5;
            }
            .stMarkdown, .stText, .stDataFrame, .stButton > button, .stSlider, .stSelectbox {
                color: #f5f5f5 !important;
            }
            .stTextInput, .stTextArea, .stSelectbox, .stMultiSelect, .stDateInput {
                color: white !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            html, body, .stApp {
                background-color: #D3D3D3;
                color: #D3D3D3;
            }
            .stMarkdown, .stText, .stDataFrame, .stButton > button, .stSlider, .stSelectbox {
                color: #D3D3D3 !important;
            }
            .stTextInput, .stTextArea, .stSelectbox, .stMultiSelect, .stDateInput {
                color: white !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

apply_theme(dark_mode)

# --- Hide Streamlit UI Elements ---
st.markdown("""
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .stApp > footer {display: none;}
    .viewerBadge_container__1QSob {display: none !important;}
    </style>
""", unsafe_allow_html=True)

# --- Style Override ---
st.markdown("""
    <style>
    .main {background-color: #f9f9f9; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;}
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    .title {font-size: 1.5rem; font-weight: 600; margin-bottom: 0.5rem; color: #ffffff;}
    .section {margin-top: 2rem; margin-bottom: 2rem;}
    .subtitle {font-size: 1.25rem; font-weight: 600; color: #005BAC; margin-top: 1rem;}
    .content {font-size: 1rem; line-height: 1.6; color: #FFFFFF;}
    .button {background-color: #002664; color: white; border-radius: 12px; padding: 0.6rem 1rem; border: none; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://idss-proxy.imgix.net/https%3A%2F%2Ffiles.idss.com%2FC32%2F0efcbc6c-d7cc-4aa2-9ee5-ca7e854a3fe3.png?auto=compress%2Cformat&fit=max&h=1080&q=80&w=1920&s=25f63e35e4c282d2d2a004f9827045c7" width="150">
    </div>
    """,
    unsafe_allow_html=True
)

# --- Navigation ---
section = st.selectbox("", [
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
        Welcome to the 2025 U.S. Open at Oakmont! This mobile booklet is your go-to guide for everything you need during championship week — from schedules and dining options to transportation and player services. We’re thrilled to have you here and are committed to making your experience seamless and unforgettable.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif section == "Schedule Overview":
    st.markdown("""
    <div class='section'>
        <div class='subtitle'>Key Championship Dates</div>
        <div class='content'>
        <br>
            Player Registration<br>
            &emsp;&emsp;• Saturday, June 8th (12:00 P.M. - 6:00 P.M.)<br>
            &emsp;&emsp;• Sunday, June 9th (7:00 A.M. - 6:00 P.M.)<br>
            &emsp;&emsp;• Monday, June 10th (6:00 A.M. - 6:00 P.M.)<br>
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
