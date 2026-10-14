# -*- coding: utf-8 -*-
"""Marina Park Cafe — static site generator (marinapark.cafe).
Run: python3 build.py  → writes index.html, menu.html, robots.txt, sitemap.xml, llms.txt
"""
import os, html, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://marinapark.cafe"
NAME = "마리나파크 카페"
NAME_EN = "Marina Park Cafe"
HOURS = "매일 10:00 – 22:00"
HOURS_EN = "Daily 10:00 – 22:00"
BRUNCH_UNTIL = "16:00"
TEL = "02-537-2440"; TEL_RAW = "+82-2-537-2440"
EMAIL = "ficonvention@gmail.com"
ADDRESS = "서울특별시 서초구 반포동 115-1 (서래나루 · 반포한강공원) 마리나파크 1층"
ADDRESS_SHORT = "서울 서초구 반포동 115-1 서래나루"
ADDRESS_EN = "1F Marina Park, 115-1 Banpo-dong, Seocho-gu, Seoul (Seoraenaru, Banpo Han River Park)"
ADDRESS_SHORT_EN = "Seoraenaru, Banpo-dong, Seocho-gu, Seoul"
INSTA = "https://www.instagram.com/marinapark_banpo"
INSTA_HANDLE = "@marinapark_banpo"
MAIN_SITE = "https://marinapark.co.kr"
RESERVE = "mailto:ficonvention@gmail.com?subject=%5B%EB%A7%88%EB%A6%AC%EB%82%98%ED%8C%8C%ED%81%AC%20%EC%B9%B4%ED%8E%98%5D%20%EC%98%88%EC%95%BD%20%EB%AC%B8%EC%9D%98&body=%EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94%2C%20%EC%98%88%EC%95%BD%20%EB%AC%B8%EC%9D%98%EB%93%9C%EB%A6%BD%EB%8B%88%EB%8B%A4.%0A%0A%E2%96%A0%20%EC%9D%B4%EB%A6%84%20/%20%EC%97%B0%EB%9D%BD%EC%B2%98%3A%20%0A%E2%96%A0%20%ED%9D%AC%EB%A7%9D%20%EB%82%A0%EC%A7%9C%C2%B7%EC%8B%9C%EA%B0%84%3A%20%0A%E2%96%A0%20%EC%9D%B8%EC%9B%90%3A%20%0A%E2%96%A0%20%EB%AA%A8%EC%9E%84%20%EC%A2%85%EB%A5%98%28%EC%83%9D%EC%9D%BC%C2%B7%EB%8F%99%ED%98%B8%ED%9A%8C%C2%B7%EB%B8%8C%EB%9D%BC%EC%9D%B4%EB%8D%9C%EC%83%A4%EC%9B%8C%C2%B7%EC%86%8C%EB%AA%A8%EC%9E%84%20%EB%93%B1%29%3A%20%0A%E2%96%A0%20%EC%9A%94%EC%B2%AD%EC%82%AC%ED%95%AD%28%EC%BC%80%EC%9D%B4%ED%81%AC%20%EB%B0%98%EC%9E%85%2C%20%EB%8D%B0%EC%BD%94%20%EB%93%B1%29%3A%20%0A%0A%EA%B0%90%EC%82%AC%ED%95%A9%EB%8B%88%EB%8B%A4."
RESERVE_EN = "mailto:ficonvention@gmail.com?subject=%5BMarina%20Park%20Cafe%5D%20Reservation%20inquiry&body=Hello%2C%20I%27d%20like%20to%20make%20a%20reservation.%0A%0A-%20Name%20%2F%20Phone%3A%20%0A-%20Date%20%26%20time%3A%20%0A-%20Number%20of%20guests%3A%20%0A-%20Occasion%20(birthday%2C%20bridal%20shower%2C%20small%20party...)%3A%20%0A-%20Requests%20(cake%2C%20decoration...)%3A%20%0A%0AThank%20you."
MAP_GOOGLE = "https://www.google.com/maps?q=%EC%84%9C%EC%9A%B8+%EC%84%9C%EC%B4%88%EA%B5%AC+%EB%B0%98%ED%8F%AC%EB%8F%99+115-1"
MAP_NAVER = "https://map.naver.com/p/search/%EB%A7%88%EB%A6%AC%EB%82%98%ED%8C%8C%ED%81%AC%20%EC%B9%B4%ED%8E%98%20%EB%B0%98%ED%8F%AC"
TODAY = datetime.date.today().isoformat()

# ----------------------------------------------------------------------
# MENU (2026 menu board — 단위: 천 원)
# ----------------------------------------------------------------------
MENU = [
  ("Food", "FOOD", "", "", [
    ("고르곤졸라 / 마르게리따 피자", "Gorgonzola Cheese Pizza / Margherita Pizza", "22.0", ""),
    ("페퍼로니 / 쉬림프 피자", "Pepperoni Pizza / Shrimp Pizza", "24.0", ""),
    ("돈까스 / 치즈돈까스", "Pork Cutlet / Cheese Pork Cutlet", "18.0 / 20.0", ""),
    ("함박스테이크", "Hamburg Steak", "26.0", ""),
    ("볶음밥 (김치 / 새우)", "Fried Rice (Kimchi / Shrimp)", "18.0", ""),
    ("까르보나라 / 쉬림프 오일 파스타", "Carbonara / Shrimp Oil Pasta", "22.0", ""),
    ("감자튀김 / 나초 & 멕시칸 살사", "French Fries / Nachos & Salsa", "10.0 / 12.0", ""),
    ("버팔로윙 & 칩스 / 쉬림프 & 칩스", "Wings & Chips / Shrimp & Chips", "20.0", ""),
    ("샐러드 (연어 / 치킨 / 부라타 치즈)", "Salad (Salmon / Chicken / Burrata)", "22.0", ""),
    ("떡볶이 / 닭강정", "Tteokbokki / Sweet & Sour Chicken", "20.0", ""),
    ("먹태 / 먹태 세트 (먹태 + 스텔라 2잔 330ml)", "Pollack / Pollack Set", "19.0 / 27.0", ""),
    ("찹스테이크 / 바베큐 폭립", "Chop Steak / BBQ Pork Ribs", "32.0 / 30.0", ""),
  ]),
  ("Brunch Set", "BRUNCH SET", f"PM {BRUNCH_UNTIL}까지 판매 · Sale until {BRUNCH_UNTIL}", "", [
    ("브런치 + 커피", "Brunch + Coffee — 호밀빵 + 버터 · 베이컨 & 소시지 · 계란후라이 · 샐러드", "20.0", ""),
  ]),
  ("Coffee", "COFFEE", "HOT / ICE", "hot-ice", [
    ("에스프레소", "Espresso", "4.0", ""),
    ("에스프레소 콘파냐", "Espresso Con Panna", "4.5", ""),
    ("아메리카노 (디카페인 +0.5)", "Americano", "5.0", "5.5"),
    ("원조 냉커피", "Original Iced Coffee", "", "6.0"),
    ("카푸치노", "Cappuccino", "5.5", "6.0"),
    ("카페라떼", "Cafe Latte", "5.5", "6.0"),
    ("바닐라라떼", "Vanilla Latte", "6.0", "6.5"),
    ("카라멜라떼", "Caramel Latte", "6.0", "6.5"),
    ("돌체라떼", "Dolce Latte", "6.0", "6.5"),
    ("카라멜 마끼아또", "Caramel Macchiato", "6.0", "6.5"),
    ("카페모카 (생크림 +0.5)", "Cafe Mocha", "6.0", "6.5"),
    ("콜드브루", "Cold Brew", "5.5", "6.0"),
    ("브루라떼", "Brew Latte", "6.0", "6.5"),
    ("아포가토", "Affogato", "", "6.5"),
  ]),
  ("Beverage", "BEVERAGE", "HOT / ICE", "hot-ice", [
    ("핫초코", "Hot Choco", "5.5", "6.0"),
    ("민트초코라떼", "Mint Chocolate Latte", "6.0", "6.5"),
    ("고구마라떼", "Sweet Potato Latte", "6.5", "7.0"),
    ("딸기라떼", "Strawberry Latte", "", "7.0"),
    ("아이스티 (레몬 / 복숭아)", "Ice Tea (Lemon / Peach)", "", "6.0"),
    ("에이드 (레몬 / 자몽 / 청포도 / 체리)", "Ade (Lemon / Grapefruit / Green Grape / Cherry)", "", "6.5"),
    ("오렌지주스", "Orange Juice", "", "5.0"),
    ("생토마토주스", "Fresh Tomato Juice", "", "7.0"),
    ("스무디 (딸기 / 망고 / 키위)", "Smoothie (Strawberry / Mango / Kiwi)", "", "7.5"),
    ("요거트 스무디 (플레인 / 딸기 / 망고 / 키위)", "Yogurt Smoothie", "", "7.5"),
    ("파인애플 샤베트", "Pineapple Sherbet", "", "8.0"),
  ]),
  ("Tea", "TEA", "HOT / ICE", "hot-ice", [
    ("얼그레이", "Earl Grey", "5.5", "6.0"),
    ("히비스커스", "Hibiscus", "5.5", "6.0"),
    ("페퍼민트", "Peppermint", "5.5", "6.0"),
    ("카모마일", "Chamomile", "5.5", "6.0"),
    ("레몬스카이", "Lemon Sky", "5.5", "6.0"),
    ("루이보스 바닐라", "Rooibos Vanilla", "5.5", "6.0"),
    ("녹차", "Green Tea", "5.5", "6.0"),
    ("유자차 / 자몽차 / 레몬차 (청)", "Citron / Grapefruit / Lemon Tea", "6.5", "7.0"),
    ("로얄 밀크티", "Royal Milk Tea", "6.5", "7.0"),
    ("말차라떼", "Matcha Latte", "6.5", "7.0"),
  ]),
  ("Bakery", "BAKERY", "", "", [
    ("플레인 베이글 + 크림치즈", "Plain Bagel + Cream Cheese", "4.5", ""),
    ("크로크무슈", "Croque Monsieur", "5.5", ""),
    ("아이스크림 크로플", "Ice Cream Croffle", "7.5", ""),
    ("허니버터브레드", "Honey Butter Bread", "6.5", ""),
    ("조각케이크", "Piece of Cake", "7.0", ""),
  ]),
  ("Wine", "WINE", "GLASS / BOTTLE", "hot-ice", [
    ("장발몽 샤르도네 (화이트)", "Jean Balmont Chardonnay", "8.0", "60.0"),
    ("장발몽 까베르네 소비뇽 (레드)", "Jean Balmont Cabernet Sauvignon", "8.0", "60.0"),
    ("켄달-잭슨 빈트너스 리저브 샤르도네 (화이트)", "Kendall-Jackson Vintner's Reserve Chardonnay", "", "90.0"),
    ("켄달-잭슨 빈트너스 리저브 까베르네 소비뇽 (레드)", "Kendall-Jackson Vintner's Reserve Cabernet Sauvignon", "", "90.0"),
    ("Champagne", None, None, None),
    ("장발몽 브륏", "Jean Balmont Brut", "", "60.0"),
    ("모엣 샹동", "Moët & Chandon", "", "120.0"),
    ("Highball", None, None, None),
    ("짐빔 하이볼 (Glass)", "Jim Beam Highball", "8.0", ""),
    ("짐빔 버번 위스키 1병 + 토닉워터 6병", "Jim Beam Bourbon 1 bottle + Tonic Water 6 bottles", "", "120.0"),
  ]),
  ("Beer & Soju", "BEER & SOJU", "", "", [
    ("Bottle", None, None, None),
    ("코로나 / 스텔라 / 호가든 / 버드와이저 (330ml)", "Corona Extra / Stella Artois / Hoegaarden / Budweiser", "8.0", ""),
    ("코로나 / 버드와이저 5+1 세트", "Corona Extra / Budweiser 5+1 Set", "<s>48.0</s> 40.0", ""),
    ("Draft", None, None, None),
    ("스텔라 (330ml / 600ml)", "Stella Artois", "8.0 / 14.0", ""),
    ("호가든 (330ml / 600ml)", "Hoegaarden", "8.0 / 14.0", ""),
    ("한맥 (420ml / 2000ml)", "Hanmac", "8.0 / 35.0", ""),
    ("Soju", None, None, None),
    ("화요 (25°, 375ml)", "Hwayo", "35.0", ""),
  ]),
]

# Food photos (file, 한글, 영문)
DISHES = [
  ("cafe-27.jpg", "까르보나라", "Carbonara"),
  ("cafe-28.jpg", "쉬림프 오일 파스타", "Shrimp Oil Pasta"),
  ("cafe-25.jpg", "찹스테이크", "Chop Steak"),
  ("cafe-35.jpg", "함박스테이크", "Hamburg Steak"),
  ("cafe-29.jpg", "돈까스", "Pork Cutlet"),
  ("cafe-34.jpg", "볶음밥 (김치 / 새우)", "Fried Rice"),
  ("cafe-26.jpg", "쉬림프 & 칩스", "Shrimp & Chips"),
  ("cafe-31.jpg", "연어 샐러드", "Salmon Salad"),
  ("cafe-33.jpg", "부라타 치즈 샐러드", "Burrata Salad"),
  ("cafe-36.jpg", "치킨 샐러드", "Chicken Salad"),
  ("cafe-24.jpg", "떡볶이", "Tteokbokki"),
  ("cafe-23.jpg", "먹태", "Grilled Dried Pollack"),
]

# ----------------------------------------------------------------------
def esc(s): return html.escape(s, quote=True)

def menu_section(cat, lang="ko"):
    title_ko, title_en, note, cls, rows = cat
    if lang == "en": note = note.replace(f"PM {BRUNCH_UNTIL}까지 판매 · ", "")
    out = [f'<article class="menu-card" id="m-{title_en.lower().replace(" ", "-").replace("&", "and")}">']
    out.append(f'<header class="menu-head"><h3>{title_en}</h3><span class="menu-note">{note}</span></header>')
    out.append('<table>')
    for ko, en, p1, p2 in rows:
        if en is None:
            out.append(f'<tr class="menu-group"><th colspan="3">{ko}</th></tr>'); continue
        price = f'<td class="m-price">{p1}</td><td class="m-price">{p2}</td>' if cls == "hot-ice" else f'<td class="m-price" colspan="2">{p1}</td>'
        name = f'{esc(en)}<span class="m-en">{ko}</span>' if lang == "en" else f'{ko}<span class="m-en">{esc(en)}</span>'
        out.append(f'<tr><td class="m-name">{name}</td>{price}</tr>')
    out.append('</table></article>')
    return "\n".join(out)

def jsonld_cafe():
    import json
    d = {
      "@context": "https://schema.org",
      "@type": ["CafeOrCoffeeShop", "Restaurant"],
      "name": NAME, "alternateName": NAME_EN,
      "url": SITE_URL, "image": f"{SITE_URL}/images/cafe-13.jpg",
      "telephone": TEL_RAW, "email": EMAIL,
      "servesCuisine": ["Coffee", "Italian", "Dessert", "Brunch", "Wine", "Beer"],
      "priceRange": "₩₩",
      "address": {"@type": "PostalAddress", "streetAddress": "반포동 115-1 마리나파크 1층 (서래나루, 반포한강공원)",
                  "addressLocality": "서초구", "addressRegion": "서울특별시", "addressCountry": "KR"},
      "geo": {"@type": "GeoCoordinates", "latitude": 37.5116, "longitude": 126.9971},
      "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
         "opens": "10:00", "closes": "22:00"}],
      "hasMenu": f"{SITE_URL}/menu.html",
      "sameAs": [INSTA, MAIN_SITE],
      "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": "Han River view terrace", "value": True},
                         {"@type": "LocationFeatureSpecification", "name": "Private party (10–30 guests)", "value": True},
                         {"@type": "LocationFeatureSpecification", "name": "Parking (Banpo Han River Park)", "value": True}],
      "parentOrganization": {"@type": "Organization", "name": "마리나파크 Marina Park", "url": MAIN_SITE},
    }
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + '</script>'

def jsonld_faq(items):
    import json
    d = {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + '</script>'

EN_OF = {"index.html": "en.html", "menu.html": "menu-en.html"}
KO_OF = {v: k for k, v in EN_OF.items()}

def page(fname, title, desc, body, og="images/cafe-13.jpg", extra_ld="", kw="", lang="ko"):
    url = f"{SITE_URL}/{'' if fname == 'index.html' else fname}"
    home = "en.html" if lang == "en" else "index.html"
    menu = "menu-en.html" if lang == "en" else "menu.html"
    nav = [(f"{home}#about", "About"), (menu, "Menu"), (f"{home}#dishes", "Dishes"),
           (f"{home}#party", "Private Party"), (f"{home}#visit", "Visit")]
    nav_html = "".join(f'<a href="{h}">{t}</a>' for h, t in nav)
    if lang == "en":
        alt_href, alt_label, alt_hreflang = KO_OF[fname], "한국어", "ko"
    else:
        alt_href, alt_label, alt_hreflang = EN_OF[fname], "English", "en"
    lang_btn = f'<a class="nav-lang" href="{alt_href}" hreflang="{alt_hreflang}" lang="{alt_hreflang}">{alt_label}</a>'
    ko_url = f"{SITE_URL}/{'' if (fname if lang=='ko' else KO_OF[fname]) == 'index.html' else (fname if lang=='ko' else KO_OF[fname])}"
    en_url = f"{SITE_URL}/{fname if lang=='en' else EN_OF[fname]}"
    hreflang = f'<link rel="alternate" hreflang="ko" href="{ko_url}">\n<link rel="alternate" hreflang="en" href="{en_url}">\n<link rel="alternate" hreflang="x-default" href="{ko_url}">'
    T = (lambda ko, en: en) if lang == "en" else (lambda ko, en: ko)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{f'<meta name="keywords" content="{esc(kw)}">' if kw else ''}
<link rel="canonical" href="{url}">
{hreflang}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAME_EN}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/{og}">
<meta property="og:locale" content="{"en_US" if lang == "en" else "ko_KR"}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Noto+Serif+KR:wght@300;400;600&family=Noto+Sans+KR:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v=2">
{jsonld_cafe()}
{extra_ld}
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{home}"><span class="brand-mark">MARINA PARK</span><span class="brand-sub">Cafe &amp; Restaurant · Banpo Han River</span></a>
    <button class="nav-toggle" aria-label="{T("메뉴 열기", "Open menu")}" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="site-nav">{nav_html}<a class="nav-insta" href="{INSTA}" target="_blank" rel="noopener">Instagram</a>{lang_btn}</nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap foot-grid">
    <div>
      <p class="foot-brand">MARINA PARK CAFE</p>
      <p class="foot-sub">{T("반포 한강공원 서래나루 · 한강뷰 카페 &amp; 레스토랑", "Seoraenaru, Banpo Han River Park · Riverside cafe &amp; restaurant")}</p>
      <p class="foot-hours">{T(HOURS, HOURS_EN)} · {T(f"브런치 {BRUNCH_UNTIL}까지", f"Brunch until {BRUNCH_UNTIL}")}</p>
    </div>
    <div>
      <p>{T(ADDRESS, ADDRESS_EN)}</p>
      <p>Tel <a href="tel:{TEL_RAW}">{TEL}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p><a href="{INSTA}" target="_blank" rel="noopener">Instagram {INSTA_HANDLE}</a> · <a href="{MAIN_SITE}" target="_blank" rel="noopener">{T("마리나파크 연회·웨딩", "Marina Park Banquet &amp; Wedding")} marinapark.co.kr</a></p>
    </div>
  </div>
  <p class="wrap copy">© {datetime.date.today().year} Marina Park. All rights reserved.</p>
</footer>
<div id="lightbox" class="lightbox" aria-hidden="true"><button class="lb-close" aria-label="{T("닫기","Close")}">×</button><button class="lb-prev" aria-label="{T("이전","Previous")}">‹</button><img alt=""><button class="lb-next" aria-label="{T("다음","Next")}">›</button></div>
<script src="js/main.js"></script>
</body>
</html>"""

def fig(src, alt, cls="", lightbox=True):
    a = f'<a href="images/{src}" data-lightbox>' if lightbox else ''
    b = '</a>' if lightbox else ''
    return f'<figure class="{cls}">{a}<img src="images/{src}" alt="{esc(alt)}" loading="lazy">{b}</figure>'

# ----------------------------------------------------------------------
# INDEX
# ----------------------------------------------------------------------
def build(lang):
  T = (lambda ko, en: en) if lang == "en" else (lambda ko, en: ko)
  RSV = RESERVE_EN if lang == "en" else RESERVE
  faq_items = [
    ("마리나파크 카페 영업시간은 어떻게 되나요?", f"{HOURS} 영업합니다. 브런치 세트는 오후 {BRUNCH_UNTIL}까지 주문 가능합니다. 행사 대관이 있는 날은 일부 공간 이용이 제한될 수 있습니다."),
    ("카페는 어디에 있나요? 주차는요?", "서울 서초구 반포동 115-1 서래나루(반포한강공원) 마리나파크 1층입니다. 반포한강공원 주차장을 이용하시면 되고, 한강 산책 후 들르기 좋은 위치입니다."),
    ("한강이 보이는 자리가 있나요?", "1층 전체가 한강을 바라보는 통창 구조이며, 레드 어닝이 있는 야외 테라스에서는 한강과 서울 도심 스카이라인을 바로 앞에서 즐기실 수 있습니다."),
    ("생일 모임이나 소규모 파티도 가능한가요?", "카페 가든·테라스에서 10~30명 규모의 생일 모임, 동호회, 브라이덜 샤워, 소규모 송년 모임을 예약하실 수 있습니다. 케이크 반입과 간단한 데코가 가능하며, 더 큰 행사는 마리나파크 2층 컨벤션홀과 3층 루프탑 가든을 이용합니다."),
    ("식사 메뉴도 있나요?", "피자, 파스타, 돈까스, 함박스테이크, 찹스테이크, 볶음밥 등 식사 메뉴와 브런치 세트, 와인·맥주·하이볼을 함께 준비하고 있습니다."),
  ] if lang == "ko" else [
    ("What are the opening hours?", f"We are open {HOURS_EN.lower()}. Brunch sets are served until {BRUNCH_UNTIL}. On days with private events, part of the space may be reserved."),
    ("Where is the cafe? Is there parking?", "On the ground floor of Marina Park at Seoraenaru, Banpo Han River Park (115-1 Banpo-dong, Seocho-gu, Seoul). Use the Banpo Han River Park parking lot — a short walk along the river."),
    ("Do you have seats with a river view?", "The whole ground floor faces the Han River through floor-to-ceiling windows, and the outdoor terrace under the red awning looks straight onto the river and the Seoul skyline."),
    ("Can I book a birthday or a small party?", "Yes — the cafe garden and terrace host groups of 10–30 for birthdays, club meetings, bridal showers and small year-end parties. You may bring a cake and simple decorations. Larger events use the 2F convention hall and 3F rooftop garden of Marina Park."),
    ("Do you serve meals?", "Yes: pizza, pasta, pork cutlet, hamburg steak, chop steak, fried rice and more, plus a brunch set, wine, beer and highballs."),
  ]
  faq_html = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in faq_items)

  dish_cards = "".join(
      f'<figure class="dish"><a href="images/{f}" data-lightbox><img src="images/{f}" alt="{esc(ko)} — {esc(en)}, {T("마리나파크 카페", NAME_EN)}" loading="lazy"></a><figcaption><b>{T(ko, esc(en))}</b><span>{T(esc(en), ko)}</span></figcaption></figure>'
      for f, ko, en in DISHES)

  index_body = f"""
  <section class="hero">
    <img class="hero-bg" src="images/cafe-13.jpg" alt="{T("마리나파크 카페 테라스에서 바라본 한강 노을", "Han River sunset from the Marina Park Cafe terrace")}" fetchpriority="high">
    <div class="hero-box">
      <p class="eyebrow">BANPO · HAN RIVER · SEORAENARU</p>
      <h1>MARINA PARK<br><em>Cafe</em></h1>
      <p class="hero-ko">{T("한강이 눈앞에 펼쳐지는 반포한강공원 서래나루의 카페 &amp; 레스토랑", "A cafe &amp; restaurant at Seoraenaru, Banpo Han River Park — the river right in front of you")}</p>
      <p class="hero-meta"><span class="pill">{T(HOURS, HOURS_EN)}</span><span class="pill">Brunch until {BRUNCH_UNTIL}</span><span class="pill">River Terrace</span></p>
      <p class="hero-cta"><a class="btn" href="{T("menu.html","menu-en.html")}">Menu</a><a class="btn btn-ghost" href="{RSV}">{T("예약하기","Reserve")}</a><a class="btn btn-ghost" href="#visit">{T("오시는 길","Directions")}</a></p>
    </div>
  </section>

  <section class="section" id="about">
    <div class="wrap two-col">
      <div class="col-text">
        <p class="eyebrow">ABOUT</p>
        <h2>River, light, <em>and a slow cup</em></h2>
        <p>{T("마리나파크 카페는 반포한강공원 서래나루, 한강 위에 떠 있는 듯한 마리나파크 1층에 있습니다. 통창 너머로 한강과 서울의 스카이라인이 이어지고, 레드 어닝 아래 야외 테라스에서는 노을과 야경을 가장 가까이에서 만날 수 있습니다.", "Marina Park Cafe sits on the ground floor of Marina Park at Seoraenaru, Banpo Han River Park — a building that seems to float on the river. Floor-to-ceiling windows open onto the Han River and the Seoul skyline, and the terrace under the red awning puts you right in front of the sunset and the city lights.")}</p>
        <p>{T("커피와 티, 디저트부터 피자·파스타·스테이크 같은 식사 메뉴, 저녁의 와인과 맥주, 하이볼까지 — 한강 산책 후 가볍게 들르는 시간도, 특별한 날의 긴 식사도 어울리는 공간입니다.", "Coffee, tea and desserts; pizza, pasta and steak; wine, beer and highballs in the evening — a place for a quick stop after a riverside walk, or a long dinner on a special day.")}</p>
        <ul class="facts">
          <li><b>{T("영업시간","Hours")}</b>{T(HOURS, HOURS_EN)}</li>
          <li><b>{T("브런치","Brunch")}</b>{T(f"오후 {BRUNCH_UNTIL}까지", f"until {BRUNCH_UNTIL}")}</li>
          <li><b>{T("위치","Location")}</b>{T(ADDRESS_SHORT, ADDRESS_SHORT_EN)} · {T("마리나파크 1층","Marina Park 1F")}</li>
          <li><b>{T("문의","Contact")}</b><a href="tel:{TEL_RAW}">{TEL}</a></li>
        </ul>
        <p class="en-summary" lang="en" {"hidden" if lang == "en" else ""}>Marina Park Cafe is a riverside cafe &amp; restaurant on the ground floor of Marina Park at Seoraenaru, Banpo Han River Park, Seoul. Floor-to-ceiling river views, a red-awning terrace, coffee and desserts, Italian plates, brunch until {BRUNCH_UNTIL}, wine, beer and highballs. Open daily 10:00–22:00.</p>
      </div>
      <div class="col-media">
        {fig("cafe-01.jpg", T("마리나파크 카페 야외 테라스와 반포 한강공원 전경", "Marina Park Cafe terrace and Banpo Han River Park"), "tall")}
        {fig("cafe-20.jpg", T("마리나파크 카페 입구 저녁 풍경", "Marina Park Cafe entrance in the evening"), "")}
      </div>
    </div>
  </section>

  <section class="section section-dark" id="terrace">
    <div class="wrap">
      <p class="eyebrow center">THE TERRACE</p>
      <h2 class="center">Sunset on the Han <em>from your table</em></h2>
      <div class="gallery">
        {fig("cafe-14.jpg", T("마리나파크 카페 테라스 — 한강 위 노을", "Terrace — sunset over the Han River"))}
        {fig("cafe-02.jpg", T("마리나파크 카페 테라스 저녁, 세빛섬 야경", "Terrace at dusk with Some Sevit lights"))}
        {fig("cafe-09.jpg", T("마리나파크 카페 실내에서 본 야간 테라스", "Night terrace seen from inside"))}
        {fig("cafe-08.jpg", T("마리나파크에서 바라본 한강 노을과 세빛섬", "Han River sunset and Some Sevit from Marina Park"))}
        {fig("cafe-11.jpg", T("마리나파크 카페 테라스 라운지 소파석", "Terrace lounge sofas"))}
        {fig("cafe-03.jpg", T("마리나파크 카페 가든 테이블 세팅과 한강", "Garden table setting by the river"))}
      </div>
    </div>
  </section>

  <section class="section" id="dishes">
    <div class="wrap">
      <p class="eyebrow center">SIGNATURE DISHES</p>
      <h2 class="center">Italian plates <em>&amp; comfort food</em></h2>
      <p class="center sub">{T("피자 · 파스타 · 돈까스 · 함박스테이크 · 찹스테이크 · 볶음밥 · 샐러드 · 떡볶이 · 먹태", "Pizza · Pasta · Pork Cutlet · Hamburg Steak · Chop Steak · Fried Rice · Salads · Tteokbokki · Grilled Pollack")}</p>
      <div class="dish-grid">{dish_cards}</div>
      <p class="center"><a class="btn btn-dark" href="{T("menu.html","menu-en.html")}">{T("전체 메뉴 보기","See the full menu")}</a></p>
    </div>
  </section>

  <section class="section section-cream" id="party">
    <div class="wrap two-col rev">
      <div class="col-media">
        {fig("bldg-03.jpg", T("마리나파크 가든 야간 파티 — 조명과 한강 야경", "Evening party in the Marina Park garden"), "tall")}
      </div>
      <div class="col-text">
        <p class="eyebrow">PRIVATE PARTY</p>
        <h2>Small gatherings <em>by the river</em></h2>
        <p>{T("카페 가든과 테라스에서 10~30명 규모의 생일 모임, 동호회, 브라이덜 샤워, 소규모 송년 모임을 예약하실 수 있습니다. 케이크 반입과 간단한 데코가 가능하고, 한강 노을이 자연스러운 배경이 됩니다.", "The cafe garden and terrace can be booked for groups of 10–30: birthdays, club gatherings, bridal showers and small year-end parties. Bring a cake and simple decorations — the river sunset does the rest.")}</p>
        <p>{T("50명 이상의 연회, 기업행사, 예식은 같은 건물 2층 컨벤션홀(100~300명)과 3층 루프탑 가든에서 진행합니다 — ", "Banquets of 50 or more, corporate events and weddings are held in the 2F convention hall (100–300 guests) and the 3F rooftop garden of the same building — ")}<a href="{MAIN_SITE}" target="_blank" rel="noopener">{T("마리나파크 연회·웨딩 안내", "Marina Park banquet &amp; wedding")}</a>.</p>
        <p class="hero-cta"><a class="btn btn-dark" href="{RSV}">{T("예약하기 (이메일)", "Reserve by email")}</a><a class="btn btn-ghost-dark" href="tel:{TEL_RAW}">{T("전화", "Call")} {TEL}</a></p>
      </div>
    </div>
  </section>

  <section class="section" id="building">
    <div class="wrap">
      <p class="eyebrow center">MARINA PARK</p>
      <h2 class="center">A house on the river, <em>three floors of occasions</em></h2>
      <div class="gallery">
        {fig("bldg-02.jpg", T("마리나파크 건물 외관 — 1층 카페의 레드 어닝", "Marina Park — the cafe's red awning on the ground floor"), "wide")}
        {fig("bldg-04.jpg", T("마리나파크 가든 야간 행사와 한강 다리 야경", "Garden event at night with the bridge lights"))}
        {fig("cafe-19.jpg", T("마리나파크 야경 — 한강 위의 건물 전경", "Marina Park at night on the river"))}
        {fig("bldg-05.jpg", T("마리나파크 3층 루프탑 가든 잔디와 한강 전경", "3F rooftop garden lawn and the river"))}
        {fig("bldg-01.jpg", T("마리나파크 1층 마리나 카페 외관", "Marina Cafe exterior, ground floor"))}
      </div>
      <p class="center sub">{T("1F 마리나파크 카페 · 2F 컨벤션홀 (100~300명) · 3F 루프탑 가든", "1F Marina Park Cafe · 2F Convention Hall (100–300 guests) · 3F Rooftop Garden")}</p>
    </div>
  </section>

  <section class="section section-cream" id="visit">
    <div class="wrap two-col">
      <div class="col-text">
        <p class="eyebrow">VISIT</p>
        <h2>Find us <em>at Seoraenaru</em></h2>
        <ul class="facts">
          <li><b>{T("주소","Address")}</b>{T(ADDRESS, ADDRESS_EN)}</li>
          <li><b>{T("영업시간","Hours")}</b>{T(HOURS, HOURS_EN)}</li>
          <li><b>{T("전화","Phone")}</b><a href="tel:{TEL_RAW}">{TEL}</a></li>
          <li><b>{T("주차","Parking")}</b>{T("반포한강공원 주차장 이용", "Banpo Han River Park parking lot")}</li>
          <li><b>{T("대중교통","Transit")}</b>{T("고속터미널역 · 신반포역에서 반포한강공원 서래나루 방향", "From Express Bus Terminal or Sinbanpo station, walk toward Seoraenaru in Banpo Han River Park")}</li>
          <li><b>Instagram</b><a href="{INSTA}" target="_blank" rel="noopener">{INSTA_HANDLE}</a></li>
        </ul>
        <p class="hero-cta"><a class="btn btn-dark" href="{MAP_NAVER}" target="_blank" rel="noopener">{T("네이버 지도","Naver Map")}</a><a class="btn btn-ghost-dark" href="{MAP_GOOGLE}" target="_blank" rel="noopener">Google Maps</a></p>
      </div>
      <div class="col-media">
        {fig("cafe-12.jpg", T("마리나파크 카페 입구 — 레드 어닝과 Cafe 사인", "Cafe entrance — red awning and Cafe sign"), "tall")}
      </div>
    </div>
  </section>

  <section class="section" id="faq">
    <div class="wrap narrow">
      <p class="eyebrow center">FAQ</p>
      <h2 class="center">{T("자주 묻는 질문", "Frequently asked questions")}</h2>
      <div class="faq">{faq_html}</div>
    </div>
  </section>
  """

  # ----------------------------------------------------------------------
  # MENU PAGE
  # ----------------------------------------------------------------------
  menu_cards = "\n".join(menu_section(c, lang) for c in MENU)
  menu_nav = "".join(f'<a href="#m-{c[1].lower().replace(" ", "-").replace("&", "and")}">{c[1].title()}</a>' for c in MENU)
  menu_body = f"""
  <section class="page-hero">
    <img class="hero-bg" src="images/cafe-27.jpg" alt="{T("마리나파크 카페 까르보나라", "Carbonara at Marina Park Cafe")}">
    <div class="hero-box small">
      <p class="eyebrow">MENU</p>
      <h1>Marina Park <em>Cafe</em></h1>
      <p class="hero-ko">{T(f"{HOURS} · 브런치 세트 {BRUNCH_UNTIL}까지 · 가격 단위 천 원 (예: 5.5 = 5,500원)", f"{HOURS_EN} · Brunch set until {BRUNCH_UNTIL} · Prices in thousand KRW (e.g. 5.5 = ₩5,500)")}</p>
    </div>
  </section>
  <nav class="menu-jump"><div class="wrap">{menu_nav}</div></nav>
  <section class="section">
    <div class="wrap">
      <div class="menu-grid">
  {menu_cards}
      </div>
      <p class="center note">{T("메뉴와 가격은 사정에 따라 변경될 수 있습니다. 단체 예약·카페 파티 문의", "Menu and prices are subject to change. Group reservations &amp; cafe parties:")} <a href="tel:{TEL_RAW}">{TEL}</a> · <a href="{RSV}">{EMAIL}</a></p>
    </div>
  </section>
  """
  return index_body, menu_body, faq_items

ko_index, ko_menu, ko_faq = build("ko")
en_index, en_menu, en_faq = build("en")
# ----------------------------------------------------------------------
pages = {
  "index.html": dict(title="마리나파크 카페 — 반포 한강공원 서래나루 한강뷰 카페 & 레스토랑 | Marina Park Cafe",
    desc=f"반포한강공원 서래나루 마리나파크 1층 한강뷰 카페. 커피·디저트·브런치·피자·파스타·스테이크·와인. {HOURS}. 레드 어닝 테라스, 10~30명 소규모 파티 예약. 02-537-2440",
    body=ko_index, extra_ld=jsonld_faq(ko_faq),
    kw="반포 한강 카페, 서래나루 카페, 한강뷰 카페, 반포한강공원 카페, 마리나파크 카페, 한강 테라스 카페, 반포 브런치, 한강 레스토랑"),
  "menu.html": dict(title="메뉴 — 마리나파크 카페 | 커피·브런치·피자·파스타·와인 | Marina Park Cafe Menu",
    desc=f"마리나파크 카페 전체 메뉴와 가격. 커피·티·음료·베이커리·브런치 세트·피자·파스타·돈까스·스테이크·와인·맥주·하이볼. {HOURS}.",
    body=ko_menu, og="images/cafe-27.jpg",
    kw="마리나파크 카페 메뉴, 반포 한강 카페 메뉴, 서래나루 브런치, 한강 피자 파스타, 반포 와인바"),
  "en.html": dict(title="Marina Park Cafe — Han River view cafe & restaurant at Banpo, Seoul",
    desc=f"Riverside cafe & restaurant on the ground floor of Marina Park, Seoraenaru, Banpo Han River Park, Seoul. Coffee, desserts, brunch, pizza, pasta, steak, wine. {HOURS_EN}. Red-awning terrace, private parties for 10–30. +82-2-537-2440",
    body=en_index, extra_ld=jsonld_faq(en_faq), lang="en",
    kw="Han River cafe, Banpo cafe Seoul, river view cafe Seoul, Seoraenaru cafe, Marina Park Cafe, Han River terrace restaurant, brunch Banpo"),
  "menu-en.html": dict(title="Menu — Marina Park Cafe | Coffee, Brunch, Pizza, Pasta, Wine",
    desc=f"Full menu and prices of Marina Park Cafe: coffee, tea, drinks, bakery, brunch set, pizza, pasta, pork cutlet, steak, wine, beer, highballs. {HOURS_EN}.",
    body=en_menu, og="images/cafe-27.jpg", lang="en",
    kw="Marina Park Cafe menu, Han River cafe menu, Banpo brunch, Seoul river pizza pasta, Banpo wine bar"),
}
for fname, kw in pages.items():
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
        f.write(page(fname, **kw))

with open(os.path.join(ROOT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
            "".join(f"  <url><loc>{SITE_URL}/{'' if p == 'index.html' else p}</loc><lastmod>{TODAY}</lastmod></url>\n" for p in pages) + "</urlset>\n")
with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as f:
    f.write(f"""# {NAME} ({NAME_EN})
> 반포한강공원 서래나루 마리나파크 1층의 한강뷰 카페 & 레스토랑. {HOURS}, 브런치 세트 {BRUNCH_UNTIL}까지. 커피·티·디저트·브런치·피자·파스타·돈까스·스테이크·와인·맥주·하이볼. 레드 어닝 야외 테라스, 10~30명 소규모 파티 예약 가능.

- 주소: {ADDRESS}
- 전화: {TEL} · 이메일: {EMAIL} · Instagram: {INSTA}
- 주차: 반포한강공원 주차장
- 메뉴: {SITE_URL}/menu.html
- 연회·웨딩(2층 컨벤션홀 100~300명, 3층 루프탑 가든): {MAIN_SITE}
""")
with open(os.path.join(ROOT, "CNAME"), "w") as f:
    f.write("marinapark.cafe\n")
print("built:", ", ".join(pages), "+ robots/sitemap/llms/CNAME")
