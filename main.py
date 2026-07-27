import streamlit as st
from post_generator import generate_post
from utils import create_pdf, create_docx

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.markdown("""
    <style>

    /* ===========================================
                    PAGE BACKGROUND
    =========================================== */

    .stApp{
    background-image: url("https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=1920&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

    /* Hide Streamlit Header & Footer */

    header{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    /* ===========================================
                    MAIN CARD
    =========================================== */

    .block-container{

        max-width:760px;

        margin-top:35px;

        margin-bottom:35px;

        padding:45px;

        border-radius:24px;

        background:#F3F6FB;

        box-shadow:
            0 15px 40px rgba(15,23,42,.12);

        border:1px solid rgba(148,163,184,.18);

    }

    /* ===========================================
                    TITLE
    =========================================== */

    h1{

        text-align:center;

        color:#1E3A8A;

        font-size:48px;

        font-weight:700;

        margin-bottom:5px;

    }

    .subtitle{

        text-align:center;

        color:#64748B;

        font-size:19px;

        margin-bottom:35px;

    }

    /* ===========================================
                    LABELS
    =========================================== */

    label{

        color:#334155 !important;

        font-weight:600;

        font-size:15px;

    }

    /* ===========================================
                  TEXT INPUT
    =========================================== */

    .stTextInput input{

        background:#FFFFFF !important;

        color:#111827 !important;

        border:1px solid #CBD5E1 !important;

        border-radius:12px !important;

        padding:12px !important;

        font-size:16px !important;

    }

    .stTextInput input:focus{

        border:2px solid #2563EB !important;

        box-shadow:0 0 10px rgba(37,99,235,.25);

    }

    /* ===========================================
                  SELECT BOX
    =========================================== */

    div[data-baseweb="select"]{

        background:#FFFFFF !important;

        border-radius:12px !important;

        border:1px solid #CBD5E1 !important;

    }

    div[data-baseweb="select"] *{

        background:#FFFFFF !important;

        color:#111827 !important;

    }

    /* ===========================================
                  DROPDOWN MENU
    =========================================== */

    ul{

        background:#FFFFFF !important;

    }

    li{

        color:#111827 !important;

    }

    /* ===========================================
                  BUTTON
    =========================================== */

    .stButton>button{

        width:100%;

        height:58px;

        border:none;

        border-radius:14px;

        background:linear-gradient(
            90deg,
            #3B82F6,
            #2563EB
        );

        color:white;

        font-size:18px;

        font-weight:700;

        transition:.25s;

    }

    .stButton>button:hover{

        background:linear-gradient(
            90deg,
            #2563EB,
            #1D4ED8
        );

        transform:translateY(-2px);

        box-shadow:0 8px 18px rgba(37,99,235,.30);

    }

    /* ===========================================
              GENERATED CONTENT
    =========================================== */

    .stMarkdown{

        color:#1E293B;

        font-size:17px;

        line-height:1.8;

    }

    /* ===========================================
                SUCCESS MESSAGE
    =========================================== */

    .stAlert{

        border-radius:12px;

    }

    /* ===========================================
                 SCROLLBAR
    =========================================== */

    ::-webkit-scrollbar{

        width:10px;

    }

    ::-webkit-scrollbar-thumb{

        background:#94A3B8;

        border-radius:10px;

    }

    ::-webkit-scrollbar-track{

        background:#E2E8F0;

    }

    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h1>📚 EduGenAI</h1>

    <p class="subtitle">
    AI Powered Academic Content Generator
    </p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        selected_tag = st.text_input("Enter the Topic !")
    with col2:
        selected_length = st.selectbox("Length", options=length_options)
    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    tone_options = [
        "Academic",
        "Formal",
        "Professional",
        "Friendly",
        "Casual",
        "Creative"
    ]

    education_options = [
        "School",
        "High School",
        "College",
        "Undergraduate",
        "Graduate"
    ]

    content_options = [
        "Assignment",
        "Essay",
        "Notes",
        "Research Article",
        "Blog",
        "Speech"
    ]

    selected_content = st.selectbox(
        "Content Type",
        content_options
    )

    selected_tone = st.selectbox(
        "Tone",
        tone_options
    )

    selected_education = st.selectbox(
        "Education Level",
        education_options
    )

    if st.button("🚀 Generate"):
        post = generate_post(
            selected_length,
            selected_language,
            selected_tag,
            selected_tone,
            selected_education,
            selected_content,
        )

        st.markdown("---")

        st.subheader("✨ Generated Content")

        st.write(post)

        pdf = create_pdf(post)
        docx = create_docx(post)

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                "📄 Download PDF",
                data=pdf,
                file_name="EduGenAI_Content.pdf",
                mime="application/pdf",
            )

        with col2:
            st.download_button(
                "📝 Download DOCX",
                data=docx,
                file_name="EduGenAI_Content.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )

if __name__ == "__main__":
    main()