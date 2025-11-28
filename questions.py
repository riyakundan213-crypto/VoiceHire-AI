# questions.py
# Expanded professional question bank across many IT & business fields.

QUESTION_BANK = {
    "general": [
        "Tell me about yourself.",
        "Why do you want this role?",
        "What are your strengths and weaknesses?",
        "Describe a challenge you faced and how you solved it.",
        "Where do you see yourself in 5 years?",
        "Tell me about a time you showed leadership.",
        "How do you handle deadlines?"
    ],

    "data_science": [
        "Explain a machine learning project you worked on.",
        "How do you deal with missing data?",
        "Which model would you choose for classification?",
        "What is bias-variance tradeoff?",
        "Explain cross-validation and why it's used.",
        "How do you evaluate a regression model?",
        "Describe feature engineering you performed in a project."
    ],

    "machine_learning": [
        "What is regularization and why is it useful?",
        "Explain gradient descent.",
        "Difference between bagging and boosting.",
        "How does a random forest work?",
        "Explain deep learning vs classical ML.",
        "What is overfitting and how to prevent it?"
    ],

    "nlp": [
        "What is tokenization?",
        "Explain word embeddings.",
        "How do you handle out-of-vocabulary words?",
        "Describe a text classification pipeline.",
        "What is attention mechanism?"
    ],

    "data_engineer": [
        "Explain an ETL pipeline.",
        "What is partitioning?",
        "How do you optimize SQL queries?",
        "Explain OLAP vs OLTP."
    ],

    "data_analyst": [
        "How do you clean a dataset?",
        "Explain a dashboard you created.",
        "Which charts suit different data types?",
        "How do you validate data quality?"
    ],

    "software_development": [
        "Explain SOLID principles.",
        "What is OOP?",
        "How do you design REST APIs?",
        "Explain debugging process.",
        "What are design patterns?"
    ],

    "web_development": [
        "Frontend vs backend roles.",
        "How responsive design works.",
        "What is CORS?",
        "Lifecycle of an HTTP request."
    ],

    "devops": [
        "What is CI/CD?",
        "Explain Docker.",
        "What is Kubernetes?",
        "How do you monitor production apps?"
    ],

    "cloud": [
        "Describe AWS/GCP/Azure services.",
        "What is serverless?",
        "Explain IAM security."
    ],

    "cybersecurity": [
        "What is XSS?",
        "Explain SQL injection.",
        "What is HTTPS?",
        "Authentication vs authorization."
    ],

    "finance": [
        "Explain ROE and ROI.",
        "What is cash flow?",
        "How to evaluate a financial project?"
    ],

    "business_analysis": [
        "How do you gather requirements?",
        "Explain use-case diagram.",
        "How do you prioritize tasks?"
    ],

    "marketing": [
        "Describe a digital campaign.",
        "What metrics matter?",
        "Explain SEO basics."
    ],

    "hr": [
        "Describe conflict resolution.",
        "How to judge cultural fit?",
        "Onboarding steps?"
    ],

    "ux_ui": [
        "Principles of good UX.",
        "Describe user research.",
        "How do you turn feedback into design?"
    ],

    "qa_testing": [
        "Explain test case design.",
        "Unit vs integration vs system testing.",
        "How to prioritize tests?"
    ],

    "general_technical": [
        "Explain a technical project.",
        "How do you handle technical debt?",
        "Describe a decision you made using data."
    ]
}

ROLE_TO_FIELDS = {
    "data": ["data_science", "data_analyst", "machine_learning", "nlp", "data_engineer"],
    "analyst": ["data_analyst", "data_science"],
    "machine": ["machine_learning","data_science"],
    "ml": ["machine_learning","data_science"],
    "engineer": ["software_development","devops","cloud","data_engineer"],
    "developer": ["software_development","web_development"],
    "devops": ["devops","cloud"],
    "cloud": ["cloud","devops"],
    "security": ["cybersecurity"],
    "qa": ["qa_testing"],
    "finance": ["finance","business_analysis"],
    "marketing": ["marketing"],
    "hr": ["hr","general"],
    "design": ["ux_ui"],
    "product": ["business_analysis","general_technical"]
}

ALL_FIELDS = list(QUESTION_BANK.keys())
