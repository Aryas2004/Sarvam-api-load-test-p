# Sarvam API Load Testing Report

This repository contains load testing scripts and results for the Sarvam API, using [Locust](https://locust.io/) to simulate traffic and capture performance metrics under different configurations.

---

## Test Configurations

We used the following configurations to test the `/transliterate` API:

| Test    | Users | RPS | Duration |
|---------|-------|-----|----------|
| Test 1  | 1     | 1   | 1m       |
| Test 2  | 5     | 2   | 1m       |
| Test 3  | 10    | 2   | 3m       |
| Test 4  | 25    | 4   | 5m       |

---

## Metrics Captured

- ✅ **p50 (Median) Latency**  
- ✅ **p75 and p95 Latency**  
- ✅ **Average Response Time**  
- ✅ **Requests per Second (RPS)**  
- ✅ **Error Rate**  
- ✅ **Language-wise Latency** *(planned/optional)*

---

## Folder Structure

sarvam-api-load-test/
├── locustfile.py # Locust script for /transliterate API
├── results/
│ ├── test1_stats.csv
│ ├── test2_stats.csv
│ ├── test3_stats.csv
│ ├── test4_stats.csv
│ └── google_sheet_link.txt # Contains link to Google Sheets summary
├── report/
│ └── interpretation_summary.md # Key insights and interpretation
└── README.md


 Navigate to the `results/` folder to view raw Locust exports and to `report/` for the insights summary.

---

## Google Sheets Report

🔗 **[Click here to view the full performance report](https://docs.google.com/spreadsheets/d/12JWWnXaT81N7gOeAZtRX6137LQxk734uwbVthTp83yE/edit?usp=sharing)**  
Includes raw data, summary table, configuration details, interpretation, and performance charts.

---

##  Interpretation Summary

- **Test 4 (25 users, 4 RPS)** showed the **highest error rate (65%)** and increased p95 latency (150ms).
- **Test 3 (10 users, 2 RPS)** had **stable performance with zero failures**, making it an optimal config.
- **Failures spiked beyond 10 users**, indicating system strain at higher concurrency.
- **Latency (p75/p95)** increased steeply with higher user load, while **p50 stayed relatively stable** at lower load levels.

---

## Submission Checklist

- ✅ Locust test script with sweep logic and percentile capture
- ✅ Google Sheet report with labeled tabs and performance graphs
- ✅ Summary and interpretation of performance results

## Run the test
locust -f locustfile.py
