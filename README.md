# Online Store Dashboard

This repository contains a complete data analytics project for a fictional online store. The goal is to simulate a real-world data analyst workflow using Python, SQL, and Tableau Public.

## Project Objective

To explore and answer typical business questions, such as:

- What are the best-selling products?
- Which customers generate the most revenue?
- How do sales vary by month and country?
- What is the customer repeat rate?

## Tools and Technologies

- Python: for data simulation, transformation, and preprocessing (pandas, sqlite3)
- SQL: for querying the data using SQLite
- Tableau Public: for building interactive visualizations and dashboards
- Git and GitHub: for version control and documentation

## Project Structure

```
online-store-dashboard/
├── data/             # Simulated CSV or SQLite files
├── sql/              # SQL query files used during the analysis
├── scripts/          # Python scripts for generating and processing data
├── dashboards/       # Tableau (.twbx) files and exported screenshots
├── README.md         # Project documentation
└── requirements.txt  # Python dependencies
```

## Dataset

The dataset is fully synthetic and includes:

- `customers.csv`: customer IDs, names, countries, ages, etc.
- `orders.csv`: order IDs, customer IDs, timestamps, totals
- `products.csv`: product IDs, names, categories
- `order_items.csv`: items per order, quantities, prices

## Getting Started

1. Clone the repository

   ```bash
   git clone https://github.com/JayroMartinez/online-store-dashboard.git
   cd online-store-dashboard
   ```

2. (Optional) Create a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages

   ```bash
   pip install -r requirements.txt
   ```

4. Run the scripts in the `scripts/` directory  
   Generate or preprocess the data by running the appropriate Python files.

5. Open the data files in Tableau Public  
   Use the cleaned/generated files from the `data/` folder to build dashboards.

## Visual Output

Screenshots of the dashboards created in Tableau will be added to the `dashboards/` folder and included below.

## Notes

- All data used in this project is fictitious and created for educational purposes.
- Tableau Public dashboards will be published and linked once available.
