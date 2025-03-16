import streamlit as st
import random
st.set_page_config(page_title="ค้นหาตัวตน", page_icon="🔑", layout="centered")

# ---------- ธีม UI ----------
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/premium-photo/pitch-black-background-with-copy-space-abstract_1248375-3448.jpg?uid=R60393279&ga=GA1.1.1470301244.1741927351&semt=ais_hybrid");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    
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
        background-color: #9933FF;
        color: #3c3c3c;
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
st.markdown("<h1 style='color: white; text-align: center;'>SoulSage</h1>", unsafe_allow_html=True)
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
    st.session_state.selected_option_index = None # เก็บ index ของตัวเลือกที่ถูกเลือก

# ---------- Flow: คำโปรย -> คำถาม ----------
if st.session_state.step < len(journey) * 2:
    if st.session_state.step % 2 == 0:  # แสดงคำโปรย
        intro_index = st.session_state.step // 2
        st.markdown(f'<div class="intro-text">{journey[intro_index]["intro"]}</div>', unsafe_allow_html=True)
        if st.button("🔮 ต่อไป"):
            st.session_state.step += 1
            st.session_state.selected_option_index = None # รีเซ็ตเมื่อไปหน้าใหม่
            st.rerun()
    else:  # แสดงคำถาม
        q_index = st.session_state.step // 2
        q_data = journey[q_index]
        st.markdown(f'<div class="question">{q_data["question"]}</div>', unsafe_allow_html=True)
        options = q_data["options"]
        for i, option in enumerate(options):
            if st.button(option, key=f"{q_index}_{option}"):
                st.session_state.selected_option_index = i # บันทึก index ของตัวเลือก
                st.session_state.selected_option = option # บันทึกตัวเลือกที่เลือก
                # ไม่ต้อง rerun ที่นี่

        if st.session_state.selected_option_index is not None:
            st.write(f"คุณเลือก: {options[st.session_state.selected_option_index]}")
            if st.button("🔮 ต่อไป"):
                st.session_state.responses.append(options[st.session_state.selected_option_index])
                st.session_state.step += 1
                st.session_state.selected_option_index = None # รีเซ็ตเมื่อไปหน้าใหม่
                st.rerun()

else:
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
        "การค้นหาความจริง": "ผู้เฝ้าดู",
        "เงาที่สะท้อนความจริง": "ผู้เฝ้าดู",
        "ฉันเป็นเพียงผู้เฝ้าดู": "ผู้เฝ้าดู",

        "ฉันกำลังเดินทางไปหาบางสิ่งที่ฉันกำลังตามหา": "นักเดินทาง",
        "ฉันไม่แน่ใจว่าฉันอยู่ที่นี่ทำไม": "นักเดินทาง",
        "ฉันกำลังค้นหาบางอย่าง": "นักเดินทาง",
        "ตัวฉันเอง": "นักเดินทาง",
        "ฉันในแบบที่ฉันยังค้นหาตัวเองอยู่": "นักเดินทาง",

        "ยอมรับมันและทำความเข้าใจกับมัน": "ผู้รังสรรค์",
        "โลกที่ฉันสามารถสร้างได้เอง": "ผู้รังสรรค์",
        "เธอสามารถเป็นอะไรก็ได้ถ้าใจเธอต้องการ": "ผู้รังสรรค์",
        "เปลวไฟที่ลุกโชนในความมืด": "ผู้รังสรรค์",
        "ฉันในแบบที่ฉันหวังจะเป็น": "ผู้รังสรรค์",

        "ฉันพร้อมจะก้าวผ่านทุกอย่าง": "นักรบเงา",
        "เธอแข็งแกร่งกว่าที่คิด": "นักรบเงา",
        "ส่องแสงของตัวเอง": "นักรบเงา",
        "ความกลัวที่จะถูกลืม": "นักรบเงา",
        "ฉันในแบบที่ฉันกลัวจะเป็น": "นักรบเงา",

        "ฉันยังไม่รู้ว่าฉันเป็นใคร": "ผู้หลงลืม",
        "ซ่อนตัวและรอให้ความมืดมิดผ่านไป": "ผู้หลงลืม",
        "เสียงกระซิบที่ไม่มีวันดับ": "ผู้หลงลืม",
        "โลกที่ไม่มีอดีตหรืออนาคตมีแต่ปัจจุบัน": "ผู้หลงลืม",
        "ฉันกำลังแสดงบทบาทที่ผู้คนต้องการให้ฉันเป็น": "ผู้หลงลืม",

        "ความหวังที่ไม่เคยดับ": "ผู้ถือแสง",
        "อิสรภาพ": "ผู้ถือแสง",
        "โลกที่เต็มไปด้วยความฝัน": "ผู้ถือแสง",
        "เธอยังกลัวบางสิ่ง": "ผู้ถือแสง",
        "ฉันในแบบที่ฉันเป็น": "ผู้ถือแสง"
    }

    # นับคะแนนของแต่ละบุคลิก
    for response in st.session_state.responses:
        if response in mapping:
            personalities[mapping[response]] += 1

    # ค้นหาบุคลิกที่ได้คะแนนสูงสุด
    personality = max(personalities, key=personalities.get)

    st.markdown(f"""
        <div style="
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
            border: 2px solid #ffcc00;
            padding: 15px;
            border-radius: 10px;
            background-color: rgba(0, 0, 0, 0.5);
            margin-bottom: 20px;
            text-align: center;
        ">
            🌟 คุณคือ {personality}
        </div>
    """, unsafe_allow_html=True)

    image_filename = f"{personality}.jpg"
    image_path = image_filename

    try:
        st.image(image_path, caption=f"ภาพแทนบุคลิกของ {personality}", width = 150)  # เปลี่ยนตรงนี้
    except FileNotFoundError:
        st.error(f"ไม่พบรูปภาพสำหรับบุคลิก: {personality}")

    # ---------- ปุ่มแชร์ ----------
    st.markdown("<h3 style='color: white; text-align: center;'>📢 แชร์ผลลัพธ์ของคุณ</h3>", unsafe_allow_html=True)
    share_url = "https://soulsage-personal-app-happy-day.streamlit.app/"
    qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={share_url}"
    st.image(qr_code_url, caption="📱 สแกน QR Code เพื่อเปิดลิงก์", width = 150)  # เปลี่ยนตรงนี้

    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    if st.button("🔄 เริ่มใหม่"):
        st.session_state.step = 0
        st.session_state.responses = []
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # ปิด div container
    st.markdown("</div>", unsafe_allow_html=True)
