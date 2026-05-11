import streamlit as st

st.set_page_config(
    page_title="eFaktura Konverteri",
    page_icon="⚡",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"], .stApp {
    font-family: 'DM Sans', sans-serif;
    background-color: #0a0a0a;
    color: #d4d4d4;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 720px; padding: 4rem 2rem 6rem; }

/* ── Header ── */
.hub-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #404040;
    margin-bottom: 1.2rem;
}
.hub-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 2.4rem;
    font-weight: 600;
    color: #f0f0f0;
    line-height: 1.1;
    margin-bottom: 0.6rem;
    letter-spacing: -0.03em;
}
.hub-sub {
    font-size: 0.95rem;
    color: #505050;
    line-height: 1.6;
    max-width: 480px;
    margin-bottom: 3.5rem;
}

/* ── Divider ── */
.divider {
    border: none;
    border-top: 1px solid #1c1c1c;
    margin: 2.5rem 0;
}

/* ── Section label ── */
.section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #303030;
    margin-bottom: 1.2rem;
}

/* ── Cards ── */
.card {
    display: block;
    text-decoration: none;
    background: #111111;
    border: 1px solid #1e1e1e;
    border-radius: 6px;
    padding: 1.5rem 1.75rem;
    margin-bottom: 0.75rem;
    transition: border-color 0.2s, background 0.2s, transform 0.15s;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    background: var(--accent);
    opacity: 0;
    transition: opacity 0.2s;
}
.card:hover {
    border-color: #2a2a2a;
    background: #141414;
    transform: translateX(3px);
}
.card:hover::before { opacity: 1; }

.card-step {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 0.5rem;
    opacity: 0.8;
}
.card-title {
    font-size: 1rem;
    font-weight: 600;
    color: #e8e8e8;
    margin-bottom: 0.4rem;
    letter-spacing: -0.01em;
}
.card-desc {
    font-size: 0.83rem;
    color: #505050;
    line-height: 1.55;
}
.card-arrow {
    position: absolute;
    right: 1.5rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 1rem;
    color: #2a2a2a;
    transition: color 0.2s, right 0.2s;
}
.card:hover .card-arrow {
    color: var(--accent);
    right: 1.2rem;
}

/* ── Note box ── */
.note {
    background: #0f0f0f;
    border: 1px solid #1a1a1a;
    border-left: 3px solid #c8f55a;
    border-radius: 4px;
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.75rem;
    font-size: 0.82rem;
    color: #505050;
    line-height: 1.6;
}
.note strong { color: #c8f55a; font-weight: 500; }

/* ── Footer ── */
.hub-footer {
    margin-top: 4rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.1em;
    color: #252525;
    text-align: center;
}
</style>

<div class="hub-eyebrow">Servier · Interni alati</div>
<h1 class="hub-title">eFaktura<br>Konverteri</h1>
<p class="hub-sub">Konverzija Business Central Excel exporta u UBL XML format za slanje putem Sistema eFaktura (SEF). Izaberi odgovarajući tip dokumenta.</p>

<hr class="divider">

<div class="section-label">Fakture</div>

<div class="note">
    <strong>Napomena za fakture:</strong> Przed konverzijom obavezno proveri lot brojeve u Lot Finder alatu i obogati Excel fajl ispravnim podacima.
</div>

<a class="card" href="https://invoice-converter-bng8er2uezdi2kklxzls6z.streamlit.app/" target="_blank" style="--accent: #c8f55a;">
    <div class="card-step">Korak 1 od 2 · Lot Finder →  Korak 2 od 2 · Konverter</div>
    <div class="card-title">Konverter Faktura</div>
    <div class="card-desc">Konvertuje Posted Sales Invoice Excel export u UBL Invoice XML (tip 380). Koristi nakon provere lot brojeva.</div>
    <span class="card-arrow">→</span>
</a>

<hr class="divider">

<div class="section-label">Knjižna odobrenja</div>

<a class="card" href="https://tkvwdvijz4fhhyzkt2jrzf.streamlit.app/" target="_blank" style="--accent: #f5a623;">
    <div class="card-step">Tip · Vezano za fakturu</div>
    <div class="card-title">Knjižno Odobrenje — sa referencom na fakturu</div>
    <div class="card-desc">Za knjižna odobrenja koja ispravljaju konkretnu fakturu. Potreban broj i datum originalne fakture.</div>
    <span class="card-arrow">→</span>
</a>

<a class="card" href="https://dokument-o-smanjenju-za-period-w2iwapp4j6njpjsmvu8x54u.streamlit.app/" target="_blank" style="--accent: #f5a623;">
    <div class="card-step">Tip · Periodično</div>
    <div class="card-title">Knjižno Odobrenje — za period</div>
    <div class="card-desc">Za periodična knjižna odobrenja (npr. kvartalni rabati). Unosi se samo period od/do, bez veze sa fakturom.</div>
    <span class="card-arrow">→</span>
</a>

<a class="card" href="https://dokument-o-smanjenju-ntssfgp8uwqeewqjnqzin5.streamlit.app/" target="_blank" style="--accent: #f5a623;">
    <div class="card-step">Tip · Ostalo</div>
    <div class="card-title">Knjižno Odobrenje — opšti</div>
    <div class="card-desc">Opšti konverter knjižnih odobrenja za ostale slučajeve koji ne spadaju u gornje kategorije.</div>
    <span class="card-arrow">→</span>
</a>

<hr class="divider">

<div class="hub-footer">Interni alat · Samo za internu upotrebu · mfin.gov.rs EN 16931 / UBL 2.1</div>
""", unsafe_allow_html=True)
