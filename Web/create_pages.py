import os
import re

def main():
    base_dir = '/Users/depa/Desktop/StudentSWC/Web'
    index_path = os.path.join(base_dir, 'index.html')
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into parts
    navbar_end = content.find('</nav>') + len('</nav>')
    footer_start = content.find('<!-- Footer -->')
    
    head_and_nav = content[:navbar_end]
    footer_and_scripts = content[footer_start:]

    # --- Personnel Page ---
    personnel_body = """
    <!-- Page Header -->
    <header class="page-header" style="padding-top: 150px; padding-bottom: 60px; text-align: center;">
        <div class="container">
            <h1 class="page-title"><span style="color: var(--color-primary-gold);">บุคลากร</span>ที่สำคัญ</h1>
            <p class="page-subtitle" style="color: white;">คณะครูอาจารย์และที่ปรึกษาสภานักเรียนโรงเรียนศรีวิชัยวิทยา</p>
        </div>
    </header>

    <section class="section" style="min-height: 40vh; display: flex; align-items: center; justify-content: center;">
        <div class="container" style="text-align: center;">
             <i class="fa-solid fa-person-digging" style="font-size: 4rem; color: var(--color-primary-gold); margin-bottom: 20px;"></i>
             <h2 style="color: white;">กำลังรวบรวมข้อมูลบุคลากร</h2>
             <p style="color: var(--color-text-muted); margin-top: 10px;">โปรดรอติดตามการอัปเดตข้อมูลในเร็วๆ นี้ครับ</p>
        </div>
    </section>
    """
    
    # Needs to ensure class="dark-theme" is on body if we want dark theme, but index.html isn't dark theme.
    # index.html has <body>. We can change it to <body class="dark-theme"> for these specific pages to match candidates.
    p_head = head_and_nav.replace('<title>สภานักเรียน - โรงเรียนศรีวิชัยวิทยา</title>', '<title>บุคลากรที่สำคัญ | Sriwichaiwittaya</title>')
    p_head = p_head.replace('<body>', '<body class="dark-theme">')
    
    with open(os.path.join(base_dir, 'personnel.html'), 'w', encoding='utf-8') as f:
        f.write(p_head + personnel_body + footer_and_scripts)


    # --- Directory Page ---
    directory_body = """
    <!-- Page Header -->
    <header class="page-header" style="padding-top: 150px; padding-bottom: 60px; text-align: center;">
        <div class="container">
            <h1 class="page-title"><span style="color: var(--color-primary-gold);">ทำเนียบ</span>สภานักเรียน</h1>
            <p class="page-subtitle" style="color: white;">ประวัติและรายนามคณะกรรมการสภานักเรียนโรงเรียนศรีวิชัยวิทยารุ่นต่างๆ</p>
        </div>
    </header>

    <section class="section" style="min-height: 40vh; display: flex; align-items: center; justify-content: center;">
        <div class="container" style="text-align: center;">
             <i class="fa-solid fa-clock-rotate-left" style="font-size: 4rem; color: var(--color-primary-gold); margin-bottom: 20px;"></i>
             <h2 style="color: white;">กำลังรวบรวมข้อมูลทำเนียบรุ่น</h2>
             <p style="color: var(--color-text-muted); margin-top: 10px;">โปรดรอติดตามการอัปเดตข้อมูลในเร็วๆ นี้ครับ</p>
        </div>
    </section>
    """
    
    d_head = head_and_nav.replace('<title>สภานักเรียน - โรงเรียนศรีวิชัยวิทยา</title>', '<title>ทำเนียบสภานักเรียน | Sriwichaiwittaya</title>')
    d_head = d_head.replace('<body>', '<body class="dark-theme">')
    
    with open(os.path.join(base_dir, 'directory.html'), 'w', encoding='utf-8') as f:
        f.write(d_head + directory_body + footer_and_scripts)

    print("Created personnel.html and directory.html successfully.")

if __name__ == "__main__":
    main()
