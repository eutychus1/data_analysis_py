
# =======================
# Task 1: Load and Explore Dataset
# =======================
try:
    # Load your dataset
    df = pd.read_csv("sales_data_updated.csv")
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    df = pd.DataFrame()  # empty fallback
except Exception as e:
    print(f"An error occurred while loading the dataset: {e}")
    df = pd.DataFrame()

# Inspect the first few rows
print("First 5 rows:")
print(df.head())

# Check structure and missing values
print("\nDataset Info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Clean missing values (if any)
df = df.dropna()

# =======================
# Task 2: Basic Data Analysis
# =======================

# Descriptive statistics
print("\nDescriptive statistics:")
print(df.describe(numeric_only=True))

# Calculate total revenue
total_revenue = df["Revenue ($)"].sum()
print(f"\nTotal Revenue: ${total_revenue:,.2f}")

# Find the best-selling product based on Quantity Sold
best_selling_product = (
    df.groupby("Product")["Quantity Sold"].sum().idxmax()
)
print(f"Best-Selling Product: {best_selling_product}")

# Identify the day with the highest sales (Quantity Sold)
day_highest_sales = (
    df.groupby("Date (YYYY-MM-DD)")["Quantity Sold"].sum().idxmax()
)
print(f"Day with Highest Sales: {day_highest_sales}")

# Save the summary to a text file
summary_text = f"""
Sales Summary Report
---------------------
Total Revenue: ${total_revenue:,.2f}
Best-Selling Product: {best_selling_product}
Day with Highest Sales: {day_highest_sales}
"""
with open("sales_summary.txt", "w") as f:
    f.write(summary_text)
print("\nSummary saved to sales_summary.txt")

# =======================
# Task 3: Data Visualization
# =======================

# 1. Revenue per Product (Bar Chart)
plt.figure(figsize=(8,5))
df.groupby("Product")["Revenue ($)"].sum().plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Total Revenue per Product")
plt.xlabel("Product")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Quantity Sold per Day (Line Chart)
plt.figure(figsize=(8,5))
df.groupby("Date (YYYY-MM-DD)")["Quantity Sold"].sum().plot(kind="line", marker="o")
plt.title("Daily Quantity Sold")
plt.xlabel("Date")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Histogram of Revenue ($)
plt.figure(figsize=(8,5))
plt.hist(df["Revenue ($)"], bins=15, color="orange", edgecolor="black")
plt.title("Distribution of Revenue per Transaction")
plt.xlabel("Revenue ($)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# =======================
# Findings / Observations
# =======================
print("""
 Findings:
1. We identified the product contributing the most sales quantity overall.
2. The day with the highest sales can be used for promotions or planning.
3. Bar and line charts show which products/dates generate most revenue.
4. Revenue distribution helps identify typical transaction sizes.
""")
