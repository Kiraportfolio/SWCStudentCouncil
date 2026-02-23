import os
import re
import glob

def main():
    base_dir = '/Users/depa/Desktop/StudentSWC/Web'
    index_path = os.path.join(base_dir, 'index.html')
    
    with open(index_path, 'r', encoding='utf-8') as f:
        index_content = f.read()
        
    nav_match = re.search(r'(<!-- Navbar -->\s*<nav class="navbar(?:s)?">.*?</nav>)', index_content, re.DOTALL)
    if not nav_match:
        nav_match = re.search(r'(<nav class="navbar(?:s)?">.*?</nav>)', index_content, re.DOTALL)
    nav_content = nav_match.group(1)

    footer_fab_match = re.search(r'(<!-- Footer -->.*?)<script', index_content, re.DOTALL)
    footer_fab_content = footer_fab_match.group(1)

    html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)
    
    for filepath in html_files:
        if os.path.abspath(filepath) == os.path.abspath(index_path):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace Navbar
        content = re.sub(r'<!-- Navbar -->\s*<nav class="navbar.*?">.*?</nav>', nav_content, content, flags=re.DOTALL)
        content = re.sub(r'<nav class="navbar.*?">.*?</nav>', nav_content, content, flags=re.DOTALL)

        # Replace Footer up to script
        content = re.sub(r'<!-- Footer -->.*?(?=<script)', footer_fab_content, content, flags=re.DOTALL)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print(f"Updated {len(html_files)-1} files.")

if __name__ == "__main__":
    main()
