import base64, os

# Read images
def get_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

logo_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\.gemini\antigravity\brain\c200eeb1-5eb2-4df8-a23c-4225cec1b3ae\media__1773310644442.jpg")
play_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\.gemini\antigravity\brain\c200eeb1-5eb2-4df8-a23c-4225cec1b3ae\media__1773310650794.jpg")

html = f'''<!DOCTYPE html>
<html lang="hi-Latn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
<title>PayEcho – UPI Mobile Soundbox | Free UPI Payment Voice Alert App</title>
<meta name="description" content="PayEcho aapke phone ko smart UPI Soundbox bana deta hai. Har payment par awaaz mein alert! Free download karo Google Play se.">
<link rel="icon" type="image/jpeg" href="data:image/jpeg;base64,{logo_b64}">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&family=Noto+Sans+Devanagari:wght@400;600;700&display=swap" rel="stylesheet">
<style>
/* ===== RESET & BASE ===== */
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
html{{scroll-behavior:smooth;font-size:16px;}}
body{{font-family:'Poppins',sans-serif;color:#0D1B2A;background:#F0F7FF;overflow-x:hidden;-webkit-text-size-adjust:100%;}}
.hindi{{font-family:'Noto Sans Devanagari','Poppins',sans-serif;}}
img{{max-width:100%;display:block;height:auto;}}
a{{text-decoration:none;color:inherit;}}

/* ===== REVEAL ANIMATION ===== */
.reveal{{opacity:0;transform:translateY(40px);transition:opacity .7s ease,transform .7s ease;}}
.reveal.visible{{opacity:1;transform:translateY(0);}}

/* ===== NAVBAR ===== */
.navbar{{position:fixed;top:0;left:0;width:100%;z-index:1000;background:rgba(21,101,192,.97);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);padding:10px 0;transition:box-shadow .3s,padding .3s;}}
.navbar.scrolled{{box-shadow:0 4px 20px rgba(0,0,0,.3);padding:6px 0;}}
.nav-inner{{max-width:1200px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:0 20px;}}
.nav-brand{{display:flex;align-items:center;gap:10px;flex-shrink:0;}}
.nav-brand img{{width:36px;height:36px;border-radius:8px;}}
.nav-brand span{{font-size:1.2rem;font-weight:800;color:#fff;}}
.nav-brand .echo{{color:#FDD835;}}
.nav-links{{display:flex;gap:24px;align-items:center;}}
.nav-links a{{color:rgba(255,255,255,.85);font-size:.85rem;font-weight:600;transition:color .3s;}}
.nav-links a:hover{{color:#FDD835;}}
.nav-cta{{background:#FDD835;color:#0D1B2A;padding:10px 22px;border-radius:50px;font-weight:700;font-size:.85rem;display:inline-flex;align-items:center;gap:8px;transition:transform .3s,box-shadow .3s;white-space:nowrap;flex-shrink:0;}}
.nav-cta:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(253,216,53,.4);}}

/* Hamburger */
.hamburger{{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:8px;z-index:1001;}}
.hamburger span{{display:block;width:24px;height:2.5px;background:#fff;border-radius:2px;transition:all .3s;}}
.hamburger.active span:nth-child(1){{transform:rotate(45deg) translate(5px,5px);}}
.hamburger.active span:nth-child(2){{opacity:0;}}
.hamburger.active span:nth-child(3){{transform:rotate(-45deg) translate(5px,-5px);}}

/* Mobile Menu */
.mobile-menu{{display:none;position:fixed;top:0;left:0;width:100%;height:100vh;background:rgba(13,71,161,.98);backdrop-filter:blur(10px);z-index:999;flex-direction:column;align-items:center;justify-content:center;gap:24px;opacity:0;pointer-events:none;transition:opacity .3s;}}
.mobile-menu.active{{opacity:1;pointer-events:all;}}
.mobile-menu a{{color:#fff;font-size:1.2rem;font-weight:600;padding:12px 24px;border-radius:12px;transition:background .3s;}}
.mobile-menu a:hover{{background:rgba(255,255,255,.1);}}
.mobile-menu .nav-cta{{font-size:1rem;padding:14px 32px;margin-top:16px;}}

/* ===== HERO ===== */
.hero{{background:linear-gradient(135deg,#0D47A1,#1565C0,#1E88E5);position:relative;padding:120px 20px 80px;overflow:hidden;min-height:100vh;display:flex;align-items:center;}}
.hero::before{{content:'';position:absolute;inset:0;background-image:radial-gradient(circle,rgba(255,255,255,.07) 1px,transparent 1px);background-size:24px 24px;}}
.hero-inner{{max-width:1200px;margin:0 auto;display:flex;align-items:center;gap:60px;position:relative;z-index:2;width:100%;}}
.hero-text{{flex:1;min-width:0;}}
.hero-phone{{flex:0 0 280px;position:relative;}}
.hero-app-badge{{display:inline-flex;align-items:center;gap:12px;margin-bottom:16px;}}
.hero-app-badge img{{width:52px;height:52px;border-radius:14px;}}
.hero-app-badge span{{font-size:1.1rem;font-weight:700;color:#fff;}}
.live-badge{{display:inline-flex;align-items:center;gap:8px;background:rgba(67,160,71,.25);border:1px solid #43A047;border-radius:50px;padding:6px 16px;margin-bottom:20px;font-size:.8rem;font-weight:600;color:#A5D6A7;}}
.live-dot{{width:8px;height:8px;border-radius:50%;background:#43A047;animation:blink 1.5s infinite;}}
@keyframes blink{{0%,100%{{opacity:1;}}50%{{opacity:.3;}}}}
.hero h1{{font-size:clamp(1.8rem, 5vw, 3rem);font-weight:900;color:#fff;line-height:1.2;margin-bottom:20px;}}
.hero h1 .yellow{{color:#FDD835;}}
.hero h1 .light{{color:#90CAF5;}}
.hero-sub{{color:rgba(255,255,255,.85);font-size:clamp(.88rem, 2.5vw, 1.05rem);line-height:1.7;margin-bottom:32px;max-width:540px;}}
.hero-btns{{display:flex;gap:12px;flex-wrap:wrap;}}
.btn-primary{{background:#FDD835;color:#0D1B2A;padding:14px 24px;border-radius:50px;font-weight:700;display:inline-flex;align-items:center;gap:10px;transition:transform .3s,box-shadow .3s;font-size:clamp(.82rem, 2vw, .95rem);white-space:nowrap;}}
.btn-primary img{{height:22px;width:auto;}}
.btn-primary:hover{{transform:translateY(-3px);box-shadow:0 10px 30px rgba(253,216,53,.4);}}
.btn-ghost{{border:2px solid rgba(255,255,255,.5);color:#fff;padding:14px 24px;border-radius:50px;font-weight:600;font-size:clamp(.82rem, 2vw, .95rem);transition:background .3s,transform .3s;white-space:nowrap;}}
.btn-ghost:hover{{background:rgba(255,255,255,.1);transform:translateY(-3px);}}
.trust-row{{display:flex;gap:16px;margin-top:28px;flex-wrap:wrap;}}
.trust-item{{color:rgba(255,255,255,.8);font-size:.78rem;font-weight:600;display:flex;align-items:center;gap:6px;}}

/* Phone Mockup */
.phone-mockup{{width:230px;background:#fff;border-radius:36px;padding:8px;box-shadow:0 30px 60px rgba(0,0,0,.3);animation:floatPhone 4s ease-in-out infinite;position:relative;margin:0 auto;}}
@keyframes floatPhone{{0%,100%{{transform:translateY(0) rotate(1deg);}}50%{{transform:translateY(-16px) rotate(-1deg);}}}}
.phone-screen{{background:#E3F2FD;border-radius:28px;overflow:hidden;}}
.phone-header{{background:linear-gradient(135deg,#1565C0,#1E88E5);padding:14px 12px;display:flex;align-items:center;gap:8px;}}
.phone-header img{{width:26px;height:26px;border-radius:6px;}}
.phone-header-text{{color:#fff;}}
.phone-header-text .ph-title{{font-size:.7rem;font-weight:700;}}
.phone-header-text .ph-sub{{font-size:.5rem;opacity:.8;}}
.pay-card{{background:linear-gradient(135deg,#43A047,#66BB6A);margin:10px;border-radius:14px;padding:14px;text-align:center;color:#fff;animation:pulseCard 2.5s ease-in-out infinite;}}
@keyframes pulseCard{{0%,100%{{transform:scale(1);}}50%{{transform:scale(1.03);}}}}
.pay-card .check{{font-size:1.3rem;}}
.pay-card .pay-label{{font-size:.65rem;font-weight:600;margin-top:4px;}}
.pay-card .pay-amount{{font-size:1.4rem;font-weight:900;}}
.pay-card .pay-hindi{{font-size:.55rem;margin-top:4px;}}
.sound-bars{{display:flex;justify-content:center;gap:4px;padding:10px 0;}}
.sound-bars span{{display:block;width:5px;background:#1565C0;border-radius:3px;animation:barAnim 1s ease-in-out infinite alternate;}}
.sound-bars span:nth-child(1){{height:12px;animation-delay:0s;}}
.sound-bars span:nth-child(2){{height:20px;animation-delay:.1s;}}
.sound-bars span:nth-child(3){{height:28px;animation-delay:.2s;}}
.sound-bars span:nth-child(4){{height:24px;animation-delay:.3s;}}
.sound-bars span:nth-child(5){{height:18px;animation-delay:.4s;}}
.sound-bars span:nth-child(6){{height:14px;animation-delay:.5s;}}
@keyframes barAnim{{0%{{height:6px;}}100%{{height:28px;}}}}
.lang-pills{{display:flex;gap:4px;padding:6px 10px;flex-wrap:wrap;justify-content:center;}}
.lang-pills span{{background:#BBDEFB;color:#0D47A1;font-size:.5rem;padding:3px 8px;border-radius:20px;font-weight:600;}}
.pay-history{{padding:8px 10px 14px;}}
.pay-history-item{{display:flex;justify-content:space-between;font-size:.55rem;padding:4px 0;border-bottom:1px solid #E0E0E0;color:#546E7A;}}

/* Floating Cards */
.float-card{{position:absolute;background:#fff;border-radius:14px;padding:10px 16px;box-shadow:0 8px 24px rgba(0,0,0,.15);font-size:.7rem;font-weight:700;color:#0D1B2A;white-space:nowrap;z-index:5;}}
.fc1{{top:-10px;right:-60px;animation:floatCard 3.5s ease-in-out infinite;}}
.fc2{{bottom:60px;left:-70px;animation:floatCard 4s ease-in-out infinite .5s;}}
.fc3{{bottom:10px;right:-50px;animation:floatCard 3.8s ease-in-out infinite 1s;}}
@keyframes floatCard{{0%,100%{{transform:translateY(0);}}50%{{transform:translateY(-10px);}}}}

/* ===== STATS RIBBON ===== */
.stats{{background:#fff;box-shadow:0 4px 20px rgba(0,0,0,.08);padding:28px 20px;}}
.stats-inner{{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(5,1fr);gap:16px;text-align:center;}}
.stat-item{{text-align:center;padding:8px;}}
.stat-num{{font-size:clamp(1.2rem, 3vw, 1.7rem);font-weight:900;color:#1565C0;}}
.stat-label{{font-size:clamp(.6rem, 1.5vw, .72rem);text-transform:uppercase;color:#546E7A;font-weight:600;letter-spacing:1px;margin-top:4px;}}

/* ===== SECTION COMMONS ===== */
.section{{padding:clamp(50px, 8vw, 80px) 20px;}}
.section-tag{{display:inline-block;background:rgba(21,101,192,.08);color:#1565C0;font-size:.8rem;font-weight:700;padding:6px 18px;border-radius:50px;margin-bottom:12px;}}
.section-title{{font-size:clamp(1.5rem, 4vw, 2.1rem);font-weight:900;color:#0D1B2A;margin-bottom:36px;}}
.section-light .section-tag{{background:rgba(255,255,255,.15);color:#FDD835;}}
.section-light .section-title{{color:#fff;}}

/* ===== HOW IT WORKS ===== */
.how{{background:#E3F2FD;}}
.steps-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;position:relative;max-width:1100px;margin:0 auto;}}
.step-card{{background:#fff;border-radius:20px;padding:28px 20px;text-align:center;transition:transform .3s,box-shadow .3s;position:relative;}}
.step-card:hover{{transform:translateY(-8px);box-shadow:0 16px 40px rgba(21,101,192,.15);}}
.step-num{{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#1565C0,#1E88E5);color:#fff;font-size:1.1rem;font-weight:800;display:flex;align-items:center;justify-content:center;margin:0 auto 16px;}}
.step-icon{{font-size:2rem;margin-bottom:10px;}}
.step-card h3{{font-size:1rem;font-weight:700;margin-bottom:8px;}}
.step-card p{{font-size:.82rem;color:#546E7A;line-height:1.5;}}

/* ===== FEATURES ===== */
.features-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;max-width:1100px;margin:0 auto;}}
.feature-card{{background:#E3F2FD;border:1px solid #BBDEFB;border-radius:16px;padding:24px 20px;transition:transform .3s,box-shadow .3s,background .3s;position:relative;overflow:hidden;}}
.feature-card::after{{content:'';position:absolute;bottom:0;left:0;width:100%;height:4px;background:linear-gradient(90deg,#1565C0,#1E88E5);transform:scaleX(0);transition:transform .3s;}}
.feature-card:hover{{transform:translateY(-6px);box-shadow:0 12px 35px rgba(21,101,192,.12);background:#fff;}}
.feature-card:hover::after{{transform:scaleX(1);}}
.feature-icon{{font-size:2rem;margin-bottom:12px;}}
.feature-card h3{{font-size:.92rem;font-weight:700;margin-bottom:6px;}}
.feature-card p{{font-size:.8rem;color:#546E7A;line-height:1.5;}}

/* ===== PRICING ===== */
.pricing{{background:linear-gradient(135deg,#0D47A1,#1565C0,#1E88E5);}}
.pricing-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;max-width:1000px;margin:0 auto;align-items:start;}}
.price-card{{background:#fff;border-radius:20px;padding:32px 24px;text-align:center;transition:transform .3s;}}
.price-card.popular{{border:3px solid #FDD835;transform:scale(1.04);}}
.price-card:hover{{transform:translateY(-6px);}}
.price-card.popular:hover{{transform:scale(1.04) translateY(-6px);}}
.price-badge{{background:#FDD835;color:#0D1B2A;font-size:.7rem;font-weight:800;padding:4px 14px;border-radius:20px;display:inline-block;margin-bottom:10px;}}
.price-card h3{{font-size:1.2rem;font-weight:800;margin-bottom:8px;}}
.price-card .price{{font-size:1.8rem;font-weight:900;color:#1565C0;margin:10px 0;}}
.price-card .price small{{font-size:.8rem;font-weight:400;color:#546E7A;}}
.price-card ul{{list-style:none;text-align:left;margin:20px 0;}}
.price-card ul li{{font-size:.82rem;padding:6px 0;border-bottom:1px solid #eee;display:flex;align-items:center;gap:8px;}}
.price-card ul li::before{{content:'✓';color:#43A047;font-weight:700;}}
.price-btn{{display:inline-block;padding:12px 28px;border-radius:50px;font-weight:700;font-size:.88rem;transition:transform .3s,box-shadow .3s;}}
.price-btn-outline{{border:2px solid #1565C0;color:#1565C0;}}
.price-btn-fill{{background:#FDD835;color:#0D1B2A;}}
.price-btn:hover{{transform:translateY(-3px);box-shadow:0 8px 20px rgba(0,0,0,.12);}}

/* ===== WHO SHOULD USE ===== */
.who{{background:linear-gradient(135deg,#0D47A1,#1565C0);}}
.chips{{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;max-width:900px;margin:0 auto;}}
.chip{{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);color:#fff;padding:10px 20px;border-radius:50px;font-size:.88rem;font-weight:600;transition:transform .3s,background .3s;cursor:default;}}
.chip:hover{{background:rgba(253,216,53,.2);transform:scale(1.03);}}

/* ===== PRIVACY ===== */
.privacy{{background:#E3F2FD;}}
.privacy-inner{{max-width:1000px;margin:0 auto;display:flex;align-items:center;gap:60px;}}
.shield{{font-size:6rem;animation:shieldPulse 2s ease-in-out infinite;flex-shrink:0;}}
@keyframes shieldPulse{{0%,100%{{transform:scale(1);}}50%{{transform:scale(1.08);}}}}
.privacy-content{{flex:1;min-width:0;}}
.privacy-points{{list-style:none;margin-top:20px;}}
.privacy-points li{{font-size:.88rem;padding:8px 0;display:flex;align-items:center;gap:10px;}}
.privacy-points li::before{{content:'✓';color:#43A047;font-weight:700;font-size:1.1rem;}}

/* ===== REVIEWS ===== */
.reviews-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;max-width:1000px;margin:0 auto;}}
.review-card{{background:#E3F2FD;border:2px solid transparent;border-radius:16px;padding:28px 24px;transition:transform .3s,border-color .3s;}}
.review-card:hover{{transform:translateY(-5px);border-color:#1565C0;}}
.review-stars{{color:#FDD835;font-size:1.1rem;margin-bottom:10px;}}
.review-text{{font-size:.86rem;color:#0D1B2A;line-height:1.6;margin-bottom:16px;font-style:italic;}}
.reviewer{{display:flex;align-items:center;gap:12px;}}
.reviewer-avatar{{width:40px;height:40px;border-radius:50%;background:#1565C0;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem;flex-shrink:0;}}
.reviewer-info .rname{{font-size:.85rem;font-weight:700;}}
.reviewer-info .rdate{{font-size:.72rem;color:#546E7A;}}

/* ===== FINAL CTA ===== */
.final-cta{{background:linear-gradient(135deg,#0D47A1,#1565C0,#1E88E5);text-align:center;padding:clamp(50px, 8vw, 80px) 20px;}}
.final-cta h2{{font-size:clamp(1.5rem, 4vw, 2.2rem);font-weight:900;color:#fff;}}
.final-cta h2 .yellow{{color:#FDD835;}}
.final-cta .subtitle{{color:rgba(255,255,255,.8);margin:16px 0 32px;font-size:clamp(.88rem, 2vw, 1rem);}}
.cta-play-btn{{display:inline-flex;align-items:center;gap:16px;background:#fff;padding:14px 28px;border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,.2);transition:transform .3s,box-shadow .3s;}}
.cta-play-btn:hover{{transform:translateY(-3px);box-shadow:0 16px 40px rgba(0,0,0,.3);}}
.cta-play-btn img{{height:36px;width:auto;}}
.cta-play-btn span{{font-size:clamp(.85rem, 2vw, 1rem);font-weight:700;color:#0D1B2A;}}
.cta-note{{color:rgba(255,255,255,.6);font-size:.78rem;margin-top:16px;}}

/* ===== FOOTER ===== */
.footer{{background:#0D1B2A;padding:40px 20px;}}
.footer-inner{{max-width:1100px;margin:0 auto;}}
.footer-top{{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:20px;margin-bottom:24px;}}
.footer-brand{{display:flex;align-items:center;gap:10px;}}
.footer-brand img{{width:36px;height:36px;border-radius:8px;}}
.footer-brand span{{color:#fff;font-size:1rem;font-weight:700;}}
.footer-links{{display:flex;gap:20px;flex-wrap:wrap;}}
.footer-links a{{color:rgba(255,255,255,.6);font-size:.82rem;transition:color .3s;}}
.footer-links a:hover{{color:#FDD835;}}
.footer-bottom{{text-align:center;color:rgba(255,255,255,.4);font-size:.75rem;padding-top:20px;border-top:1px solid rgba(255,255,255,.08);}}

/* ============================================================
   RESPONSIVE BREAKPOINTS
   ============================================================ */

/* === 1440px+ Large Desktop === */
@media(min-width:1441px){{
  .hero-inner{{max-width:1300px;gap:80px;}}
  .hero h1{{font-size:3.2rem;}}
  .hero-phone{{flex:0 0 320px;}}
  .phone-mockup{{width:260px;}}
  .section-title{{font-size:2.3rem;}}
}}

/* === 1024px - 1200px Small Desktop === */
@media(max-width:1200px){{
  .hero-inner{{gap:40px;}}
  .features-grid{{grid-template-columns:repeat(3,1fr);}}
}}

/* === 900px - 1024px Tablet Landscape === */
@media(max-width:1024px){{
  .hero-phone{{flex:0 0 240px;}}
  .phone-mockup{{width:200px;}}
  .fc1{{right:-40px;}}
  .fc2{{left:-50px;}}
  .fc3{{right:-30px;}}
  .steps-grid{{grid-template-columns:repeat(2,1fr);}}
  .pricing-grid{{grid-template-columns:repeat(3,1fr);gap:16px;}}
  .price-card{{padding:28px 20px;}}
}}

/* === 768px - 900px Tablet Portrait === */
@media(max-width:900px){{
  /* Navbar: show hamburger */
  .nav-links{{display:none;}}
  .hamburger{{display:flex;}}
  .mobile-menu{{display:flex;}}
  
  /* Hero: stack vertically */
  .hero{{padding:100px 20px 60px;min-height:auto;}}
  .hero-inner{{flex-direction:column;text-align:center;gap:40px;}}
  .hero-sub{{margin-left:auto;margin-right:auto;}}
  .hero-btns{{justify-content:center;}}
  .trust-row{{justify-content:center;}}
  .hero-phone{{flex:0 0 auto;}}

  /* Features */
  .features-grid{{grid-template-columns:repeat(2,1fr);}}
  
  /* Reviews */
  .reviews-grid{{grid-template-columns:repeat(2,1fr);}}
  
  /* Privacy */
  .privacy-inner{{flex-direction:column;text-align:center;gap:30px;}}
  .privacy-points li{{justify-content:center;}}
}}

/* === 576px - 768px Large Phone / Small Tablet === */
@media(max-width:768px){{
  /* Stats */
  .stats-inner{{grid-template-columns:repeat(3,1fr);}}
  
  /* Pricing - stack */
  .pricing-grid{{grid-template-columns:1fr;max-width:400px;}}
  .price-card.popular{{transform:none;}}
  .price-card.popular:hover{{transform:translateY(-6px);}}
  
  /* Steps */
  .steps-grid{{grid-template-columns:repeat(2,1fr);gap:16px;}}
  
  /* Footer */
  .footer-top{{flex-direction:column;align-items:center;text-align:center;}}
  .footer-links{{justify-content:center;}}
  .footer-brand span{{font-size:.88rem;}}
  
  /* Chips */
  .chip{{padding:8px 16px;font-size:.82rem;}}
  
  /* CTA button */
  .cta-play-btn{{flex-direction:column;gap:8px;padding:16px 24px;}}
}}

/* === 480px - 576px Mobile === */
@media(max-width:576px){{
  /* Hero */
  .hero{{padding:90px 16px 50px;}}
  .hero-app-badge img{{width:42px;height:42px;}}
  .hero-btns{{flex-direction:column;align-items:center;width:100%;}}
  .btn-primary,.btn-ghost{{width:100%;justify-content:center;text-align:center;padding:12px 20px;}}
  .trust-row{{gap:12px;}}
  .trust-item{{font-size:.72rem;}}
  
  /* Phone mockup */
  .phone-mockup{{width:190px;}}
  .float-card{{display:none;}}
  
  /* Stats */
  .stats-inner{{grid-template-columns:repeat(3,1fr);gap:10px;}}
  .stat-num{{font-size:1.1rem;}}
  .stat-label{{font-size:.55rem;letter-spacing:.5px;}}
  
  /* Steps */
  .steps-grid{{grid-template-columns:1fr;max-width:340px;margin:0 auto;}}
  .step-card{{padding:24px 16px;}}
  
  /* Features */
  .features-grid{{grid-template-columns:1fr;max-width:400px;margin:0 auto;}}
  
  /* Reviews */
  .reviews-grid{{grid-template-columns:1fr;max-width:400px;margin:0 auto;}}
  
  /* Section padding */
  .section{{padding:40px 16px;}}
  .section-title{{margin-bottom:28px;}}
  
  /* Privacy */
  .shield{{font-size:4.5rem;}}
  .privacy-points li{{font-size:.82rem;}}
  
  /* Navbar CTA */
  .nav-cta{{padding:8px 16px;font-size:.78rem;}}
  .nav-brand span{{font-size:1.05rem;}}
  .nav-brand img{{width:30px;height:30px;}}
}}

/* === 320px - 480px Small Phone === */
@media(max-width:480px){{
  html{{font-size:15px;}}
  
  .hero h1{{font-size:1.6rem;}}
  .hero-sub{{font-size:.85rem;}}
  .live-badge{{font-size:.7rem;padding:5px 12px;}}
  .hero-app-badge img{{width:38px;height:38px;}}
  
  .phone-mockup{{width:170px;}}
  
  .stats{{padding:20px 12px;}}
  .stats-inner{{grid-template-columns:repeat(3,1fr);gap:8px;}}
  .stat-num{{font-size:1rem;}}
  
  .chips{{gap:8px;}}
  .chip{{padding:7px 14px;font-size:.75rem;}}
  
  .section-tag{{font-size:.72rem;padding:5px 14px;}}
  
  .footer-links{{gap:12px;}}
  .footer-links a{{font-size:.75rem;}}
  .footer-bottom{{font-size:.68rem;}}
  
  .cta-play-btn img{{height:28px;}}
  .cta-play-btn span{{font-size:.85rem;}}
  .cta-note{{font-size:.7rem;}}
  
  .review-card{{padding:20px 16px;}}
  .review-text{{font-size:.82rem;}}
  
  .price-card{{padding:24px 16px;}}
  .price-card h3{{font-size:1.1rem;}}
  .price-card .price{{font-size:1.6rem;}}
  .price-card ul li{{font-size:.78rem;}}
}}

/* === Ultra-small 320px === */
@media(max-width:360px){{
  html{{font-size:14px;}}
  .nav-inner{{padding:0 12px;}}
  .nav-cta{{padding:7px 14px;font-size:.72rem;}}
  .hero{{padding:85px 12px 40px;}}
  .phone-mockup{{width:155px;}}
  .section{{padding:36px 12px;}}
  .stats{{padding:16px 8px;}}
  .stat-num{{font-size:.9rem;}}
  .stat-label{{font-size:.5rem;}}
}}

</style>
</head>
<body>

<!-- NAVBAR -->
<nav class="navbar" id="navbar">
<div class="nav-inner">
<a href="#" class="nav-brand">
<img src="data:image/jpeg;base64,{logo_b64}" alt="PayEcho Logo">
<span>Pay<span class="echo">Echo</span></span>
</a>
<div class="nav-links">
<a href="#how">Kaise Kaam Karta Hai</a>
<a href="#features">Features</a>
<a href="#pricing">Pricing</a>
<a href="#reviews">Reviews</a>
</div>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" target="_blank" class="nav-cta">▶ Free Download</a>
<div class="hamburger" id="hamburger" onclick="toggleMenu()">
<span></span><span></span><span></span>
</div>
</div>
</nav>

<!-- MOBILE MENU -->
<div class="mobile-menu" id="mobileMenu">
<a href="#how" onclick="toggleMenu()">Kaise Kaam Karta Hai</a>
<a href="#features" onclick="toggleMenu()">Features</a>
<a href="#pricing" onclick="toggleMenu()">Pricing</a>
<a href="#reviews" onclick="toggleMenu()">Reviews</a>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" target="_blank" class="nav-cta" onclick="toggleMenu()">▶ Free Download</a>
</div>

<!-- HERO -->
<section class="hero" id="hero">
<div class="hero-inner">
<div class="hero-text">
<div class="hero-app-badge">
<img src="data:image/jpeg;base64,{logo_b64}" alt="PayEcho">
<span style="color:#fff;font-weight:800;">PayEcho</span>
</div>
<div class="live-badge"><span class="live-dot"></span> India ka #1 Free UPI Soundbox App</div>
<h1>Har Payment Par<br><span class="yellow">Awaaz Mein</span><br><span class="light">Alert Aayega!</span> &#x1F50A;</h1>
<p class="hero-sub">PayEcho aapke phone ko ek smart UPI Soundbox bana deta hai — ₹ amount turant bolta hai jab bhi payment aata hai. Koi hardware nahi, koi fee nahi — bilkul free!</p>
<div class="hero-btns">
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" target="_blank" class="btn-primary">
<img src="data:image/jpeg;base64,{play_b64}" alt="Google Play"> Google Play Se Download Karo
</a>
<a href="#how" class="btn-ghost">Kaise Kaam Karta Hai ↓</a>
</div>
<div class="trust-row">
<span class="trust-item">⭐ 5.0 Rating</span>
<span class="trust-item">🆓 100% Free</span>
<span class="trust-item">🔒 Secure</span>
<span class="trust-item">⚡ 1 Min Setup</span>
</div>
</div>
<div class="hero-phone">
<div class="float-card fc1">⚡ Instant Alert!</div>
<div class="float-card fc2">🌐 8+ Languages</div>
<div class="float-card fc3">📊 Payment History</div>
<div class="phone-mockup">
<div class="phone-screen">
<div class="phone-header">
<img src="data:image/jpeg;base64,{logo_b64}" alt="PayEcho">
<div class="phone-header-text">
<div class="ph-title">PayEcho</div>
<div class="ph-sub">UPI Mobile Soundbox</div>
</div>
</div>
<div class="pay-card">
<div class="check">✅</div>
<div class="pay-label">Payment Received!</div>
<div class="pay-amount">₹ 250</div>
<div class="pay-hindi hindi">दो सौ पचास रुपये प्राप्त हुए</div>
</div>
<div class="sound-bars"><span></span><span></span><span></span><span></span><span></span><span></span></div>
<div class="lang-pills">
<span>🇮🇳 <span class="hindi">हिंदी</span></span>
<span><span class="hindi">मराठी</span></span>
<span>English</span>
<span><span class="hindi">தமிழ்</span></span>
</div>
<div class="pay-history">
<div class="pay-history-item"><span>GPay</span><span>₹150</span></div>
<div class="pay-history-item"><span>PhonePe</span><span>₹500</span></div>
<div class="pay-history-item"><span>Paytm</span><span>₹75</span></div>
</div>
</div>
</div>
</div>
</div>
</section>

<!-- STATS RIBBON -->
<section class="stats reveal">
<div class="stats-inner">
<div class="stat-item"><div class="stat-num">5.0 ⭐</div><div class="stat-label">Rating</div></div>
<div class="stat-item"><div class="stat-num">500+</div><div class="stat-label">Downloads</div></div>
<div class="stat-item"><div class="stat-num">FREE</div><div class="stat-label">No Cost</div></div>
<div class="stat-item"><div class="stat-num">1 Min</div><div class="stat-label">Setup</div></div>
<div class="stat-item"><div class="stat-num">8+</div><div class="stat-label">Languages</div></div>
</div>
</section>

<!-- HOW IT WORKS -->
<section class="section how reveal" id="how">
<div style="text-align:center;">
<span class="section-tag">⚙️ Kaise Kaam Karta Hai</span>
<h2 class="section-title">Sirf 4 Simple Steps — Bas Ho Gaya!</h2>
</div>
<div class="steps-grid">
<div class="step-card reveal"><div class="step-num">1</div><div class="step-icon">📲</div><h3>App Install Karo</h3><p>Google Play se free mein download karo</p></div>
<div class="step-card reveal"><div class="step-num">2</div><div class="step-icon">🔔</div><h3>Permission Do</h3><p>Notification access allow karo</p></div>
<div class="step-card reveal"><div class="step-num">3</div><div class="step-icon">🌐</div><h3>Language Chuno</h3><p>Hindi, Marathi, English ya koi bhi language</p></div>
<div class="step-card reveal"><div class="step-num">4</div><div class="step-icon">🎉</div><h3>Done! Sunna Shuru!</h3><p>Ab har UPI payment par awaaz aayegi</p></div>
</div>
</section>

<!-- FEATURES -->
<section class="section reveal" id="features">
<div style="text-align:center;">
<span class="section-tag">✨ Features</span>
<h2 class="section-title">Sab Kuch FREE Mein Milega</h2>
</div>
<div class="features-grid">
<div class="feature-card reveal"><div class="feature-icon">⚡</div><h3>Instant Voice Alert</h3><p>Payment aate hi turant awaaz mein amount bolta hai</p></div>
<div class="feature-card reveal"><div class="feature-icon">🌐</div><h3>Multiple Indian Languages</h3><p>Hindi, Marathi, Telugu, Tamil, Kannada, Bengali</p></div>
<div class="feature-card reveal"><div class="feature-icon">📢</div><h3>Volume & Speed Control</h3><p>Shor ke hisaab se awaaz adjust karo</p></div>
<div class="feature-card reveal"><div class="feature-icon">📊</div><h3>Payment History</h3><p>Daily/weekly/monthly payment records</p></div>
<div class="feature-card reveal"><div class="feature-icon">💬</div><h3>Custom Thank You Message</h3><p>"Dhanyavaad! Fir aana!" jaisa custom alert</p></div>
<div class="feature-card reveal"><div class="feature-icon">📱</div><h3>QR Code Display</h3><p>UPI QR code seedha app mein dikhao customers ko</p></div>
<div class="feature-card reveal"><div class="feature-icon">👥</div><h3>Staff Support</h3><p>Multiple devices par alerts milenge</p></div>
<div class="feature-card reveal"><div class="feature-icon">🔒</div><h3>100% Secure & Private</h3><p>Bank access nahi, SMS nahi padhta</p></div>
</div>
</section>

<!-- PRICING -->
<section class="section section-light pricing reveal" id="pricing">
<div style="text-align:center;">
<span class="section-tag">💎 Premium Plans</span>
<h2 class="section-title">Low Price Mein Premium Features</h2>
</div>
<div class="pricing-grid">
<div class="price-card reveal">
<h3>FREE Plan</h3>
<div class="price">₹0</div>
<ul>
<li>Basic voice alerts</li>
<li>Hindi language only</li>
<li>Payment history (7 days)</li>
<li>Suitable for: Personal use</li>
</ul>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" target="_blank" class="price-btn price-btn-outline">Start Free</a>
</div>
<div class="price-card popular reveal">
<span class="price-badge">Most Popular</span>
<h3>PRO Plan</h3>
<div class="price">₹XX <small>/ month</small></div>
<ul>
<li>All languages (8+)</li>
<li>Custom thank you message</li>
<li>Payment history (unlimited)</li>
<li>Staff support (2 devices)</li>
<li>Volume & speed control</li>
<li>QR Code display</li>
</ul>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" target="_blank" class="price-btn price-btn-fill">Get Pro</a>
</div>
<div class="price-card reveal">
<h3>BUSINESS Plan</h3>
<div class="price">₹XX <small>/ month</small></div>
<ul>
<li>Everything in Pro</li>
<li>Staff support (5 devices)</li>
<li>Priority support</li>
</ul>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" target="_blank" class="price-btn price-btn-outline">Get Business</a>
</div>
</div>
</section>

<!-- WHO SHOULD USE -->
<section class="section section-light who reveal">
<div style="text-align:center;">
<span class="section-tag">👥 Kaun Use Kare</span>
<h2 class="section-title">Kisi Bhi Business Ke Liye</h2>
</div>
<div class="chips">
<span class="chip">🛒 Kirana & Grocery</span>
<span class="chip">🏪 General Store</span>
<span class="chip">☕ Café & Restaurant</span>
<span class="chip">🛵 Delivery Counter</span>
<span class="chip">💈 Salon & Parlour</span>
<span class="chip">🧑‍⚕️ Doctors & Clinics</span>
<span class="chip">🏋️ Gym & Fitness</span>
<span class="chip">📚 Coaching Classes</span>
<span class="chip">🌽 Street Vendor</span>
<span class="chip">🔧 Repair Services</span>
<span class="chip">🧺 Sabzi & Fruit Stall</span>
<span class="chip">📦 Online Sellers</span>
</div>
</section>

<!-- PRIVACY -->
<section class="section privacy reveal">
<div class="privacy-inner">
<div class="shield">🛡️</div>
<div class="privacy-content">
<span class="section-tag">🔐 Privacy & Security</span>
<h2 class="section-title">Aapka Data 100% Safe Hai</h2>
<p style="color:#546E7A;margin-bottom:16px;font-size:clamp(.85rem,2vw,.95rem);">Hum aapki privacy ko seriously lete hain. PayEcho sirf notifications se kaam karta hai.</p>
<ul class="privacy-points">
<li>Bank account access bilkul nahi karta</li>
<li>SMS messages nahi padhta</li>
<li>Koi bhi data third party ke saath share nahi</li>
<li>Sirf on-screen notifications se kaam karta hai</li>
<li>Google Play Verified — Rated 3+ Safe</li>
</ul>
</div>
</div>
</section>

<!-- REVIEWS -->
<section class="section reveal" id="reviews">
<div style="text-align:center;">
<span class="section-tag">💬 Real Reviews</span>
<h2 class="section-title">Log Kya Kehte Hain?</h2>
</div>
<div class="reviews-grid">
<div class="review-card reveal">
<div class="review-stars">★★★★★</div>
<p class="review-text">"Simple, fast, and free. The voice alert feature works perfectly in my busy shop."</p>
<div class="reviewer">
<div class="reviewer-avatar">DP</div>
<div class="reviewer-info"><div class="rname">Dhiraj Patil</div><div class="rdate">Jan 30, 2026</div></div>
</div>
</div>
<div class="review-card reveal">
<div class="review-stars">★★★★★</div>
<p class="review-text">"Best app for shopkeepers and small businesses. Free hai aur bahut useful features hain."</p>
<div class="reviewer">
<div class="reviewer-avatar">AB</div>
<div class="reviewer-info"><div class="rname">Anveeshka Bhosale</div><div class="rdate">Mar 10, 2026</div></div>
</div>
</div>
<div class="review-card reveal">
<div class="review-stars">★★★★★</div>
<p class="review-text">"App is very easy to use and effective for shopkeepers. UPI alert mobile sound box — ekdum perfect!"</p>
<div class="reviewer">
<div class="reviewer-avatar">AU</div>
<div class="reviewer-info"><div class="rname">Avinash Ukirade</div><div class="rdate">Mar 10, 2026</div></div>
</div>
</div>
</div>
</section>

<!-- FINAL CTA -->
<section class="final-cta reveal">
<h2>Aaj Hi Download Karo<br><span class="yellow">Bilkul FREE! 🎉</span></h2>
<p class="subtitle">Hardware soundbox kharidne ki zarurat nahi.</p>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" target="_blank" class="cta-play-btn">
<img src="data:image/jpeg;base64,{play_b64}" alt="Google Play">
<span>Google Play Se Download Karo</span>
</a>
<p class="cta-note">Free · Plans start from ₹XX only · Works on Android 5.0+</p>
</section>

<!-- FOOTER -->
<footer class="footer">
<div class="footer-inner">
<div class="footer-top">
<div class="footer-brand">
<img src="data:image/jpeg;base64,{logo_b64}" alt="PayEcho">
<span>PayEcho – UPI Mobile Soundbox</span>
</div>
<div class="footer-links">
<a href="https://thinktankapps.netlify.app/privacy" target="_blank">Privacy Policy</a>
<a href="mailto:bhavarkaran888@gmail.com">Support</a>
<a href="https://karanbhavar.netlify.app/" target="_blank">Developer Website</a>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" target="_blank">Google Play</a>
</div>
</div>
<div class="footer-bottom">© 2026 Think Tank Apps · Made with ❤️ in Maharashtra 🇮🇳</div>
</div>
</footer>

<script>
// Fixed navbar shadow
window.addEventListener('scroll',()=>{{
  document.getElementById('navbar').classList.toggle('scrolled',window.scrollY>50);
}});

// Scroll reveal using IntersectionObserver
const obs=new IntersectionObserver((entries)=>{{
  entries.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('visible');obs.unobserve(e.target);}}}});
}},{{threshold:0.08,rootMargin:'0px 0px -40px 0px'}});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));

// Hamburger toggle
function toggleMenu(){{
  document.getElementById('hamburger').classList.toggle('active');
  document.getElementById('mobileMenu').classList.toggle('active');
  document.body.style.overflow=document.getElementById('mobileMenu').classList.contains('active')?'hidden':'';
}}
</script>
</body>
</html>
'''

output_path = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"✅ Responsive landing page created at: {output_path}")
print(f"   File size: {os.path.getsize(output_path):,} bytes")
