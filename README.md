# 🧾 Task 7 - Data Analysis Using SQLite, Pandas, and Matplotlib

## 📖 Overview
This project demonstrates how to integrate **SQL** queries with **Python** for efficient data analysis and visualization.  
We use a **SQLite** database (`sales_data.db`) to store and query sales records, then process results using **pandas** and visualize with **matplotlib**.

---

## 🎯 Objective
- Connect a SQLite database using Python  
- Run aggregation queries (SUM, GROUP BY)  
- Analyze total revenue and quantities by product  
- Visualize sales performance using bar charts  

---

## 📂 Folder Structure
Task_7_Data_Analysis/
│
├── data/
│ └── sales_data.db # SQLite database file
│
├── output/
│ ├── sales_chart.png # Revenue visualization
│
├── task7_solution.py # Python analysis script
│
└── README.md # Project documentation


---

## ⚙️ Technologies Used
| Tool | Purpose |
|------|----------|
| **SQLite** | Database engine |
| **Python (sqlite3)** | Database connection |
| **pandas** | Data manipulation & analysis |
| **matplotlib** | Data visualization |

---

## 🧠 Step-by-Step Execution

### 2 Install Dependencies
```bash
pip install pandas matplotlib
```
### 2 Run the Script
```bash
python task7_solution.py
```

Sample Output
product	total_qty	revenue
Widget C	6	179.94
Widget A	17	169.83
Widget B	8	159.92
Widget D	1	49.99


### Author

Name: Rushikesh Palekar
Project: Task 7 - Data Analytics with SQLite & Python
Tools: Python, SQLite, Pandas, Matplotlib
