# 📊 Sarvam API Load Testing – Interpretation Summary

This report summarizes the results of load testing conducted on the `/transliterate` endpoint of the Sarvam API using Locust. Four test configurations were executed to observe how the system performs under varying levels of traffic.

---

## ✅ Test Configurations

| Test    | Users | RPS | Duration |
|---------|-------|-----|----------|
| Test 1  | 1     | 1   | 1m       |
| Test 2  | 5     | 2   | 1m       |
| Test 3  | 10    | 2   | 3m       |
| Test 4  | 25    | 4   | 5m       |

---

## 📌 Key Insights

| Question                                       | Observation                                                                 |
|------------------------------------------------|------------------------------------------------------------------------------|
| **Which configuration caused high latency or errors?** | Test 4 showed the highest error rate (65%) and p95 latency of 150ms.        |
| **Which configuration is optimal?**           | Test 3 maintained stable latency and had 0% failure rate.                   |
| **Where did things break?**                   | In Test 4, 1976 out of 3040 requests failed – system couldn't handle the load. |
| **Any pattern in latency (p50, p75, p95)?**   | p50 remained stable, while p75 and p95 latencies increased sharply after 10 users. |
| **Summary/Takeaway**                          | The system handles up to 10 users well. Beyond that, latency and errors spike. |

---

## 📈 Observed Performance Metrics

| Metric        | Test 1 | Test 2 | Test 3 | Test 4 |
|---------------|--------|--------|--------|--------|
| p50 (Median)  | 130ms  | 130ms  | 140ms  | 43ms   |
| p75           | 140ms  | 150ms  | 150ms  | 120ms  |
| p95           | 160ms  | 460ms  | 200ms  | 150ms  |
| Avg RT        | 134.95 | 170.82 | 142.69 | 73.59  |
| Error Rate    | 0%     | 0%     | 0%     | 65%    |

---

## 📌 Conclusion

- Performance is reliable up to **10 users** and **2 RPS**.
- Beyond that, the API shows signs of **overload and significant failure**.
- Consider scaling infrastructure or rate-limiting traffic if user count increases beyond this range.

---

📄 For visual charts and raw numbers, refer to the full [Google Sheet Report](https://docs.google.com/spreadsheets/d/12JWWnXaT81N7gOeAZtRX6137LQxk734uwbVthTp83yE/edit?usp=sharing).
