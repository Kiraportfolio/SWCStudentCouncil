import os

def main():
    filepath = '/Users/depa/Desktop/StudentSWC/Web/style.css'
    
    css_content = """

/* =========================================================================
   HOMEPAGE REDESIGN STYLES
   ========================================================================= */

/* Hero Redesign Enhancements */
.hero {
    position: relative;
    overflow: hidden;
    background: radial-gradient(circle at 10% 20%, rgba(32, 99, 63, 0.05) 0%, transparent 20%),
                radial-gradient(circle at 90% 80%, rgba(255, 215, 0, 0.05) 0%, transparent 20%);
}

.hero-tagline {
    display: inline-block;
    padding: 8px 16px;
    background: rgba(32, 99, 63, 0.1);
    color: var(--color-primary-green);
    border-radius: 50px;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 20px;
    letter-spacing: 1px;
}

.hero-shape {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    z-index: -1;
    opacity: 0.5;
}

.hero-shape-1 {
    width: 300px;
    height: 300px;
    background: var(--color-primary-green);
    top: -50px;
    right: -50px;
}

.hero-shape-2 {
    width: 250px;
    height: 250px;
    background: var(--color-primary-gold);
    bottom: -50px;
    left: -50px;
}

/* Sections & Typography */
.bg-light {
    background-color: var(--color-bg-light);
}

.section {
    padding: 80px 0;
}

.mb-4 { margin-bottom: 1.5rem; }
.mb-5 { margin-bottom: 3rem; }
.mt-4 { margin-top: 1.5rem; }
.text-center { text-align: center; }

.section-title {
    font-size: 2.2rem;
    color: var(--color-text-main);
    margin-bottom: 10px;
}

.section-title.text-white {
    color: white;
}

.highlight-text {
    color: var(--color-primary-green);
}

.highlight-gold {
    color: var(--color-primary-gold);
}

.section-subtitle {
    color: var(--color-text-muted);
    font-size: 1.1rem;
}

.text-gold { color: var(--color-primary-gold); }
.text-green { color: var(--color-primary-green); }
.text-blue { color: #3b82f6; }
.text-red { color: #ef4444; }
.text-white { color: white; }
.text-white-80 { color: rgba(255, 255, 255, 0.8); }

.bg-green-light { background: rgba(32, 99, 63, 0.1); }
.bg-gold-light { background: rgba(255, 215, 0, 0.15); }
.bg-blue-light { background: rgba(59, 130, 246, 0.1); }
.bg-red-light { background: rgba(239, 68, 68, 0.1); }

/* Updates Section */
.updates-grid {
    display: grid;
    grid-template-columns: 3fr 2fr;
    gap: 40px;
}

.column-title {
    font-size: 1.3rem;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.news-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
}

.news-card {
    background: white;
    border-radius: var(--border-radius-md);
    padding: 20px;
    display: flex;
    gap: 20px;
    box-shadow: var(--shadow-sm);
    transition: var(--transition-normal);
    border: 1px solid var(--color-border);
}

.news-card:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-md);
    border-color: rgba(32, 99, 63, 0.2);
}

.news-date {
    background: var(--color-bg-light);
    color: var(--color-primary-green);
    font-weight: 700;
    padding: 10px 15px;
    border-radius: var(--border-radius-sm);
    text-align: center;
    min-width: 80px;
    height: fit-content;
}

.news-content h4 {
    margin-bottom: 8px;
    font-size: 1.1rem;
}

.news-content p {
    color: var(--color-text-muted);
    font-size: 0.95rem;
    margin-bottom: 12px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.read-more {
    color: var(--color-primary-green);
    font-weight: 600;
    font-size: 0.9rem;
    display: inline-flex;
    align-items: center;
    gap: 5px;
}

.read-more:hover {
    color: #144629;
    gap: 8px; /* Micro animation on hover */
}

/* Featured Event */
.event-featured {
    background: white;
    border-radius: var(--border-radius-md);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--color-border);
    transition: var(--transition-normal);
}

.event-featured:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-3px);
}

.event-poster-placeholder {
    height: 160px;
    background: linear-gradient(135deg, var(--color-primary-green), #144629);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 1.2rem;
    font-weight: 700;
    gap: 10px;
}

.event-poster-placeholder i {
    font-size: 2.5rem;
    color: var(--color-primary-gold);
}

.event-details {
    padding: 24px;
}

.event-details h4 {
    font-size: 1.2rem;
    margin-bottom: 12px;
}

.event-details p {
    color: var(--color-text-muted);
    margin-bottom: 8px;
    font-size: 0.95rem;
    display: flex;
    align-items: center;
    gap: 8px;
}

.event-countdown {
    margin-top: 20px;
    display: flex;
    align-items: center;
    gap: 8px;
    background: var(--color-bg-light);
    padding: 12px;
    border-radius: var(--border-radius-sm);
    justify-content: center;
    font-weight: bold;
}

.cd-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: white;
    padding: 5px 10px;
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.cd-box strong {
    font-size: 1.2rem;
    color: var(--color-primary-green);
    line-height: 1;
}

.cd-box small {
    font-size: 0.7rem;
    color: var(--color-text-muted);
    font-weight: normal;
}

/* Student Voice Section */
.student-voice-section {
    background: linear-gradient(135deg, #111 0%, #222 100%);
    position: relative;
    overflow: hidden;
}

.student-voice-section::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: url('data:image/svg+xml;utf8,<svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="2" cy="2" r="2" fill="rgba(255,255,255,0.05)"/></svg>');
}

.voice-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
    position: relative;
    z-index: 2;
}

.status-stats {
    display: flex;
    gap: 30px;
    margin-top: 15px;
}

.stat-item {
    display: flex;
    flex-direction: column;
}

.stat-num {
    font-size: 2.5rem;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 5px;
}

.stat-label {
    color: rgba(255, 255, 255, 0.6);
    font-size: 0.85rem;
}

.voice-form-wrapper {
    background: white;
    border-radius: var(--border-radius-lg);
    padding: 32px;
    box-shadow: var(--shadow-lg);
}

.voice-form h3 {
    margin-bottom: 20px;
    font-size: 1.5rem;
    text-align: center;
}

.form-group {
    margin-bottom: 16px;
}

.form-group label {
    display: block;
    margin-bottom: 6px;
    font-weight: 500;
    font-size: 0.9rem;
    color: var(--color-text-main);
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 12px 16px;
    border: 1px solid var(--color-border);
    border-radius: var(--border-radius-sm);
    font-family: inherit;
    font-size: 0.95rem;
    transition: var(--transition-fast);
    background: var(--color-bg-light);
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--color-primary-green);
    background: white;
    box-shadow: 0 0 0 3px rgba(32, 99, 63, 0.1);
}

/* Quick Links Section */
.quick-links-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
}

.quick-link-card {
    background: white;
    padding: 24px;
    border-radius: var(--border-radius-md);
    text-align: center;
    transition: var(--transition-normal);
    border: 1px solid var(--color-border);
    box-shadow: var(--shadow-sm);
    display: flex;
    flex-direction: column;
    align-items: center;
}

.quick-link-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-md);
    border-color: var(--color-primary-green);
}

.icon-wrapper {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    margin-bottom: 16px;
    transition: var(--transition-normal);
}

.quick-link-card:hover .icon-wrapper {
    transform: scale(1.1);
}

.quick-link-card h4 {
    font-size: 1.1rem;
    margin-bottom: 8px;
    color: var(--color-text-main);
}

.quick-link-card p {
    font-size: 0.85rem;
    color: var(--color-text-muted);
}

/* Responsive Adjustments */
@media (max-width: 900px) {
    .updates-grid,
    .voice-wrapper {
        grid-template-columns: 1fr;
    }
    .quick-links-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 600px) {
    .news-card {
        flex-direction: column;
        gap: 12px;
    }
    .news-date {
        align-self: flex-start;
    }
    .quick-links-grid {
        grid-template-columns: 1fr;
    }
    .status-stats {
        flex-direction: column;
        gap: 15px;
    }
}
"""

    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(css_content)
        
    print("Appended new styles to style.css successfully.")

if __name__ == "__main__":
    main()
