import streamlit as st
from PIL import Image
import pytesseract
import io
import pdf2image as p2i
from extract_key import extract_key_info

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler\poppler-24.08.0\Library\bin"
st.set_page_config(page_title="Insurance Claim OCR", layout="centered")

st.title("📄 OCR for processing insurance documents")
st.markdown("Upload an image or pdf file of an insurance claim form and extract text using AI. (English Only)")
uploaded_file = st.file_uploader("Choose an file", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file:
    file_type = uploaded_file.type
    extracted = ''
    try:
        with st.spinner("Processing. . ."):
            if file_type == "application/pdf":
                images = p2i.convert_from_bytes(uploaded_file.read(), poppler_path=POPPLER_PATH)
                for i, img in enumerate(images):
                    extracted += f"\n--- Page {i+1} ---\n"
                    extracted += pytesseract.image_to_string(img)
            else:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", use_container_width=True)
                extracted = pytesseract.image_to_string(image)
        with st.container():
            st.success("✅Extraction Completed!")
            st.subheader("Extracted Text:")
            # st.text_area("Result", extracted, height=400, disabled=True)
            st.code(extracted, language='text', height=400)
        with st.container():
            info = extract_key_info(extracted)
            st.subheader("Key Information:")
            key_info = ""
            if info:
                for key, val in info.items():
                    key_info += (f"{key}: {val}\n")
                st.code(key_info, language='text', height=400)
            else:
                st.warning("Cannot extract key information")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info('Please upload file to begin')