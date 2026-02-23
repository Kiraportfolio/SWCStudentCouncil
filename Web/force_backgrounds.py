import re

def main():
    filepath = '/Users/depa/Desktop/StudentSWC/Web/style.css'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The block we appended last time started with:
    # /* =========================================================================
    #    BASE LIGHT THEME OVERRIDES AND PRESIDENT CARD FIX 
    #    ========================================================================= */

    # We will replace that entire block with a more robust one that includes .members-section

    replacement = """
/* =========================================================================
   BASE LIGHT THEME OVERRIDES AND PRESIDENT CARD FIX 
   ========================================================================= */

/* Explicitly set light background for standard pages (like member.html) */
body:not(.dark-theme) {
    background: #ffffff !important;
    color: var(--color-primary-black);
}

/* Fix President Section Background for Light Theme */
body:not(.dark-theme) .president-section {
    background: linear-gradient(135deg, rgba(255,255,255,1) 0%, rgba(245,245,245,1) 100%) !important;
    position: relative;
    padding: 60px 20px;
    text-align: center;
}

body:not(.dark-theme) .president-section::before {
    display: none !important; 
}

/* Fix Party Members Section Background for Light Theme */
body:not(.dark-theme) .members-section {
    background: #ffffff !important;
    padding: 60px 0 80px;
}

body:not(.dark-theme) .members-section::before {
    display: none !important;
}

/* Fix President Image Wrapper so it doesn't look like a giant black void */
body:not(.dark-theme) .president-image-wrapper {
    background: transparent !important;
    border-radius: var(--border-radius-lg);
    overflow: hidden;
    margin: 30px auto;
    position: relative;
    z-index: 2;
    transition: var(--transition-normal);
    max-width: 300px !important; /* Made even smaller to match cards */
    aspect-ratio: 3/4;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
    border: 1px solid var(--color-border) !important;
}

body:not(.dark-theme) .president-image-wrapper::before,
body:not(.dark-theme) .president-image-wrapper::after {
    display: none !important;
}

body:not(.dark-theme) .president-image-wrapper img {
    border-radius: var(--border-radius-lg);
    object-position: top;
}

/* President button adjustment for light theme */
body:not(.dark-theme) .btn-president {
    background: var(--color-primary-green) !important;
    color: white !important;
    border-color: var(--color-primary-green) !important;
}

body:not(.dark-theme) .btn-president:hover {
    background: var(--color-primary-gold) !important;
    color: var(--color-primary-black) !important;
    border-color: var(--color-primary-gold) !important;
    box-shadow: 0 8px 25px rgba(255, 215, 0, 0.4) !important;
}
"""

    # We will search for the old block and replace it, or if not found, just append
    pattern = re.compile(r'/\* =========================================================================\n   BASE LIGHT THEME OVERRIDES AND PRESIDENT CARD FIX \n   =========================================================================\s*\*/.*?$', re.DOTALL)
    
    if pattern.search(content):
        updated_content = pattern.sub(replacement.strip(), content)
    else:
        updated_content = content + "\n\n" + replacement.strip()

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print("Updated light theme backgrounds with specific overrides in style.css")

if __name__ == "__main__":
    main()
