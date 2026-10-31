import base64, os
from google_play_scraper import reviews, Sort
from datetime import datetime

# --- AUTO-FETCH PLAY STORE REVIEWS ---
AVATAR_COLORS = ['#EA4335','#4285F4','#34A853','#FBBC05','#A142F4','#FF6D01','#24C1E0','#F538A0','#00BCD4','#FF5722','#3F51B5','#009688','#795548','#607D8B','#E91E63','#9C27B0','#00897B','#D81B60','#5E35B1','#039BE5']
PLAY_URL = 'https://play.google.com/store/apps/details?id=com.bhava.upialert'

def fetch_reviews():
    try:
        result, _ = reviews('com.bhava.upialert', lang='en', country='in', sort=Sort.NEWEST, count=50)
        # Filter 4-5 star reviews with text
        good = [r for r in result if r['score'] >= 4 and r['content'] and len(r['content'].strip()) > 10]
        if not good:
            return None
        return good
    except Exception as e:
        print(f'⚠️ Could not fetch reviews: {e}')
        return None

def build_review_card(name, text, date_str, idx, img_url=None):
    color = AVATAR_COLORS[idx % len(AVATAR_COLORS)]
    letter = name[0].upper()
    stars = '★★★★★'
    if img_url:
        avatar = f'<img src="{img_url}" class="rev-av" style="object-fit:cover;" referrerpolicy="no-referrer">'
    else:
        avatar = f'<div class="rev-av" style="background:{color}">{letter}</div>'
    return f'<a href="{PLAY_URL}" target="_blank" class="rev-card"><div class="rev-stars">{stars}</div><p class="rev-text hindi">"{text}"</p><div class="rev-user">{avatar}<div><div class="rev-name">{name}</div><div class="rev-date">{date_str}</div></div></div></a>'

def generate_review_html():
    fetched = fetch_reviews()
    if fetched:
        print(f'✅ Fetched {len(fetched)} reviews from Play Store')
        cards = []
        for i, r in enumerate(fetched):
            name = r['userName']
            text = r['content'].strip()
            dt = r['at']
            date_str = dt.strftime('%B %d, %Y') if isinstance(dt, datetime) else str(dt)
            cards.append(build_review_card(name, text, date_str, i, r.get('userImage')))
        # Original + Duplicate for seamless infinite loop
        all_cards = '\n'.join(cards)
        dup_cards = '\n'.join(cards)
        return f'{all_cards}\n<!-- Duplicate for seamless infinite loop -->\n{dup_cards}'
    else:
        print('⚠️ Using fallback reviews')
        return None

review_cards_html = generate_review_html()

def get_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

logo_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\.gemini\antigravity\brain\c200eeb1-5eb2-4df8-a23c-4225cec1b3ae\media__1773310644442.jpg")
play_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\playstore.png")
star_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Rating.png")

step1_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\software.png")
step2_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Permission.png")
step3_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\languages.png")
step4_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Done.png")
mobile_app_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\mobile-app.png")
msg_icon_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\message (1).png")
lang_icon_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\languages.png")
hist_icon_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\track.png")

who1_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Kirana Store.png")
who2_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Cafe.png")
who3_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Delivery Counter.png")
who4_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Saloon.png")
who5_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Clinic And Doctor.png")
who6_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Gym.png")
who7_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Coaching.png")
who8_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Street Vendor.png")
who9_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\repair-shop.png")
who10_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Sabzi And Fruit.png")
who11_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\Online Seller.png")
who12_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\General Store.png")
people_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\People.png")
privacy_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\privacy.png")
wus_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\What User Say.png")

# --- CUSTOM FEATURE ICONS ---
# In variables me double quotes ke andar apni image ka absolute path paste karein.
# Jaise: img_fc1 = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\instant.png"
# Agar blank rakhoge (r"") toh default emoji show hoga.
img_fc1  = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\alarm.png"  # Instant Alert
img_fc2  = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\languages.png"  # 8+ Languages
img_fc3  = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\history.png"  # History Tracked
img_fc4  = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\volume-control.png"  # Volume Control
img_fc5  = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\campaign.png"  # Custom Messages
img_fc6  = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\qr-code.png"  # QR Code Display
img_fc7  = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\teamwork.png"  # Staff Support
img_fc8  = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\insurance.png"  # 100% Secure
img_fc9  = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\free-of-charge.png"  # Always Free
img_fc10 = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\Public\payment-method.png"  # All UPI Apps

def get_fc_icon(path, default_emoji):
    if path and os.path.exists(path):
        try:
            b64 = get_b64(path)
            # image ki height/width aur blend mode yaha set hai
            return f'<img src="data:image/png;base64,{b64}" style="width:20px;height:20px;object-fit:contain;mix-blend-mode:multiply;" alt="icon">'
        except:
            pass
    return default_emoji

icon_1 = get_fc_icon(img_fc1, "⚡")
icon_2 = get_fc_icon(img_fc2, "🌐")
icon_3 = get_fc_icon(img_fc3, "📊")
icon_4 = get_fc_icon(img_fc4, "📢")
icon_5 = get_fc_icon(img_fc5, "💬")
icon_6 = get_fc_icon(img_fc6, "📱")
icon_7 = get_fc_icon(img_fc7, "👥")
icon_8 = get_fc_icon(img_fc8, "🔒")
icon_9 = get_fc_icon(img_fc9, "🆓")
icon_10 = get_fc_icon(img_fc10, "🎯")
# ----------------------------

css = """
:root{--blue:#1565C0;--blue2:#1976D2;--dark-blue:#0D47A1;--light-blue:#E3F2FD;--bg-alt:#F0F7FF;--yellow:#FDD835;--green:#43A047;--dark:#0D1B2A;--gray:#546E7A;--white:#fff;--font:'Poppins',sans-serif;--hindi:'Noto Sans Devanagari','Poppins',sans-serif;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:var(--font);color:var(--dark);background:var(--white);overflow-x:hidden;-webkit-text-size-adjust:100%;}
.hindi{font-family:var(--hindi);}
img{max-width:100%;display:block;height:auto;}
a{text-decoration:none;color:inherit;}

/* REVEAL */
.reveal{opacity:0;transform:translateY(40px);transition:opacity .7s ease,transform .7s ease;}
.reveal.visible{opacity:1;transform:translateY(0);}
.hero-anim{opacity:0;transform:translateY(30px);animation:heroIn .8s ease forwards;}
@keyframes heroIn{to{opacity:1;transform:translateY(0);}}

/* NAVBAR */
.navbar{position:fixed;top:0;left:0;width:100%;z-index:1000;padding:16px 0;transition:all .4s;}
.navbar.scrolled{background:var(--blue);box-shadow:0 2px 20px rgba(0,0,0,.2);padding:10px 0;}
.nav-inner{max-width:1200px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:0 24px;}
.nav-brand{display:flex;align-items:center;gap:10px;}
.nav-brand img{width:38px;height:38px;border-radius:10px;}
.nav-brand span{font-size:1.25rem;font-weight:800;color:var(--white);}
.nav-brand .echo{color:var(--yellow);}
.nav-links{display:flex;gap:28px;align-items:center;}
.nav-links a{color:rgba(255,255,255,.8);font-size:.88rem;font-weight:600;transition:color .3s;}
.nav-links a:hover{color:var(--yellow);}
.nav-cta{background:var(--yellow);color:var(--dark);padding:10px 24px;border-radius:50px;font-weight:700;font-size:.88rem;transition:all .3s;display:inline-flex;align-items:center;gap:8px;}
.nav-cta:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(253,216,53,.4);}
.hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:8px;z-index:1001;}
.hamburger span{display:block;width:24px;height:2.5px;background:var(--white);border-radius:2px;transition:all .3s;}
.hamburger.active span:nth-child(1){transform:rotate(45deg) translate(5px,5px);}
.hamburger.active span:nth-child(2){opacity:0;}
.hamburger.active span:nth-child(3){transform:rotate(-45deg) translate(5px,-5px);}
.mobile-menu{display:none;position:fixed;inset:0;background:rgba(13,71,161,.98);z-index:999;flex-direction:column;align-items:center;justify-content:center;gap:24px;opacity:0;pointer-events:none;transition:opacity .3s;}
.mobile-menu.active{opacity:1;pointer-events:all;}
.mobile-menu a{color:var(--white);font-size:1.2rem;font-weight:600;padding:12px 24px;}

/* HERO */
.hero{background:linear-gradient(135deg,var(--dark-blue) 0%,var(--blue) 50%,var(--blue2) 100%);position:relative;padding:160px 24px 120px;min-height:100vh;display:flex;align-items:center;overflow:hidden;}
.hero::before{content:'';position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.06) 1px,transparent 1px);background-size:28px 28px;}
.hero-inner{max-width:1200px;margin:0 auto;display:flex;align-items:center;gap:80px;position:relative;z-index:2;width:100%;}
.hero-text{flex:1;min-width:0;}
.hero-phone{flex:0 0 440px;position:relative;min-height:580px;display:flex;align-items:center;justify-content:center;}
.hero-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:50px;padding:8px 20px;margin-bottom:24px;font-size:.82rem;font-weight:600;color:rgba(255,255,255,.9);}
.hero h1{font-size:clamp(2.5rem,5vw,4.5rem);font-weight:900;color:var(--white);line-height:1.15;margin-bottom:16px;}
.hero h1 .yellow{color:var(--yellow);}
.hero-subtitle{font-size:clamp(1rem,2vw,1.3rem);color:rgba(255,255,255,.85);margin-bottom:16px;font-weight:600;}
.hero-body{color:rgba(255,255,255,.7);font-size:clamp(.88rem,1.5vw,1rem);line-height:1.8;margin-bottom:32px;max-width:520px;}
.hero-btns{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:32px;}
.btn-yellow{background:var(--yellow);color:var(--dark);padding:14px 28px;border-radius:50px;font-weight:700;font-size:.92rem;display:inline-flex;align-items:center;gap:10px;transition:all .3s;}
.btn-yellow img{height:22px;}
.btn-yellow:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(253,216,53,.4);}
.btn-ghost{border:2px solid rgba(255,255,255,.4);color:var(--white);padding:14px 28px;border-radius:50px;font-weight:600;font-size:.92rem;transition:all .3s;}
.btn-ghost:hover{background:rgba(255,255,255,.1);transform:translateY(-3px);}
.trust-row{display:flex;gap:24px;flex-wrap:wrap;}
.trust-item{color:rgba(255,255,255,.75);font-size:.8rem;font-weight:600;display:flex;align-items:center;gap:6px;}

/* PHONE MOCKUP */
.phone-mockup{width:310px;background:var(--white);border-radius:44px;padding:12px;box-shadow:0 40px 100px rgba(0,0,0,.4);animation:floatPhone 4s ease-in-out infinite;position:relative;margin:0 auto;}
@keyframes floatPhone{0%,100%{transform:translateY(0) rotate(.5deg);}50%{transform:translateY(-18px) rotate(-.5deg);}}
.phone-screen{background:var(--light-blue);border-radius:34px;overflow:hidden;}
.ph-head{background:linear-gradient(135deg,var(--blue),var(--blue2));padding:20px 16px;display:flex;align-items:center;gap:12px;}
.ph-head img{width:32px;height:32px;border-radius:9px;}
.ph-head-text{color:var(--white);}
.ph-head-text .t{font-size:.8rem;font-weight:800;letter-spacing:.5px;}
.ph-head-text .s{font-size:.55rem;opacity:.85;}
.ph-pay{background:linear-gradient(135deg,#43A047,#66BB6A);margin:16px 14px;border-radius:20px;padding:24px 16px;text-align:center;color:var(--white);animation:pulse 2.5s ease-in-out infinite;box-shadow:0 12px 30px rgba(67,160,71,.2);}
@keyframes pulse{0%,100%{transform:scale(1);}50%{transform:scale(1.03);}}
.ph-pay .ck{font-size:1.6rem;}.ph-pay .lb{font-size:.7rem;font-weight:700;margin-top:6px;}
.ph-pay .am{font-size:1.8rem;font-weight:900;letter-spacing:1px;margin:4px 0;}.ph-pay .hi{font-size:.6rem;margin-top:4px;}
.sbars{display:flex;justify-content:center;gap:5px;padding:18px 0;}
.sbars span{display:block;width:6px;background:var(--blue);border-radius:4px;animation:bar 1s ease-in-out infinite alternate;}
.sbars span:nth-child(1){height:14px;animation-delay:0s;}
.sbars span:nth-child(2){height:24px;animation-delay:.1s;}
.sbars span:nth-child(3){height:34px;animation-delay:.2s;}
.sbars span:nth-child(4){height:28px;animation-delay:.3s;}
.sbars span:nth-child(5){height:20px;animation-delay:.4s;}
.sbars span:nth-child(6){height:16px;animation-delay:.5s;}
@keyframes bar{0%{height:8px;}100%{height:34px;}}
.lp{display:flex;gap:6px;padding:8px 14px;flex-wrap:wrap;justify-content:center;}
.lp span{background:#BBDEFB;color:#0D47A1;font-size:.55rem;padding:4px 10px;border-radius:20px;font-weight:700;}
.phist{padding:10px 16px 22px;}
.phist-r{display:flex;justify-content:space-between;font-size:.65rem;padding:8px 0;border-bottom:1px solid #E0E0E0;color:var(--gray);}
.fc{position:absolute;background:rgba(255,255,255,.95);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-radius:16px;padding:10px 18px 10px 14px;box-shadow:0 8px 32px rgba(0,0,0,.18),0 2px 8px rgba(0,0,0,.08);font-size:.75rem;font-weight:700;color:var(--dark);white-space:nowrap;z-index:5;display:flex;align-items:center;gap:10px;border:1px solid rgba(255,255,255,.6);transition:transform .3s,box-shadow .3s;}
.fc .fc-emoji{display:flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:10px;font-size:1rem;flex-shrink:0;}
.fc:hover{transform:scale(1.08)!important;box-shadow:0 12px 40px rgba(0,0,0,.25);}
.fc1{top:80px;left:calc(100% - 15px);right:auto;animation:flt 3.5s ease-in-out infinite;}
.fc1 .fc-emoji{background:linear-gradient(135deg,#FFF3E0,#FFE0B2);}
.fc2{top:130px;right:calc(100% - 15px);left:auto;animation:flt2 4s ease-in-out infinite .5s;}
.fc2 .fc-emoji{background:linear-gradient(135deg,#E3F2FD,#BBDEFB);}
.fc3{top:180px;left:calc(100% - 15px);right:auto;animation:flt 3.8s ease-in-out infinite 1s;}
.fc3 .fc-emoji{background:linear-gradient(135deg,#E8F5E9,#C8E6C9);}
.fc4{top:30px;right:calc(100% - 15px);left:auto;animation:flt2 3.6s ease-in-out infinite .3s;}
.fc4 .fc-emoji{background:linear-gradient(135deg,#FCE4EC,#F8BBD0);}
.fc5{top:230px;right:calc(100% - 15px);left:auto;animation:flt 4.2s ease-in-out infinite .8s;}
.fc5 .fc-emoji{background:linear-gradient(135deg,#F3E5F5,#E1BEE7);}
.fc6{top:280px;left:calc(100% - 15px);right:auto;animation:flt2 3.4s ease-in-out infinite 1.2s;}
.fc6 .fc-emoji{background:linear-gradient(135deg,#E0F7FA,#B2EBF2);}
.fc7{top:330px;right:calc(100% - 15px);left:auto;animation:flt 3.9s ease-in-out infinite .4s;}
.fc7 .fc-emoji{background:linear-gradient(135deg,#FFF8E1,#FFECB3);}
.fc8{top:430px;right:calc(100% - 15px);left:auto;animation:flt2 4.1s ease-in-out infinite .7s;}
.fc8 .fc-emoji{background:linear-gradient(135deg,#E8F5E9,#A5D6A7);}
.fc9{top:380px;left:calc(100% - 15px);right:auto;animation:flt 3.7s ease-in-out infinite 1.1s;}
.fc9 .fc-emoji{background:linear-gradient(135deg,#E8EAF6,#C5CAE9);}
.fc10{top:480px;left:calc(100% - 15px);right:auto;animation:flt2 3.3s ease-in-out infinite .6s;}
.fc10 .fc-emoji{background:linear-gradient(135deg,#FBE9E7,#FFCCBC);}
@keyframes flt{0%,100%{transform:translateY(0);}50%{transform:translateY(-14px);}}
@keyframes flt2{0%,100%{transform:translateY(0) rotate(0deg);}50%{transform:translateY(-12px) rotate(1.5deg);}}

/* STATS */
.stats{background:var(--white);border-bottom:1px solid #E0E0E0;padding:32px 24px;}
.stats-inner{max-width:1000px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;}
.stat{text-align:center;flex:1;position:relative;}
.stat+.stat::before{content:'';position:absolute;left:0;top:15%;height:70%;width:1px;background:#E0E0E0;}
.stat-n{font-size:clamp(1.3rem,3vw,1.8rem);font-weight:900;color:var(--blue);}
.stat-l{font-size:.68rem;text-transform:uppercase;color:var(--gray);font-weight:600;letter-spacing:1px;margin-top:4px;}

/* SECTION */
.sec{padding:clamp(60px,10vw,100px) 24px;}
.sec-tag{display:inline-block;background:rgba(21,101,192,.08);color:var(--blue);font-size:.82rem;font-weight:700;padding:6px 18px;border-radius:50px;margin-bottom:12px;}
.sec-title{font-size:clamp(1.6rem,4vw,2.4rem);font-weight:900;color:var(--dark);margin-bottom:20px;line-height:1.2;}
.sec-sub{color:var(--gray);font-size:clamp(.88rem,2vw,1rem);max-width:600px;line-height:1.7;}
.sec-center{text-align:center;}.sec-center .sec-sub{margin:0 auto 40px;}
.sec-light .sec-tag{background:rgba(255,255,255,.15);color:var(--yellow);}
.sec-light .sec-title,.sec-light .sec-sub{color:var(--white);}

/* HOW IT WORKS */
.how-bg{background:var(--light-blue);}
.steps{display:flex;gap:24px;max-width:1100px;margin:40px auto 0;position:relative;}
.steps::before{content:'';position:absolute;top:50px;left:10%;right:10%;height:2px;border-top:2px dashed #90CAF5;z-index:0;}
.step{flex:1;background:var(--white);border-radius:20px;padding:32px 20px;text-align:center;position:relative;z-index:1;transition:all .3s;}
.step:hover{transform:translateY(-8px);box-shadow:0 16px 40px rgba(21,101,192,.12);}
.step-n{width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,var(--blue),var(--blue2));color:var(--white);font-size:1.15rem;font-weight:800;display:flex;align-items:center;justify-content:center;margin:0 auto 16px;}
.step-i{font-size:2.2rem;margin-bottom:10px;}
.step h3{font-size:1rem;font-weight:700;margin-bottom:6px;}
.step p{font-size:.82rem;color:var(--gray);line-height:1.5;}

/* FEATURE BLOCKS */
.feat-block{padding:clamp(80px,10vw,120px) 24px;}
.feat-inner{max-width:1100px;margin:0 auto;display:flex;align-items:center;gap:clamp(40px,6vw,90px);}
.feat-inner.reverse{flex-direction:row-reverse;}
.feat-visual{flex:1;min-width:0;display:flex;justify-content:center;}
.feat-content{flex:1;min-width:0;}
.feat-content .sec-tag{margin-bottom:12px;}
.feat-content .sec-title{margin-bottom:16px;}
.feat-content p{color:var(--gray);font-size:.95rem;line-height:1.8;margin-bottom:20px;}
.feat-content ul{list-style:none;}
.feat-content ul li{font-size:.92rem;padding:8px 0;display:flex;align-items:center;gap:12px;color:var(--dark);font-weight:600;}
.feat-content ul li::before{content:'✅';font-size:1rem;}
.feat-card{background:var(--white);border-radius:24px;padding:40px;box-shadow:0 12px 50px rgba(21,101,192,.08);transition:transform .3s;width:100%;max-width:360px;}
.feat-card:hover{transform:translateY(-5px);}
.feat-card.green-card{background:linear-gradient(135deg,#43A047,#66BB6A);color:var(--white);text-align:center;}
.feat-card.green-card .gc-icon{font-size:3.5rem;margin-bottom:12px;}
.feat-card.green-card .gc-amt{font-size:3rem;font-weight:900;line-height:1;}
.feat-card.green-card .gc-label{font-size:.95rem;margin-top:8px;opacity:.9;}
.sw{display:flex;justify-content:center;gap:6px;margin-top:20px;}
.sw span{width:6px;border-radius:4px;background:rgba(255,255,255,.5);animation:bar .8s ease-in-out infinite alternate;}
.sw span:nth-child(1){height:16px;animation-delay:0s;}.sw span:nth-child(2){height:24px;animation-delay:.1s;}
.sw span:nth-child(3){height:32px;animation-delay:.2s;}.sw span:nth-child(4){height:28px;animation-delay:.3s;}
.sw span:nth-child(5){height:20px;animation-delay:.4s;}
.lang-card h4{font-size:.95rem;font-weight:700;margin-bottom:16px;color:var(--blue);}
.lang-list{display:flex;flex-wrap:wrap;gap:10px;}
.lang-list span{background:var(--bg-alt);color:var(--blue);padding:10px 20px;border-radius:50px;font-size:.85rem;font-weight:600;border:1px solid #BBDEFB;}
.lang-list span.active{background:var(--blue);color:var(--white);border-color:var(--blue);}
.hist-card h4{font-size:.95rem;font-weight:700;margin-bottom:16px;color:var(--blue);}
.hist-row{display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid #eee;font-size:.9rem;}
.hist-row .app{font-weight:700;}.hist-row .amt{color:var(--green);font-weight:800;}
.hist-total{display:flex;justify-content:space-between;padding:16px 0 0;font-weight:900;color:var(--blue);font-size:1.1rem;margin-top:8px;border-top:2px solid #eee;}
.msg-card h4{font-size:.95rem;font-weight:700;margin-bottom:16px;color:var(--blue);}
.msg-input{background:#F5F5F5;border:2px solid #E0E0E0;border-radius:12px;padding:14px 16px;font-size:.9rem;color:var(--dark);margin-bottom:16px;display:block;width:100%;outline:none;}
.msg-preview{background:var(--bg-alt);border-radius:12px;padding:16px;font-size:.9rem;color:var(--blue);font-weight:600;display:flex;align-items:center;gap:10px;}
.msg-preview::before{content:'🔊';font-size:1.2rem;}

/* PRICING */
.pricing-bg{background:linear-gradient(135deg,var(--dark-blue),var(--blue),var(--blue2));}
.pricing-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;max-width:1000px;margin:40px auto 0;align-items:start;}
.p-card{background:var(--white);border-radius:24px;padding:40px 32px;text-align:center;transition:all .3s;border:2px solid transparent;}
.p-card.pop{border-color:var(--yellow);transform:scale(1.05);box-shadow:0 20px 60px rgba(0,0,0,.2);}
.p-card:hover{transform:translateY(-8px);box-shadow:0 20px 50px rgba(0,0,0,.12);}
.p-card.pop:hover{transform:scale(1.05) translateY(-8px);}
.p-badge{background:var(--yellow);color:var(--dark);font-size:.75rem;font-weight:800;padding:6px 16px;border-radius:20px;display:inline-block;margin-bottom:16px;}
.p-card h3{font-size:1.4rem;font-weight:800;margin-bottom:8px;}
.p-card .price{font-size:2.2rem;font-weight:900;color:var(--blue);margin:12px 0;}
.p-card .price small{font-size:.85rem;font-weight:400;color:var(--gray);}
.p-card ul{list-style:none;text-align:left;margin:24px 0;}
.p-card ul li{font-size:.88rem;padding:8px 0;border-bottom:1px solid #f0f0f0;display:flex;align-items:center;gap:10px;font-weight:600;color:var(--gray);}
.p-card ul li::before{content:'✓';color:var(--green);font-weight:800;font-size:1rem;}
.p-btn{display:inline-block;padding:14px 32px;border-radius:50px;font-weight:700;font-size:.95rem;transition:all .3s;}
.p-btn-o{border:2px solid var(--blue);color:var(--blue);}
.p-btn-y{background:var(--yellow);color:var(--dark);}
.p-btn:hover{transform:translateY(-3px);box-shadow:0 8px 20px rgba(0,0,0,.12);}
.pricing-note{text-align:center;color:rgba(255,255,255,.6);font-size:.85rem;margin-top:32px;}

/* WHO USES */
.who-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;max-width:1100px;margin:40px auto 0;}
.who-card{background:var(--light-blue);border-radius:16px;padding:28px 24px;transition:all .3s;}
.who-card:hover{transform:translateY(-5px);box-shadow:0 12px 30px rgba(21,101,192,.1);background:var(--white);}
.who-card .wc-icon{font-size:2.2rem;margin-bottom:12px;}
.who-card h4{font-size:.95rem;font-weight:700;margin-bottom:6px;}
.who-card p{font-size:.8rem;color:var(--gray);line-height:1.6;}

/* PRIVACY */
.priv-inner{max-width:1000px;margin:0 auto;display:flex;align-items:center;gap:80px;}
.priv-shield{text-align:center;flex-shrink:0;}
.priv-shield-icon{font-size:7rem;animation:shieldPulse 2s ease-in-out infinite;display:block;}
@keyframes shieldPulse{0%,100%{transform:scale(1);filter:drop-shadow(0 0 10px rgba(67,160,71,.3));}50%{transform:scale(1.08);filter:drop-shadow(0 0 30px rgba(67,160,71,.5));}}
.priv-shield-text{color:var(--green);font-weight:800;font-size:.95rem;margin-top:12px;}
.priv-content{flex:1;}
.priv-list{list-style:none;margin-top:24px;}
.priv-list li{font-size:.95rem;padding:10px 0;display:flex;align-items:center;gap:12px;font-weight:600;color:var(--dark);}
.priv-list li::before{content:'✓';color:var(--green);font-weight:800;font-size:1.2rem;}

/* REVIEWS */
.rev-scroll-wrap{overflow:hidden;position:relative;max-width:100vw;margin:40px auto 0;}
.rev-scroll-wrap::before,.rev-scroll-wrap::after{content:'';position:absolute;top:0;bottom:0;width:80px;z-index:2;pointer-events:none;}
.rev-scroll-wrap::before{left:0;background:linear-gradient(to right,var(--light-blue),transparent);}
.rev-scroll-wrap::after{right:0;background:linear-gradient(to left,var(--light-blue),transparent);}
.rev-track{display:flex;gap:28px;animation:revScroll 60s linear infinite;width:max-content;}
.rev-track:hover{animation-play-state:paused;}
@keyframes revScroll{0%{transform:translateX(0);}100%{transform:translateX(-50%);}}
.rev-card{background:var(--white);border-radius:24px;padding:36px 28px;border-bottom:4px solid transparent;transition:all .3s;box-shadow:0 4px 20px rgba(0,0,0,.05);min-width:320px;max-width:320px;flex-shrink:0;cursor:pointer;text-decoration:none;color:inherit;display:block;}
.rev-card:hover{transform:translateY(-5px);border-bottom-color:var(--blue);box-shadow:0 16px 40px rgba(0,0,0,.1);}
.rev-stars{color:var(--yellow);font-size:1.2rem;margin-bottom:16px;}
.rev-text{font-size:.9rem;color:var(--gray);line-height:1.7;margin-bottom:24px;font-style:italic;}
.rev-user{display:flex;align-items:center;gap:16px;}
.rev-av{width:46px;height:46px;border-radius:50%;background:var(--blue);color:var(--white);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1rem;overflow:hidden;flex-shrink:0;}\nimg.rev-av{border:2px solid #e0e0e0;}
.rev-name{font-size:.9rem;font-weight:700;color:var(--dark);}
.rev-date{font-size:.75rem;color:var(--gray);}

/* FINAL CTA */
.cta-section{background:linear-gradient(135deg,var(--dark-blue),var(--blue),var(--blue2));text-align:center;padding:clamp(80px,10vw,140px) 24px;position:relative;overflow:hidden;}
.cta-section::before{content:'';position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.05) 1px,transparent 1px);background-size:24px 24px;}
.cta-logo{width:88px;height:88px;border-radius:24px;margin:0 auto 32px;box-shadow:0 12px 40px rgba(0,0,0,.3);}
.cta-section h2{font-size:clamp(1.8rem,4vw,2.8rem);font-weight:900;color:var(--white);margin-bottom:20px;position:relative;}
.cta-section h2 .yellow{color:var(--yellow);}
.cta-section .cta-sub{color:rgba(255,255,255,.8);max-width:600px;margin:0 auto 40px;font-size:clamp(.95rem,2vw,1.1rem);line-height:1.7;position:relative;}
.cta-big-btn{display:inline-flex;align-items:center;gap:16px;background:var(--white);padding:18px 40px;border-radius:50px;box-shadow:0 16px 50px rgba(0,0,0,.25);transition:all .3s;position:relative;}
.cta-big-btn:hover{transform:translateY(-4px);box-shadow:0 24px 60px rgba(0,0,0,.35);}
.cta-big-btn img{height:36px;}
.cta-big-btn span{font-size:1.05rem;font-weight:800;color:var(--dark);}
.cta-note{color:rgba(255,255,255,.5);font-size:.82rem;margin-top:20px;position:relative;font-weight:600;}

/* FOOTER */
.footer{background:var(--dark);padding:80px 24px 40px;}
.footer-inner{max-width:1100px;margin:0 auto;}
.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1.5fr;gap:40px;margin-bottom:60px;}
.footer-brand{display:flex;align-items:center;gap:12px;margin-bottom:16px;}
.footer-brand img{width:40px;height:40px;border-radius:10px;}
.footer-brand span{color:var(--white);font-weight:800;font-size:1.1rem;}
.footer p.fb-sub{color:rgba(255,255,255,.5);font-size:.85rem;line-height:1.7;margin-bottom:8px;}
.footer h4{color:var(--white);font-size:.95rem;font-weight:700;margin-bottom:20px;}
.footer-col a{display:block;color:rgba(255,255,255,.6);font-size:.85rem;padding:6px 0;transition:color .3s;font-weight:600;}
.footer-col a:hover{color:var(--yellow);}
.footer-play{display:inline-flex;align-items:center;gap:12px;background:rgba(255,255,255,.08);padding:12px 20px;border-radius:12px;margin-top:10px;transition:background .3s;}
.footer-play:hover{background:rgba(255,255,255,.15);}
.footer-play img{height:30px;}
.footer-play span{color:var(--white);font-size:.82rem;font-weight:700;}
.footer-rating{color:rgba(255,255,255,.5);font-size:.78rem;margin-top:12px;font-weight:600;}
.footer-bottom{border-top:1px solid rgba(255,255,255,.08);padding-top:24px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px;}
.footer-bottom p{color:rgba(255,255,255,.4);font-size:.8rem;}
.footer-bottom a{color:rgba(255,255,255,.4);font-size:.8rem;transition:color .3s;}
.footer-bottom a:hover{color:var(--yellow);}

/* RESPONSIVE */
@media(min-width:1441px){.hero-inner{max-width:1300px;}.phone-mockup{width:310px;}.feat-card{max-width:400px;}}
@media(max-width:1024px){.hero-inner{gap:50px;}.hero-phone{flex:0 0 380px;min-height:520px;}.feat-inner{gap:50px;}.steps{flex-wrap:wrap;}.steps::before{display:none;}.step{flex:0 0 calc(50% - 12px);}.who-grid{grid-template-columns:repeat(2,1fr);}.pricing-grid{grid-template-columns:repeat(3,1fr);gap:16px;}.p-card{padding:32px 20px;}}
@media(max-width:900px){
.nav-links{display:none;}.hamburger{display:flex;}.mobile-menu{display:flex;}.hero{padding:120px 20px 80px;min-height:auto;overflow:visible;}
.hero-inner{flex-direction:column;text-align:center;gap:60px;}.hero-body{margin:0 auto 32px;}.hero-btns{justify-content:center;}.trust-row{justify-content:center;}
.hero-phone{flex:0 0 auto;width:100%;display:flex;justify-content:center;}
.phone-mockup{transform:scale(0.95);transform-origin:center top;margin-bottom:80px;}
.fc{padding:12px 18px;font-size:0.85rem;border:2px solid var(--white);box-shadow:0 12px 40px rgba(0,0,0,.25);width:max-content;max-width:220px;}
.fc .fc-emoji{width:34px;height:34px;font-size:1.1rem;}
.fc2, .fc4, .fc5, .fc7, .fc8{right:auto;left:-25px;}
.fc1, .fc3, .fc6, .fc9, .fc10{left:auto;right:-25px;}
.fc4{top:30px;z-index:10;}
.fc1{top:80px;z-index:11;}
.fc2{top:130px;z-index:12;}
.fc3{top:180px;z-index:13;}
.fc5{top:230px;z-index:14;}
.fc6{top:280px;z-index:15;}
.fc7{top:330px;z-index:16;}
.fc9{top:380px;z-index:17;}
.fc8{top:430px;z-index:18;}
.fc10{top:480px;z-index:19;}
.feat-inner,.feat-inner.reverse{flex-direction:column;text-align:center;}.feat-content ul li{justify-content:center;}.rev-grid{grid-template-columns:1fr 1fr;}
.priv-inner{flex-direction:column;text-align:center;gap:40px;}.priv-list li{justify-content:center;}
}
@media(max-width:768px){
.phone-mockup{transform:scale(0.9);margin-bottom:60px;}
.pricing-grid{grid-template-columns:1fr;max-width:400px;}.p-card.pop{transform:none;}.p-card.pop:hover{transform:translateY(-8px);}
.stats-inner{flex-wrap:wrap;}.stat{flex:0 0 33.33%;}.stat:nth-child(4),.stat:nth-child(5){flex:0 0 50%;}.stat+.stat::before{display:none;}
.footer-grid{grid-template-columns:1fr 1fr;}.step{flex:0 0 100%;}
}
@media(max-width:576px){
.hero{padding:100px 16px 40px;}.hero-btns{flex-direction:column;width:100%;align-items:center;}.btn-yellow,.btn-ghost{width:100%;justify-content:center;}
.phone-mockup{transform:scale(0.82);margin-bottom:20px;}
.who-grid{grid-template-columns:1fr;}.rev-grid{grid-template-columns:1fr;}.footer-grid{grid-template-columns:1fr;}
.cta-big-btn{flex-direction:column;gap:12px;padding:16px 28px;}.nav-cta{padding:8px 16px;font-size:0.78rem;}
}
@media(max-width:400px){
html{font-size:14px;}
.phone-mockup{transform:scale(0.75);margin-bottom:-10px;}
.hero{padding:80px 12px 30px;}.feat-block{padding:60px 16px;}.feat-card{padding:24px;}
}
"""

html = f"""<!DOCTYPE html>
<html lang="hi-Latn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PayEcho – UPI Mobile Soundbox | Aapka Phone Hi Aapka Soundbox Hai</title>
<meta name="description" content="Har UPI payment par turant awaaz. Kirana, dukaan, café — PayEcho aapke phone ko smart UPI Soundbox bana deta hai. Free download!">
<link rel="icon" type="image/jpeg" href="data:image/jpeg;base64,{logo_b64}">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800;900&family=Noto+Sans+Devanagari:wght@400;600;700&display=swap" rel="stylesheet">
<style>
{css}
</style>
</head>
<body>

<nav class="navbar" id="navbar">
<div class="nav-inner">
<a href="#" class="nav-brand">
<img src="data:image/jpeg;base64,{logo_b64}" alt="PayEcho Logo">
<span>Pay<span class="echo">Echo</span></span>
</a>
<div class="nav-links">
<a href="#features">Features</a>
<a href="#how">How It Works</a>
<a href="#pricing">Pricing</a>
<a href="#reviews">Reviews</a>
</div>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" class="nav-cta">Download Free</a>
<div class="hamburger" id="hamburger" onclick="toggleMenu()">
<span></span><span></span><span></span>
</div>
</div>
</nav>

<div class="mobile-menu" id="mobileMenu">
<a href="#features" onclick="toggleMenu()">Features</a>
<a href="#how" onclick="toggleMenu()">How It Works</a>
<a href="#pricing" onclick="toggleMenu()">Pricing</a>
<a href="#reviews" onclick="toggleMenu()">Reviews</a>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" class="nav-cta" onclick="toggleMenu()">Download Free</a>
</div>

<section class="hero">
<div class="hero-inner">
<div class="hero-text hero-anim">
<div class="hero-badge">🔊 India's Free UPI Soundbox App</div>
<h1 class="hindi">Aapka Phone Hi<br><span class="yellow">Aapka Soundbox Hai</span></h1>
<p class="hero-subtitle hindi">Har UPI payment par turant awaaz — free mein</p>
<p class="hero-body hindi">Kirana, dukaan, café — jab bhi koi payment aata hai, PayEcho turant amount bolta hai. Koi hardware nahi kharidna, koi monthly charge nahi.</p>
<div class="hero-btns">
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" class="btn-yellow">
<img src="data:image/png;base64,{play_b64}" alt="Google Play"> Download Free on Google Play
</a>
<a href="#how" class="btn-ghost">See How It Works ↓</a>
</div>
<div class="trust-row">
<span class="trust-item">⭐ 5.0 Rating</span>
<span class="trust-item">🆓 Free</span>
<span class="trust-item">⚡ 1 Min Setup</span>
<span class="trust-item">🔒 Secure & Private</span>
</div>
</div>
<div class="hero-phone reveal">
<div class="phone-mockup">
<div class="fc fc1"><span class="fc-emoji">{icon_1}</span> Instant Alert</div>
<div class="fc fc2"><span class="fc-emoji">{icon_2}</span> 8+ Languages</div>
<div class="fc fc3"><span class="fc-emoji">{icon_3}</span> History Tracked</div>
<div class="fc fc4"><span class="fc-emoji">{icon_4}</span> Volume Control</div>
<div class="fc fc5"><span class="fc-emoji">{icon_5}</span> Custom Messages</div>
<div class="fc fc6"><span class="fc-emoji">{icon_6}</span> QR Code Display</div>
<div class="fc fc7"><span class="fc-emoji">{icon_7}</span> Staff Support</div>
<div class="fc fc8"><span class="fc-emoji">{icon_8}</span> 100% Secure</div>
<div class="fc fc9"><span class="fc-emoji">{icon_9}</span> Always Free</div>
<div class="fc fc10"><span class="fc-emoji">{icon_10}</span> All UPI Apps</div>
<div class="phone-screen">
<div class="ph-head">
<img src="data:image/jpeg;base64,{logo_b64}" alt="PayEcho">
<div class="ph-head-text">
<div class="t">PayEcho</div>
<div class="s">UPI Mobile Soundbox</div>
</div>
</div>
<div class="ph-pay">
<div class="ck" style="display:flex;justify-content:center;margin-bottom:6px;"><img src="data:image/png;base64,{mobile_app_b64}" style="height:45px;" alt="App"></div>
<div class="lb">Payment Received!</div>
<div class="am">₹ 250</div>
<div class="hi hindi">दो सौ पचास रुपये प्राप्त हुए</div>
</div>
<div class="sbars"><span></span><span></span><span></span><span></span><span></span><span></span></div>
<div class="lp">
<span>🇮🇳 <span class="hindi">हिंदी</span></span>
<span><span class="hindi">मराठी</span></span>
<span>English</span>
<span><span class="hindi">தமிழ்</span></span>
</div>
<div class="phist">
<div class="phist-r"><span class="app">GPay</span><span class="amt">₹150</span></div>
<div class="phist-r"><span class="app">PhonePe</span><span class="amt">₹500</span></div>
<div class="phist-r"><span class="app">Paytm</span><span class="amt">₹75</span></div>
</div>
</div>
</div>
</div>
</div>
</section>

<section class="stats reveal">
<div class="stats-inner">
<div class="stat"><div class="stat-n" style="display:flex;align-items:center;justify-content:center;gap:6px;">5.0 <img src="data:image/png;base64,{star_b64}" alt="Star" style="height:28px;mix-blend-mode:multiply;"></div><div class="stat-l">Stars</div></div>
<div class="stat"><div class="stat-n">500+</div><div class="stat-l">Downloads</div></div>
<div class="stat"><div class="stat-n">100%</div><div class="stat-l">Free</div></div>
<div class="stat"><div class="stat-n">1 Min</div><div class="stat-l">Setup</div></div>
<div class="stat"><div class="stat-n">8+</div><div class="stat-l">Languages</div></div>
</div>
</section>

<section class="sec how-bg reveal" id="how">
<div class="sec-center">
<span class="sec-tag">⚙️ Simple Setup</span>
<h2 class="sec-title hindi">Sirf 4 Steps Mein Ready — 1 Minute Mein!</h2>
</div>
<div class="steps">
<div class="step reveal"><div class="step-n">1</div><div class="step-i"><img src="data:image/png;base64,{step1_b64}" style="height:48px;mix-blend-mode:multiply;margin:0 auto;" alt="Install"></div><h3>Install</h3><p class="hindi">Google Play se free download</p></div>
<div class="step reveal"><div class="step-n">2</div><div class="step-i"><img src="data:image/png;base64,{step2_b64}" style="height:48px;mix-blend-mode:multiply;margin:0 auto;" alt="Permission"></div><h3>Permission</h3><p class="hindi">Notification access allow karo</p></div>
<div class="step reveal"><div class="step-n">3</div><div class="step-i"><img src="data:image/png;base64,{step3_b64}" style="height:48px;mix-blend-mode:multiply;margin:0 auto;" alt="Language"></div><h3>Language</h3><p class="hindi">Apni language chuno (8+ Indian languages)</p></div>
<div class="step reveal"><div class="step-n">4</div><div class="step-i"><img src="data:image/png;base64,{step4_b64}" style="height:48px;mix-blend-mode:multiply;margin:0 auto;" alt="Done"></div><h3>Done!</h3><p class="hindi">Payments sunna shuru!</p></div>
</div>
</section>

<section class="feat-block reveal" id="features">
<div class="feat-inner">
<div class="feat-content">
<span class="sec-tag">⚡ Instant Alerts</span>
<h2 class="sec-title hindi">Payment Aate Hi Phone Bolta Hai</h2>
<p class="hindi">Jaise hi koi UPI payment aata hai — chahe GPay ho, PhonePe ho, Paytm ho ya BHIM — aapka phone seedha bolta hai kitna amount aaya. Screen dekhne ki zarurat bilkul nahi.</p>
<ul>
<li>Works with ALL UPI apps</li>
<li>Alert within milliseconds of payment</li>
<li>Clear and loud voice announcement</li>
</ul>
</div>
<div class="feat-visual">
<div class="feat-card green-card reveal">
<div class="gc-icon"><img src="data:image/png;base64,{mobile_app_b64}" style="height:56px;margin:0 auto;" alt="App"></div>
<div class="gc-amt">₹ 500</div>
<div class="gc-label hindi">Payment Received</div>
<div class="sw"><span></span><span></span><span></span><span></span><span></span></div>
</div>
</div>
</div>
</section>

<section class="feat-block how-bg reveal">
<div class="feat-inner reverse">
<div class="feat-content">
<span class="sec-tag"><img src="data:image/png;base64,{lang_icon_b64}" style="height:16px;vertical-align:middle;mix-blend-mode:multiply;"> Multiple Languages</span>
<h2 class="sec-title hindi">Apni Bhasha Mein Suno</h2>
<p class="hindi">Hindi, Marathi, Telugu, Tamil, Kannada, Bengali, Gujarati — 8 se zyada Indian languages mein payment alert suniye. Apne customers ko unki bhasha mein acknowledge karein.</p>
<ul>
<li>8+ Indian regional languages</li>
<li>Change language anytime in settings</li>
<li>Clear pronunciation of ₹ amounts</li>
</ul>
</div>
<div class="feat-visual">
<div class="feat-card lang-card reveal">
<h4>Select Language</h4>
<div class="lang-list">
<span class="active hindi">हिंदी (Hindi)</span>
<span class="hindi">मराठी (Marathi)</span>
<span>English</span>
<span class="hindi">தமிழ் (Tamil)</span>
<span class="hindi">తెలుగు (Telugu)</span>
<span class="hindi">ಕన్నಡ (Kannada)</span>
<span class="hindi">বাংলা (Bengali)</span>
</div>
</div>
</div>
</div>
</section>

<section class="feat-block reveal">
<div class="feat-inner">
<div class="feat-content">
<span class="sec-tag"><img src="data:image/png;base64,{hist_icon_b64}" style="height:16px;vertical-align:middle;mix-blend-mode:multiply;"> Track Payments</span>
<h2 class="sec-title hindi">Sab Payments Ek Jagah</h2>
<p class="hindi">Din bhar ke sab UPI payments ki history app ke andar hi milegi. Daily, weekly, monthly totals — without any spreadsheet or manual record-keeping.</p>
<ul>
<li>Daily / Weekly / Monthly records</li>
<li>Filter by UPI app (GPay, PhonePe etc.)</li>
<li>Quick total summary on home screen</li>
</ul>
</div>
<div class="feat-visual">
<div class="feat-card hist-card reveal">
<h4>Today's Payments</h4>
<div class="hist-row"><span class="app">Google Pay</span><span class="amt">+ ₹450</span></div>
<div class="hist-row"><span class="app">PhonePe</span><span class="amt">+ ₹1,200</span></div>
<div class="hist-row"><span class="app">Paytm</span><span class="amt">+ ₹320</span></div>
<div class="hist-row"><span class="app">Amazon Pay</span><span class="amt">+ ₹85</span></div>
<div class="hist-total"><span>Total</span><span>₹ 2,055</span></div>
</div>
</div>
</div>
</section>

<section class="feat-block how-bg reveal">
<div class="feat-inner reverse">
<div class="feat-content">
<span class="sec-tag"><img src="data:image/png;base64,{msg_icon_b64}" style="height:16px;vertical-align:middle;mix-blend-mode:multiply;"> Custom Messages</span>
<h2 class="sec-title hindi">Apna Personal Touch Add Karo</h2>
<p class="hindi">Payment announce hone ke baad apna custom thank-you message set karo. Customers ko personalized experience do — bilkul apne style mein.</p>
<ul>
<li>Custom audio message after amount</li>
<li>Set your shop name, thank you line</li>
<li>Volume and speed adjustable</li>
</ul>
</div>
<div class="feat-visual">
<div class="feat-card msg-card reveal">
<h4>Custom Alert Message</h4>
<input type="text" class="msg-input hindi" value="Dhanyavaad! Sharma Ji Store mein fir aana." readonly>
<div class="msg-preview hindi">₹500 prapt hue. Dhanyavaad! Sharma Ji Store mein fir aana.</div>
</div>
</div>
</div>
</section>

<section class="sec pricing-bg sec-light reveal" id="pricing">
<div class="sec-center">
<span class="sec-tag">💎 Subscription Plans</span>
<h2 class="sec-title hindi">Premium Features, Bahut Kam Daam Mein</h2>
<p class="sec-sub hindi">Koi hidden charge nahi — sirf aapko jo chahiye wo lo</p>
</div>
<div class="pricing-grid">
<div class="p-card reveal">
<h3>Free</h3>
<div class="price">₹0 <small>/ always</small></div>
<ul>
<li>Basic UPI voice alerts</li>
<li>Hindi language</li>
<li>7-day payment history</li>
<li>Single device</li>
</ul>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" class="p-btn p-btn-o">Get Started Free</a>
</div>
<div class="p-card pop reveal">
<span class="p-badge">Most Popular</span>
<h3>Pro</h3>
<div class="price">₹49 <small>/ month</small></div>
<ul>
<li>All 8+ Indian languages</li>
<li>Custom thank-you message</li>
<li>Unlimited payment history</li>
<li>Volume & speed control</li>
<li>QR Code display</li>
<li>2 staff devices</li>
</ul>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" class="p-btn p-btn-y">Get Pro</a>
</div>
<div class="p-card reveal">
<h3>Business</h3>
<div class="price">₹99 <small>/ month</small></div>
<ul>
<li>Everything in Pro</li>
<li>Up to 5 staff devices</li>
<li>Priority customer support</li>
<li>Early access to new features</li>
</ul>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" class="p-btn p-btn-o">Get Business</a>
</div>
</div>
<p class="pricing-note">All plans available on Google Play. Cancel anytime.</p>
</section>

<section class="sec reveal">
<div class="sec-center">
<span class="sec-tag"><img src="data:image/png;base64,{people_b64}" style="height:16px;vertical-align:middle;mix-blend-mode:multiply;"> Perfect For</span>
<h2 class="sec-title hindi">Har Chhote Business Ke Liye Bana Hai</h2>
</div>
<div class="who-grid">
<div class="who-card reveal"><div class="wc-icon"><img src="data:image/png;base64,{who1_b64}" style="height:40px;mix-blend-mode:multiply;"></div><h4>Kirana Store</h4><p class="hindi">Stock dekhte waqt payment ki awaaz sun lo</p></div>
<div class="who-card reveal"><div class="wc-icon"><img src="data:image/png;base64,{who2_b64}" style="height:40px;mix-blend-mode:multiply;"></div><h4>Caf&eacute; &amp; Restaurant</h4><p class="hindi">Customers serve karte waqt payment confirm karo</p></div>
<div class="who-card reveal"><div class="wc-icon"><img src="data:image/png;base64,{who3_b64}" style="height:40px;mix-blend-mode:multiply;"></div><h4>Delivery Counter</h4><p class="hindi">Orders handle karte waqt missed payments avoid karo</p></div>
<div class="who-card reveal"><div class="wc-icon"><img src="data:image/png;base64,{who4_b64}" style="height:40px;mix-blend-mode:multiply;"></div><h4>Salon &amp; Parlour</h4><p class="hindi">Client ke saath busy ho, phone mat dekho</p></div>
<div class="who-card reveal"><div class="wc-icon"><img src="data:image/png;base64,{who5_b64}" style="height:40px;mix-blend-mode:multiply;"></div><h4>Clinic &amp; Doctor</h4><p class="hindi">Patient attention mein payments track karo</p></div>
<div class="who-card reveal"><div class="wc-icon"><img src="data:image/png;base64,{who6_b64}" style="height:40px;mix-blend-mode:multiply;"></div><h4>Gym &amp; Studio</h4><p class="hindi">Members ko attend karte waqt payment confirm karo</p></div>
<div class="who-card reveal"><div class="wc-icon"><img src="data:image/png;base64,{who7_b64}" style="height:40px;mix-blend-mode:multiply;"></div><h4>Coaching Classes</h4><p class="hindi">Students padhate waqt fee payments suno</p></div>
<div class="who-card reveal"><div class="wc-icon"><img src="data:image/png;base64,{who8_b64}" style="height:40px;mix-blend-mode:multiply;"></div><h4>Street Vendor</h4><p class="hindi">Outdoor environment mein loud alerts kaam aate hain</p></div>
<div class="who-card reveal"><div class="wc-icon"><img src="data:image/png;base64,{who9_b64}" style="height:40px;mix-blend-mode:multiply;"></div><h4>Repair Shop</h4><p class="hindi">Haath gande ho tab bhi phone touch karne ki zarurat nahi</p></div>
<div class="who-card reveal"><div class="wc-icon"><img src="data:image/png;base64,{who10_b64}" style="height:40px;mix-blend-mode:multiply;"></div><h4>Sabzi &amp; Fruit</h4><p class="hindi">Busy market mein har payment confirm karo</p></div>
<div class="who-card reveal"><div class="wc-icon"><img src="data:image/png;base64,{who11_b64}" style="height:40px;mix-blend-mode:multiply;"></div><h4>Online Seller</h4><p class="hindi">Multiple orders handle karte waqt payments track karo</p></div>
<div class="who-card reveal"><div class="wc-icon"><img src="data:image/png;base64,{who12_b64}" style="height:40px;mix-blend-mode:multiply;"></div><h4>General Store</h4><p class="hindi">Counter par busy raho, payments auto-track hoti rahein</p></div>
</div>
</section>

<section class="sec reveal">
<div class="priv-inner">
<div class="priv-shield reveal">
<div class="priv-shield-icon">🛡️</div>
<div class="priv-shield-text">100% Secure</div>
</div>
<div class="priv-content reveal">
<span class="sec-tag"><img src="data:image/png;base64,{privacy_b64}" style="height:16px;vertical-align:middle;mix-blend-mode:multiply;"> Your Privacy Matters</span>
<h2 class="sec-title hindi">Aapka Data Sirf Aapke Phone Mein</h2>
<p class="hindi" style="color:var(--gray);font-size:.95rem;line-height:1.7;">PayEcho sirf aapke phone ki notifications padh ke kaam karta hai. Koi bank account access nahi, koi SMS scan nahi, koi server pe data nahi jaata. Sab kuch aapke device par locally process hota hai.</p>
<ul class="priv-list hindi">
<li>Bank account access nahi karta</li>
<li>SMS messages nahi padhta</li>
<li>No data shared with third parties</li>
<li>Works locally on your device only</li>
<li>Google Play Verified — Rated for 3+</li>
</ul>
</div>
</div>
</section>

<section class="sec how-bg reveal" id="reviews">
<div class="sec-center">
<span class="sec-tag"><img src="data:image/png;base64,{wus_b64}" style="height:16px;vertical-align:middle;mix-blend-mode:multiply;"> What Users Say</span>
<h2 class="sec-title">5 Star Reviews — Google Play Par</h2>
</div>
<div class="rev-scroll-wrap">
<div class="rev-track">
{review_cards_html}
</div>
</div>
</div>
</section>

<section class="cta-section reveal">
<img src="data:image/jpeg;base64,{logo_b64}" class="cta-logo reveal" alt="PayEcho">
<h2 class="hindi reveal">Aaj Hi Start Karo — <span class="yellow">Bilkul Free Mein!</span></h2>
<p class="cta-sub hindi reveal">Hardware soundbox pe ₹3000-5000 mat barbaad karo. Aapka phone hi soundbox ban sakta hai — abhi download karo.</p>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" class="cta-big-btn reveal">
<img src="data:image/png;base64,{play_b64}" alt="Google Play">
<span>Download on Google Play</span>
</a>
<p class="cta-note reveal">Free · Plans from ₹49 · Android 5.0+</p>
</section>

<footer class="footer">
<div class="footer-inner">
<div class="footer-grid">
<div>
<div class="footer-brand"><img src="data:image/jpeg;base64,{logo_b64}" alt="PayEcho"><span>PayEcho</span></div>
<p class="fb-sub">UPI Mobile Soundbox</p>
<p class="fb-sub hindi">Made with ❤️ in Maharashtra 🇮🇳</p>
</div>
<div class="footer-col">
<h4>Product</h4>
<a href="#features">Features</a>
<a href="#how">How It Works</a>
<a href="#pricing">Pricing</a>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert">Download</a>
</div>
<div class="footer-col">
<h4>Support</h4>
<a href="https://thinktankapps.netlify.app/privacy">Privacy Policy</a>
<a href="mailto:bhavarkaran888@gmail.com">Contact Us</a>
<a href="https://karanbhavar.netlify.app/">Developer</a>
</div>
<div class="footer-col">
<h4>Get The App</h4>
<a href="https://play.google.com/store/apps/details?id=com.bhava.upialert" class="footer-play">
<img src="data:image/png;base64,{play_b64}" alt="Play Store"><span>Google Play</span>
</a>
<p class="footer-rating">5.0 ★ · 500+ Downloads</p>
</div>
</div>
<div class="footer-bottom">
<p>© 2026 Think Tank Apps. All rights reserved.</p>
<div>
<a href="https://thinktankapps.netlify.app/privacy">Privacy Policy</a> &nbsp;|&nbsp; <a href="mailto:bhavarkaran888@gmail.com">Support</a>
</div>
</div>
</div>
</footer>

<script>
window.addEventListener('scroll',()=>{{
  document.getElementById('navbar').classList.toggle('scrolled',window.scrollY>50);
}});

const obs=new IntersectionObserver((entries)=>{{
  entries.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('visible');obs.unobserve(e.target);}}}});
}},{{threshold:0.1}});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));

function toggleMenu(){{
  document.getElementById('hamburger').classList.toggle('active');
  document.getElementById('mobileMenu').classList.toggle('active');
  document.body.style.overflow=document.getElementById('mobileMenu').classList.contains('active')?'hidden':'';
}}
</script>
</body>
</html>"""

output_path = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"✅ PhonePe-inspired landing page created at: {output_path}")
