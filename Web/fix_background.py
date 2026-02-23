import os
import re

def main():
    filepath = '/Users/depa/Desktop/StudentSWC/Web/style.css'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The background is likely defaulting to something dark or transparent, or the gradient is still applying.
    # We will explicitly add a rule for the body element when NOT in dark-theme
    
    css_append = """

/* =========================================================================
   BASE LIGHT THEME OVERRIDES AND PRESIDENT CARD FIX 
   ========================================================================= */

/* Explicitly set light background for standard pages (like member.html) */
body:not(.dark-theme) {
    background-color: #ffffff; /* Explicit white background */
    color: var(--color-primary-black);
}

/* Fix President Section Background for Light Theme */
body:not(.dark-theme) .president-section {
    background: linear-gradient(135deg, rgba(255,255,255,1) 0%, rgba(245,245,245,1) 100%);
    position: relative;
    padding: 60px 20px;
    text-align: center;
}

body:not(.dark-theme) .president-section::before {
    /* override any dark radial gradients if they exist */
    display: none; 
}

/* Fix President Image Wrapper so it doesn't look like a giant black void */
body:not(.dark-theme) .president-image-wrapper {
    background-color: transparent;
    border-radius: var(--border-radius-lg);
    overflow: hidden;
    margin: 30px auto;
    position: relative;
    z-index: 2;
    transition: var(--transition-normal);
    max-width: 400px; /* Instead of filling full width or being huge */
    aspect-ratio: 3/4; /* Control the shape better */
    box-shadow: 0 10px 30px rgba(0,0,0,0.1); /* Lighter shadow for light theme */
    border: 1px solid var(--color-border);
}

body:not(.dark-theme) .president-image-wrapper::after {
    /* Remove any inner dark gradients from the dark theme */
    display: none;
}

body:not(.dark-theme) .president-image-wrapper img {
    border-radius: var(--border-radius-lg);
}

/* President button adjustment for light theme */
body:not(.dark-theme) .btn-president {
    background: var(--color-primary-green);
    color: white;
}

body:not(.dark-theme) .btn-president:hover {
    background: var(--color-primary-gold);
    color: var(--color-primary-black);
    box-shadow: 0 8px 25px rgba(255, 215, 0, 0.4);
}
"""

    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(css_append)
        
    print("Appended base light theme and President card fixes to style.css successfully.")

if __name__ == "__main__":
    main()
