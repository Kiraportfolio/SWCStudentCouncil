import re
import os

def main():
    filepath = '/Users/depa/Desktop/StudentSWC/Web/index.html'
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_hero_and_sections = """
    <!-- Hero Section -->
    <section class="hero">
        <div class="container hero-content">
            <div class="hero-tagline">#รับฟังทุกเสียง #สร้างสรรค์ทุกโอกาส</div>
            <h1 class="hero-title">
                เพราะโรงเรียนที่ดี<br>
                เริ่มจากการ <span style="color: var(--color-primary-red);">กล้าลอง</span>
            </h1>
            <div class="hero-image-wrapper">
                <img src="images/Us.png" alt="กล้านำ ทำจริง - Sriwichaiwittaya" class="hero-subtitle-image">
            </div>

            <div class="hero-actions">
                <a href="#student-voice" class="btn btn-primary" style="background: linear-gradient(135deg, var(--color-primary-gold), #DAA520); color: black;">
                    <i class="fa-solid fa-bullhorn"></i> ร้องเรียน/เสนอแนะ
                </a>
                <a href="#quick-links" class="btn btn-secondary">
                    <i class="fa-solid fa-calendar-days"></i> ปฏิทินกิจกรรม
                </a>
            </div>
        </div>
        
        <!-- Animated Background Elements -->
        <div class="hero-shape hero-shape-1"></div>
        <div class="hero-shape hero-shape-2"></div>
    </section>

    <!-- Latest Updates Section (News & Events) -->
    <section class="section updates-section bg-light" id="updates">
        <div class="container">
            <div class="section-header text-center mb-5">
                <h2 class="section-title">ความเคลื่อนไหว<span class="highlight-text">ล่าสุด</span></h2>
                <p class="section-subtitle">ติดตามข่าวสารและกิจกรรมที่น่าสนใจจากสภานักเรียน</p>
            </div>
            
            <div class="updates-grid">
                <!-- News Column -->
                <div class="news-column">
                    <h3 class="column-title"><i class="fa-solid fa-newspaper text-gold"></i> ข่าวประชาสัมพันธ์</h3>
                    <div class="news-list">
                        <div class="news-card">
                            <div class="news-date">15 ก.พ.</div>
                            <div class="news-content">
                                <h4>ประกาศรับสมัครคณะกรรมการชุดใหม่</h4>
                                <p>เปิดรับสมัครนักเรียนเพื่อร่วมเป็นส่วนหนึ่งของสภานักเรียนประจำปีการศึกษา 2569...</p>
                                <a href="news.html" class="read-more">อ่านต่อ <i class="fa-solid fa-arrow-right"></i></a>
                            </div>
                        </div>
                        <div class="news-card">
                            <div class="news-date">10 ก.พ.</div>
                            <div class="news-content">
                                <h4>สรุปผลการแข่งขันกีฬาภายใน</h4>
                                <p>ภาพบรรยากาศและสรุปเหรียญรางวัลการแข่งขันกีฬาสีประจำปีที่ผ่านมา...</p>
                                <a href="news.html" class="read-more">อ่านต่อ <i class="fa-solid fa-arrow-right"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Events Column -->
                <div class="events-column">
                    <h3 class="column-title"><i class="fa-solid fa-calendar-check text-green"></i> กิจกรรมเร็วๆ นี้</h3>
                    <div class="event-featured">
                        <div class="event-poster-placeholder">
                            <i class="fa-solid fa-music"></i>
                            <span>SWC Music Contest 2026</span>
                        </div>
                        <div class="event-details">
                            <h4>ประกวดวงดนตรีสากล</h4>
                            <p><i class="fa-regular fa-clock"></i> 28 กุมภาพันธ์ 2569 | 15:30 น.</p>
                            <p><i class="fa-solid fa-location-dot"></i> หอประชุมใหญ่</p>
                            
                            <!-- Countdown Mini -->
                            <div class="event-countdown">
                                <span class="cd-box"><strong id="cd-days">08</strong><small>วัน</small></span>:
                                <span class="cd-box"><strong id="cd-hours">12</strong><small>ชม.</small></span>:
                                <span class="cd-box"><strong id="cd-mins">45</strong><small>นาที</small></span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Student Voice Section -->
    <section class="section student-voice-section" id="student-voice">
        <div class="container">
            <div class="voice-wrapper">
                <div class="voice-content">
                    <h2 class="section-title text-white">ทุกเสียง<span class="highlight-gold">มีความหมาย</span></h2>
                    <p class="text-white-80">มีปัญหา เสนอแนะ หรืออยากให้สภานักเรียนช่วยอะไร? บอกเราได้เลยที่นี่ ทุกข้อความจะถูกนำไปพิจารณาอย่างจริงจัง</p>
                    
                    <div class="tracking-status mt-4">
                        <h4>สถานะการดำเนินงานปัจจุบัน</h4>
                        <div class="status-stats">
                            <div class="stat-item">
                                <span class="stat-num text-gold">42</span>
                                <span class="stat-label">เรื่องที่รับแจัง</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-num text-white">35</span>
                                <span class="stat-label">แก้ไขแล้ว</span>
                            </div>
                            <div class="stat-item">
                                <span class="stat-num text-white">7</span>
                                <span class="stat-label">กำลังดำเนินการ</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="voice-form-wrapper">
                    <form class="voice-form" action="#" method="POST" onsubmit="event.preventDefault(); alert('ขอบคุณสำหรับความคิดเห็น! ระบบกำลังบันทึกข้อมูล');">
                        <h3>ส่งข้อเสนอแนะ</h3>
                        <div class="form-group">
                            <label>หัวข้อเรือง</label>
                            <input type="text" placeholder="เช่น ขอให้ซ่อมพัดลมโรงอาหาร" required>
                        </div>
                        <div class="form-group">
                            <label>หมวดหมู่</label>
                            <select required>
                                <option value="" disabled selected>เลือกหมวดหมู่...</option>
                                <option value="facility">อาคารสถานที่/สิ่งอำนวยความสะดวก</option>
                                <option value="academic">วิชาการ/การเรียนการสอน</option>
                                <option value="activity">กิจกรรม/ชมรม</option>
                                <option value="other">อื่นๆ</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label>รายละเอียด</label>
                            <textarea rows="4" placeholder="อธิบายปัญหาหรือข้อเสนอแนะของคุณ..." required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary w-100">ส่งข้อความ <i class="fa-solid fa-paper-plane"></i></button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Quick Links Section -->
    <section class="section quick-links-section bg-light" id="quick-links">
        <div class="container">
            <div class="section-header text-center mb-4">
                <h2 class="section-title">เข้าถึง<span class="highlight-text">รวดเร็ว</span></h2>
            </div>
            
            <div class="quick-links-grid">
                <a href="#" class="quick-link-card">
                    <div class="icon-wrapper bg-green-light">
                        <i class="fa-solid fa-calendar-alt text-green"></i>
                    </div>
                    <h4>ปฏิทินวิชาการ</h4>
                    <p>ดาวน์โหลดปฏิทินปีการศึกษา</p>
                </a>
                
                <a href="#" class="quick-link-card">
                    <div class="icon-wrapper bg-gold-light">
                        <i class="fa-solid fa-utensils text-gold"></i>
                    </div>
                    <h4>เมนูอาหารกลางวัน</h4>
                    <p>ดูรายการอาหารสัปดาห์นี้</p>
                </a>
                
                <a href="#" class="quick-link-card">
                    <div class="icon-wrapper bg-blue-light">
                        <i class="fa-solid fa-shirt text-blue"></i>
                    </div>
                    <h4>ระเบียบการแต่งกาย</h4>
                    <p>คู่มือการแต่งกายที่ถูกต้อง</p>
                </a>
                
                <a href="#" class="quick-link-card">
                    <div class="icon-wrapper bg-red-light">
                        <i class="fa-solid fa-bullhorn text-red"></i>
                    </div>
                    <h4>แจ้งซ่อม/ปัญหา</h4>
                    <p>ระบบแจ้งซ่อมออนไลน์</p>
                </a>
            </div>
        </div>
    </section>
    """

    # We need to replace the old Hero section with the new content
    import re
    # Match from <!-- Hero Section --> up to the end of </section> for the hero
    pattern = re.compile(r'<!-- Hero Section -->.*?</section>', re.DOTALL)
    
    # Check if we can find it
    if pattern.search(content):
        updated_content = pattern.sub(new_hero_and_sections, content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("Updated index.html successfully.")
    else:
        print("Could not find Hero Section in index.html to replace.")

if __name__ == "__main__":
    main()
