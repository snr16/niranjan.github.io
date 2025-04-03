import os
from flask import render_template, url_for
from app import create_app
from app.config import PORTFOLIO_CONFIG

def build_static_site():
    # Create Flask app
    app, _ = create_app()
    
    # Create a test request context
    with app.test_request_context():
        with app.app_context():
            # Override url_for to use relative paths
            def relative_url_for(endpoint, **values):
                if endpoint == 'static':
                    return f"static/{values['filename']}"
                return url_for(endpoint, **values)
            
            app.jinja_env.globals['url_for'] = relative_url_for
            
            # Render the template with the config data
            rendered = render_template('index.html', data=PORTFOLIO_CONFIG)
            
            # Write the rendered template to index.html
            with open('index.html', 'w') as f:
                f.write(rendered)
            
            print("Static site built successfully!")

if __name__ == '__main__':
    build_static_site() 