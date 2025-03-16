import streamlit as st
import random
st.set_page_config(page_title="ค้นหาตัวตน", page_icon="🔑", layout="centered")

# ---------- ธีม UI ----------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.thestreetratchada.com/upload/contents/17084010569.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    h1 {
        color: #ffcc00;
        text-align: center;
    }
    .question {
        font-size: 20px;
        font-weight: bold;
        color: #f5f5f5;
        border: 2px solid #ffcc00;
        padding: 10px;
        border-radius: 10px;
        background-color: rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
        text-align: center;
    }
    .option {
        font-size: 18px;
        color: #ffffff;
        border: 2px solid #ffcc00;
        padding: 10px;
        border-radius: 5px;
        background-color: rgba(0, 0, 0, 0.5);
        margin-bottom: 10px;
        cursor: pointer;
        transition: transform 0.2s ease, background-color 0.2s ease;
        text-align: center;
    }
    .option:hover {
        transform: scale(1.05);
    }
    .option.selected {
        background-color: #ffcc00;
        color: #000000;
    }
    .intro-text {
        border: 2px solid #ffcc00;
        padding: 10px;
        border-radius: 10px;
        background-color: rgba(0, 0, 0, 0.5);
        color: #ffffff;
        font-size: 18px;
        margin-bottom: 20px;
        text-align: center;
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
    st.session_state.selected_option = ""

# ---------- Flow: คำโปรย -> คำถาม ----------
if st.session_state.step < len("intro") + len("questions"):
    if st.session_state.step % 2 == 0:  # แสดงคำโปรย
        intro_index = st.session_state.step // 2
        st.markdown(f'<div class="intro-text">{"intro"[intro_index]}</div>', unsafe_allow_html=True)
    else:  # แสดงคำถาม
        q_index = st.session_state.step // 2
        q_data = "questions"[q_index]
        st.markdown(f'<div class="question">{q_data["question"]}</div>', unsafe_allow_html=True)
        for option in q_data["options"]:
            if st.button("option", key=f"{q_index}_{option}"):
                st.session_state.responses.append("option")
                st.session_state.step += 1
                st.rerun()
    
    if st.button("🔮 ต่อไป"):
        st.session_state.step += 1
        st.rerun()

else:
    st.write(f"## 🌟 คุณคือ **{personality}**")
    personalities = {
        "ผู้เฝ้าดู": 0,
        "นักเดินทาง": 0,
        "ผู้รังสรรค์": 0,
        "นักรบเงา": 0,
        "ผู้หลงลืม": 0,
        "ผู้ถือแสง": 0
    }

    # กำหนดการจับคู่คำตอบกับบุคลิกภาพ
    mapping = {
        "ฉันต้องการเข้าใจทุกสิ่ง": "ผู้เฝ้าดู",
        "ค้นหาความหมายจากมัน": "ผู้เฝ้าดู",
        "ฉันกำลังเดินทางไปหาบางสิ่งที่ฉันกำลังตามหา": "ผู้เฝ้าดู",
        "ฉันเป็นเพียงผู้เฝ้าดู": "ผู้เฝ้าดู",
        "ตัวฉันเอง": "ผู้เฝ้าดู",
        "เสียงกระซิบที่ไม่มีวันดับ": "ผู้เฝ้าดู",
        "โลกที่ไม่มีอดีตหรืออนาคตมีแต่ปัจจุบัน": "ผู้เฝ้าดู",
        "ฉันในแบบที่ฉันเป็น": "ผู้เฝ้าดู",

        "ค้นหาความหมายจากมัน": "นักเดินทาง",
        "การค้นหาความจริง": "นักเดินทาง",
        "ฉันกำลังเดินทางไปหาบางสิ่งที่ฉันกำลังตามหา": "นักเดินทาง",
        "ฉันไม่แน่ใจว่าฉันอยู่ที่นี่ทำไม": "นักเดินทาง",
        "ตัวฉันเอง": "นักเดินทาง",
        "ฉันในแบบที่ฉันยังค้นหาตัวเองอยู่": "นักเดินทาง",
        "เธอสามารถเป็นอะไรก็ได้ถ้าใจเธอต้องการ": "นักเดินทาง",
        "ส่องแสงของตัวเอง": "นักเดินทาง",
        "เสียงกระซิบที่ไม่มีวันดับ": "นักเดินทาง",
        "ความหวังที่ไม่เคยดับ": "นักเดินทาง",
        "อิสรภาพ": "นักเดินทาง",
        "เธอยังกลัวบางสิ่ง": "นักเดินทาง",
        "ฉันในแบบที่ฉันเป็น": "นักเดินทาง",
        
        "ยอมรับมันและทำความเข้าใจกับมัน": "ผู้รังสรรค์",
        "โลกที่ฉันสามารถสร้างได้เอง": "ผู้รังสรรค์",
        "ฉันกำลังค้นหาบางอย่าง": "ผู้รังสรรค์",
        "ตัวฉันเอง": "ผู้รังสรรค์",
        "ฉันในแบบที่ฉันยังค้นหาตัวเองอยู่": "ผู้รังสรรค์",
        "เธอสามารถเป็นอะไรก็ได้ถ้าใจเธอต้องการ": "ผู้รังสรรค์",
        "เปลวไฟที่ลุกโชนในความมืด": "ผู้รังสรรค์",
        "ฉันในแบบที่ฉันหวังจะเป็น": "ผู้รังสรรค์",
        "เสียงกระซิบที่ไม่มีวันดับ": "ผู้รังสรรค์",
        "ฉันกำลังแสดงบทบาทที่ผู้คนต้องการให้ฉันเป็น": "ผู้รังสรรค์",
        "ฉันในแบบที่ฉันเป็น": "ผู้รังสรรค์",

        "เงาที่สะท้อนความจริง": "นักรบเงา",
        "เปลวไฟที่ลุกโชนในความมืด": "นักรบเงา",
        "ฉันกำลังเดินทางไปหาบางสิ่งที่ฉันกำลังตามหา": "นักรบเงา",
        "ฉันพร้อมจะก้าวผ่านทุกอย่าง": "นักรบเงา",
        "ความกลัวที่จะถูกลืม": "นักรบเงา",
        "ฉันในแบบที่ฉันกลัวจะเป็น": "นักรบเงา",
        "ตัวฉันเอง": "นักรบเงา",
        "ยอมรับมันและทำความเข้าใจกับมัน": "นักรบเงา",
        "ซ่อนตัวและรอให้ความมืดมิดผ่านไป": "นักรบเงา",
        "โลกที่ไม่มีอดีตหรืออนาคตมีแต่ปัจจุบัน": "นักรบเงา",
        "ความหวังที่ไม่เคยดับ": "นักรบเงา",
        "โลกที่ไม่มีอดีตหรืออนาคตมีแต่ปัจจุบัน": "นักรบเงา",
        "เธอยังกลัวบางสิ่ง": "นักรบเงา",
        "ฉันในแบบที่ฉันเป็น": "นักรบเงา",
        
        "ฉันยังไม่รู้ว่าฉันเป็นใคร": "ผู้หลงลืม",
        "ฉันเป็นเพียงผู้เฝ้าดู": "ผู้หลงลืม",
        "ฉันไม่แน่ใจว่าฉันอยู่ที่นี่ทำไม": "ผู้หลงลืม",
        "ตัวฉันเอง": "ผู้หลงลืม",
        "เปลวไฟที่ลุกโชนในความมืด": "ผู้หลงลืม",
        "ฉันในแบบที่ฉันยังค้นหาตัวเองอยู่": "ผู้หลงลืม",
        "เธอสามารถเป็นอะไรก็ได้ถ้าใจเธอต้องการ": "ผู้หลงลืม",
        "ฉันในแบบที่ฉันหวังจะเป็น": "ผู้หลงลืม",
        "เธอแข็งแกร่งกว่าที่คิด": "ผู้หลงลืม",
        "ความกลัวที่จะถูกลืม": "ผู้หลงลืม",
        "ซ่อนตัวและรอให้ความมืดมิดผ่านไป": "ผู้หลงลืม",
        "ฉันกำลังแสดงบทบาทที่ผู้คนต้องการให้ฉันเป็น": "ผู้หลงลืม",
        "เธอยังกลัวบางสิ่ง": "ผู้หลงลืม",
        "ฉันในแบบที่ฉันเป็น": "ผู้หลงลืม",

        "เงาที่สะท้อนความจริง": "ผู้ถือแสง",
        "ฉันกำลังค้นหาบางอย่าง": "ผู้ถือแสง",
        "ตัวฉันเอง": "ผู้ถือแสง",
        "ซ่อนตัวและรอให้ความมืดมิดผ่านไป": "ผู้ถือแสง",
        "เปลวไฟที่ลุกโชนในความมืด": "ผู้ถือแสง",
        "ฉันพร้อมจะก้าวผ่านทุกอย่าง": "ผู้ถือแสง",
        "เธอแข็งแกร่งกว่าที่คิด": "ผู้ถือแสง",
        "ส่องแสงของตัวเอง": "ผู้ถือแสง",
        "ความหวังที่ไม่เคยดับ": "ผู้ถือแสง",
        "อิสรภาพ": "ผู้ถือแสง",
        "โลกที่เต็มไปด้วยความฝัน": "ผู้รังสรรค์",
        "ฉันในแบบที่ฉันเป็น": "ผู้ถือแสง",
    }

    # นับคะแนนของแต่ละบุคลิก
    for response in st.session_state.responses:
        if response in mapping:
            personalities[mapping[response]] += 1

    # ค้นหาบุคลิกที่ได้คะแนนสูงสุด
    personality = max(personalities, key=personalities.get)

    

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
