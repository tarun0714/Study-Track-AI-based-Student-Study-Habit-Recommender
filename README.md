# 🛍️ Online Retail Dataset — Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the [Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail) from the UCI Machine Learning Repository. The dataset contains transactional data for a UK-based and registered non-store online retail business between December 2010 and December 2011.

The main goal of this analysis is to:
- Understand **sales trends**, **customer behavior**, and **product performance**
- Identify **top-selling products** and **key markets**
- Uncover **seasonal patterns** and **revenue drivers**
- Support **data-driven business decisions** through visual insights

---

## 📂 Dataset Description

**Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/online+retail)  
**Format:** Excel file (`Online Retail.xlsx`)  
**Size:** 541,909 transactions  
**Time Period:** December 2010 - December 2011

### Dataset Attributes

| Column Name     | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| InvoiceNo       | Unique 6-digit invoice number for each transaction                         |
| StockCode       | Unique product/item code                                                    |
| Description     | Product name                                                                |
| Quantity        | Number of units purchased per transaction                                   |
| InvoiceDate     | Date and time of transaction                                               |
| UnitPrice       | Product price per unit (British Pound Sterling £)                          |
| CustomerID      | Unique customer identifier                                                  |
| Country         | Customer's country of residence                                             |

---

## 🛠️ Technologies Used

- **Python 3.x** – Programming language
- **Pandas** – Data manipulation and analysis
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical graphics
- **Jupyter Notebook** – Interactive analysis environment
- **OpenPyXL** – Excel file handling

---

## 🧼 Data Cleaning & Preprocessing

The dataset required several cleaning steps to ensure accurate analysis:

1. **Column Name Standardization** – Removed extra whitespace from column headers
2. **Missing Value Treatment** – Handled missing CustomerID entries
3. **Duplicate Removal** – Eliminated redundant transaction records
4. **Date Conversion** – Transformed InvoiceDate to datetime format for temporal analysis
5. **Feature Engineering** – Created a new `Revenue` column by multiplying Quantity × UnitPrice
6. **Data Quality Checks** – Validated data types and identified outliers

---

## 📊 Analysis Components

### 🔍 Key Analyses Performed

1. **Product Performance Analysis**
   - Identified top 10 products by total revenue
   - Analyzed product popularity and sales distribution
   - Revealed concentration of sales in specific items

2. **Geographic Distribution**
   - Mapped customer distribution across countries
   - Identified primary markets and growth opportunities
   - Highlighted UK dominance in transaction volume

3. **Correlation Analysis**
   - Examined relationships between Quantity, UnitPrice, and Revenue
   - Discovered patterns in pricing and purchase behavior
   - Created visual heatmap for easy interpretation

4. **Temporal Trends**
   - Tracked monthly revenue patterns over the year
   - Identified seasonal peaks and valleys
   - Uncovered business cycles and demand fluctuations

---

## 📈 Key Insights & Findings

### 💡 Business Intelligence

- **Revenue Concentration:** A small subset of products generates the majority of total revenue (Pareto principle)
- **Geographic Focus:** The United Kingdom accounts for the largest share of transactions
- **Strong Correlations:** Quantity and Revenue show significant positive correlation
- **Seasonal Patterns:** Clear seasonal demand spikes suggest opportunities for targeted marketing
- **Pricing Variability:** UnitPrice shows diverse patterns across different product categories

### 🎯 Actionable Recommendations

- Focus inventory management on high-revenue products
- Develop market expansion strategies for underserved regions
- Plan promotional campaigns around identified seasonal peaks
- Optimize pricing strategies based on correlation insights

---

## 🔮 Future Enhancements

### Potential Next Steps

- **Customer Segmentation:** Implement RFM (Recency, Frequency, Monetary) analysis to categorize customers
- **Predictive Analytics:** Build forecasting models for sales prediction
- **Market Basket Analysis:** Identify product associations and cross-selling opportunities
- **Interactive Dashboard:** Create real-time visualization dashboard using Plotly or Tableau
- **Churn Analysis:** Develop customer retention strategies
- **Anomaly Detection:** Identify unusual transaction patterns

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Jupyter Notebook
- Basic understanding of data analysis concepts

### Installation

1. **Clone the repository:**
```bash
   git clone https://github.com/your-username/STUDYTRACK_AI_STUDENTRECOMMENDER.git
   cd STUDYTRACK_AI_STUDENTRECOMMENDER/MILESTONE\ 1
```

2. **Install required packages:**
```bash
   pip install pandas matplotlib seaborn openpyxl jupyter
```

3. **Download the dataset:**
   - Ensure `Online Retail.xlsx` is placed in the `data/` folder

4. **Launch Jupyter Notebook:**
```bash
   jupyter notebook Milestone1_EDA.ipynb
```

5. **Execute the analysis:**
   - Run all cells sequentially to reproduce the analysis

---

## 📚 References & Resources

- [UCI Machine Learning Repository - Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Visualization Gallery](https://seaborn.pydata.org/examples/index.html)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Exploratory Data Analysis Best Practices](https://towardsdatascience.com/exploratory-data-analysis-8fc1cb20fd15)

---

## 👨‍💻 Author

**Tarun Gupta**  
🎓 Manipal University Jaipur  
📧 tarungupta0714@gmail.com  

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/STUDYTRACK_AI_STUDENTRECOMMENDER/issues).

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- UCI Machine Learning Repository for providing the dataset
- The open-source community for excellent data analysis tools
- Manipal University Jaipur for academic support
---
