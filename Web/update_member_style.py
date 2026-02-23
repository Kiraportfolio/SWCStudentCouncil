import os

def main():
    filepath = '/Users/depa/Desktop/StudentSWC/Web/style.css'
    
    css_content = """

/* =========================================================================
   MEMBER CATEGORY RESTRUCTURING
   ========================================================================= */

.department-header {
    margin-top: 40px;
    margin-bottom: 25px;
    display: flex;
    align-items: center;
    gap: 15px;
}

.department-header h3 {
    font-size: 1.4rem;
    color: var(--color-primary-black);
    display: flex;
    align-items: center;
    gap: 12px;
    white-space: nowrap;
}

.dept-line {
    height: 2px;
    flex-grow: 1;
    background: linear-gradient(to right, rgba(0,0,0,0.1), transparent);
}

/* Adjust grid for single items */
.candidates-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
}
"""

    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(css_content)
        
    print("Appended member category styles to style.css successfully.")

if __name__ == "__main__":
    main()
