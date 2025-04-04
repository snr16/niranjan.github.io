# Personal Portfolio

A modern, responsive portfolio website that generates a static site for GitHub Pages deployment.

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/snr16/my-portifolio.git
cd my-portifolio
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Customize your portfolio:
   - Edit `app/config.py` with your information
   - Add your profile image to `static/images/`
   - Update the theme colors in `static/css/style.css`

4. Generate static site:
```bash
python build.py
```
This will create an `index.html` file in the root directory with all your information from `config.py`.

## Local Development

1. Set up your virtual environment (if not already done):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the development server:
```bash
python run.py
```

4. Open your browser and visit:
   - http://localhost:5000

The development server will automatically reload when you make changes to the code.

## Project Structure

```
niranjan-portfolio/
├── app/
│   ├── templates/
│   │   ├── base.html          # Base template with layout
│   │   └── index.html         # Main content template
│   ├── __init__.py            # Flask app initialization
│   ├── config.py              # Your portfolio content
│   └── routes.py              # Flask routes
├── static/                    # Static assets
│   ├── css/
│   │   └── style.css         # Custom styles
│   ├── js/
│   │   └── main.js           # Custom JavaScript
│   └── images/               # Image assets
├── build.py                  # Static site generator
├── .gitignore               # Git ignore rules
├── README.md                # Documentation
└── index.html              # Generated static site
```

## Deployment

1. After running `build.py`, commit and push your changes:
```bash
git add .
git commit -m "Update portfolio"
git push
```

2. Enable GitHub Pages:
   - Go to your repository settings
   - Navigate to "Pages"
   - Select the `main` branch as the source
   - Save the changes

3. Your portfolio will be available at:
   `https://snr16.github.io/my-portifolio/`

## Configuration Guide

The main configuration file is `app/config.py`. This contains all your portfolio data:

### Personal Information
```python
'personal_info': {
    'name': 'Your Name',
    'title': 'Your Title/Role',
    'bio': 'Your Bio',
    'github': 'https://github.com/yourusername',
    'linkedin': 'https://linkedin.com/in/yourusername'
}
```

### Education
```python
'education': [
    {
        'institution': 'University Name',
        'degree': 'Degree Name',
        'date': 'Start Date - End Date',
        'gpa': 'GPA'
    }
]
```

### Experience
```python
'experience': [
    {
        'company': 'Company Name',
        'position': 'Position Title',
        'date': 'Start Date - End Date',
        'achievements': [
            'Achievement 1',
            'Achievement 2'
        ]
    }
]
```

### Projects
```python
'projects': [
    {
        'name': 'Project Name',
        'description': 'Project description',
        'technologies': 'Technologies used',
        'github': 'https://github.com/yourusername/projectname'
    }
]
```

### Skills
```python
'skills': {
    'categories': [
        {
            'name': 'Category Name',
            'icon': 'fas fa-icon-name',
            'items': [
                {'name': 'Skill Name', 'icon': 'fab fa-icon-name'}
            ]
        }
    ],
    'certifications': [
        {
            'name': 'Certification Name',
            'icon': 'fas fa-certificate',
            'date': 'Year',
            'link': 'certification-url'
        }
    ]
}
```

## Contact Form

The contact form uses Formspree. To enable:
1. Create a form at https://formspree.io/
2. Add your form ID to the contact form in `index.html`

## Resume Management

To manage your resume files:
1. Place your resume files in `app/static/resumes/`
2. Update the resume links in `app/config.py`:
```python
'personal_info': {
    # ... other personal info ...
    'resumes': [
        {
            'name': 'Resume (Software Engineer)',
            'file': 'software_engineer_resume.pdf'
        },
        {
            'name': 'Resume (Data Scientist)',
            'file': 'data_scientist_resume.pdf'
        }
    ]
}
```
3. If you have multiple resumes, they will appear in a dropdown menu
4. If you have a single resume, it will appear as a direct download button

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.


