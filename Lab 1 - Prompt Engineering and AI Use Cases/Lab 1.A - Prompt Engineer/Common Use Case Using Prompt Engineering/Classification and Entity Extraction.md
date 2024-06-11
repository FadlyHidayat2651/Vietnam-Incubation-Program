## Classification and Entity Extraction Financial use cases
In this demonstration, your objective is to effectively get **Classification and Entity Extraction Financial** based on the information from the passage text based on your specific requirements. Feel free to use zero-shot, one-shot, or few-shot learning, and adjust your model parameters and instructions from the prompt.

***

### Description:
Your task is to classify and extract the information based on the Financial Metrics Earnings Reports

**Instructions:**


Based on a publicly traded company's annual or quarterly earnings report, identify and extract the following financial metrics, along with appropriate period and comparable figures (if available):
1. Revenue
2. Net Income
3. Earnings Before Interest, Taxes, Depreciation, and Amortization (EBITDA)
4. Cash Flow
Be sure to include the reporting period (for example, Q1 2023 or FY 2022) and any comparable figures from prior periods mentioned alongside the metrics. Also, provide the source or page number of the report where each metric is found.


**Example:**


Inputs:
Acme Corp. reported net income of $45.2 million for the fourth quarter of 2022, up from $40.1 million in the same quarter a year earlier. Net profit was $5.3 million, up from $4.8 million in Q4 2021.

Output:
- Revenue: $45.2 million (Q4 2022), $40.1 million (Q4 2021)
- Net Income: $5.3 million (Q4 2022), $4.8 million (Q4 2021)

Inputs:
For fiscal year 2022, Beta Inc. had net income of $150 million, and EBITDA of $200 million. Cash flow from operations was reported at $180 million.


Output:
```
- Net Income: $150 million (FY 2022)
- EBITDA: $200 million (FY 2022)
- Cash Flow: $180 million (FY 2022)
```

**Exercise:**


Input: Gamma Industries announced revenue of $75 million for the first quarter of 2023, with net income of $10 million. EBITDA for the period was reported at $15 million, while cash flow from operations was $20 million.


Output: ???


Input: PT. XYZ announced revenue of IDR 500 billion for the first quarter of 2023, with a net profit of IDR 50 billion. EBITDA for the period was reported at IDR 75 billion, while cash flow from operations was IDR 100 billion.


Output: ???