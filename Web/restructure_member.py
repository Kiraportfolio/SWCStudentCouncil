import re
import os

def main():
    filepath = '/Users/depa/Desktop/StudentSWC/Web/member.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The new structured content
    new_structure = """
    <!-- Party Members Section -->
    <section class="members-section">
        <div class="container">
            <div class="members-header" style="margin-bottom: 50px;">
                <h2 style="color: var(--color-primary-black);">คณะกรรมการสภานักเรียน</h2>
                <div class="members-header-line"></div>
                <!-- Dropdown instruction -->
                <p style="color: var(--color-text-muted); margin-top: 15px;">แบ่งตามสายงาน</p>
            </div>

            <!-- Vice Presidents Category -->
            <div class="department-header">
                <h3><i class="fa-solid fa-user-group" style="color: var(--color-primary-gold);"></i> รองประธานนักเรียน</h3>
                <div class="dept-line"></div>
            </div>
            <div class="candidates-grid" style="margin-bottom: 40px;">
                <!-- Candidate 2 -->
                <div class="candidate-card" onclick="openCandidateModal(2)">
                    <div class="candidate-img-wrapper">
                        <img src="images/candidates/02_vice_1/2.png" alt="200">
                    </div>
                    <div class="candidate-info">
                        <span class="candidate-role">รองประธานนักเรียนคนที่ 1</span>
                        <h3 style="color: var(--color-primary-black);">นายณัธนนท์ วุ่นนา</h3>
                        <p class="candidate-motto">""</p>
                        <button class="btn-text">ดูประวัติ <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                </div>

                <!-- Candidate 3 -->
                <div class="candidate-card" onclick="openCandidateModal(3)">
                    <div class="candidate-img-wrapper">
                        <img src="images/candidates/03_vice_2/3.png" alt="200">
                    </div>
                    <div class="candidate-info">
                        <span class="candidate-role">รองประธานนักเรียนคนที่ 2</span>
                        <h3 style="color: var(--color-primary-black);">นางสาววิลาสินี ปู่สุข</h3>
                        <p class="candidate-motto">""</p>
                        <button class="btn-text">ดูประวัติ <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                </div>
            </div>

            <!-- Secretary Category -->
            <div class="department-header">
                <h3><i class="fa-solid fa-pen-nib" style="color: var(--color-primary-green);"></i> ฝ่ายเลขานุการ</h3>
                <div class="dept-line"></div>
            </div>
            <div class="candidates-grid" style="margin-bottom: 40px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); max-width: 400px; margin-left: auto; margin-right: auto;">
                <!-- Candidate 4 -->
                <div class="candidate-card" onclick="openCandidateModal(4)">
                    <div class="candidate-img-wrapper">
                        <img src="images/candidates/04_secretary/9.png" alt="200">
                    </div>
                    <div class="candidate-info">
                        <span class="candidate-role">คณะกรรมการฝ่ายเลขานุการ</span>
                        <h3 style="color: var(--color-primary-black);">นายจักพันธ์ โพธางาม</h3>
                        <p class="candidate-motto">""</p>
                        <button class="btn-text">ดูประวัติ <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                </div>
            </div>
            
            <!-- Public Relations Category -->
            <div class="department-header">
                <h3><i class="fa-solid fa-bullhorn" style="color: #3b82f6;"></i> ฝ่ายประชาสัมพันธ์</h3>
                <div class="dept-line"></div>
            </div>
            <div class="candidates-grid" style="margin-bottom: 40px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); max-width: 400px; margin-left: auto; margin-right: auto;">
                <!-- Candidate 5 -->
                <div class="candidate-card" onclick="openCandidateModal(5)">
                    <div class="candidate-img-wrapper">
                        <img src="images/candidates/05_pr/6.png" alt="200">
                    </div>
                    <div class="candidate-info">
                        <span class="candidate-role">คณะกรรมการฝ่ายประชาสัมพันธ์</span>
                        <h3 style="color: var(--color-primary-black);">นางสาวปุญญานันท์ สำราญจิตร์</h3>
                        <p class="candidate-motto">""</p>
                        <button class="btn-text">ดูประวัติ <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                </div>
            </div>
            
            <!-- Treasurer Category -->
            <div class="department-header">
                <h3><i class="fa-solid fa-coins" style="color: #eab308;"></i> ฝ่ายเหรัญญิก</h3>
                <div class="dept-line"></div>
            </div>
            <div class="candidates-grid" style="margin-bottom: 40px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); max-width: 400px; margin-left: auto; margin-right: auto;">
                <!-- Candidate 6 -->
                <div class="candidate-card" onclick="openCandidateModal(6)">
                    <div class="candidate-img-wrapper">
                        <img src="images/candidates/06_treasurer/10.png" alt=" 200">
                    </div>
                    <div class="candidate-info">
                        <span class="candidate-role">คณะกรรมการฝ่ายเหรัญญิก</span>
                        <h3 style="color: var(--color-primary-black);">นายเฉลิมชนม์ คนชม</h3>
                        <p class="candidate-motto">""</p>
                        <button class="btn-text">ดูประวัติ <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                </div>
            </div>

            <!-- Discipline Category -->
            <div class="department-header">
                <h3><i class="fa-solid fa-scale-balanced" style="color: #ef4444;"></i> ฝ่ายปกครอง</h3>
                <div class="dept-line"></div>
            </div>
            <div class="candidates-grid" style="margin-bottom: 40px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); max-width: 400px; margin-left: auto; margin-right: auto;">
                <!-- Candidate 7 -->
                <div class="candidate-card" onclick="openCandidateModal(7)">
                    <div class="candidate-img-wrapper">
                        <img src="images/candidates/07_discipline/5.png" alt=" 200">
                    </div>
                    <div class="candidate-info">
                        <span class="candidate-role">คณะกรรมการฝ่ายปกครอง</span>
                        <h3 style="color: var(--color-primary-black);">นายธนภัทร สุวรรณประดิษฐ์</h3>
                        <p class="candidate-motto">""</p>
                        <button class="btn-text">ดูประวัติ <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                </div>
            </div>

            <!-- Activities Category -->
            <div class="department-header">
                <h3><i class="fa-solid fa-calendar-star" style="color: #8b5cf6;"></i> ฝ่ายกิจกรรม</h3>
                <div class="dept-line"></div>
            </div>
            <div class="candidates-grid" style="margin-bottom: 40px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); max-width: 400px; margin-left: auto; margin-right: auto;">
                <!-- Candidate 8 -->
                <div class="candidate-card" onclick="openCandidateModal(8)">
                    <div class="candidate-img-wrapper">
                        <img src="images/candidates/08_activities/7.png" alt=" 200">
                    </div>
                    <div class="candidate-info">
                        <span class="candidate-role">คณะกรรมการฝ่ายกิจกรรม</span>
                        <h3 style="color: var(--color-primary-black);">นายธนดล แสงอรุณ</h3>
                        <p class="candidate-motto">""</p>
                        <button class="btn-text">ดูประวัติ <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                </div>
            </div>

            <!-- Academic Category -->
            <div class="department-header">
                <h3><i class="fa-solid fa-book-open-reader" style="color: #14b8a6;"></i> ฝ่ายวิชาการ</h3>
                <div class="dept-line"></div>
            </div>
            <div class="candidates-grid" style="margin-bottom: 40px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); max-width: 400px; margin-left: auto; margin-right: auto;">
                <!-- Candidate 9 -->
                <div class="candidate-card" onclick="openCandidateModal(9)">
                    <div class="candidate-img-wrapper">
                        <img src="images/candidates/09_academic/4.png" alt=" 200">
                    </div>
                    <div class="candidate-info">
                        <span class="candidate-role">คณะกรรมการฝ่ายวิชาการ</span>
                        <h3 style="color: var(--color-primary-black);">นางสาวณัชชาพัชร์ พุทธขันธ์</h3>
                        <p class="candidate-motto">""</p>
                        <button class="btn-text">ดูประวัติ <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                </div>
            </div>

            <!-- Host Category -->
            <div class="department-header">
                <h3><i class="fa-solid fa-handshake" style="color: #f97316;"></i> ฝ่ายปฏิคม</h3>
                <div class="dept-line"></div>
            </div>
            <div class="candidates-grid" style="margin-bottom: 40px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); max-width: 400px; margin-left: auto; margin-right: auto;">
                <!-- Candidate 10 -->
                <div class="candidate-card" onclick="openCandidateModal(10)">
                    <div class="candidate-img-wrapper">
                        <img src="images/candidates/10_host/8.png" alt="200">
                    </div>
                    <div class="candidate-info">
                        <span class="candidate-role">คณะกรรมการฝ่ายปฏิคม</span>
                        <h3 style="color: var(--color-primary-black);">นายศุภกฤษ์ หอมขจร</h3>
                        <p class="candidate-motto">""</p>
                        <button class="btn-text">ดูประวัติ <i class="fa-solid fa-arrow-right"></i></button>
                    </div>
                </div>
            </div>

        </div>
    </section>
    """

    # We need to replace the old "Party Members Section" with the new content
    import re
    # Match from <!-- Party Members Section --> up to the end of </section> for the members section
    pattern = re.compile(r'<!-- Party Members Section -->.*?</section>', re.DOTALL)
    
    # Check if we can find it
    if pattern.search(content):
        updated_content = pattern.sub(new_structure, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Updated member.html successfully.")
    else:
        print("Could not find Party Members Section in member.html to replace.")

if __name__ == "__main__":
    main()
