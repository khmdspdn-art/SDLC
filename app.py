import streamlit as st
import pandas as pd
import random

# Konfigurasi Halaman
st.set_page_config(
    page_title="E-Modul Interaktif: SDLC & Model Pengembangan (Edisi Lengkap)",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk Styling Modern & Gamifikasi
st.markdown("""
<style>
    .main-header {
        font-size: 2.3rem;
        color: #1E3A8A;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #3B82F6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }
    .locked-card {
        background-color: #FEF2F2;
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #EF4444;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Inisialisasi Session State
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "badges" not in st.session_state:
    st.session_state.badges = []
if "lkpd_submitted" not in st.session_state:
    st.session_state.lkpd_submitted = False
if "quiz_unlocked" not in st.session_state:
    st.session_state.quiz_unlocked = False

# Sidebar Navigasi
st.sidebar.title("🧭 Navigasi Media Ajar")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Pilih Menu Pembelajaran:",
    [
        "🏠 Beranda & Misi", 
        "📚 Literasi Mendalam: Konsep SDLC", 
        "🔍 Eksplorasi Model (Waterfall, Agile, dll)", 
        "📝 LKPD Interaktif (Studi Kasus)", 
        "🎮 Tantangan Kuis (10 Soal PG)"
    ]
)

# Sidebar Profil / Status Gamifikasi Siswa
st.sidebar.markdown("---")
st.sidebar.subheader("👤 Status Petualang")
level = 1 + (st.session_state.xp // 100)
st.sidebar.markdown(f"⭐ **XP:** `{st.session_state.xp}` | Level `{level}`")
st.sidebar.progress(min((st.session_state.xp % 100) / 100.0, 1.0))

# Status Kunci Kuis di Sidebar
if not st.session_state.lkpd_submitted:
    st.sidebar.warning("🔒 Kuis: **TERKUNCI** *(Selesaikan & Kirim LKPD terlebih dahulu!)*")
else:
    st.sidebar.success("🔓 Kuis: **TERBUKA** 🎉")

if st.session_state.badges:
    st.sidebar.markdown("🏆 **Lencana Diraih:**")
    for b in st.session_state.badges:
        st.sidebar.markdown(f"- {b}")

# ==========================================
# 1. BERANDA & MISI
# ==========================================
if menu == "🏠 Beranda & Misi":
    st.markdown('<p class="main-header">🚀 Petualangan Model Pengembangan Perangkat Lunak</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Media Pembelajaran Berbasis Penemuan (Discovery Learning) & Gamifikasi</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Selamat Datang di E-Modul Interaktif Rekayasa Perangkat Lunak! 👋
        Aplikasi ini dirancang bagi siswa SMK/SMA untuk memahami secara mendalam bagaimana perangkat lunak dibangun dari nol hingga siap digunakan oleh pengguna. 
        
        #### 🎯 Alur Petualangan Belajar Anda:
        1. **Literasi Mendalam:** Memahami teori dasar siklus hidup perangkat lunak (*Software Development Life Cycle* / SDLC).
        2. **Eksplorasi Model:** Menemukan karakteristik unik, kelebihan, kekurangan, dan contoh nyata dari berbagai model (Waterfall, Agile, Prototyping, Spiral, V-Model, RAD).
        3. **LKPD Interaktif:** Menganalisis skenario studi kasus dunia nyata dan merumuskan argumen pemilihan model. *(⚠️ Wajib dikirim agar Kuis Terbuka!)*
        4. **Tantangan Kuis (10 Soal PG):** Menguji pemahaman komprehensif Anda dengan 5 pilihan jawaban (A, B, C, D, E) untuk meraih lencana master tertinggi!
        """)
        if st.button("🚀 Mulai Petualangan (+10 XP)", type="primary"):
            st.session_state.xp += 10
            st.success("🎉 Selamat! Anda mendapatkan +10 XP karena memulai misi hari ini!")
            st.rerun()
            
    with col2:
        st.info("💡 **Tips Guru:** Modul ini menggunakan pendekatan interaktif dengan Pandas DataFrame dan sistem Gamifikasi agar proses pembelajaran penemuan konsep (*discovery*) jauh lebih menyenangkan!")
        st.image("https://img.freepik.com/free-vector/programming-concept-illustration_114360-1351.jpg", use_container_width=True)

# ==========================================
# 2. LITERASI MENDALAM: KONSEP SDLC
# ==========================================
elif menu == "📚 Literasi Mendalam: Konsep SDLC":
    st.markdown("## 📚 Zona Literasi Mendalam: Apa itu SDLC & Mengapa Diperlukan?")
    st.write("Pelajari materi di bawah ini secara saksama sebelum Anda mengeksplorasi model-model spesifik.")

    tab1, tab2, tab3 = st.tabs(["📖 Pengertian & Tahapan Utama", "🔍 Mengapa Model Berbeda-Beda?", "📊 Tabel Perbandingan Komprehensif"])
    
    with tab1:
        st.markdown("""
        <div class="card">
        <h3>Definisi Komprehensif SDLC</h3>
        <p><b>Software Development Life Cycle (SDLC)</b> atau Siklus Hidup Pengembangan Perangkat Lunak adalah proses sistematis yang digunakan oleh tim pengembang untuk merancang, mengembangkan, menguji, dan mendeploy (menerbitkan) perangkat lunak berkualitas tinggi.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### ⚙️ 6 Tahapan Umum dalam SDLC:")
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown("""
            1. **Planning (Perencanaan):** Menentukan tujuan, kelayakan finansial, sumber daya, dan penjadwalan proyek.
            2. **Analysis (Analisis Kebutuhan):** Mengumpulkan spesifikasi rinci dari pengguna (*user requirements*).
            3. **Design (Perancangan):** Membuat arsitektur sistem, desain database, antarmuka pengguna (UI/UX), dan diagram alur.
            """)
        with col_t2:
            st.markdown("""
            4. **Implementation (Pengkodean):** Menulis kode program menggunakan bahasa pemrograman yang sesuai.
            5. **Testing (Pengujian):** Memeriksa *bug*, kesalahan logika, dan memastikan sistem berjalan sesuai spesifikasi.
            6. **Deployment & Maintenance (Peluncuran & Pemeliharaan):** Merilis sistem ke server produksi serta melakukan pembaruan berkala.
            """)

    with tab2:
        st.markdown("### ❓ Mengapa Ada Banyak Sekali Model SDLC?")
        st.write("Setiap proyek perangkat lunak memiliki karakteristik unik. Faktor-faktor yang menentukan pemilihan model meliputi:")
        st.markdown("""
        - **Kepastian Kebutuhan:** Apakah klien sudah tahu persis apa yang mereka inginkan dari awal, atau kebutuhannya masih berkembang?
        - **Skala dan Kompleksitas:** Apakah proyek ini aplikasi skala kecil (misal: profil sekolah) atau sistem kritikal skala besar (misal: sistem kendali penerbangan)?
        - **Keterbatasan Anggaran & Waktu:** Apakah tenggat waktu sangat ketat atau fleksibel?
        - **Tingkat Risiko:** Seberapa besar kerugian jika terjadi kegagalan sistem di tengah jalan?
        """)

    with tab3:
        st.markdown("### 📊 Tabel Matriks Perbandingan Model SDLC")
        data_matrix = {
            "Model": ["Waterfall", "Agile", "Prototyping", "Spiral", "V-Model", "RAD"],
            "Fokus Utama": ["Urutan Linier", "Kolaborasi & Iterasi", "Visualisasi Desain", "Manajemen Risiko", "Validasi Pengujian Dini", "Kecepatan & Prototype Cepat"],
            "Kelebihan Utama": ["Struktur sangat rapi & jelas", "Sangat adaptif terhadap perubahan", "Klien langsung melihat bentuk awal", "Menekan risiko kegagalan fatal", "Kualitas pengujian sangat tinggi", "Waktu pengerjaan relatif singkat"],
            "Kekurangan Utama": ["Sangat kaku jika ada revisi", "Sulit mengontrol anggaran pasti", "Klien sering fokus ke tampilan fisik", "Biaya konsultasi risiko mahal", "Kurang fleksibel di tengah jalan", "Butuh tim ahli yang sangat solid"]
        }
        df_matrix = pd.DataFrame(data_matrix)
        st.dataframe(df_matrix, use_container_width=True)
        
        if "📚 Literate Master" not in st.session_state.badges:
            if st.button("Klaim Badge Literasi (+15 XP)"):
                st.session_state.xp += 15
                st.session_state.badges.append("📚 Literate Master")
                st.success("Hebat! Anda mendapatkan Badge '📚 Literate Master'!")
                st.rerun()

# ==========================================
# 3. EKSPLORASI MODEL
# ==========================================
elif menu == "🔍 Eksplorasi Model (Waterfall, Agile, dll)":
    st.markdown("## 🔍 Zona Eksplorasi Mandiri Model Perangkat Lunak")
    st.write("Pilih salah satu model di bawah ini untuk memahami detail karakteristik, kelebihan, kekurangan, dan contoh kasusnya.")

    model_pilihan = st.selectbox(
        "Pilih Model Pengembangan:",
        [
            "-- Silakan Pilih Model --",
            "1. Model Waterfall (Air Terjun)", 
            "2. Model Agile", 
            "3. Model Prototyping", 
            "4. Model Spiral", 
            "5. Model V-Model",
            "6. Model RAD (Rapid Application Development)"
        ]
    )

    if model_pilihan == "1. Model Waterfall (Air Terjun)":
        st.markdown("### 🌊 Model Waterfall (Klasik / Linier)")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - **Deskripsi:** Pendekatan sekuensial di mana setiap tahap harus diselesaikan sepenuhnya sebelum melangkah ke tahap berikutnya. Tidak ada tumpang tindih fase.
            - **Kapan Digunakan:** Kebutuhan sistem sudah baku, spesifikasi tidak akan berubah, dan teknologi sudah dipahami sepenuhnya oleh pengembang.
            - **Contoh Nyata:** Pembuatan perangkat lunak sistem kalkulator saintifik baku atau sistem pencatatan inventaris kantor yang prosedurnya tidak pernah berubah.
            """)
        with col2:
            st.info("💡 **Kata Kunci:** Sekuensial, Kaku, Dokumen Tebal, Satu Arah.")

    elif model_pilihan == "2. Model Agile":
        st.markdown("### ⚡ Model Agile")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - **Deskripsi:** Pendekatan iteratif yang membagi proyek ke dalam bagian-bagian kecil (disebut *Sprint* berdurasi 1-4 minggu) dengan evaluasi terus-menerus bersama klien.
            - **Kapan Digunakan:** Startup digital, aplikasi inovatif, atau proyek yang kebutuhannya sangat dinamis dan cepat berubah mengikuti tren pasar.
            - **Contoh Nyata:** Pengembangan aplikasi e-commerce, startup transportasi online, atau game mobile update berkala.
            """)
        with col2:
            st.info("💡 **Kata Kunci:** Iteratif, Fleksibel, Kolaborasi Klien, Sprint.")

    elif model_pilihan == "3. Model Prototyping":
        st.markdown("### 🎨 Model Prototyping")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - **Deskripsi:** Membuat model tiruan (prototype) fungsional terlebih dahulu agar pengguna dapat berinteraksi langsung dan memberikan umpan balik visual sebelum sistem akhir dibangun.
            - **Kapan Digunakan:** Klien kesulitan mendefinisikan kebutuhan secara abstrak atau antarmuka (*UI/UX*) memegang peranan penentu kesuksesan.
            - **Contoh Nyata:** Desain awal portal pendaftaran mahasiswa baru berbasis web atau sistem informasi rekam medis rumah sakit.
            """)
        with col2:
            st.info("💡 **Kata Kunci:** Model Tiruan, Umpan Balik Visual, Desain Awal.")

    elif model_pilihan == "4. Model Spiral":
        st.markdown("### 🌀 Model Spiral")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - **Deskripsi:** Menggabungkan keunggulan model iteratif dengan kontrol sistematis dari model waterfall, dengan penekanan khusus pada analisis dan mitigasi risiko di setiap putaran spiral.
            - **Kapan Digunakan:** Proyek skala besar yang sangat kompleks, berisiko tinggi, dan melibatkan biaya investasi yang besar.
            - **Contoh Nyata:** Sistem navigasi satelit atau kendali pesawat terbang, perangkat lunak pertahanan militer, dan sistem perbankan inti berskala nasional.
            """)
        with col2:
            st.info("💡 **Kata Kunci:** Analisis Risiko, Kompleksitas Tinggi, Putaran Evaluasi.")

    elif model_pilihan == "5. Model V-Model":
        st.markdown("### ✔️ Model V-Model (Validation & Verification)")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - **Deskripsi:** Perluasan dari model Waterfall di mana setiap fase pengembangan di sisi kiri memiliki fase pengujian (*testing*) pasangannya di sisi kanan yang membentuk huruf "V".
            - **Kapan Digunakan:** Sistem di mana pengujian ketat sangat dibutuhkan sejak awal perancangan karena kesalahan sekecil apapun berdampak fatal.
            - **Contoh Nyata:** Perangkat lunak pengendali alat medis rumah sakit (MRI/CT Scan) atau sistem pengereman otomatis kendaraan (ABS).
            """)
        with col2:
            st.info("💡 **Kata Kunci:** Pengujian Paralel, Validasi Dini, Keamanan Tinggi.")

    elif model_pilihan == "6. Model RAD (Rapid Application Development)":
        st.markdown("### 🚀 Model RAD (Rapid Application Development)")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - **Deskripsi:** Model pengembangan inkremental berkecepatan tinggi yang memanfaatkan komponen yang sudah ada (*reusable components*) dan prototyping intensif dalam waktu singkat (biasanya 60-90 hari).
            - **Kapan Digunakan:** Sistem informasi bisnis yang membutuhkan kecepatan rilis tinggi dan dapat modularisasi dengan baik.
            - **Contoh Nyata:** Pembuatan sistem manajemen inventaris toko retail atau dashboard pelaporan cepat internal perusahaan.
            """)
        with col2:
            st.info("💡 **Kata Kunci:** Kecepatan Tinggi, Komponen Siap Pakai, Time-boxing.")

# ==========================================
# 4. LKPD INTERAKTIF (STUDI KASUS)
# ==========================================
elif menu == "📝 LKPD Interaktif (Studi Kasus)":
    st.markdown("## 📝 Lembar Kerja Peserta Didik (LKPD) Digital")
    st.markdown("Analisis skenario kasus di bawah ini secara cermat. **Catatan Penting:** Anda wajib mengisi dan mengirim LKPD ini agar menu Kuis Terbuka!")

    st.markdown("""
    <div class="card">
    <h4>📌 Studi Kasus Proyek SMK:</h4>
    <p><i>"SMKN 1 Lemahsugih merencanakan pembuatan aplikasi Ujian Sekolah Berbasis Android dan Web secara mandiri. Pihak sekolah menginginkan seluruh fitur ujian, bank soal, dan pengamanan kecurangan sudah dikunci spesifikasinya sesuai POS (Prosedur Operasional Standar) dinas pendidikan tanpa ada perubahan mendadak di tengah pelaksanaan ujian, serta seluruh modul dikerjakan secara runtut dari analisis hingga uji coba akhir."</i></p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("form_lkpd_lengkap"):
        nama_siswa = st.text_input("Nama Lengkap Siswa:")
        kelas_siswa = st.text_input("Kelas / Jurusan (Contoh: XI Rekayasa Perangkat Lunak):")
        
        pilihan_model_lkpd = st.radio(
            "Berdasarkan studi kasus di atas, model SDLC manakah yang paling tepat dan mengapa?",
            [
                "Model Waterfall (Air Terjun) - Karena aturan & spesifikasi sudah baku/kaku sesuai POS tanpa perubahan di tengah jalan.",
                "Model Agile - Karena ujian harus diubah setiap 5 menit sekali.",
                "Model Prototyping - Karena sekolah hanya ingin melihat bentuk tombol tanpa sistem ujian.",
                "Model Spiral - Karena aplikasi ujian roket militer berisiko tinggi."
            ]
        )
        
        analisis_alasan = st.text_area("Tuliskan argumen atau alasan ilmiah mengapa Anda memilih model tersebut:")
        
        submit_lkpd = st.form_submit_button("📤 Kirim Lembar Kerja (LKPD)")
        
        if submit_lkpd:
            if nama_siswa and analisis_alasan:
                st.session_state.lkpd_submitted = True
                st.session_state.xp += 35
                if "📝 LKPD Master" not in st.session_state.badges:
                    st.session_state.badges.append("📝 LKPD Master")
                st.success(f"Luar biasa, **{nama_siswa}**! LKPD Anda berhasil dikirim dan direkam. Menu Kuis sekarang resmi **TERBUKA**! 🎉")
                st.balloons()
            else:
                st.error("Mohon lengkapi Nama Lengkap dan Alasan Analisis Anda sebelum mengirim LKPD!")

# ==========================================
# 5. KUIS & TANTANGAN XP (10 SOAL PG - 5 OPSI)
# ==========================================
elif menu == "🎮 Tantangan Kuis (10 Soal PG)":
    st.markdown("## 🎮 Tantangan Kuis Komprehensif (10 Soal Pilihan Ganda)")
    
    # Validasi Kunci Akses Kuis berdasarkan LKPD
    if not st.session_state.lkpd_submitted:
        st.markdown("""
        <div class="locked-card">
        <h3>🔒 KUIS TERKUNCI!</h3>
        <p>Maaf, Anda belum dapat mengakses Kuis ini. Sesuai aturan pembelajaran, Anda <b>wajib mengisi dan mengirimkan Lembar Kerja (LKPD)</b> terlebih dahulu di menu <b>"📝 LKPD Interaktif (Studi Kasus)"</b>.</p>
        <p><i>Silakan kembali ke menu LKPD, selesaikan analisis kasus, lalu kuis akan terbuka secara otomatis!</i></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.success("🔓 Kuis Terbuka! Silakan jawab 10 pertanyaan pilihan ganda berikut dengan teliti (masing-masing 5 opsi A-E).")

        with st.form("quiz_10_soal"):
            
            # Soal 1
            st.markdown("**1. Apa kepanjangan dari akronim SDLC dalam rekayasa perangkat lunak?**")
            q1 = st.radio("Pilih Opsi:", [
                "A. System Design Life Cycle",
                "B. Software Development Life Cycle",
                "C. Software Data Logic Control",
                "D. Structured Deployment Local Computer",
                "E. Standard Digital Logic Creation"
            ], key="q1")

            # Soal 2
            st.markdown("**2. Manakah tahapan pertama yang umumnya dilakukan dalam model pengembangan Waterfall?**")
            q2 = st.radio("Pilih Opsi:", [
                "A. Pengkodean (Coding)",
                "B. Pengujian (Testing)",
                "C. Analisis Kebutuhan (Requirements Analysis)",
                "D. Pemeliharaan (Maintenance)",
                "E. Peluncuran Produk (Deployment)"
            ], key="q2")

            # Soal 3
            st.markdown("**3. Model pengembangan yang pengerjaannya dilakukan secara linier dan berurutan dari atas ke bawah seperti air terjun disebut...**")
            q3 = st.radio("Pilih Opsi:", [
                "A. Model Agile",
                "B. Model Spiral",
                "C. Model Waterfall",
                "D. Model Prototyping",
                "E. Model RAD"
            ], key="q3")

            # Soal 4
            st.markdown("**4. Karakteristik utama yang membedakan metodologi Agile dibanding model tradisional adalah...**")
            q4 = st.radio("Pilih Opsi:", [
                "A. Kaku dan tidak boleh ada perubahan sama sekali",
                "B. Pengerjaan dilakukan dalam siklus pendek (Sprint) dan sangat adaptif terhadap perubahan",
                "C. Dokumentasi harus mencapai 1000 halaman sebelum koding",
                "D. Tidak memerlukan pengujian sistem sama sekali",
                "E. Hanya dikerjakan oleh satu orang programmer"
            ], key="q4")

            # Soal 5
            st.markdown("**5. Kapan waktu yang paling tepat untuk menggunakan Model Prototyping?**")
            q5 = st.radio("Pilih Opsi:", [
                "A. Ketika kebutuhan sistem sudah sangat kaku dan tidak pernah berubah",
                "B. Ketika klien atau pengguna belum bisa mendefinisikan kebutuhan sistem secara jelas di awal",
                "C. Ketika anggaran proyek sangat terbatas dan tidak ingin membuat desain visual",
                "D. Ketika proyek dikerjakan dalam waktu 10 tahun",
                "E. Ketika perangkat lunak tidak memiliki antarmuka sama sekali"
            ], key="q5")

            # Soal 6
            st.markdown("**6. Fokus utama yang membuat Model Spiral sangat unik dibandingkan model lainnya adalah penekanan pada...**")
            q6 = st.radio("Pilih Opsi:", [
                "A. Analisis dan mitigasi risiko yang mendalam di setiap putaran",
                "B. Pembuatan game animasi 3 dimensi",
                "C. Penggunaan bahasa pemrograman Python saja",
                "D. Kecepatan penulisan kode tanpa desain",
                "E. Penjualan lisensi perangkat lunak"
            ], key="q6")

            # Soal 7
            st.markdown("**7. Dalam model V-Model (Validation & Verification), apa pasangan dari fase pengkodean (coding) di sisi pengujian?**")
            q7 = st.radio("Pilih Opsi:", [
                "A. Ujian Nasional",
                "B. Unit Testing & Component Testing",
                "C. Pemasangan kabel jaringan",
                "D. Pembayaran pajak perusahaan",
                "E. Wawancara klien"
            ], key="q7")

            # Soal 8
            st.markdown("**8. Apa keuntungan utama dari pembuatan Prototype di awal pengembangan sistem?**")
            q8 = st.radio("Pilih Opsi:", [
                "A. Sistem langsung selesai 100% tanpa revisi",
                "B. Pengguna dapat melihat representasi visual dan memberikan masukan nyata",
                "C. Memastikan server tidak pernah down",
                "D. Menghapus kebutuhan akan database",
                "E. Membuat ukuran file aplikasi menjadi sangat kecil"
            ], key="q8")

            # Soal 9
            st.markdown("**9. Model RAD (Rapid Application Development) sangat mengandalkan hal berikut untuk mempercepat penyelesaian proyek, KECUALI:**")
            q9 = st.radio("Pilih Opsi:", [
                "A. Komponen yang dapat digunakan kembali (reusable components)",
                "B. Prototyping intensif",
                "C. Waktu pengerjaan yang dibatasi (time-boxing)",
                "D. Proses birokrasi dan dokumentasi linier yang memakan waktu berbulan-bulan",
                "E. Kolaborasi tim yang erat"
            ], key="q9")

            # Soal 10
            st.markdown("**10. Jika sebuah startup fintech ingin meluncurkan fitur dompet digital baru dalam waktu 2 minggu untuk merespons tren pasar yang cepat, model SDLC mana yang paling ideal?**")
            q10 = st.radio("Pilih Opsi:", [
                "A. Model Waterfall",
                "B. Model Agile / Scrum",
                "C. Model V-Model kaku",
                "D. Model Waterfall bertingkat sepuluh",
                "E. Model manual non-software"
            ], key="q10")

            submit_all_quiz = st.form_submit_button("🏁 Selesai & Periksa Jawaban Kuis")

            if submit_all_quiz:
                score_total = 0
                if q1.startswith("B"): score_total += 1
                if q2.startswith("C"): score_total += 1
                if q3.startswith("C"): score_total += 1
                if q4.startswith("B"): score_total += 1
                if q5.startswith("B"): score_total += 1
                if q6.startswith("A"): score_total += 1
                if q7.startswith("B"): score_total += 1
                if q8.startswith("B"): score_total += 1
                if q9.startswith("D"): score_total += 1
                if q10.startswith("B"): score_total += 1

                st.markdown("---")
                st.markdown(f"### 📊 Hasil Akhir Kuis Anda: **{score_total} / 10 Benar** (Nilai: {score_total * 10})")
                
                if score_total >= 8:
                    st.success("🌟 Luar Biasa! Anda menguasai konsep model perangkat lunak dengan sangat sempurna!")
                    st.session_state.xp += 50
                    if "🏆 SDLC Grandmaster" not in st.session_state.badges:
                        st.session_state.badges.append("🏆 SDLC Grandmaster")
                    st.balloons()
                elif score_total >= 5:
                    st.info("👍 Kerja bagus! Pemahaman Anda sudah baik, namun baca kembali materi beberapa model untuk hasil maksimal.")
                    st.session_state.xp += 25
                else:
                    st.warning("⚠️ Tetap semangat! Silakan tinjau kembali menu Zona Literasi & Eksplorasi Model sebelum mencoba kuis kembali.")