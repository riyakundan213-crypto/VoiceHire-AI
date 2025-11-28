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
        "Explain gradient descent and its variants.",
        "Difference between bagging and boosting.",
        "How does a random forest work?",
        "Explain deep learning vs classical ML.",
        "What is overfitting and how to prevent it?"
    ],

    "nlp": [
        "What is tokenization?",
        "Explain word embeddings (Word2Vec/GloVe).",
        "How do you handle out-of-vocabulary words?",
        "Describe a text classification pipeline you built.",
        "What is attention mechanism?"
    ],

    "data_engineer": [
        "Explain an ETL pipeline you built or would build.",
        "What is partitioning and why is it used?",
        "How do you optimize SQL queries?",
        "Explain OLAP vs OLTP."
    ],

    "data_analyst": [
        "How do you clean a dataset before analysis?",
        "Explain a dashboard you created and metrics tracked.",
        "Which charts would you choose for categorical vs numerical data?",
        "How do you validate data quality?"
    ],

    "software_development": [
        "Explain SOLID principles.",
        "What is OOP and give examples.",
        "How do you design RESTful APIs?",
        "Explain how you debug and test code.",
        "What design patterns have you used?"
    ],

    "web_development": [
        "Difference between frontend and backend responsibilities.",
        "Explain how responsive design works.",
        "What is CORS and how to handle it?",
        "Describe the lifecycle of an HTTP request."
    ],

    "devops": [
        "What is CI/CD and why is it important?",
        "Explain Docker and containerization benefits.",
        "What is Kubernetes and when to use it?",
        "How do you monitor application health in production?"
    ],

    "cloud": [
        "Describe a service on AWS/GCP/Azure you used and why.",
        "What is serverless computing?",
        "Explain IAM and security best practices for cloud."
    ],

    "cybersecurity": [
        "What is XSS and how to prevent it?",
        "Explain SQL Injection and mitigation.",
        "What is HTTPS and how does it work?",
        "Describe authentication vs authorization."
    ],

    "finance": [
        "Explain basic financial ratios (ROE, ROI).",
        "What is cash flow and why is it important?",
        "How do you perform a financial analysis of a project?"
    ],

    "business_analysis": [
        "How do you gather requirements for a project?",
        "Explain a use-case analysis you performed.",
        "How do you prioritize requirements?"
    ],

    "marketing": [
        "Describe a digital marketing campaign you would run for a product.",
        "What metrics matter most in marketing?",
        "Explain SEO basics and how to measure success."
    ],

    "hr": [
        "Describe a time you resolved conflict in a team.",
        "How do you assess a candidate’s cultural fit?",
        "What steps do you follow for onboarding a new hire?"
    ],

    "ux_ui": [
        "What are key principles of good UX design?",
        "Describe a user research method you used.",
        "How do you convert user feedback into product changes?"
    ],

    "qa_testing": [
        "Explain test case design and give an example.",
        "Difference between unit, integration, and system testing.",
        "How do you prioritize test execution?"
    ],

    "general_technical": [
        "Explain a technical project you led and the impact it had.",
        "How do you keep technical debt under control?",
        "Describe a problem where you used data to make a decision."
    ]
}

# Mapping common role keywords to preferred fields
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

