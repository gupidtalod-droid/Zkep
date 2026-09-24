import datetime
from openpyxl import Workbook
import streamlit as st

st.title("📋 ระบบบันทึก Morning KYT & Warehouse Readiness")
st.write(
    "กรอกข้อมูลประจำวัน สามารถกดเพิ่มหรือลบแต่ละข้อความได้จากปุ่มด้านหลังข้อความ"
)

# 1. กำหนดค่าเริ่มต้นใน session_state (ข้อมูลหลักยังคงมีค่าเริ่มต้นตามเดิม)
if "main_works" not in st.session_state:
  st.session_state.main_works = [
      "รับสินค้า 5 เที่ยว / จ่ายสินค้า 15 เที่ยว",
      "เตรียมสินค้าจัดส่งก่อน 10:00 น. 8 เที่ยว",
  ]

if "ready_items" not in st.session_state:
  st.session_state.ready_items = [
      "พนักงานมา 12 คน ครบตามแผน",
      (
          "พนักงานรายวันมา 13 จากแผน 14 คน จัดคนงานแยกตามจุดลงสินค้าแต่ละประเภทแล้ว"
      ),
      "รถโฟล์คลิฟท์ 1 คัน พร้อมใช้งาน",
      "พื้นที่รับ–จ่ายสินค้า พร้อมใช้งาน",
  ]

if "kyt_items" not in st.session_state:
  st.session_state.kyt_items = [
      "เน้นย้ำการเช็กงานเตรียมรอกระจาย",
      "เน้นย้ำดูแลการเข้า–ออกบริเวณจุดโหลด",
      (
          "ย้ำการทำ 5ส ให้พื้นที่ทำงานและจุดเก็บเอกสารสะอาด เป็นระเบียบ"
          " ค้นหาของได้รวดเร็ว"
      ),
  ]

if "problem_items" not in st.session_state:
  st.session_state.problem_items = ["ไม่มี"]

if "file_ready" not in st.session_state:
  st.session_state.file_ready = False

# --- ข้อมูลทั่วไป (แก้ค่าเริ่มต้นให้เป็นช่องว่าง) ---
st.subheader("📌 ข้อมูลทั่วไป")
col1, col2 = st.columns(2)
with col1:
  branch = st.text_input("สาขา", "")
  reporter = st.text_input("ผู้รายงาน", "")
with col2:
  selected_date = st.date_input("วันที่", datetime.date.today())
  date_str = selected_date.strftime("%d/%m/%Y")
  time_str = st.text_input("ประชุมทีมเสร็จเวลา", "")

participants = st.text_input("ผู้เข้าร่วม", "")

# --- 1. งานหลักวันนี้ ---
st.subheader("1. งานหลักวันนี้")
temp_main_works = []
for i, item in enumerate(st.session_state.main_works):
  cols = st.columns([5, 1])
  with cols[0]:
    val = st.text_input(
        f"งานหลักข้อที่ {i+1}", value=item, key=f"main_input_{i}"
    )
    temp_main_works.append(val)
  with cols[1]:
    st.write("")
    if st.button("🗑️ ลบ", key=f"del_main_{i}"):
      st.session_state.main_works.pop(i)
      st.rerun()
st.session_state.main_works = temp_main_works

if st.button("➕ เพิ่มงานหลัก"):
  st.session_state.main_works.append("")
  st.rerun()

# --- 2. ความพร้อมก่อนเริ่มงาน ---
st.subheader("2. ความพร้อมก่อนเริ่มงาน")
temp_ready_items = []
for i, item in enumerate(st.session_state.ready_items):
  cols = st.columns([5, 1])
  with cols[0]:
    val = st.text_input(
        f"ความพร้อมข้อที่ {i+1}", value=item, key=f"ready_input_{i}"
    )
    temp_ready_items.append(val)
  with cols[1]:
    st.write("")
    if st.button("🗑️ ลบ", key=f"del_ready_{i}"):
      st.session_state.ready_items.pop(i)
      st.rerun()
st.session_state.ready_items = temp_ready_items

if st.button("➕ เพิ่มความพร้อม"):
  st.session_state.ready_items.append("")
  st.rerun()

# --- 3. ประเด็น KYT ที่คุยกับทีมวันนี้ ---
st.subheader("3. ประเด็น KYT ที่คุยกับทีมวันนี้")
temp_kyt_items = []
for i, item in enumerate(st.session_state.kyt_items):
  cols = st.columns([5, 1])
  with cols[0]:
    val = st.text_input(
        f"ประเด็น KYT ข้อที่ {i+1}", value=item, key=f"kyt_input_{i}"
    )
    temp_kyt_items.append(val)
  with cols[1]:
    st.write("")
    if st.button("🗑️ ลบ", key=f"del_kyt_{i}"):
      st.session_state.kyt_items.pop(i)
      st.rerun()
st.session_state.kyt_items = temp_kyt_items

if st.button("➕ เพิ่มประเด็น KYT"):
  st.session_state.kyt_items.append("")
  st.rerun()

# --- 4. ปัญหาค้าง/เรื่องที่ต้องประสาน ---
st.subheader("4. ปัญหาค้าง/เรื่องที่ต้องประสาน")
temp_problem_items = []
for i, item in enumerate(st.session_state.problem_items):
  cols = st.columns([5, 1])
  with cols[0]:
    val = st.text_input(
        f"ปัญหาข้อที่ {i+1}", value=item, key=f"problem_input_{i}"
    )
    temp_problem_items.append(val)
  with cols[1]:
    st.write("")
    if st.button("🗑️ ลบ", key=f"del_problem_{i}"):
      st.session_state.problem_items.pop(i)
      st.rerun()
st.session_state.problem_items = temp_problem_items

if st.button("➕ เพิ่มปัญหา"):
  st.session_state.problem_items.append("")
  st.rerun()

# --- 5. สถานะสาขา ---
st.subheader("5. สถานะสาขา")
status = st.selectbox(
    "สถานะ", ["ดำเนินงานได้แต่มีข้อจำกัด", "ดำเนินงานได้ปกติ", "มีปัญหาติดขัด"]
)
status_detail = st.text_area(
    "รายละเอียดสถานะ",
    "งานเช้าดำเนินได้ตามแผนที่ปรับแล้ว ยังไม่กระทบเวลารับ–จ่ายสินค้า",
)

st.markdown("---")

# ปุ่มกดบันทึกหลัก
if st.button("💾 บันทึกข้อมูลเป็น Excel ทั้งหมด", type="primary"):
  wb = Workbook()
  ws = wb.active
  ws.title = "Morning KYT"

  data = [
      ["Morning KYT & Warehouse Readiness", ""],
      ["สาขา:", branch],
      ["วันที่:", date_str],
      ["ผู้รายงาน:", reporter],
      ["ประชุมทีมเสร็จเวลา:", time_str],
      ["ผู้เข้าร่วม:", participants],
      ["---", "---"],
      ["1. งานหลักวันนี้", ""],
  ]

  for item in st.session_state.main_works:
    data.append(["-", item])

  data.append(["---", "---"])
  data.append(["2. ความพร้อมก่อนเริ่มงาน", ""])
  for item in st.session_state.ready_items:
    data.append(["-", item])

  data.append(["---", "---"])
  data.append(["3. ประเด็น KYT ที่คุยกับทีมวันนี้", ""])
  for item in st.session_state.kyt_items:
    data.append(["-", item])

  data.append(["---", "---"])
  data.append(["4. ปัญหาค้าง/เรื่องที่ต้องประสาน", ""])
  for item in st.session_state.problem_items:
    data.append(["-", item])

  data.append(["---", "---"])
  data.append(["5. สถานะสาขา", status])
  data.append(["รายละเอียดสถานะ:", status_detail])

  for row_idx, row_data in enumerate(data, start=1):
    ws.cell(row=row_idx, column=1, value=row_data[0])
    ws.cell(row=row_idx, column=2, value=row_data[1])

  file_name = "Morning_KYT_Report.xlsx"
  wb.save(file_name)
  st.session_state.file_ready = True
  st.success(f"บันทึกข้อมูลสำเร็จ! ไฟล์ถูกเซฟชื่อว่า: {file_name}")

# ปุ่มดาวน์โหลดไฟล์
if st.session_state.file_ready:
  file_name = "Morning_KYT_Report.xlsx"
  try:
    with open(file_name, "rb") as file:
      st.download_button(
          label="📥 คลิกที่นี่เพื่อดาวน์โหลดไฟล์ Excel",
          data=file,
          file_name=file_name,
          mime=(
              "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
          ),
      )
  except FileNotFoundError:
    st.warning("กรุณากดปุ่มบันทึกข้อมูลด้านบนก่อนดาวน์โหลด")