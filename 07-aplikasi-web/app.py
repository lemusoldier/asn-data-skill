#!/usr/bin/env python3
"""Aplikasi Web Dashboard ASN (Streamlit)
Web App GUI interaktif untuk mempermudah operasional pengolahan data.
"""
import streamlit as st
import pandas as pd
import io

# Setup Halaman
st.set_page_config(
    page_title="ASN Data Tool",
    page_icon="📊",
    layout="wide"
)

st.title("📊 ASN Data Cleansing & Dashboard Tool")
st.markdown("Aplikasi web sederhana untuk membantu mengolah data dinas dengan cepat tanpa coding.")
st.divider()

# Sidebar menu
menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Pembersih Data Duplikat", "Gabung File (Merge)", "Dashboard Visualisasi"]
)

# ==================== MENU 1: CLEAN DATA ====================
if menu == "Pembersih Data Duplikat":
    st.header("🧹 Pembersih Data Duplikat")
    st.markdown("Upload file CSV atau Excel Anda di bawah ini untuk menghapus baris data NIP ganda.")
    
    uploaded_file = st.file_uploader("Pilih File Excel/CSV", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        # Load data
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            
        st.subheader("Data Asli (Sebelum Cleansing)")
        st.dataframe(df.head(10))
        st.write(f"Total data: **{len(df)}** baris")
        
        # Opsi pembersihan
        kolom_kunci = st.selectbox("Pilih kolom kunci (misal: NIP)", df.columns)
        
        if st.button("Jalankan Pembersihan"):
            df_bersih = df.drop_duplicates(subset=[kolom_kunci], keep="first")
            
            # Bersihkan spasi jika kolom bertipe string
            if df_bersih[kolom_kunci].dtype == 'object':
                df_bersih[kolom_kunci] = df_bersih[kolom_kunci].str.strip()
                
            st.success("✅ Pembersihan selesai!")
            st.write(f"Total data bersih: **{len(df_bersih)}** baris (Dihapus {len(df) - len(df_bersih)} baris duplikat)")
            
            st.subheader("Data Hasil Pembersihan")
            st.dataframe(df_bersih.head(10))
            
            # Download button
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df_bersih.to_excel(writer, index=False, sheet_name='Data Bersih')
            
            st.download_button(
                label="📥 Download Excel Bersih",
                data=output.getvalue(),
                file_name="data_bersih.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

# ==================== MENU 2: MERGE FILE ====================
elif menu == "Gabung File (Merge)":
    st.header("🔀 Gabung Beberapa File")
    st.markdown("Upload beberapa file Excel/CSV dengan struktur kolom yang sama untuk digabung menjadi satu.")
    
    uploaded_files = st.file_uploader(
        "Pilih 2 atau lebih File Excel/CSV", 
        type=["csv", "xlsx"], 
        accept_multiple_files=True
    )
    
    if len(uploaded_files) >= 2:
        st.success(f"Terbaca {len(uploaded_files)} file siap gabung.")
        
        if st.button("Gabungkan Sekarang"):
            df_list = []
            for f in uploaded_files:
                if f.name.endswith(".csv"):
                    df = pd.read_csv(f)
                else:
                    df = pd.read_excel(f)
                df_list.append(df)
            
            df_gabungan = pd.concat(df_list, ignore_index=True)
            
            st.success("✅ Semua file berhasil digabung!")
            st.write(f"Total baris gabungan: **{len(df_gabungan)}** baris")
            st.dataframe(df_gabungan.head(10))
            
            # Download button
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df_gabungan.to_excel(writer, index=False, sheet_name='Gabungan')
            
            st.download_button(
                label="📥 Download Hasil Gabungan",
                data=output.getvalue(),
                file_name="rekap_gabungan.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    elif len(uploaded_files) == 1:
        st.warning("Silakan upload minimal 1 file lagi untuk digabungkan.")

# ==================== MENU 3: DASHBOARD ====================
elif menu == "Dashboard Visualisasi":
    st.header("📈 Dashboard Visualisasi Cepat")
    st.markdown("Upload file rekap pegawai Anda untuk melihat visualisasi dan grafiknya.")
    
    uploaded_file = st.file_uploader("Upload File Rekap", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            
        col1, col2 = st.columns(2)
        
        # Cek kolom yang umum
        kolom_unit = [c for c in df.columns if 'unit' in c.lower() or 'bidang' in c.lower()]
        kolom_gol = [c for c in df.columns if 'golongan' in c.lower() or 'gol' in c.lower()]
        
        with col1:
            if kolom_unit:
                st.subheader("Distribusi per Unit Kerja")
                unit_counts = df[kolom_unit[0]].value_counts()
                st.bar_chart(unit_counts)
            else:
                st.info("Kolom 'Unit Kerja' tidak ditemukan.")
                
        with col2:
            if kolom_gol:
                st.subheader("Sebaran Golongan")
                gol_counts = df[kolom_gol[0]].value_counts().sort_index()
                st.bar_chart(gol_counts)
            else:
                st.info("Kolom 'Golongan' tidak ditemukan.")
                
        st.subheader("Statistik Ringkas")
        col_stat1, col_stat2, col_stat3 = st.columns(3)
        col_stat1.metric("Total Pegawai", f"{len(df)} orang")
        
        kolom_gaji = [c for c in df.columns if 'gaji' in c.lower() or 'penerimaan' in c.lower()]
        if kolom_gaji:
            gaji_avg = df[kolom_gaji[0]].mean()
            gaji_sum = df[kolom_gaji[0]].sum()
            col_stat2.metric("Rata-rata Gaji", f"Rp {gaji_avg:,.0f}")
            col_stat3.metric("Total Anggaran Gaji", f"Rp {gaji_sum:,.0f}")
