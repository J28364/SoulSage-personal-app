import streamlit as st
import random
st.set_page_config(page_title="ค้นหาตัวตน", page_icon="🔑", layout="centered")

# ---------- ธีม UI ----------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-photo/aesthetic-blue-spectrum-lens-flare-purple-background_53876-104437.jpg");
        background-size: cover;
    }
    h1 {
        color: #ffcc00;
        text-align: center;
    }
    .question {
        font-size: 20px;
        font-weight: bold;
        color: #f5f5f5;
    }
    .option {
        font-size: 18px;
        color: #ffffff;
    }
    .button-container {
        position: fixed;
        bottom: 20px;
        right: 60px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("SoulSage")

# ---------- คำถาม ----------
journey = [
    {"intro": "🔮 คุณเคยได้ยินเสียงในใจที่เงียบกว่าคำพูดใดๆ หรือไม่? เสียงนั้นอาจเป็นคำตอบที่คุณเฝ้าตามหา",
     "question": "💭 ถ้าจิตวิญญาณของคุณสามารถพูดได้ มันจะบอกอะไรกับคุณ?",
     "options": ["ฉันต้องการเข้าใจทุกสิ่ง", "ฉันยังไม่รู้ว่าฉันเป็นใคร", "ฉันกำลังเดินทางไปสู่บางสิ่ง",
                 "ฉันพร้อมจะก้าวผ่านทุกอย่าง"]},

    {"intro": "🌌 ภายในตัวเรามีดวงดาวที่ดับไปแล้ว และดวงดาวที่ยังส่องแสง... คุณคือดวงดาวแบบไหน?",
     "question": "✨ เมื่อคุณเผชิญกับความมืดมิด คุณเลือกที่จะ...",
     "options": ["ส่องแสงของตัวเอง", "ซ่อนตัวและรอให้ความมืดผ่านไป", "ค้นหาความหมายจากมัน",
                 "ยอมรับมันเป็นส่วนหนึ่งของฉัน"]},

    {"intro": "🌌 ภายในตัวเรามีดวงดาวที่ดับไปแล้ว และดวงดาวที่ยังส่องแสง... คุณคือดวงดาวแบบไหน?",
     "question": "✨ เมื่อคุณเผชิญกับความมืดมิด คุณเลือกที่จะ...",
     "options": ["ส่องแสงของตัวเอง", "ซ่อนตัวและรอให้ความมืดผ่านไป", "ค้นหาความหมายจากมัน",
                 "ยอมรับมันเป็นส่วนหนึ่งของฉัน"]},

    {"intro": "🌌 ภายในตัวเรามีดวงดาวที่ดับไปแล้ว และดวงดาวที่ยังส่องแสง... คุณคือดวงดาวแบบไหน?",
     "question": "✨ เมื่อคุณเผชิญกับความมืดมิด คุณเลือกที่จะ...",
     "options": ["ส่องแสงของตัวเอง", "ซ่อนตัวและรอให้ความมืดผ่านไป", "ค้นหาความหมายจากมัน",
                 "ยอมรับมันเป็นส่วนหนึ่งของฉัน"]},
]

# ---------- เซ็ตค่าเริ่มต้น ----------
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.responses = []

# ---------- Flow: คำโปรย -> คำถาม ----------
if st.session_state.step < len(journey) * 2:
    index = st.session_state.step // 2
    if st.session_state.step % 2 == 0:
        st.write(f"### {journey[index]['intro']}")
    else:
        st.write(f"## {journey[index]['question']}")
        response = st.radio("", journey[index]["options"], key=f"q{index}")
        if response:
            st.session_state.responses.append(response)

    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    if st.button("🔮 ต่อไป"):
        st.session_state.step += 1
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- แสดงผลลัพธ์ ----------
else:
    personalities = ["ผู้เฝ้าดู", "นักเดินทาง", "ผู้รังสรรค์", "นักรบเงา", "ผู้หลงลืม", "ผู้ถือแสง"]
    personality = random.choice(personalities)
    st.write(f"## 🌟 คุณคือ **{personality}**")

    # ---------- ปุ่มแชร์ ----------
    share_url = "https://soulsage-personal-app.streamlit.app/"
    st.subheader("📢 แชร์ผลลัพธ์ของคุณ")
    qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={share_url}"
    st.image(qr_code_url, caption="📱 สแกน QR Code เพื่อเปิดลิงก์")

    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    if st.button("🔄 เริ่มใหม่"):
        st.session_state.step = 0
        st.session_state.responses = []
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
