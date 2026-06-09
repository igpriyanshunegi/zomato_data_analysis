# 🍽️ Zomato Restaurant Data Analysis

A comprehensive exploratory data analysis (EDA) of Zomato restaurant data from Bengaluru, India. This project uncovers insights into restaurant types, ratings, pricing, online ordering trends, and customer engagement using Python's data science stack.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis & Visualizations](#analysis--visualizations)
- [Key Findings](#key-findings)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

---

## Overview

This project performs an end-to-end exploratory data analysis on Zomato's restaurant listings. The goal is to answer business questions such as:

- Which restaurant types are most common on Zomato?
- Do restaurants offering online ordering receive higher ratings?
- What is the typical cost for two people across different restaurant types?
- Which restaurant type receives the most customer votes?

---

## Dataset

**File:** `Zomato-data.csv`

| Column | Description |
|--------|-------------|
| `name` | Name of the restaurant |
| `online_order` | Whether the restaurant accepts online orders (`Yes`/`No`) |
| `book_table` | Whether table booking is available (`Yes`/`No`) |
| `rate` | Customer rating (format: `x.x/5`) |
| `votes` | Total number of customer votes/reviews |
| `approx_cost(for two people)` | Estimated cost for two people (in INR ₹) |
| `listed_in(type)` | Category/type of restaurant (e.g., Buffet, Cafes, Dining) |

**Sample size:** ~150+ restaurant entries across multiple categories including Buffet, Cafes, Dining, and others.

---

## Project Structure

```
zomato_data_analysis/
│
├── Zomato-data.csv               # Raw dataset
├── Zomato_data_analysis.py       # Main analysis script
└── README.md                     # Project documentation
```

---

## Installation

### Prerequisites

- Python 3.7+
- pip

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/igpriyanshunegi/zomato_data_analysis.git
   cd zomato_data_analysis
   ```

2. **Install required libraries**
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

3. **Place the dataset** in the same directory as the script, named `Zomato-data.csv`.

---

## Usage

Run the analysis script directly:

```bash
python Zomato_data_analysis.py
```

This will:
- Load and clean the dataset
- Print dataset info and missing value counts to the console
- Display 8 sequential visualizations
- Print a summary of the restaurant with the highest number of votes

---

## Analysis & Visualizations

The script generates the following 8 plots:

### 1. 📊 Distribution of Restaurant Types
A count plot showing how many restaurants fall under each category (Buffet, Cafes, Dining, etc.).

### 2. ⭐ Distribution of Restaurant Ratings
A count plot of all restaurant rating values to understand the rating spread across the dataset.

### 3. 💰 Distribution of Approximate Cost for Two
A histogram showing how restaurant pricing is distributed — useful for identifying the most common price ranges.

### 4. 🏆 Average Ratings by Restaurant Type
A horizontal bar chart comparing the mean rating across different restaurant categories.

### 5. 📱 Online Order Availability
A count plot showing the split between restaurants that do and don't offer online ordering.

### 6. 🗳️ Total Votes by Restaurant Type
A line plot visualizing customer engagement (total votes) grouped by restaurant type.

### 7. 📦 Ratings vs. Online Order (Boxplot)
A boxplot comparing the rating distributions for restaurants with and without online ordering — reveals if online ordering correlates with better ratings.

### 8. 🔥 Heatmap: Restaurant Type vs. Online Order
A heatmap showing the count of restaurants for each combination of restaurant type and online order availability.

---

## Key Findings

- **Dining** is the most listed restaurant type on Zomato in this dataset.
- Restaurants **with online ordering** tend to have slightly higher median ratings compared to those without.
- The majority of restaurants fall in the **₹300–₹800** price range for two people.
- **Cafes and Dining** restaurants accumulate the most customer votes, indicating higher engagement.
- A small number of restaurants (e.g., *Empire Restaurant*, *Meghana Foods*) dominate vote counts, suggesting strong brand loyalty.

---

## Technologies Used

| Tool | Purpose |
|------|---------|
| **Python 3** | Core programming language |
| **Pandas** | Data loading, cleaning, and manipulation |
| **NumPy** | Numerical operations |
| **Matplotlib** | Base plotting library |
| **Seaborn** | Statistical data visualization |

---

## Contributing

Contributions, bug reports, and feature requests are welcome!

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> **Note:** This dataset is intended for educational and analytical purposes only. Restaurant data sourced from Zomato listings in Bengaluru, India.
