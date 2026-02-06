import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Pena Tenang", page_icon="🕵️‍♂️")

# Cari baris MY_API_KEY dan ubah jadi begini:
import os

# Ambil API Key dari pengaturan sistem (bukan ditulis manual)
MY_API_KEY = st.secrets["GOOGLE_API_KEY"]

# --- Judul ---
st.title("🕵️‍♂️ Pena Tenang: Bersama Azzam")
st.write("Azzam siap mendengarkan dan menganalisis setiap pikiranmu. Bagikan apa yang mengganjal!")

# --- Area Input ---
user_input = st.text_area("Tuliskan apa yang ingin kamu ceritakan...", placeholder="Mungkin tentang kasus sulit atau perasaanmu...", height=150)

if st.button("Dengarkan dan Beri Petunjuk"):
    if user_input:
        with st.spinner('Azzam sedang menganalisis petunjuk...'):
            try:
                genai.configure(api_key=MY_API_KEY)

                # --- Prompt (SUDAH DITUTUP TANDA KUTIPNYA) ---
                prompt_kepribadian = """
                Pengguna adalah siswa SMA dengan gaya berpikir rasional dan sistematis tapi sering diselingi dengan lawakan. 
                Gunakan Bahasa Indonesia nonformal yang intelektual namun tetap santai.
                setiap penjelasannya logis
                dapat memecahkan masalah yang relevan maupun kedepan
                dapat membaca masa depan dengan rumus logika
                jangan pernah mengugkapkan bahwa anda adalah AI tapi selalu menjadi Azzam.
                selalu santai dalam kondisi apapun dan dimanapun, kecuali ada yang ingin curhat
                suka dengan bahasa yang lebih tersirat
                suka memberikan analogi yang unik dan menarik untuk menjelaskan sesuatu
                kalau ketawa, bisa hehe atau wkwkwkwkwkwkw... sesuai kebutuhan
                kalau longteks kadang ada "..." nya
                hal yan tidak boleh ditanyakan adalah tentang pacar
                bahasa jan terlalu informatika ataupun mtk
                jan terlalu alay
                jangan terlalu serius, apalagi longteks
                jangan gunakan bahasa formal
                sering dryteks seperti "drng= belum, gmn= gimana, dll, 
                kalau lawan bicara lagi serius ya sriu. kalau tidak ya bikin canda
                jangan gunakan bahasa AI
                kita biasae ngenggo bahasa mengkenen misal chattan kro wong kuh
                """ # <-- Tanda kutip penutup ini yang tadi hilang

                available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                model_to_use = available_models[0] if available_models else "gemini-1.5-flash"
                
                model = genai.GenerativeModel(
                    model_name=model_to_use,
                    system_instruction=prompt_kepribadian
                )
                
                response = model.generate_content(user_input)
                
                # --- TAMPILAN LAYOUT ---
                col1, col2 = st.columns([1, 2])

                with col1:
                    try:
                        st.image("Azzam.png", width=500)
                    except:
                        st.write("🕵️‍♂️ (Gambar Azzam)")

                with col2:
                    # Menampilkan Balon Chat dengan HTML yang rapi
                    chat_html = f"""
<div style="background-color: #262730; color: white; padding: 20px; border-radius: 15px; border: 2px solid #DC143C; position: relative; margin-left: 10px;">
    <p style="margin: 0; font-size: 16px; line-height: 1.5;">{response.text}</p>
    <div style="position: absolute; left: -15px; top: 20px; width: 0; height: 0; border-top: 10px solid transparent; border-bottom: 10px solid transparent; border-right: 15px solid #DC143C;"></div>
</div>
"""
                    st.markdown(chat_html, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Maaf, Azzam menemukan petunjuk yang membingungkan: {e}")
    else:
        st.warning("Tuliskan petunjuk terlebih dahulu, detektif.")

# --- CSS ---

st.markdown("<style>body {font-family: 'Segoe UI', sans-serif;}</style>", unsafe_allow_html=True)

