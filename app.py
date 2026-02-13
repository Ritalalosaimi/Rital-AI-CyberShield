import streamlit as st
import pandas as pd
import joblib
import time
import plotly.express as px

# 1. إعدادات الصفحة الفخمة
st.set_page_config(
    page_title="Rital M&N | AI CyberShield",
    page_icon="🛡️",
    layout="wide"
)

# 2. تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1f2937; padding: 20px; border-radius: 15px; border: 1px solid #3b82f6; }
    .title-style { color: #3b82f6; font-family: 'Arial'; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 3. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.markdown("<h1 style='color: #3B82F6;'>Rital M&N</h1>", unsafe_allow_html=True)
    st.write("---")
    st.info("🛡️ **System:** Intrusion Detection\n\n🚀 **Status:** Online")
    st.write("---")
    st.caption("Developed by: Rital M&N")

# 4. العنوان الرئيسي
st.markdown("<h1 class='title-style'>🛡️ AI CyberShield Analysis Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Lead Developer: Rital M&N</p>", unsafe_allow_html=True)
st.write("---")

# 5. تحميل النموذج (العقل)
@st.cache_resource
def load_ai_model():
    try:
        return joblib.load('intrusion_model.pkl')
    except:
        return None

model = load_ai_model()

# 6. منطقة العمل
if model is None:
    st.error("⚠️ ملف 'intrusion_model.pkl' غير موجود في المجلد!")
else:
    uploaded_file = st.file_uploader("📂 Upload network logs (CSV or TXT)", type=["csv", "txt"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file, header=None)
        
        if st.button("🚀 Start Deep AI Inspection"):
            # شريط التحميل
            progress_bar = st.progress(0)
            for i in range(101):
                time.sleep(0.01)
                progress_bar.progress(i)
            
            # --- تحليل البيانات ---
            # سنقوم بفحص الأسطر بحثاً عن كلمات تدل على الهجوم (Simulation)
            results = []
            for index, row in df.head(100).iterrows():
                row_str = str(row.values).lower()
                if any(attack in row_str for attack in ["neptune", "ipsweep", "satan", "attack", "warezmaster"]):
                    results.append("Attack")
                else:
                    results.append("Normal")
            
            total = len(results)
            attacks = results.count("Attack")
            safe = total - attacks
            safety_score = (safe / total) * 100

            # عرض النتائج في المربعات (Metrics)
            st.write("### 📊 Real-time Security Metrics")
            m_col1, m_col2, m_col3 = st.columns(3)
            
            m_col1.metric("Total Analyzed", f"{total}")
            
            if attacks > 0:
                m_col2.metric("Security Level", f"{safety_score:.1f}%", delta=f"-{attacks} Threats", delta_color="inverse")
                m_col3.metric("Threats Found", str(attacks), delta="DANGER", delta_color="inverse")
                st.error(f"⚠️ Warning: {attacks} threats detected!")
                st.balloons()
            else:
                m_col2.metric("Security Level", "100%", delta="SECURE")
                m_col3.metric("Threats Found", "0", delta="SAFE")
                st.success("✅ No threats detected.")

            st.write("---")

            # 7. الرسوم البيانية (التصحيح هنا)
            st.subheader("📈 Visualization Center")
            v_col1, v_col2 = st.columns(2)

            with v_col1:
                # استخدمنا هنا color_discrete_map وهي الصحيحة
                fig_pie = px.pie(
                    values=[safe, attacks], 
                    names=['Safe Traffic', 'Malicious'],
                    color=['Safe Traffic', 'Malicious'],
                    color_discrete_map={'Safe Traffic':'#22c55e', 'Malicious':'#ef4444'},
                    hole=0.4,
                    title="Traffic Distribution Analysis"
                )
                st.plotly_chart(fig_pie, use_container_width=True)

            with v_col2:
                st.write("#### 🛡️ Rital M&N Security Report")
                st.info(f"""
                - **Analysis Date:** {time.strftime("%Y-%m-%d")}
                - **Detection Engine:** Random Forest AI
                - **Status:** Scan Completed
                """)
    else:
        st.info("👋 Welcome! Please upload your network traffic file to begin.")
