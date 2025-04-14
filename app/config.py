"""
Generic configuration for the portfolio website.
This file contains placeholder data that you can replace with your own information.
"""

# Portfolio Configuration
PORTFOLIO_CONFIG = {
    'personal_info': {
        'name': 'Niranjan',
        'title': 'Machine Learning Engineer',
        'bio': 'A passionate developer with expertise in machine learning, data engineering, and data science.',
        'email': 'sadulaniranjan@gmail.com',
        'phone': '+1 551 998 9024',
        'location': 'Hoboken, NJ',
        'github': 'https://github.com/snr16',
        'linkedin': 'https://linkedin.com/in/niranjansadula'
    },
    'about_me': {
        'summary': [
            "I'm Niranjan, a Machine Learning Engineer with a strong background in data engineering and machine learning.",
            "I hold a Master's in Machine Learning from Stevens Institute of Technology and a B.Tech. in Electrical Engineering from IIT Patna.",
            "I've evolved from working with circuits to crafting sophisticated AI systems.At Quantiphi, I've built high-performance data pipelines and AI solutions that make a real difference - from automating workflows to developing real-time monitoring systems. My sweet spot? Building scalable AI systems that blend technical precision with practical impact. Whether it's fine-tuning deep learning models or orchestrating big data workflows, I bring a mix of technical expertise and creative problem-solving to every project.",
            "Currently seeking full-time opportunities in AI, Data Science, and Data Engineering where I can contribute to building innovative and scalable solutions. Let's create something amazing together!"
        ],
        'interests': [
            "Machine Learning",
            "Data Engineering",
            "Natural Language Processing",
            "Computer Vision"
        ],
    },
    'education': [
        {
            'institution': 'Stevens Institute of Technology',
            'degree': 'Master of Science in Machine Learning',
            'date': 'Aug 2023 - Dec 2024',
            'gpa': '3.87/4.0',
            'location': 'Hoboken, NJ'
        },
        {
            'institution': 'Indian Institute of Technology, Patna',
            'degree': 'Bachelor of Technology in Electrical Engineering',
            'date': 'Aug 2017 - Jul 2021',
            'gpa': '3.3/4.0',
            'location': 'Patna, India'
        }
    ],
    'experience': [
        {
            'company': 'Quantiphi Inc.',
            'position': 'Machine Learning Engineer',
            'date': 'Jan 2022 - Aug 2023',
            'location': 'Mumbai, India',
            'achievements': [
                'Engineered scalable event-driven workflows using Google Cloud Functions, Cloud Storage, and BigQuery, reducing data redundancy by 30% and boosting processing speeds by 50%',
                'Deployed automated solutions via Google Document AI, reducing average processing duration from 30 minutes to 10 minutes per document',
                'Implemented event-driven triggers with Kafka and automated ETL workflows using Airflow and Cloud Dataflow, reducing system latency by 50%',
                'Designed and deployed a real-time alerting and monitoring system using Google Cloud Monitoring and Logging, reducing failure detection time by 70%',
                'Researched deep learning techniques for healthcare use cases, including AI-assisted medical imaging and patient readmission prediction',
                'Leveraged AlphaFold for protein structure prediction, improving drug efficacy analysis by 30%'
            ]
        },
        {
            'company': 'Quantiphi Inc.',
            'position': 'Machine Learning Intern',
            'date': 'Sep 2021 - Dec 2021',
            'location': 'Mumbai, India',
            'achievements': [
                'Developed an AI-driven vehicle damage assessment system, enhancing accuracy by 20% with inference speed under 250ms',
                'Created a scalable ML pipeline using TensorFlow, MLflow, and Prometheus, ensuring 95% reproducibility',
                'Optimized ML pipelines and enhanced model efficiency with TensorFlow implementation',
                'Analyzed 10+ state-of-the-art research papers during an intensive 4-month trainee program'
            ]
        }
    ],
    'skills': { 
        'categories': [
            {
                'name': 'Programming Languages',
                'icon': 'fas fa-code',
                'items': [
                    {'name': 'Python', 'icon': 'fab fa-python'},
                    {'name': 'R', 'icon': 'fas fa-chart-line'},
                    {'name': 'SQL', 'icon': 'fas fa-database'},
                    {'name': 'Java', 'icon': 'fab fa-java'},
                    {'name': 'Bash Scripting', 'icon': 'fas fa-terminal'}
                ]
            },
            {
                'name': 'Machine Learning & AI',
                'icon': 'fas fa-brain',
                'items': [
                    {'name': 'TensorFlow', 'icon': 'fas fa-project-diagram'},
                    {'name': 'PyTorch', 'icon': 'fas fa-project-diagram'},
                    {'name': 'Scikit-learn', 'icon': 'fas fa-project-diagram'},
                    {'name': 'Langchain', 'icon': 'fas fa-robot'},
                    {'name': 'LLMs', 'icon': 'fas fa-robot'}
                ]
            },
            {
                'name': 'Big Data & Cloud',
                'icon': 'fas fa-cloud',
                'items': [
                    {'name': 'Apache Spark', 'icon': 'fas fa-database'},
                    {'name': 'Kafka', 'icon': 'fas fa-stream'},
                    {'name': 'Google Cloud', 'icon': 'fab fa-google'},
                    {'name': 'AWS', 'icon': 'fab fa-aws'},
                    {'name': 'Snowflake', 'icon': 'fas fa-snowflake'}
                ]
            },
            {
                'name': 'DevOps & Tools',
                'icon': 'fas fa-tools',
                'items': [
                    {'name': 'Docker', 'icon': 'fab fa-docker'},
                    {'name': 'Kubernetes', 'icon': 'fas fa-cube'},
                    {'name': 'Apache Airflow', 'icon': 'fas fa-wind'},
                    {'name': 'Git', 'icon': 'fab fa-git-alt'},
                    {'name': 'MySQL', 'icon': 'fas fa-database'}
                ]
            }
        ],
        'certifications': [
            {
                'name': 'Professional Machine Learning Engineer GCP',
                'icon': 'fas fa-certificate',
                'date': '2023',
                'link': 'https://www.credly.com/badges/3bbb4769-6512-43bb-b81b-44b54dc61e4d/public_url'
            },
            {
                'name': 'Google Cloud Associate Cloud Engineer',
                'icon': 'fas fa-certificate',
                'date': '2023',
                'link': 'https://www.credly.com/badges/86a5e5b2-5aa4-4ff8-bef8-9b8b73bf5982/public_url'
            },
            {
                'name': 'AWS Solution Architect Associate',
                'icon': 'fas fa-certificate',
                'date': '2023',
                'link': 'https://www.credly.com/badges/4e42ac26-5ce5-4664-ab05-55db7cd77ef9/public_url'
            }
        ]
    },
    'projects': [
        {
            'name': 'AI-Powered Fitness Tracker and Health Monitoring Bot',
            'description': 'Developed an AI-driven health monitoring bot using WHOOP API, Google Cloud, and LLMs, generating personalized insights with visualizations, reducing manual reporting by 15 hours per week, and improving user engagement.',
            'technologies': ['Python', 'GCP', 'Docker', 'LLM', 'Langchain'],
            'github': 'https://github.com/snr16/Whoop_bot'
        },
        {
            'name': 'Analysis of Adverse Drug Effects Using Big Data',
            'description': 'Streamlined an ELT pipeline with Apache Airflow to process 100GB of openFDA JSON data, optimizing Parquet-based storage and enhancing ML model performance, achieving 92% accuracy with a fine-tuned Multi-Layer Perceptron (MLP) model.',
            'technologies': ['Apache Airflow', 'MLFlow', 'DataBricks'],
            'github': 'https://github.com/snr16/drug-effects-analysis'
        },
        {
            'name': 'Multilabel Image Classification',
            'description': 'Designed and fine-tuned a ResNet-50 model for multi-label face attribute classification on the CelebA dataset, achieving 90% validation accuracy and a 20% F1-score boost through advanced hyperparameter tuning.',
            'technologies': ['Python', 'PyTorch', 'Sklearn', 'Pandas', 'CV2', 'PIL', 'Matplotlib'],
            'github': 'https://github.com/snr16/CelebA_multilabel_classification'
        },
        {
            'name': 'ConversationalAI with RAG & LLMs',
            'description': 'Engineered a context-aware chatbot leveraging Retrieval-Augmented Generation (RAG) with Cohere\'s Command R+, Meta\'s Llama-3, and Ollama\'s Gemma, optimizing knowledge retrieval and response accuracy. Crafted an interactive interface with Streamlit to promote accessibility.',
            'technologies': ['Python', 'LLM', 'Streamlit', 'Llamaindex'],
            'github': 'https://github.com/snr16/Chat-with-docs'
        },
         {
            'name': 'AI Mashup Generator',
            'description': 'Created an AI-powered music mashup tool that intelligently combines songs by analyzing tempo, key, and musical structure. Features high-quality audio separation, smart transitions, and automatic key/tempo matching, all accessible through a user-friendly Streamlit interface.',
            'technologies': ['Python', 'LLM', 'Streamlit', 'librosa', 'pydub', 'pyaudio'],
            'github': 'https://github.com/snr16/AI_mashup_generator'
        }
    ],
    'theme': {
        'colors': {
            'primary': '#00ff9d',
            'secondary': '#6c63ff',
            'accent': '#ff6b6b',
            'background': {
                'dark': '#0a192f',
                'light': '#112240',
                'lighter': '#1d3557'
            },
            'text': {
                'primary': '#e6f1ff',
                'secondary': '#8892b0'
            }
        },
        'font': {
            'family': 'Inter, sans-serif',
            'sizes': {
                'small': '0.875rem',
                'medium': '1rem',
                'large': '1.25rem',
                'xlarge': '2rem'
            }
        }
    },
    'resume_links': [
        {
            'name': 'ML Resume',
            'link': '/static/files/resume.pdf'
        },
        {
            'name': 'Data Science Resume',
            'link': '/static/files/resume_2.pdf'
        }
    ]
}

# Theme Configuration
THEME_CONFIG = {
    'primary_color': '#007bff',
    'secondary_color': '#6c757d',
    'background_color': '#ffffff',
    'text_color': '#212529',
    'font_family': 'Roboto, sans-serif'
} 