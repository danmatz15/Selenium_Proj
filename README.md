# 📈 Fresh Investment

## Selenium Test Automation for a Stock Trading Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python" />
  <img src="https://img.shields.io/badge/Selenium-Automation-success?logo=selenium" />
  <img src="https://img.shields.io/badge/Allure-Reporting-yellow?logo=allure" />
  <img src="https://img.shields.io/badge/Jenkins-CI/CD-red?logo=jenkins" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

🚀 A full-featured QA automation suite for a real-time stock trading simulation platform.  
Built with ❤️ using Python, Selenium, Allure, and Jenkins.

---

## 📸 Screenshots

> Here are screenshots showcasing the stock trading platform interface and automation execution:

**Screenshot 1: Interface of the Stock Trading Platform**
<p align="center">
  <img src="https://raw.githubusercontent.com/danmatz15/Selenium_Proj/main/Screenshot_1.png" width="800" alt="Stock Trading Platform Screenshot" />
</p>

**Screenshot 2: Automation Execution**
<p align="center">
  <img src="https://github.com/danmatz15/Selenium_Proj/blob/main/%D7%A6%D7%99%D7%9C%D7%95%D7%9D%20%D7%9E%D7%A1%D7%9A%202025-04-24%20081729.png" width="800" alt="Automation Execution Screenshot" />
</p>

**Screenshot 3: Detailed Test Report**
<p align="center">
  <img src="https://github.com/danmatz15/Selenium_Proj/blob/main/%D7%A6%D7%99%D7%9C%D7%95%D7%9D%20%D7%9E%D7%A1%D7%9A%202025-04-24%20081633.png" width="800" alt="Test Report Screenshot" />
</p>

---

## ✨ Features

- 🔍 **Visual Stock Analysis Validation**
- 💸 **Buy Action Simulation**
- 💰 **Balance Updates Post-Trade**
- 📊 **Allure Visual Test Reports**
- 🔁 **CI/CD with Jenkins Integration**

---

## 🧠 Tech Stack

| Category       | Tools              |
|----------------|--------------------|
| Language       | Python 3.10        |
| Automation     | Selenium WebDriver |
| Test Framework | Pytest             |
| Reporting      | Allure Framework   |
| CI/CD          | Jenkins            |

---

## 📁 Folder Structure

```
PythonProject4/
├── allure-report/        # Allure HTML reports
├── allure-results/       # Raw test result files
├── pages/                # Page Object Model (POM) classes
├── tests/                # Pytest test cases
│   ├── all.py
│   ├── base_test.py
│   ├── conftest.py
│   └── page1.test.py
├── utils/                # Helper functions (optional)
├── config.ini            # Environment config
├── requirements.txt      # Python dependencies
└── README.md             # You're here :)
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-user/FreshInvestment-Test.git
cd FreshInvestment-Test
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Tests

```bash
pytest --alluredir=allure-results
```

### 4️⃣ Generate Allure Report

```bash
allure serve allure-results
```

---

## 🔧 Configuration

Update `config.ini` with your environment (URLs, credentials, etc.).  
All test data is modular and separated from logic in the POM structure.

---

## ✅ TO-DO List

- [ ] Integrate Allure Reports
- [ ] Add balance check functionality
- [ ] Jenkins CI pipeline setup
- [ ] Add Slack/Email alerts for failed builds
- [ ] Expand to mobile viewports with Appium
- [ ] Add multi-browser support (Chrome, Firefox, Edge)

---

## 🗺️ Roadmap

| Milestone               | Status      | ETA        |
|-------------------------|-------------|------------|
| ✅ Basic Flow Tests      | Completed   | 2025-03-20 |
| ✅ Allure Integration    | Completed   | 2025-04-01 |
| 🚧 Mobile Testing        | In Progress | Q2 2025    |
| 🔜 Cross-Browser CI      | Planned     | Q2–Q3 2025 |

---

## 👨‍💻 Maintainers

| Name           | Role                 | Contact                  |
|-----------------|----------------------|--------------------------|
| Dan Matzliach  | QA Automation Lead   | 📧 danmatz12@gmail.com   |
