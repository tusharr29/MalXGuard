# 🛡️ MalXGuard: Malware Classification System  

MalXGuard is a machine learning-based malware detection and classification system.  
It extracts features from raw `.asm` and `.bytes` files, applies NLP-based techniques, and classifies malware into multiple families using machine learning models.  

---

## 📌 Project Overview  
- Detects and classifies malware into families.  
- Uses **TF-IDF feature extraction** on assembly and bytecode files.  
- Trains a **Random Forest classifier** (extendable to other ML models).  
- Includes an **inference API** for predictions on new samples.  

---

## ⚙️ Features  
✅ Extracts features from `.asm` and `.bytes` malware files  
✅ Converts raw data into vectorized representations (TF-IDF)  
✅ Trains machine learning models for classification  
✅ Provides inference script for real-time predictions  
✅ Modular structure for easy extension  

---

## 🚀 Installation  

```bash
# Clone the repository
git clone https://github.com/tusharr29/MalXGuard.git
cd MalXGuard

# Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows

# Install dependencies
pip install -r requirements.txt
