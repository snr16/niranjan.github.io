import os
import shutil
from flask import render_template, url_for
from app import create_app
from app.config import PORTFOLIO_CONFIG

def get_files(directory):
    """Get list of files in a directory."""
    try:
        return os.listdir(directory)
    except:
        return []

def copy_directory_recursively(src, dst):
    """Copy a directory recursively."""
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_directory_recursively(s, d)
        else:
            shutil.copy2(s, d)

def copy_static_files():
    """Copy static files to root directory."""
    # Create static directory if it doesn't exist
    os.makedirs('static', exist_ok=True)
    
    # Copy the entire static directory
    copy_directory_recursively('app/static', 'static')

def build_static_site():
    try:
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
                # Add get_files to template globals
                app.jinja_env.globals['get_files'] = get_files
                
                # Render the template with the config data
                rendered = render_template('index.html', data=PORTFOLIO_CONFIG)
                
                # Write the rendered template to index.html
                with open('index.html', 'w', encoding='utf-8') as f:
                    f.write(rendered)
                
                # Copy static files to root directory
                copy_static_files()
                
                print("✓ Static site built successfully!")
                
    except Exception as e:
        print(f"Error building site: {str(e)}")
        raise

if __name__ == '__main__':
    build_static_site() 