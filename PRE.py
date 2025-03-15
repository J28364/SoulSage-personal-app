import streamlit as st
import random
st.set_page_config(page_title="ค้นหาตัวตน", page_icon="🔑", layout="centered")

# ---------- ธีม UI ----------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://cdn-om.cdnpk.net/users/603/60393279/uploads/47ddc40e-66c0-44a5-bb8d-6a6522230167/47ddc40e-66c0-44a5-bb8d-6a6522230167-thumb.jpg?token=exp=1742117214~hmac=197225bd9ae54ea872fb40fa5b8b57b9");
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
     "question": "🌓 ถ้าจิตวิญญาณของคุณสามารถพูดได้ มันจะบอกอะไรกับคุณ?",
     "options": ["ฉันต้องการเข้าใจทุกสิ่ง", "ฉันยังไม่รู้ว่าฉันเป็นใคร", "ฉันกำลังเดินทางไปหาบางสิ่งที่ฉันกำลังตามหา", "ฉันพร้อมจะก้าวผ่านทุกอย่าง"]},

    {"intro": "🌌 ภายในตัวเรามีดวงดาวที่ดับไปแล้ว และดวงดาวที่ยังส่องแสง...คุณคือดวงดาวแบบไหน?",
     "question": "🕰 เมื่อคุณเผชิญกับความมืดมิด คุณเลือกที่จะ...?",
     "options": ["ส่องแสงของตัวเอง", "ซ่อนตัวและรอให้ความมืดมิดผ่านไป", "ค้นหาความหมายจากมัน", "ยอมรับมันและทำความเข้าใจกับมัน"]},

    {"intro": "🔥 มีบางอย่างในตัวคุณที่โหยหาความหมาย แม้ว่าคุณจะไม่เคยเอ่ยมันออกมา?",
     "question": "🔥 สิ่งที่ขับเคลื่อนคุณในชีวิตคืออะไร?",
     "options": ["การค้นหาความจริง", "ความกลัวที่จะถูกลืม", "ความหวังที่ไม่เคยดับ", "หาคำตอบเชิงเหตุผล"]},

    {"intro": "🌊 ความคิดของคุณเป็นเหมือนมหาสมุทร มันสงบนิ่ง หรือเต็มไปด้วยคลื่นลม",
     "question": "🌑 ถ้าความคิดของคุณสามารถกลายเป็นสิ่งที่จับต้องได้ มันจะเป็นอะไร?",
     "options": ["กระแสน้ำที่เปลี่ยนแปลงตลอดเวลา", "เงาที่สะท้อนความจริง", "เปลวไฟที่ลุกโชนในความมืด", "เสียงกระซิบที่ไม่มีวันดับ"]},

    {"intro": "✨ เราเดินผ่านผู้คนนับพัน แต่บางครั้งเรากลับรู้สึกโดดเดี่ยวที่สุดในหมู่ผู้คนนับล้าน?",
     "question": "🌠 เมื่อคุณอยู่ท่ามกลางผู้คน คุณรู้สึกว่า?",
     "options": ["ฉันเป็นเพียงผู้เฝ้าดู", "ฉันกำลังแสดงบทบาทที่ผู้คนต้องการให้ฉันเป็น", "ฉันไม่แน่ใจว่าฉันอยู่ที่นี่ทำไม", "ฉันเป็นตัวเองที่สุดเมื่ออยู่ลำพัง"]},

    {"intro": "💭 ทุกคนต่างมีเงาของตัวเอง และเงานั้นพูดกับคุณในบางคืน?",
     "question": "🎭 หากเงาของคุณสามารถพูดได้ มันจะบอกอะไรกับคุณ?",
     "options": ["เธอแข็งแกร่งกว่าที่คิด", "เธอยังกลัวบางสิ่ง", "เธอกำลังค้นหาบางอย่าง", "เธอสามารถเป็นอะไรก็ได้ถ้าใจเธอต้องการ"]},

    {"intro": "🌙 คุณเคยรู้สึกไหมว่าคุณกำลังเดินอยู่ระหว่างสองโลก?",
     "question": "📖 ถ้าคุณสามารถเลือกโลกตัวเองได้ คุณจะเลือก...?",
     "options": ["โลกที่เต็มไปด้วยความจริง", "โลกที่เต็มไปด้วยความฝัน", "โลกที่ฉันสามารถสร้างได้เอง", "โลกที่ไม่มีอดีตหรืออนาคตมีแต่ปัจจุบัน"]},

    {"intro": "🕊️ คุณกำลังวิ่งหนีบางสิ่ง หรือกำลังเดินทางไปหามัน?",
     "question": "🎶 อะไรคือสิ่งที่คุณค้นหาอยู่ในชีวิต?",
     "options": ["อิสรภาพ", "คำตอบ", "ใครบางคน", "ตัวฉันเอง"]},

    {"intro": "🌟 ตอนนี้ คุณอยู่ที่นี่ พร้อมกับความจริงที่ไม่มีใครบิดเบือน...คุณพร้อมจะมองเห็นตัวเองแล้วหรือยัง?",
     "question": "🌍 คำถามสุดท้าย...ถ้าคุณสามารถเห็นตัวเองอย่างแท้จริง คุณคิดว่าคุณจะเห็นอะไร?",
     "options": ["ฉันในแบบที่ฉันเป็น", "ฉันในแบบที่ฉันกลัวจะเป็น", "ฉันในแบบที่ฉันหวังจะเป็น", "ฉันในแบบที่ฉันยังค้นหาตัวเองอยู่"]},
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
    share_url = "https://soulsage-personal-app-happy-day.streamlit.app/"
    st.subheader("📢 แชร์ผลลัพธ์ของคุณ")
    qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={share_url}"
    st.image(qr_code_url, caption="📱 สแกน QR Code เพื่อเปิดลิงก์")

    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    if st.button("🔄 เริ่มใหม่"):
        st.session_state.step = 0
        st.session_state.responses = []
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
