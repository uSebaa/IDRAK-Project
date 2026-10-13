import streamlit as st
import joblib
import numpy as np
from textwrap import dedent
from pathlib import Path
from html import escape

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="IDRAK | Banking Made Smarter",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent

# ==================================================
# DESIGN SYSTEM
# ==================================================

st.markdown("""
<style>
/* IDRAK Logo - Remove Extra Spacing */

[data-testid="stImage"] {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

[data-testid="stImage"] img {
    display: block;
}
/* ==========================================
   WHY IDRAK - EQUAL SIZE CARDS
   ========================================== */

.feature-card {
    height: 200px !important;
    min-height: 200px !important;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.feature-card p {
    margin-bottom: 0;
}

.feature-card p {
    margin-top: auto;
}
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #102B60;
    --blue: #1264E8;
    --light-blue: #EAF3FF;
    --background: #F7FAFF;
    --muted: #61738F;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(
        135deg,
        #F5F9FF 0%,
        #FFFFFF 65%,
        #F3F8FF 100%
    );
}

/* Hide sidebar */
[data-testid="stSidebar"],
[data-testid="collapsedControl"] {
    display: none !important;
}

/* Remove extra top spacing */
[data-testid="stHeader"] {
    height: 0;
    min-height: 0;
    background: transparent;
}

[data-testid="stToolbar"] {
    display: none;
}

/* Main container */
.block-container {
    max-width: 1280px;
    padding-top: 0.5rem !important;
    padding-bottom: 3rem;
}

/* Remove unnecessary top margin */
[data-testid="stMainBlockContainer"] {
    padding-top: 0.5rem !important;
}

/* Typography */
h1, h2, h3 {
    color: #102B60 !important;
    letter-spacing: -0.5px;
}

/* Navigation */
.nav-brand {
    font-size: 27px;
    font-weight: 800;
    color: #102B60;
    letter-spacing: 1px;
    padding-top: 7px;
}

.nav-subtitle {
    font-size: 11px;
    color: #61738F;
    margin-top: -5px;
}

/* Buttons */
div.stButton > button {
    border-radius: 12px;
    font-weight: 600;
    min-height: 45px;
    transition: all 0.2s ease;
}

div.stButton > button[kind="primary"] {
    background: linear-gradient(
        90deg,
        #1264E8,
        #267CF4
    );
    color: white;
    border: none;
    box-shadow: 0 5px 15px rgba(18, 100, 232, 0.15);
}

div.stButton > button[kind="primary"]:hover {
    background: #104FC1;
    color: white;
}

/* Hero */
.hero {
    background: linear-gradient(
        115deg,
        #E8F2FF 0%,
        #FFFFFF 75%
    );
    border: 1px solid #E0EBFB;
    border-radius: 24px;
    padding: 55px 48px;
    margin-top: 25px;
    margin-bottom: 28px;
}

.hero-badge {
    display: inline-block;
    background: #DCEBFF;
    color: #1555C8;
    padding: 8px 15px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 18px;
}

.hero-title {
    font-size: clamp(30px, 4vw, 48px);
    font-weight: 800;
    color: #102B60;
    line-height: 1.2;
}

.hero-title span {
    color: #1264E8;
}

.hero-description {
    font-size: 17px;
    color: #536987;
    max-width: 620px;
    line-height: 1.8;
    margin-top: 18px;
}

/* Feature badges */
.hero-features {
    display: flex;
    flex-wrap: wrap;
    gap: 22px;
    margin-top: 28px;
    color: #244575;
    font-size: 14px;
    font-weight: 600;
}

/* Section titles */
.section-title {
    font-size: 27px;
    font-weight: 800;
    color: #102B60;
    text-align: center;
    margin-bottom: 8px;
}

.section-subtitle {
    color: #61738F;
    text-align: center;
    font-size: 15px;
    margin-bottom: 25px;
}

/* Prediction */
.prediction-card {
    background: linear-gradient(
        115deg,
        #EAF3FF,
        #FFFFFF
    );
    border: 1px solid #DCE9FB;
    border-radius: 20px;
    padding: 28px;
    margin-top: 15px;
    margin-bottom: 20px;
}

.prediction-label {
    color: #61738F;
    font-size: 14px;
    font-weight: 500;
}

.prediction-value {
    color: #102B60;
    font-size: 29px;
    font-weight: 800;
    margin-top: 10px;
    overflow-wrap: anywhere;
}

.confidence-value {
    color: #1264E8;
    font-size: 16px;
    font-weight: 700;
    margin-top: 12px;
}

/* Info cards */
.feature-card {
    background: #FFFFFF;
    border: 1px solid #E5EDFA;
    border-radius: 18px;
    padding: 24px;
    min-height: 160px;
    box-shadow: 0 5px 20px rgba(30, 75, 140, 0.04);
}

.feature-title {
    font-size: 16px;
    font-weight: 700;
    color: #102B60;
    margin-bottom: 10px;
}

.feature-description {
    color: #61738F;
    font-size: 13px;
    line-height: 1.7;
}

/* Footer */
.footer {
    margin-top: 65px;
    padding: 30px;
    border-radius: 18px;
    background: #102B60;
    color: #FFFFFF;
    text-align: center;
}

.footer-title {
    font-size: 21px;
    font-weight: 800;
    margin-bottom: 8px;
}

.footer-description {
    color: #C8D7F2;
    font-size: 13px;
}

/* Input */
textarea {
    border-radius: 14px !important;
    border: 1px solid #DCE6F5 !important;
}

/* Responsive */
@media (max-width: 768px) {
    .hero {
        padding: 30px 22px;
    }

    .hero-title {
        font-size: 31px;
    }

    .hero-features {
        gap: 12px;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# LOAD TRAINED MODEL
# ==================================================
@st.cache_resource
def load_model_artifacts():

    model = joblib.load(
        BASE_DIR / "banking_pipeline.joblib"
    )

    categories = joblib.load(
        BASE_DIR / "categories.joblib"
    )

    # Compatibility fix for the saved Logistic Regression model
    classifier = model.named_steps["classifier"]

    if not hasattr(classifier, "multi_class"):
        classifier.multi_class = "auto"

    return model, categories


try:
    model, categories = load_model_artifacts()
    model_ready = True

except Exception as error:
    model_ready = False
    model_error = str(error)


# ==================================================
# HELPER FUNCTIONS
# ==================================================
def render_html(html):
    cleaned_html = dedent(html).strip()

    cleaned_html = "\n".join(
        line.lstrip()
        for line in cleaned_html.splitlines()
    )

    st.markdown(
        cleaned_html,
        unsafe_allow_html=True
    )
def format_intent(intent):
    return str(intent).replace("_", " ").title()


def feature_card(icon, title, description):

    render_html(f"""
    <div class="feature-card">
        <div style="font-size:27px;margin-bottom:12px;">
            {escape(icon)}
        </div>
        <div class="feature-title">
            {escape(title)}
        </div>
        <div class="feature-description">
            {escape(description)}
        </div>
    </div>
    """)

def get_routing_recommendation(confidence):

    # Demonstration thresholds, not validated routing rules.
    if confidence >= 0.75:

        return (
            "Self-Service Suggested",
            "This request may be suitable for a self-service "
            "support workflow. No banking action has been executed."
        )

    elif confidence >= 0.40:

        return (
            "Specialist Review Suggested",
            "A banking support specialist may be helpful "
            "to review this request."
        )

    else:

        return (
            "Human Review Recommended",
            "The model has low confidence in this prediction. "
            "A human support agent should review the request."
        )


def get_customer_steps(intent):

    intent = str(intent).lower()

    if intent == "lost_or_stolen_card":

        return [
            (
                "🔒 Secure Your Card",
                "Freeze your card immediately through your "
                "bank's official app, if available."
            ),
            (
                "💳 Review Transactions",
                "Check your recent transactions for "
                "any unauthorized activity."
            ),
            (
                "📱 Request a Replacement",
                "Contact your bank through its official "
                "support channels to request a replacement card."
            )
        ]

    elif "transfer" in intent:

        return [
            (
                "🔍 Check Transfer Status",
                "Review the transfer status in your banking app."
            ),
            (
                "📋 Verify Transfer Details",
                "Check the recipient details and transfer reference."
            ),
            (
                "🏦 Contact Your Bank",
                "If the transfer remains pending, contact "
                "your bank through its official support channels."
            )
        ]

    elif "atm" in intent or "cash" in intent:

        return [
            (
                "💰 Review Your Transactions",
                "Check whether the amount was deducted "
                "from your account."
            ),
            (
                "📝 Record Transaction Details",
                "Keep the ATM location, date, time, "
                "and transaction reference."
            ),
            (
                "🏦 Report the Issue",
                "Contact your bank through its official "
                "support channels."
            )
        ]

    elif "pin" in intent:

        return [
            (
                "📱 Open Your Banking App",
                "Check whether your bank offers "
                "PIN management services."
            ),
            (
                "🔒 Follow Secure Instructions",
                "Use only your bank's official channels "
                "to change or reset your PIN."
            ),
            (
                "🤝 Request Assistance",
                "Contact customer support if you "
                "cannot complete the process."
            )
        ]

    else:

        return [
            (
                "🔍 Review Your Banking Service",
                "Check the relevant service in your "
                "bank's official application."
            ),
            (
                "📋 Check Available Information",
                "Review the information related "
                "to your request."
            ),
            (
                "🤝 Contact Customer Support",
                "Contact your bank through its official "
                "support channels if you need further help."
            )
        ]

# ==================================================
# SESSION STATE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "query_text" not in st.session_state:
    st.session_state.query_text = ""

if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None


def navigate(page):
    st.session_state.page = page


def set_example(message):
    st.session_state.query_text = message
    st.session_state.prediction_result = None


def reset_request():
    st.session_state.query_text = ""
    st.session_state.prediction_result = None


# ==================================================
# TOP NAVIGATION
# ==================================================

nav_brand, nav_home, nav_services, nav_about, nav_insights = st.columns(
    [2.5, 1, 1.4, 1.4, 1.8],
    gap="small"
)

with nav_brand:

    logo_path = BASE_DIR / "idrak_logo.png"

    if logo_path.exists():
        st.image(str(logo_path), width=145)
    else:
        st.markdown(
            '<div class="nav-brand">💠 IDRAK</div>'
            '<div class="nav-subtitle">Banking Made Smarter</div>',
            unsafe_allow_html=True
        )

with nav_home:
    st.button(
        "Home",
        use_container_width=True,
        on_click=navigate,
        args=("Home",)
    )

with nav_services:
    st.button(
        "Our Services",
        use_container_width=True,
        on_click=navigate,
        args=("Our Services",)
    )

with nav_about:
    st.button(
        "About IDRAK",
        use_container_width=True,
        on_click=navigate,
        args=("About IDRAK",)
    )

with nav_insights:
    st.button(
        "AI Model Insights",
        use_container_width=True,
        on_click=navigate,
        args=("AI Model Insights",)
    )


# ==================================================
# MODEL CHECK
# ==================================================

if not model_ready:

    st.error(
        "The trained model could not be loaded. "
        "Please check the model files."
    )

    st.code(model_error)
    st.stop()


# ==================================================
# HOME PAGE
# ==================================================

if st.session_state.page == "Home":

    # ----------------------------------------------
    # HERO SECTION
    # ----------------------------------------------

    render_html("""
<div class="hero">

    <div class="hero-badge">
        ✦ AI-POWERED BANKING ASSISTANCE
    </div>

    <div class="hero-title">
        Your Banking Needs,<br>
        <span>Understood in Seconds.</span>
    </div>


    </div>

    <div class="hero-features">
        <span>⚡ Fast Classification</span>
        <span>🛡️ Customer-Focused</span>
        <span>✨ Easy to Use</span>
    </div>

</div>
""")

    # ----------------------------------------------
    # CUSTOMER INQUIRY
    # ----------------------------------------------

    render_html("""
    <div class="section-title">
        How can we help you today?
    </div>

    <div class="section-subtitle">
    Describe your banking question or request,
    and IDRAK will identify the most relevant service.
    </div>
    """)

    st.text_area(
        "Your Banking Inquiry",
        key="query_text",
        placeholder=(
            "Example: I lost my bank card "
            "and need a replacement..."
        ),
        height=130,
        max_chars=500
    )

    st.caption(
        "🔒 For your security, never share your PIN, "
        "password, or full card number."
    )

    st.markdown("#### Try an Example")

    examples = {
        "💳 Stolen Card":
            "My credit card was stolen while traveling, "
            "please freeze it immediately!",

        "⏳ Pending Transfer":
            "Why is my international wire transfer "
            "still pending after three days?",

        "🏧 ATM Cash Error":
            "The ATM did not dispense my cash "
            "but the amount was deducted from my account.",

        "🔒 PIN Change":
            "How do I change the security PIN "
            "code for my new card?"
    }

    example_cols = st.columns(4)

    for col, (label, message) in zip(
        example_cols,
        examples.items()
    ):

        with col:

            st.button(
                label,
                use_container_width=True,
                on_click=set_example,
                args=(message,)
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ----------------------------------------------
    # CLASSIFICATION ACTION
    # ----------------------------------------------

    if st.button(
        "Find My Banking Service →",
        type="primary",
        use_container_width=True
    ):

        query = st.session_state.query_text.strip()

        if not query:

            st.warning(
                "Please enter a banking inquiry first."
            )

        else:

            # REAL MODEL INFERENCE
            probabilities = model.predict_proba([query])[0]

            # Class order must match predict_proba columns
            class_labels = np.asarray(model.classes_)

            top_indices = np.argsort(
                probabilities
            )[::-1][:3]

            top_index = top_indices[0]

            top_intent = class_labels[top_index]

            top_score = float(
                probabilities[top_index]
            )

            st.session_state.prediction_result = {
                "query": query,
                "top_intent": str(top_intent),
                "top_score": top_score,
                "top_predictions": [
                    (
                        str(class_labels[index]),
                        float(probabilities[index])
                    )
                    for index in top_indices
                ]
            }

       # ==================================================
    # PREDICTION RESULTS
    # ==================================================

    result = st.session_state.prediction_result

    if result is not None:

        st.markdown("---")

        st.markdown("## ✨ We Understand Your Request!")

        st.write(
            "Here is the banking service "
            "that best matches your inquiry."
        )

        # ==========================================
        # RESULT COLUMNS
        # ==========================================

        result_col, predictions_col = st.columns(
            [1.3, 1],
            gap="large"
        )

        # ==========================================
        # LEFT COLUMN — PRIMARY PREDICTION
        # ==========================================

        with result_col:

                formatted_intent = format_intent(
                result["top_intent"]
            )

            # Customer-friendly prediction message
                if result["top_intent"] == "lost_or_stolen_card":
                    customer_message = (
                        "💳 It looks like your card was lost or stolen."
            )
                else:
                    customer_message = (
                        f"It looks like your request is related to "
                     f"{formatted_intent.lower()}."
            )

            # Prediction result card
                prediction_html = (
                '<div class="prediction-card">'
                '<div class="prediction-label">'
                'We Understand Your Concern'
                '</div>'
                '<div class="prediction-value">'
                f'{escape(customer_message)}'
                '</div>'
                '<div class="confidence-value">'
                f'Model Score: {result["top_score"] * 100:.1f}%'
                '</div>'
                '</div>'
            )

                st.markdown(
                prediction_html,
                unsafe_allow_html=True
            )

                st.progress(result["top_score"])

                st.caption(
                "The model score is not a guarantee "
                "that the prediction is correct."
            )

        # ==========================================
        # RIGHT COLUMN — OTHER PREDICTIONS
        # ==========================================

        with predictions_col:

            st.markdown("### Other Possible Services")

            for intent, score in result["top_predictions"]:

                st.markdown(
                    f"**{format_intent(intent)}** "
                    f"— {score * 100:.1f}%"
                )

                st.progress(score)

        # ==========================================
        # CUSTOMER GUIDANCE
        # ==========================================

                # ==========================================
        # CUSTOMER RECOMMENDED STEPS
        # ==========================================

        st.markdown("### 💡 Your Recommended Steps")

        steps = get_customer_steps(
            result["top_intent"]
        )

        for index, (title, description) in enumerate(
            steps, start=1
        ):
            with st.container(border=True):
                st.markdown(
                    f"#### Step {index} — {title}"
                )
                st.write(description)

        # ==========================================
        # AI SUPPORT RECOMMENDATION
        # ==========================================

        with st.expander("View AI Support Recommendation"):

            routing_title, routing_description = (
                get_routing_recommendation(
                    result["top_score"]
                )
            )

            st.markdown(f"**{routing_title}**")

            st.write(routing_description)

            st.caption(
                "Routing suggestions are illustrative. "
                "No automated workflow or support ticket "
                "has been created."
            )

        # ==========================================
        # RESET REQUEST
        # ==========================================

        st.markdown("<br>", unsafe_allow_html=True)

        st.button(
            "Start New Request",
            use_container_width=True,
            on_click=reset_request
        )

    # ----------------------------------------------
    # FEATURE CARDS
    # ----------------------------------------------

    st.markdown("---")

    st.markdown("### Why IDRAK?")

    f1, f2, f3 = st.columns(3)

    with f1:
        feature_card(
            "💬",
            "Understand Your Request",
            "Describe your banking concern "
            "in natural English."
        )

    with f2:
        feature_card(
            "🎯",
            "Identify Banking Services",
            "IDRAK predicts the most relevant "
            "banking intent using NLP."
        )

    with f3:
        feature_card(
            "🛡️",
            "Helpful Guidance",
            "Receive general suggestions "
            "for your next step."
        )


# ==================================================
# OUR SERVICES
# ==================================================

elif st.session_state.page == "Our Services":

    st.title("Our Services")

    st.write(
        "IDRAK helps customers identify banking "
        "service categories through natural language."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        feature_card(
            "💳",
            "Card Services",
            "Identify questions related to "
            "cards, PINs, and card issues."
        )

    with c2:
        feature_card(
            "💸",
            "Transfers & Payments",
            "Understand inquiries involving "
            "transfers and payment issues."
        )

    with c3:
        feature_card(
            "🏦",
            "Account Assistance",
            "Classify questions related to "
            "bank accounts and verification."
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.button(
        "Get Started →",
        type="primary",
        on_click=navigate,
        args=("Home",)
    )


# ==================================================
# ABOUT IDRAK
# ==================================================

elif st.session_state.page == "About IDRAK":

    st.title("About IDRAK")

    render_html("""
<div class="hero">

    <div class="hero-title">
        Meet IDRAK,<br>
        <span>Your Smart Banking Companion.</span>
    </div>

    <div class="hero-description">
        IDRAK is here to make your banking experience simpler
        Whether it’s a card issue, a transfer, or another banking question, IDRAK helps you understand your concern.
       Get clear guidance to help you take the next step.
    </div>

</div>
""")

    st.markdown("## How IDRAK Works")

    c1, c2, c3 = st.columns(3)

    with c1:
        feature_card(
            "✍️",
            "1.Tell Us What's Wrong",
            "Describe your banking issue in your own words. "
        )

    with c2:
        feature_card(
            "🧠",
            "2. We Understand Your Concern",
            "We Understand Your Concern"
            "what you need."
        )

    with c3:
        feature_card(
            "✨",
            "3. Get Helpful Guidance",
            "Receive suggested steps to help you "
            "handle your banking concern."
        )

    st.markdown("### Your Security Matters")

    st.info(
        "🔒 For your security, never share your password, "
        "PIN, OTP, or full card number. "
        "IDRAK will never ask you for these details."
    )

    st.caption(
        "IDRAK is a demonstration prototype. "
        "It is not affiliated with a bank and does not "
        "access accounts or execute banking transactions."
    )


# ==================================================
# AI MODEL INSIGHTS
# ==================================================

elif st.session_state.page == "AI Model Insights":

    st.title("AI Model Insights")

    st.write(
        "Explore the machine learning technology "
        "behind IDRAK."
    )

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Top-1 Accuracy",
            "89.42%"
        )

    with c2:
        st.metric(
            "Intent Categories",
            len(model.classes_)
        )

    with c3:
        st.metric(
            "Model Type",
            "Logistic Regression"
        )

    st.markdown("### Model Architecture")

    st.markdown(
        "**Customer Inquiry → TF-IDF → "
        "Logistic Regression → Intent Prediction**"
    )

    st.markdown("### Dataset")

    st.write(
        "IDRAK uses the Banking77 dataset, "
        "which contains English banking inquiries "
        "across 77 intent categories."
    )

    st.markdown("### Model Evaluation")

    st.info(
        "The displayed 89.42% Top-1 Accuracy "
        "is a previously reported project result. "
        "It is not recalculated by this dashboard."
    )

    st.caption(
        "Model performance on real-world customer "
        "messages has not been established."
    )


# ==================================================
# FOOTER
# ==================================================

st.markdown(
    """
    <div style="
        text-align: center;
        margin-top: 22px;
        margin-bottom: 25px;
        font-size: 15px;
        font-weight: 500;
        color: #142F63;
        letter-spacing: 0.3px;
    ">
        IDRAK Here to Help You Understand Your Banking Needs.
    </div>
    """,
    unsafe_allow_html=True
)
