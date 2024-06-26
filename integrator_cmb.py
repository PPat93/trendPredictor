"""
Integrator comb:
Integrates modules;
Passes flags invoking actions;
Holds actions confirmations;

API Data Retriever -> Integrator -> Analyzer
Database -> Integrator -> Analyzer
Analyzer ->Integrator -> Database
Analyzer -> Integrator -> Mailer
Database -> Integrator -> Mailer
"""

from analyzer_cmb import run_trend_analysis


def invoke_trend_analysis(ticker: str):
    """Execute trend analysis"""

    is_trend_reversed = run_trend_analysis(ticker)
    # return analysis_result TODOs
