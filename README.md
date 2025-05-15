# Online Store Dashboard

This repository contains a complete data analytics project for a fictional online store. The goal is to simulate a real-world data analyst workflow using Python, SQL, and Tableau Public.

## Project Objective

To explore and answer typical business questions, such as:

- What are the best-selling products?
- Which customers generate the most revenue?
- How do sales vary by month and country?
- What is the customer repeat rate?

## Tools and Technologies

- Python: for data simulation, transformation, and preprocessing (pandas, sqlite,...)
- SQL: for querying the data using SQLite
- Tableau Public: for building interactive visualizations and dashboards
- Git and GitHub: for version control and documentation

## Project Structure

```
online-store-dashboard/
├── data/               # SQLite database and generated CSVs
├── dashboards/
│   ├── png/            # Exported PNG images from Tableau
│   └── tableau/        # Tableau .twbx files (one per analysis)
├── scripts/            # Python scripts for data generation and analysis
├── sql/                # Optional: raw SQL queries
├── README.md           # Project documentation
└── .gitignore
```

## Dataset

The dataset is fully synthetic and includes:

- `customers`: customer IDs, names, countries, ages, etc.
- `orders`: order IDs, customer IDs, timestamps, totals
- `products`: product IDs, names, categories
- `order_items`: items per order, quantities, prices

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/JayroMartinez/online-store-dashboard.git
   cd online-store-dashboard
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages (the only required package is Pandas):

   ```bash
   pip install -r requirements.txt
   ```

4. Run the scripts in the `scripts/` directory to generate and populate the SQLite database.

5. Use Tableau Public to open and explore the `.twbx` files found in the `dashboards/tableau/` directory.

## Results

All analysis outputs are organized under the `dashboards/` folder:

- `dashboards/png/` contains exported PNG images of each Tableau visualization.
- `dashboards/tableau/` contains the corresponding `.twbx` Tableau Packaged Workbooks for each individual analysis.

