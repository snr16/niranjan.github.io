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
   - Add your profile image to `app/static/images/`
   - Update the theme colors in the config file

4. Run locally:
```bash
python app.py
```

5. Build static files:
```bash
python build.py
```

## Deployment

1. Push your changes to GitHub:
```bash
git add .
git commit -m "Update portfolio"
git push
```

2. Enable GitHub Pages:
   - Go to your repository settings
   - Navigate to "Pages"
   - Select the `gh-pages` branch as the source
   - Save the changes

3. Your portfolio will be available at:
   `https://snr16.github.io/my-portifolio/`

## Detailed Customization Guide

### 1. Configuration File Updates

The main configuration file is `app/config.py`. This file contains all the data that will be displayed on your portfolio.

#### Personal Information
```python
'personal_info': {
    'name': 'Your Name',
    'title': 'Your Title/Role',
    'bio': 'Your Bio',
    'email': 'your.email@example.com',
    'phone': 'Your Phone',
    'location': 'Your Location',
    'github': 'https://github.com/yourusername',
    'linkedin': 'https://linkedin.com/in/yourusername'
}
```

#### Education
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

#### Experience
```python
'experience': [
    {
        'company': 'Company Name',
        'position': 'Position Title',
        'date': 'Start Date - End Date',
        'achievements': [
            'Achievement 1',
            'Achievement 2',
            'Achievement 3'
        ]
    }
]
```

#### Skills
```python
'skills': {
    'categories': [
        {
            'name': 'Programming Languages',
            'icon': 'fas fa-code',
            'items': [
                {'name': 'Python', 'icon': 'fab fa-python'},
                {'name': 'JavaScript', 'icon': 'fab fa-js'},
                {'name': 'Java', 'icon': 'fab fa-java'}
            ]
        }
    ],
    'certifications': [
        {
            'name': 'Certification Name',
            'icon': 'fas fa-certificate',
            'date': 'Year',
            'link': 'https://www.credential.net/your-credential-id'
        }
    ]
}
```

#### Projects
```python
'projects': [
    {
        'name': 'Project Name',
        'description': 'A brief description of the project, what it does, and your role in it.',
        'technologies': 'Technologies used (e.g., Python, Flask, React, MongoDB)',
        'github': 'https://github.com/yourusername/projectname'
    }
]
```

### 2. Adding a Profile Image

1. Create the images directory if it doesn't exist:
```bash
mkdir -p app/static/images
```

2. Place your profile image in the `app/static/images/` directory
   - Make sure your image is square and at least 300x300 pixels for best results
   - Supported formats: JPG, PNG, WebP

### 3. Theme Customization

#### Colors
Edit `app/static/css/style.css` to customize colors:

```css
:root {
    --primary-color: #00ff9d;
    --secondary-color: #6c63ff;
    --accent-color: #ff6b6b;
    --background-dark: #0a192f;
    --background-light: #112240;
    --text-primary: #e6f1ff;
    --text-secondary: #8892b0;
}
```

#### Fonts
To change the font, update the `font-family` property in `app/static/css/style.css`:

```css
body {
    font-family: 'Your Preferred Font', sans-serif;
}
```

### 4. Adding Project Images

1. Place your project images in the `app/static/images/projects/` directory
2. Update the project image paths in `app/templates/index.html`

### 5. Project Structure

```
portfolio-website/
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/
│   │       └── your-profile-image.jpg
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   ├── __init__.py
│   ├── config.py
│   └── routes.py
├── requirements.txt
└── app.py
```

## Resume Parsing

The portfolio can parse information from your resume. Supported formats:
- PDF
- DOCX
- TXT

Information parsed includes:
- Personal details
- Education history
- Work experience
- Skills
- Projects

## Contact Form

The contact form is powered by Flask-Mail. To enable:
1. Set up your email configuration in `app/config.py`
2. Add environment variables for email credentials
3. Test the form locally before deployment

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

