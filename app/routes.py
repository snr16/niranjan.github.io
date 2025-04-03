from flask import Blueprint, render_template, request, jsonify, current_app, flash, redirect, url_for
from flask_mail import Message
from .config import PORTFOLIO_CONFIG, THEME_CONFIG

main = Blueprint('main', __name__)

def init_app(app, mail):
    @main.route('/')
    def index():
        # Create a copy of the config data
        portfolio_data = PORTFOLIO_CONFIG.copy()
        
        return render_template('index.html', 
                             data=portfolio_data,
                             theme=THEME_CONFIG)

    @main.route('/about')
    def about():
        return render_template('index.html', data=PORTFOLIO_CONFIG, title='About')

    @main.route('/experience')
    def experience():
        return render_template('index.html', data=PORTFOLIO_CONFIG, title='Experience')

    @main.route('/projects')
    def projects():
        return render_template('index.html', data=PORTFOLIO_CONFIG, title='Projects')

    @main.route('/skills')
    def skills():
        return render_template('index.html', data=PORTFOLIO_CONFIG, title='Skills')

    @main.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')
            
            if not all([name, email, message]):
                flash('Please fill in all fields', 'error')
                return redirect(url_for('main.contact'))
            
            try:
                msg = Message(
                    subject=f"New Contact Form Submission from {name}",
                    recipients=[PORTFOLIO_CONFIG['personal_info']['email']],
                    body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
                )
                mail.send(msg)
                flash('Message sent successfully!', 'success')
            except Exception as e:
                flash('An error occurred. Please try again later.', 'error')
            
            return redirect(url_for('main.contact'))
        
        return render_template('index.html', data=PORTFOLIO_CONFIG, title='Contact')

def get_language_icon(language):
    icons = {
        'Python': 'fab fa-python',
        'Java': 'fab fa-java',
        'Go': 'fab fa-golang',
        'JavaScript': 'fab fa-js',
        'TypeScript': 'fab fa-js',
        'HTML': 'fab fa-html5',
        'CSS': 'fab fa-css3',
    }
    return icons.get(language, 'fas fa-code')

def get_tech_icon(tech):
    icons = {
        'React': 'fab fa-react',
        'Vue.js': 'fab fa-vuejs',
        'Node.js': 'fab fa-node-js',
        'Angular': 'fab fa-angular',
        'Docker': 'fab fa-docker',
        'AWS': 'fab fa-aws',
        'Streamlit': 'fas fa-chart-line',
    }
    return icons.get(tech, 'fas fa-laptop-code')

def get_tool_icon(tool):
    icons = {
        'Git': 'fab fa-git-alt',
        'Docker': 'fab fa-docker',
        'AWS': 'fab fa-aws',
        'GCP': 'fab fa-google',
        'Kubernetes': 'fas fa-dharmachakra',
        'Jenkins': 'fab fa-jenkins',
        'Kafka': 'fas fa-stream',
        'Airflow': 'fas fa-wind',
    }
    return icons.get(tool.lower(), 'fas fa-tools')

def get_cert_icon(cert):
    if 'google' in cert.lower():
        return 'fab fa-google'
    elif 'aws' in cert.lower():
        return 'fab fa-aws'
    elif 'azure' in cert.lower():
        return 'fab fa-microsoft'
    return 'fas fa-certificate'

@main.route('/parse-resume', methods=['POST'])
def parse_resume_route():
    if 'resume' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
        
    resume_file = request.files['resume']
    if resume_file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
        
    if not resume_file.filename.endswith('.pdf'):
        return jsonify({'error': 'Only PDF files are supported'}), 400
        
    # Save the file temporarily
    temp_path = os.path.join('uploads', resume_file.filename)
    resume_file.save(temp_path)
    
    try:
        # Parse the resume
        # parsed_data = parse_resume(temp_path)
        
        # Clean up
        os.remove(temp_path)
        
        return jsonify(parsed_data)
    except Exception as e:
        # Clean up in case of error
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return jsonify({'error': str(e)}), 500 