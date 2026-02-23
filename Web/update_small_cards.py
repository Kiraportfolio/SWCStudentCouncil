import os

def main():
    filepath = '/Users/depa/Desktop/StudentSWC/Web/style.css'
    
    css_content = """

/* =========================================================================
   MEMBER CATEGORY & LIGHT THEME REFINEMENTS
   ========================================================================= */

/* Dark text for President section in light theme */
body:not(.dark-theme) .president-label {
    background: var(--color-primary-green);
    color: white; /* Keep label text white, but background green instead of dark */
}

body:not(.dark-theme) .president-quote {
    color: var(--color-primary-black);
}

body:not(.dark-theme) .members-header h2 {
    color: var(--color-primary-black);
}

body:not(.dark-theme) .members-header p {
    color: var(--color-text-muted);
}

/* Adjust candidate cards to be smaller */
.candidates-grid {
    display: grid;
    /* Reduced minmax from 280px to 220px to allow more/smaller cards per row */
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px; /* slightly smaller gap */
}

/* Specific grids for departments to center their cards when there are only 1-2 */
.candidates-grid.department-grid {
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    max-width: 600px; /* Allow up to ~2 cards to center nicely */
    margin-left: auto;
    margin-right: auto;
    justify-content: center;
}

.candidate-card {
    background: white;
    border-radius: var(--border-radius-md);
    padding: 15px; /* Reduced from 20px */
    text-align: center;
    transition: var(--transition-normal);
    border: 1px solid var(--color-border);
    box-shadow: var(--shadow-sm);
}

.candidate-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-md);
    border-color: var(--color-primary-green);
}

.candidate-img-wrapper {
    /* Reduced size */
    width: 150px;
    height: 150px;
    margin: 0 auto 15px;
    border-radius: 50%;
    overflow: hidden;
    position: relative;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.candidate-img-wrapper img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: var(--transition-normal);
}

.candidate-card:hover .candidate-img-wrapper img {
    transform: scale(1.05); /* Slight zoom on hover instead of 1.1 */
}

.candidate-role {
    display: inline-block;
    color: var(--color-primary-green);
    font-size: 0.8rem; /* smaller font */
    font-weight: 700;
    margin-bottom: 5px;
    letter-spacing: 0.5px;
}

.candidate-info h3 {
    color: var(--color-text-main);
    font-size: 1.1rem; /* slightly smaller name */
    margin-bottom: 5px;
}

.candidate-motto {
    color: var(--color-text-muted);
    font-size: 0.85rem;
    font-style: italic;
    margin-bottom: 12px;
}

/* Force dark text on candidate names in light mode just in case */
body:not(.dark-theme) .candidate-info h3 {
    color: var(--color-primary-black);
}

body:not(.dark-theme) .candidate-role {
    color: var(--color-primary-green);
}
"""

    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(css_content)
        
    print("Appended smaller card styles to style.css successfully.")

if __name__ == "__main__":
    main()
