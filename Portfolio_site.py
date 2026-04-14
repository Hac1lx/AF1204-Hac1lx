# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.19.10",
#     "pandas>=2.3.3",
#     "plotly>=6.5.1",
#     "pyarrow>=22.0.0",
#     "pyzmq>=27.1.0",
# ]
# ///

import marimo

__generated_with = "0.19.11"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## 📊 AF1204 — Personal Portfolio
    Hassan Ahmad Chaudhary · BSc Accounting & Finance · Bayes Business School
    """)
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import micropip
    return micropip, mo, pd


@app.cell
def _(pd):
    # Load S&P 500 dataset from remote gist URL (Week 4 — WASM deployment technique)
    # Local file loading does not work on GitHub Pages due to compression issues
    DATA_URL = (
        "https://gist.githubusercontent.com/DrAYim/"
        "80393243abdbb4bfe3b45fef58e8d3c8/raw/"
        "ed5cfd9f210bf80cb59a5f420bf8f2b88a9c2dcd/"
        "sp500_ZScore_AvgCostofDebt.csv"
    )

    raw_df = pd.read_csv(DATA_URL)

    # Data cleaning — drop rows with missing key variables (Week 2 concept)
    raw_df = raw_df.dropna(subset=["AvgCost_of_Debt", "Z_Score_lag", "Sector_Key"])

    # Winsorise at 500% to remove extreme outliers (Week 6 — data cleaning strategy)
    raw_df = raw_df[raw_df["AvgCost_of_Debt"] < 5]

    # Feature engineering (Week 4)
    raw_df["Cost_Pct"]  = raw_df["AvgCost_of_Debt"] * 100
    raw_df["MCap_B"]    = raw_df["Market_Cap"] / 1e9

    return (raw_df,)


@app.cell
def _(mo):
    tab_profile = mo.md("""
### Hassan Ahmad Chaudhary
📧 Hassan-ahmad.chaudhary@bayes.city.ac.uk &nbsp;|&nbsp; 📞 07495 558964
🔗 linkedin.com/in/hassan-ahmad-chaudhary-b44130372

---

**Profile**

First-year Accounting & Finance student at Bayes Business School with hands-on
experience in financial operations and business administration gained through managing
family business activities. Strong analytical mindset with a keen interest in
accounting, financial management, and entrepreneurship.

---

**Education**

| Qualification | Institution | Year |
|--------------|-------------|------|
| BSc Accounting & Finance | Bayes Business School, City, University of London | 2025 – 2028 |
| International Foundation Programme (Business) | INTO City, University of London | Completed 2025 |
| O Levels | Roots IVY International School, Faisalabad | Completed 2024 |

*Key Module:* AF1204 — Introduction to Data Science and AI Tools

---

**Experience**

**Operations and Administrative Assistant** *(May 2025 – Sept 2025)*
- Supported finance, accounts, procurement, and sales operations
- Led implementation of an ERP system — improving financial accuracy and reporting efficiency
- Prepared voucher entries and assisted in monthly profit and expense reporting
- Conducted supplier price comparisons and identified operational inefficiencies
- Expanded the firm's international customer base through targeted digital marketing

---

**Skills**

| Category | Details |
|----------|---------|
| 💼 Finance | Financial record-keeping · ERP data management · Business operations analysis |
| 🐍 Programming | Python · pandas · Plotly · Marimo · exception handling |
| 📊 Visualisation | Interactive charts — scatter, violin, bar, geo maps |
| 🌐 Data Collection | Web scraping concepts · Playwright · PyMuPDF |
| 🤖 AI Tools | Prompt Engineering · RAG · Google AI Studio |
| 📋 Office | Excel (formulas, data handling) · Word · PowerPoint |

**Languages:** English · Urdu · Punjabi

---

**Achievements & Interests**

- Successfully led full transition of business operations onto an ERP system
- Multiple sports awards in Badminton and Cricket
- Interests: Entrepreneurship · Investment Banking · New venture exploration
    """)
    return (tab_profile,)


@app.cell
def _(mo, tab_profile):
    portfolio = mo.ui.tabs({
        "🏠 Profile": tab_profile,
    })

    mo.md(f"""
# **Hassan Ahmad Chaudhary**
*AF1204 Portfolio · BSc Accounting & Finance · Bayes Business School*

---

{portfolio}
    """)
    return


if __name__ == "__main__":
    app.run()
