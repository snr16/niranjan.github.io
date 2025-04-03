import os
from flask import render_template
from app import create_app
from app.config import PORTFOLIO_CONFIG

def build_static_site():
    # Create Flask app
    app, _ = create_app()
    
    # Create a test request context
    with app.test_request_context():
        with app.app_context():
            # Render the template with the config data
            rendered = render_template('index.html', data=PORTFOLIO_CONFIG)
            
            # Write the rendered template to index.html
            with open('index.html', 'w') as f:
                f.write(rendered)
            
            print("Static site built successfully!")

if __name__ == '__main__':
    build_static_site() 