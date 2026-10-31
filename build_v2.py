import base64, os

def get_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

logo_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\.gemini\antigravity\brain\c200eeb1-5eb2-4df8-a23c-4225cec1b3ae\media__1773310644442.jpg")
play_b64 = get_b64(r"C:\Users\AKSHAY BHAWAR\.gemini\antigravity\brain\c200eeb1-5eb2-4df8-a23c-4225cec1b3ae\media__1773310650794.jpg")

# Build CSS
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
.hero{background:linear-gradient(135deg,var(--dark-blue) 0%,var(--blue) 50%,var(--blue2) 100%);position:relative;padding:140px 24px 100px;min-height:95vh;display:flex;align-items:center;overflow:hidden;}
.hero::before{content:'';position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.06) 1px,transparent 1px);background-size:28px 28px;}
.hero-inner{max-width:1200px;margin:0 auto;display:flex;align-items:center;gap:80px;position:relative;z-index:2;width:100%;}
.hero-text{flex:1;min-width:0;}
.hero-phone{flex:0 0 300px;position:relative;}
.hero-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);border-radius:50px;padding:8px 20px;margin-bottom:24px;font-size:.82rem;font-weight:600;color:rgba(255,255,255,.9);}
.hero h1{font-size:clamp(2rem,5vw,3.5rem);font-weight:900;color:var(--white);line-height:1.15;margin-bottom:16px;}
.hero h1 .yellow{color:var(--yellow);}
.hero-subtitle{font-size:clamp(1rem,2.5vw,1.15rem);color:rgba(255,255,255,.85);margin-bottom:16px;font-weight:600;}
.hero-body{color:rgba(255,255,255,.7);font-size:clamp(.88rem,2vw,.98rem);line-height:1.8;margin-bottom:32px;max-width:520px;}
.hero-btns{display:flex;gap:16px;flex-wrap:wrap;margin-bottom:32px;}
.btn-yellow{background:var(--yellow);color:var(--dark);padding:14px 28px;border-radius:50px;font-weight:700;font-size:.92rem;display:inline-flex;align-items:center;gap:10px;transition:all .3s;}
.btn-yellow img{height:22px;}
.btn-yellow:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(253,216,53,.4);}
.btn-ghost{border:2px solid rgba(255,255,255,.4);color:var(--white);padding:14px 28px;border-radius:50px;font-weight:600;font-size:.92rem;transition:all .3s;}
.btn-ghost:hover{background:rgba(255,255,255,.1);transform:translateY(-3px);}
.trust-row{display:flex;gap:24px;flex-wrap:wrap;}
.trust-item{color:rgba(255,255,255,.75);font-size:.8rem;font-weight:600;display:flex;align-items:center;gap:6px;}

/* PHONE MOCKUP */
.phone-mockup{width:260px;background:var(--white);border-radius:40px;padding:8px;box-shadow:0 40px 100px rgba(0,0,0,.4);animation:floatPhone 3.5s ease-in-out infinite;position:relative;margin:0 auto;}
@keyframes floatPhone{0%,100%{transform:translateY(0) rotate(.5deg);}50%{transform:translateY(-18px) rotate(-.5deg);}}
.phone-screen{background:var(--light-blue);border-radius:32px;overflow:hidden;}
.ph-head{background:linear-gradient(135deg,var(--blue),var(--blue2));padding:16px 14px;display:flex;align-items:center;gap:10px;}
.ph-head img{width:28px;height:28px;border-radius:7px;}
.ph-head-text{color:var(--white);}
.ph-head-text .t{font-size:.72rem;font-weight:700;}
.ph-head-text .s{font-size:.5rem;opacity:.8;}
.ph-pay{background:linear-gradient(135deg,#43A047,#66BB6A);margin:12px;border-radius:16px;padding:16px;text-align:center;color:var(--white);animation:pulse 2.5s ease-in-out infinite;}
@keyframes pulse{0%,100%{transform:scale(1);}50%{transform:scale(1.03);}}
.ph-pay .ck{font-size:1.4rem;}.ph-pay .lb{font-size:.65rem;font-weight:600;margin-top:4px;}
.ph-pay .am{font-size:1.5rem;font-weight:900;}.ph-pay .hi{font-size:.55rem;margin-top:4px;}
.sbars{display:flex;justify-content:center;gap:4px;padding:12px 0;}
.sbars span{display:block;width:5px;background:var(--blue);border-radius:3px;animation:bar 1s ease-in-out infinite alternate;}
.sbars span:nth-child(1){height:12px;animation-delay:0s;}
.sbars span:nth-child(2){height:20px;animation-delay:.1s;}
.sbars span:nth-child(3){height:28px;animation-delay:.2s;}
.sbars span:nth-child(4){height:24px;animation-delay:.3s;}
.sbars span:nth-child(5){height:18px;animation-delay:.4s;}
.sbars span:nth-child(6){height:14px;animation-delay:.5s;}
@keyframes bar{0%{height:6px;}100%{height:28px;}}
.lp{display:flex;gap:4px;padding:6px 12px;flex-wrap:wrap;justify-content:center;}
.lp span{background:#BBDEFB;color:#0D47A1;font-size:.5rem;padding:3px 8px;border-radius:20px;font-weight:600;}
.phist{padding:8px 12px 16px;}
.phist-r{display:flex;justify-content:space-between;font-size:.55rem;padding:4px 0;border-bottom:1px solid #E0E0E0;color:var(--gray);}
.fc{position:absolute;background:var(--white);border-radius:14px;padding:10px 16px;box-shadow:0 8px 24px rgba(0,0,0,.15);font-size:.72rem;font-weight:700;color:var(--dark);white-space:nowrap;z-index:5;}
.fc1{top:-10px;right:-65px;animation:flt 3.5s ease-in-out infinite;}
.fc2{bottom:70px;left:-75px;animation:flt 4s ease-in-out infinite .5s;}
.fc3{bottom:15px;right:-55px;animation:flt 3.8s ease-in-out infinite 1s;}
@keyframes flt{0%,100%{transform:translateY(0);}50%{transform:translateY(-12px);}}

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
.feat-block{padding:clamp(60px,10vw,100px) 24px;}
.feat-inner{max-width:1100px;margin:0 auto;display:flex;align-items:center;gap:clamp(40px,6vw,80px);}
.feat-inner.reverse{flex-direction:row-reverse;}
.feat-visual{flex:1;min-width:0;}
.feat-content{flex:1;min-width:0;}
.feat-content .sec-tag{margin-bottom:12px;}
.feat-content .sec-title{margin-bottom:16px;}
.feat-content p{color:var(--gray);font-size:.92rem;line-height:1.8;margin-bottom:20px;}
.feat-content ul{list-style:none;}
.feat-content ul li{font-size:.9rem;padding:6px 0;display:flex;align-items:center;gap:10px;color:var(--dark);}
.feat-content ul li::before{content:'✅';font-size:.85rem;}
.feat-card{background:var(--white);border-radius:24px;padding:32px;box-shadow:0 8px 40px rgba(0,0,0,.08);transition:transform .3s;}
.feat-card:hover{transform:scale(1.02);}
.feat-card.green-card{background:linear-gradient(135deg,#43A047,#66BB6A);color:var(--white);text-align:center;}
.feat-card.green-card .gc-icon{font-size:3rem;margin-bottom:12px;}
.feat-card.green-card .gc-amt{font-size:2.5rem;font-weight:900;}
.feat-card.green-card .gc-label{font-size:.9rem;margin-top:8px;}
.sw{display:flex;justify-content:center;gap:6px;margin-top:16px;}
.sw span{width:6px;border-radius:4px;background:rgba(255,255,255,.5);animation:bar .8s ease-in-out infinite alternate;}
.sw span:nth-child(1){height:16px;animation-delay:0s;}.sw span:nth-child(2){height:24px;animation-delay:.1s;}
.sw span:nth-child(3){height:32px;animation-delay:.2s;}.sw span:nth-child(4){height:28px;animation-delay:.3s;}
.sw span:nth-child(5){height:20px;animation-delay:.4s;}
.lang-card{background:var(--white);border-radius:20px;padding:28px;box-shadow:0 8px 40px rgba(0,0,0,.08);}
.lang-card h4{font-size:.9rem;font-weight:700;margin-bottom:16px;color:var(--blue);}
.lang-list{display:flex;flex-wrap:wrap;gap:8px;}
.lang-list span{background:var(--light-blue);color:var(--blue);padding:8px 16px;border-radius:50px;font-size:.8rem;font-weight:600;}
.lang-list span.active{background:var(--blue);color:var(--white);}
.hist-card{background:var(--white);border-radius:20px;padding:28px;box-shadow:0 8px 40px rgba(0,0,0,.08);}
.hist-card h4{font-size:.9rem;font-weight:700;margin-bottom:16px;color:var(--blue);}
.hist-row{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #eee;font-size:.85rem;}
.hist-row .app{font-weight:600;}.hist-row .amt{color:var(--green);font-weight:700;}
.hist-total{display:flex;justify-content:space-between;padding:12px 0;font-weight:800;color:var(--blue);font-size:1rem;}
.msg-card{background:var(--white);border-radius:20px;padding:28px;box-shadow:0 8px 40px rgba(0,0,0,.08);}
.msg-card h4{font-size:.9rem;font-weight:700;margin-bottom:16px;color:var(--blue);}
.msg-input{background:#F5F5F5;border:2px solid #E0E0E0;border-radius:12px;padding:12px 16px;font-size:.85rem;color:var(--dark);margin-bottom:12px;display:block;width:100%;}
.msg-preview{background:var(--light-blue);border-radius:12px;padding:16px;font-size:.85rem;color:var(--blue);font-weight:600;}

/* PRICING */
.pricing-bg{background:linear-gradient(135deg,var(--dark-blue),var(--blue),var(--blue2));}
.pricing-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;max-width:1000px;margin:40px auto 0;align-items:start;}
.p-card{background:var(--white);border-radius:24px;padding:36px 28px;text-align:center;transition:all .3s;border:2px solid transparent;}
.p-card.pop{border-color:var(--yellow);transform:scale(1.05);box-shadow:0 20px 60px rgba(0,0,0,.2);}
.p-card:hover{transform:translateY(-8px);box-shadow:0 20px 50px rgba(0,0,0,.12);}
.p-card.pop:hover{transform:scale(1.05) translateY(-8px);}
.p-badge{background:var(--yellow);color:var(--dark);font-size:.7rem;font-weight:800;padding:4px 14px;border-radius:20px;display:inline-block;margin-bottom:10px;}
.p-card h3{font-size:1.3rem;font-weight:800;margin-bottom:8px;}
.p-card .price{font-size:2rem;font-weight:900;color:var(--blue);margin:12px 0;}
.p-card .price small{font-size:.8rem;font-weight:400;color:var(--gray);}
.p-card ul{list-style:none;text-align:left;margin:20px 0;}
.p-card ul li{font-size:.84rem;padding:7px 0;border-bottom:1px solid #f0f0f0;display:flex;align-items:center;gap:8px;}
.p-card ul li::before{content:'✓';color:var(--green);font-weight:700;}
.p-btn{display:inline-block;padding:12px 32px;border-radius:50px;font-weight:700;font-size:.9rem;transition:all .3s;}
.p-btn-o{border:2px solid var(--blue);color:var(--blue);}
.p-btn-y{background:var(--yellow);color:var(--dark);}
.p-btn:hover{transform:translateY(-3px);box-shadow:0 8px 20px rgba(0,0,0,.12);}
.pricing-note{text-align:center;color:rgba(255,255,255,.6);font-size:.82rem;margin-top:24px;}

/* WHO USES */
.who-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;max-width:1100px;margin:40px auto 0;}
.who-card{background:var(--light-blue);border-radius:16px;padding:24px 20px;transition:all .3s;}
.who-card:hover{transform:scale(1.04);box-shadow:0 12px 30px rgba(21,101,192,.1);background:var(--white);}
.who-card .wc-icon{font-size:2rem;margin-bottom:10px;}
.who-card h4{font-size:.92rem;font-weight:700;margin-bottom:4px;}
.who-card p{font-size:.78rem;color:var(--gray);line-height:1.5;}

/* PRIVACY */
.priv-inner{max-width:1000px;margin:0 auto;display:flex;align-items:center;gap:60px;}
.priv-shield{text-align:center;}
.priv-shield-icon{font-size:6rem;animation:shieldPulse 2s ease-in-out infinite;display:block;}
@keyframes shieldPulse{0%,100%{transform:scale(1);filter:drop-shadow(0 0 10px rgba(67,160,71,.3));}50%{transform:scale(1.08);filter:drop-shadow(0 0 30px rgba(67,160,71,.5));}}
.priv-shield-text{color:var(--green);font-weight:800;font-size:.9rem;margin-top:8px;}
.priv-content{flex:1;}
.priv-list{list-style:none;margin-top:20px;}
.priv-list li{font-size:.9rem;padding:8px 0;display:flex;align-items:center;gap:10px;}
.priv-list li::before{content:'✓';color:var(--green);font-weight:800;font-size:1.1rem;}

/* REVIEWS */
.rev-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;max-width:1060px;margin:40px auto 0;}
.rev-card{background:var(--white);border-radius:20px;padding:32px 24px;border-bottom:3px solid transparent;transition:all .3s;box-shadow:0 4px 20px rgba(0,0,0,.05);}
.rev-card:hover{transform:translateY(-5px);border-bottom-color:var(--blue);box-shadow:0 16px 40px rgba(0,0,0,.1);}
.rev-stars{color:var(--yellow);font-size:1.1rem;margin-bottom:12px;}
.rev-text{font-size:.88rem;color:var(--gray);line-height:1.7;margin-bottom:20px;font-style:italic;}
.rev-user{display:flex;align-items:center;gap:12px;}
.rev-av{width:42px;height:42px;border-radius:50%;background:var(--blue);color:var(--white);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem;}
.rev-name{font-size:.88rem;font-weight:700;}
.rev-date{font-size:.72rem;color:var(--gray);}

/* FINAL CTA */
.cta-section{background:linear-gradient(135deg,var(--dark-blue),var(--blue),var(--blue2));text-align:center;padding:clamp(60px,10vw,120px) 24px;position:relative;overflow:hidden;}
.cta-section::before{content:'';position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.05) 1px,transparent 1px);background-size:24px 24px;}
.cta-logo{width:80px;height:80px;border-radius:20px;margin:0 auto 24px;box-shadow:0 8px 30px rgba(0,0,0,.3);}
.cta-section h2{font-size:clamp(1.6rem,4vw,2.5rem);font-weight:900;color:var(--white);margin-bottom:16px;position:relative;}
.cta-section h2 .yellow{color:var(--yellow);}
.cta-section .cta-sub{color:rgba(255,255,255,.7);max-width:550px;margin:0 auto 32px;font-size:clamp(.88rem,2vw,1rem);line-height:1.7;position:relative;}
.cta-big-btn{display:inline-flex;align-items:center;gap:16px;background:var(--white);padding:16px 36px;border-radius:50px;box-shadow:0 12px 40px rgba(0,0,0,.2);transition:all .3s;position:relative;}
.cta-big-btn:hover{transform:translateY(-3px);box-shadow:0 20px 50px rgba(0,0,0,.3);}
.cta-big-btn img{height:32px;}
.cta-big-btn span{font-size:1rem;font-weight:700;color:var(--dark);}
.cta-note{color:rgba(255,255,255,.5);font-size:.78rem;margin-top:16px;position:relative;}

/* FOOTER */
.footer{background:var(--dark);padding:60px 24px 30px;}
.footer-inner{max-width:1100px;margin:0 auto;}
.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:40px;margin-bottom:40px;}
.footer-brand{display:flex;align-items:center;gap:10px;margin-bottom:12px;}
.footer-brand img{width:32px;height:32px;border-radius:8px;}
.footer-brand span{color:var(--white);font-weight:700;}
.footer p.fb-sub{color:rgba(255,255,255,.5);font-size:.82rem;line-height:1.6;}
.footer h4{color:var(--white);font-size:.9rem;font-weight:700;margin-bottom:16px;}
.footer-col a{display:block;color:rgba(255,255,255,.5);font-size:.82rem;padding:4px 0;transition:color .3s;}
.footer-col a:hover{color:var(--yellow);}
.footer-play{display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.08);padding:12px 16px;border-radius:12px;margin-top:8px;}
.footer-play img{height:28px;}
.footer-play span{color:var(--white);font-size:.78rem;font-weight:600;}
.footer-rating{color:rgba(255,255,255,.5);font-size:.75rem;margin-top:8px;}
.footer-bottom{border-top:1px solid rgba(255,255,255,.08);padding-top:20px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;}
.footer-bottom p{color:rgba(255,255,255,.35);font-size:.75rem;}
.footer-bottom a{color:rgba(255,255,255,.35);font-size:.75rem;transition:color .3s;}
.footer-bottom a:hover{color:var(--yellow);}

/* RESPONSIVE */
@media(min-width:1441px){.hero-inner{max-width:1300px;}.phone-mockup{width:290px;}}
@media(max-width:1024px){.hero-inner{gap:50px;}.hero-phone{flex:0 0 260px;}.feat-inner{gap:40px;}.steps{flex-wrap:wrap;}.steps::before{display:none;}.step{flex:0 0 calc(50% - 12px);}.features-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:900px){.nav-links{display:none;}.hamburger{display:flex;}.mobile-menu{display:flex;}.hero{padding:110px 20px 60px;min-height:auto;}.hero-inner{flex-direction:column;text-align:center;gap:40px;}.hero-body{margin:0 auto 32px;}.hero-btns{justify-content:center;}.trust-row{justify-content:center;}.hero-phone{flex:0 0 auto;}.feat-inner,.feat-inner.reverse{flex-direction:column;text-align:center;}.feat-content ul li{justify-content:center;}.rev-grid{grid-template-columns:1fr 1fr;}.priv-inner{flex-direction:column;text-align:center;}.priv-list li{justify-content:center;}.who-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:768px){.pricing-grid{grid-template-columns:1fr;max-width:400px;}.p-card.pop{transform:none;}.p-card.pop:hover{transform:translateY(-8px);}.stats-inner{flex-wrap:wrap;}.stat{flex:0 0 33.33%;}.stat:nth-child(4),.stat:nth-child(5){flex:0 0 50%;}.stat+.stat::before{display:none;}.footer-grid{grid-template-columns:1fr 1fr;}.fc{display:none;}.step{flex:0 0 100%;}}
@media(max-width:576px){.hero{padding:95px 16px 40px;}.hero-btns{flex-direction:column;width:100%;align-items:center;}.btn-yellow,.btn-ghost{width:100%;justify-content:center;}.phone-mockup{width:200px;}.who-grid{grid-template-columns:1fr;}.rev-grid{grid-template-columns:1fr;}.footer-grid{grid-template-columns:1fr;}.cta-big-btn{flex-direction:column;gap:8px;padding:16px 24px;}.nav-cta{padding:8px 16px;font-size:.78rem;}}
@media(max-width:400px){html{font-size:14px;}.phone-mockup{width:170px;}.hero{padding:85px 12px 36px;}}
"""

# Write parts file
parts_path = r"C:\Users\AKSHAY BHAWAR\OneDrive\Desktop\PayEcho\parts.py"
with open(parts_path, "w", encoding="utf-8") as f:
    f.write(f'logo_b64 = """{logo_b64}"""\n')
    f.write(f'play_b64 = """{play_b64}"""\n')
    f.write(f'css = """{css}"""\n')
print("✅ Part 1 done - CSS + images saved")
