## 🩺 Multilingual Medical Support Chatbot

### 📌 Project Overview

This project implements a **Multilingual Medical Support Chatbot** capable of understanding medical queries written in **any language**. The chatbot automatically translates non-English queries into English, generates a **medically safe and informative response** using a domain-specific Large Language Model (LLM), and translates the response back into the user’s original language.

⚠️ **Medical Disclaimer:**
This chatbot provides general medical information only and **is not a substitute for professional diagnosis or treatment**.

---

## 🎯 Problem Statement

Language barriers often prevent users from accessing basic medical guidance. This project addresses that challenge by building a chatbot that provides **multilingual medical assistance** using translation models and a medical-aware LLM, delivered through an interactive **Streamlit web interface**.

---

## 🚀 Key Features

* 🌐 Multilingual input support (automatic language detection)
* 🔄 Real-time translation using Meta NLLB-200 model
* 🧠 Medical response generation using FLAN-T5
* 🖥️ Interactive and user-friendly Streamlit UI
* ⚠️ Built-in medical disclaimer
* 📦 Modular, scalable, and maintainable codebase

---

## 🧠 Technologies Used

* **Python**
* **Streamlit** (Frontend UI)
* **Hugging Face Transformers**
* **Meta NLLB-200** (Multilingual Translation)
* **Google FLAN-T5** (Medical Text Generation)
* **LangDetect**
* **PyTorch**

---

## 🏥 Business Use Cases

* Multilingual patient support
* Public health awareness
* Rural and remote healthcare guidance
* Medical education and awareness
* Symptom pre-screening before consultation

---

## 📂 Project Structure

```
Multilingual_Medical_Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── src/
    ├── translator.py
    ├── medical_llm.py
    └── utils.py
```

---

## ⚙️ Installation & Setup

### Step 1: Clone Repository

```bash
git clone https://github.com/<your-username>/Multilingual-Medical-Chatbot.git
cd Multilingual-Medical-Chatbot
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate:

* **Windows:** `venv\Scripts\activate`
* **Linux/Mac:** `source venv/bin/activate`

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

---

## 🧪 Sample Queries

**English**

```
What are the early signs of diabetes?
```

**Tamil**

```
எனக்கு காய்ச்சல் உள்ளது. பொதுவாக என்ன செய்யலாம்?
```

**Hindi**

```
उच्च रक्तचाप के सामान्य लक्षण क्या हैं?
```

---

## 📊 Dataset Information

This project uses **pre-trained models** for inference.
For fine-tuning and future enhancement, the following datasets are recommended:

* MedQuAD
* PubMedQA
* HealthcareMagic QA
  (Available via Hugging Face Datasets)

---

## 📈 Future Enhancements

* Fine-tuning medical LLM on domain-specific datasets
* Voice input and output
* Appointment booking integration
* Chat history and user profiles
* Deployment on AWS / Hugging Face Spaces

---

## 🎓 Academic Relevance

* Demonstrates real-world application of NLP and LLMs
* Covers translation, inference, deployment, and UI integration
* Follows PEP-8 coding standards and modular architecture

---

## 👨‍💻 Author

**Pavankumar J**

---

## 📜 License

This project is for **educational and research purposes only**.

---



