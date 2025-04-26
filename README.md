# Personal Portfolio

A modern, responsive portfolio website that generates a static site for GitHub Pages deployment.

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/snr16/niranjan.github.io.git
cd niranjan.github.io
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Customize your portfolio:
   - Edit `app/config.py` with your information
   - Add your profile image to `app/static/images/`
   - Add your resume(s) to `app/static/files/` (optional)
   - Update the theme colors in `app/static/css/style.css`

4. Generate static site:
```bash
python build.py
```
This will create an `index.html` file in the root directory with all your information from `config.py`.

## Project Structure

```
niranjan-portfolio/
├── app/
│   ├── templates/
│   │   ├── base.html          # Base template with layout
│   │   └── index.html         # Main content template
│   ├── static/
│   │   ├── css/              # CSS styles
│   │   ├── js/               # JavaScript files
│   │   ├── images/           # Image assets
│   │   └── files/            # Resume files
│   └── config.py             # Your portfolio content
├── build.py                  # Static site generator
├── .gitignore               # Git ignore rules
├── README.md                # Documentation
└── index.html              # Generated static site
```

## Configuration Guide

The main configuration file is `app/config.py`. This contains all your portfolio data:

### Personal Information
```python
PORTFOLIO_CONFIG = {
    'personal_info': {
        'name': 'Your Name',
        'title': 'Your Title/Role',
        'bio': 'Your Bio',
        'github': 'https://github.com/yourusername',
        'linkedin': 'https://linkedin.com/in/yourusername'
    }
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
        'technologies': ['Tech1', 'Tech2'],
        'github': 'https://github.com/yourusername/projectname',
        'image': '/static/images/project.jpg'  # Optional
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

## Resume Management

The resume feature is automatic based on PDF files in the `app/static/files/` directory:

1. Place your resume PDF files in `app/static/files/`
2. The website will automatically:
   - Show no button if no PDF files are present
   - Show a single download button if one PDF file is present
   - Show a dropdown menu if multiple PDF files are present
3. File names will be automatically formatted for display:
   - Spaces are preserved
   - Underscores are converted to spaces
   - The `.pdf` extension is removed
   - Each word is capitalized

Example:
- File: `software_engineer_resume.pdf` 
- Displays as: "Software Engineer Resume"

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
   `https://yourname.github.io/niranjan.github.io/`

## Contributing

Feel free to submit issues and enhancement requests!


