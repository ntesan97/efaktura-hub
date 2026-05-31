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
    background-color: #f7f7f5;
    color: #1a1a1a;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 680px; padding: 4rem 2rem 6rem; }

.hub-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem; letter-spacing: 0.2em; text-transform: uppercase;
    color: #aaa; margin-bottom: 1rem;
}
.hub-title {
    font-size: 2.2rem; font-weight: 600; color: #111;
    line-height: 1.15; letter-spacing: -0.03em; margin-bottom: 0.6rem;
}
.hub-sub {
    font-size: 0.92rem; color: #888; line-height: 1.65;
    max-width: 460px; margin-bottom: 3rem;
}
.section {
    background: #fff; border: 1px solid #e8e8e4;
    border-radius: 10px; padding: 1.75rem; margin-bottom: 1rem;
}
.section-header {
    display: flex; align-items: center; gap: 0.75rem;
    margin-bottom: 1.25rem; padding-bottom: 1.25rem;
    border-bottom: 1px solid #f0f0ec;
}
.section-icon {
    width: 36px; height: 36px; border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem; flex-shrink: 0;
}
.section-title { font-size: 0.95rem; font-weight: 600; color: #111; letter-spacing: -0.01em; }
.section-desc { font-size: 0.8rem; color: #999; margin-top: 0.1rem; }

.steps { display: flex; flex-direction: column; gap: 0.5rem; }
.step-row { display: flex; align-items: stretch; gap: 0.75rem; }
.step-left { display: flex; flex-direction: column; align-items: center; flex-shrink: 0; width: 28px; }
.step-num {
    width: 28px; height: 28px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-family: 'DM Mono', monospace; font-size: 0.72rem; font-weight: 500; flex-shrink: 0;
}
.step-line { width: 1px; flex: 1; margin-top: 4px; background: #e8e8e4; min-height: 12px; }
.step-content { flex: 1; padding-bottom: 0.5rem; }

.tool-link {
    display: flex; align-items: center; justify-content: space-between;
    text-decoration: none; background: #f7f7f5;
    border: 1px solid #e8e8e4; border-radius: 7px;
    padding: 0.9rem 1.1rem; margin-top: 0.4rem;
    transition: border-color 0.15s, background 0.15s, transform 0.12s;
}
.tool-link:hover { background: #f0f0ec; border-color: #d0d0cc; transform: translateY(-1px); }
.tool-link-name { font-size: 0.88rem; font-weight: 600; color: #111; margin-bottom: 0.18rem; }
.tool-link-hint { font-size: 0.75rem; color: #aaa; }
.tool-link-arrow { font-size: 0.9rem; color: #ccc; margin-left: 1rem; flex-shrink: 0; transition: transform 0.15s; }
.tool-link:hover .tool-link-arrow { transform: translateX(2px); }

.standalone-cards { display: flex; flex-direction: column; gap: 0.5rem; }
.standalone-link {
    display: flex; align-items: center; justify-content: space-between;
    text-decoration: none; background: #f7f7f5;
    border: 1px solid #e8e8e4; border-radius: 7px; padding: 1rem 1.1rem;
    transition: border-color 0.15s, background 0.15s, transform 0.12s;
}
.standalone-link:hover { background: #f0f0ec; border-color: #d0d0cc; transform: translateY(-1px); }
.standalone-link-name { font-size: 0.88rem; font-weight: 600; color: #111; margin-bottom: 0.18rem; }
.standalone-link-hint { font-size: 0.75rem; color: #aaa; }
.standalone-link-arrow { font-size: 0.9rem; color: #ccc; margin-left: 1rem; flex-shrink: 0; transition: transform 0.15s; }
.standalone-link:hover .standalone-link-arrow { transform: translateX(2px); }

.hub-footer {
    margin-top: 3rem; font-family: 'DM Mono', monospace;
    font-size: 0.63rem; letter-spacing: 0.1em; color: #ccc; text-align: center;
}
</style>

<div class="hub-eyebrow">Interni alati · eFaktura</div>
<h1 class="hub-title">eFaktura Konverteri</h1>
<p class="hub-sub">Konverzija Business Central Excel exporta u UBL XML za slanje putem Sistema eFaktura.</p>

<div class="section">
  <div class="section-header">
    <div class="section-icon" style="background:#f0fae0;">📄</div>
    <div>
      <div class="section-title">Fakture</div>
      <div class="section-desc">Dva obavezna koraka — najpre obogati podatke, zatim konvertuj</div>
    </div>
  </div>
  <div class="steps">
    <div class="step-row">
      <div class="step-left">
        <div class="step-num" style="background:#f0fae0; color:#5a9e10;">1</div>
        <div class="step-line"></div>
      </div>
      <div class="step-content">
        <a class="tool-link" href="https://tkvwdvijz4fhhyzkt2jrzf.streamlit.app/" target="_blank">
          <div>
            <div class="tool-link-name">Lot Enricher</div>
            <div class="tool-link-hint">Obogati Excel fajl ispravnim lot brojevima pre konverzije</div>
          </div>
          <span class="tool-link-arrow">→</span>
        </a>
      </div>
    </div>
    <div class="step-row">
      <div class="step-left">
        <div class="step-num" style="background:#f0fae0; color:#5a9e10;">2</div>
        <div class="step-line"></div>
      </div>
      <div class="step-content">
        <a class="tool-link" href="https://invoice-converter-bng8er2uezdi2kklxzls6z.streamlit.app/" target="_blank">
          <div>
            <div class="tool-link-name">Konverter Faktura</div>
            <div class="tool-link-hint">Konvertuj obogaćeni Excel u UBL Invoice XML (tip 380)</div>
          </div>
          <span class="tool-link-arrow">→</span>
        </a>
      </div>
    </div>
    <div class="step-row">
      <div class="step-left">
        <div class="step-num" style="background:#f0fae0; color:#5a9e10;">T</div>
      </div>
      <div class="step-content">
        <a class="tool-link" href="https://invoice-converter-test-hqpzrwh5wxpvndxmrshypj.streamlit.app/" target="_blank">
          <div>
            <div class="tool-link-name">Konverter Faktura Test</div>
            <div class="tool-link-hint">Test verzija konvertora — za proveravanje novih verzija</div>
          </div>
          <span class="tool-link-arrow">→</span>
        </a>
      </div>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-header">
    <div class="section-icon" style="background:#fff5e8;">📋</div>
    <div>
      <div class="section-title">Knjižna odobrenja</div>
      <div class="section-desc">Izaberi tip prema nameni dokumenta</div>
    </div>
  </div>
  <div class="standalone-cards">
    <a class="standalone-link" href="https://dokument-o-smanjenju-ntssfgp8uwqeewqjnqzin5.streamlit.app/" target="_blank">
      <div>
        <div class="standalone-link-name">Dokument o smanjenju</div>
        <div class="standalone-link-hint">Knjižno odobrenje vezano za konkretnu fakturu</div>
      </div>
      <span class="standalone-link-arrow">→</span>
    </a>
    <a class="standalone-link" href="https://dokument-o-smanjenju-za-period-w2iwapp4j6njpjsmvu8x54u.streamlit.app/" target="_blank">
      <div>
        <div class="standalone-link-name">Dokument o smanjenju za period</div>
        <div class="standalone-link-hint">Periodično smanjenje — kvartalni rabati, godišnji bonusi</div>
      </div>
      <span class="standalone-link-arrow">→</span>
    </a>
  </div>
</div>

<div class="hub-footer">Samo za internu upotrebu · EN 16931 / UBL 2.1 · mfin.gov.rs 2022</div>
""", unsafe_allow_html=True)
