# IDRAK | Banking Made Smarter

IDRAK is an AI-powered banking intent classification assistant designed to help customers better understand their banking inquiries.

Using Natural Language Processing (NLP), IDRAK identifies the intent behind a customer's message and provides relevant guidance through a simple, interactive interface.

## Live Demo

[Explore IDRAK](https://idrak-banking-assistant.streamlit.app/)

## Project Overview

Banking customers often struggle to identify the appropriate service or support channel for their inquiries.

IDRAK addresses this challenge by classifying customer messages into predefined banking intents and presenting helpful next steps.

The project focuses on making banking inquiries easier to understand and navigate.

## Key Features

- **Intent Classification:** Classifies banking inquiries into 77 categories.
- **Interactive Assistant:** Allows users to enter banking-related questions.
- **Model Insights:** Displays prediction scores and alternative predictions.
- **Customer Guidance:** Provides suggested next steps based on the predicted intent.
- **Responsive Interface:** Offers a Streamlit-based interface for interacting with the model.

## Dataset

**Banking77**

A banking customer service dataset containing 77 intent categories.

The dataset is used to train and evaluate the intent classification model.

## Machine Learning Approach

The classification pipeline combines:

- **TF-IDF Vectorization** for text feature extraction.
- **Logistic Regression** for multiclass intent classification.

This approach provides an efficient and interpretable baseline for banking intent recognition.

## Model Performance

| Metric | Result |
|--------|--------|
| Classification Categories | 77 |
| Model | Logistic Regression |
| Feature Extraction | TF-IDF |
| Test Accuracy | 89.42% |

## Tech Stack

- Python
- Scikit-learn
- Pandas
- NumPy
- Streamlit
- Joblib

## Project Structure

```text
IDRAK-Project/
├── app.py
├── banking_pipeline.joblib
├── categories.joblib
├── idrak_logo.png
├── IDRAK.ipynb
├── requirements.txt
└── README.md
```

## Run Locally

Clone the repository:

```bash
git clone https://github.com/uSebaa/IDRAK-Project.git
cd IDRAK-Project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run app.py
```

## Limitations

IDRAK is an educational machine learning project.

The application provides predicted banking intents and general guidance. It does not access bank accounts, execute transactions, or connect directly to banking systems.

Prediction scores represent model estimates and should not be interpreted as guarantees of correctness.

## Future Improvements

- Improve classification accuracy through model experimentation.
- Expand support for multilingual banking inquiries.
- Enhance the user experience and mobile responsiveness.
- Explore integration with banking support workflows.

---

**IDRAK — Banking Made Smarter**

*Here to Help You Understand Your Banking Needs.*
