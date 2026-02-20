import streamlit as st

# Mengatur judul aplikasi
st.set_page_config(page_title="Code Combiner for AI", page_icon="🧩")
st.title("🧩 Penggabung File untuk AI Studio")
st.write("Upload berbagai file script (misal: .py, .txt, .md, .csv) dari project Anda untuk digabungkan menjadi satu file teks.")

# Widget untuk upload banyak file
uploaded_files = st.file_uploader("Pilih file code Anda", accept_multiple_files=True)

if uploaded_files:
    combined_text = ""
    
    # Looping untuk membaca dan menggabungkan setiap file
    for file in uploaded_files:
        try:
            # Membaca isi file sebagai string
            content = file.read().decode("utf-8")
            
            # Membuat separator yang jelas agar AI tahu ini file yang berbeda
            combined_text += f"\n\n{'='*50}\n"
            combined_text += f"📄 NAMA FILE: {file.name}\n"
            combined_text += f"{'='*50}\n\n"
            
            # Memasukkan isi code
            combined_text += content
            
        except Exception as e:
            st.error(f"Gagal membaca file {file.name}. Pastikan formatnya berupa teks. Error: {e}")

    # Menampilkan preview (opsional, dibatasi 500 karakter agar tidak berat)
    st.subheader("Preview Hasil Gabungan:")
    st.text_area("Isi File Gabungan", combined_text[:500] + "...\n\n(Preview dipotong, silakan download untuk melihat versi utuh)", height=200)

    # Tombol untuk mendownload hasil gabungan
    st.download_button(
        label="📥 Download File Gabungan (.txt)",
        data=combined_text,
        file_name="gabungan_smartbim_code.txt",
        mime="text/plain"
    )
