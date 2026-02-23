import os
import re
import glob

def main():
    base_dir = '/Users/depa/Desktop/StudentSWC/Web'
    html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)
    
    favicon_tag = '    <link rel="icon" href="images/council.jpg" type="image/jpeg">\n'
    
    for filepath in html_files:
        if os.path.basename(filepath) == 'index.html':
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if '<link rel="icon"' not in content:
            # Insert after <title>
            content = re.sub(r'(</title>\s*)', r'\1' + favicon_tag, content, count=1)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
    print("Favicon added to all HTML files.")

if __name__ == "__main__":
    main()
