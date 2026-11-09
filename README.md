# FAQ Chatbot — Internship Project

Full-stack FAQ chatbot using Python, Flask, scikit-learn, TF-IDF and cosine similarity.

## Features
- Browser chat interface and suggested questions
- FAQ question/answer dataset stored in JSON
- Text cleaning and preprocessing
- TF-IDF vectorization with unigrams and bigrams
- Cosine similarity to find the closest FAQ
- Similarity threshold for unmatched questions
- Flask JSON API and responsive design

## Run on Windows (VS Code PowerShell)

Open this extracted project folder in VS Code, then run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

If PowerShell blocks activation, run this in the same terminal and retry:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Open http://127.0.0.1:5000 in your browser.

If `.venv` was created in the parent directory instead, activate it with:

```powershell
..\.venv\Scripts\Activate.ps1
```

## Folder structure

```text
FAQ_Chatbot_Internship_Project/
├── app.py
├── faq_engine.py
├── requirements.txt
├── README.md
├── data/faqs.json
├── templates/index.html
└── static/
    ├── style.css
    └── script.js
```

## API endpoints
- `GET /` — chatbot page
- `POST /api/chat` — JSON body: `{"message":"How can I apply?"}`
- `GET /api/faqs` — list FAQ questions and categories
- `GET /health` — health check

## Customize your FAQ data
Edit `data/faqs.json`. Each record must contain `category`, `question`, and `answer`. Restart Flask after editing the file.

## How it works
1. User submits a question in the chat interface.
2. JavaScript sends it to Flask `/api/chat`.
3. The FAQ engine preprocesses the text and transforms it using TF-IDF.
4. Cosine similarity compares it with the FAQ question vectors.
5. The best answer is returned if it passes the configured threshold.
6. The UI displays the answer and similarity score.

## Limitations
This is a retrieval-based FAQ bot, not generative AI. It can only answer questions represented in the FAQ dataset or phrased similarly. The threshold may need tuning. Replace the generic sample FAQs with verified FAQs for your assigned product or topic before submission.
