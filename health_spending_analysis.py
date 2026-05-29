import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    life_exp_df = pd.read_csv(
        'Health_Data_Projects/datasets/life_expectancy.csv')
    spending_df = pd.read_csv(
        'Health_Data_Projects/datasets/healthcare_expenditure.csv')
    print("Datasets loaded succefuly")

except FileNotFoundError:
    print("Error: Could not find the CSV files. Check your 'datasetes")

print("\nLife Expectancy Data Sample:")
print(life_exp_df.head(2))
print("\nHealth Spending Data Sample")
print(spending_df.head(2))

# Merging Datasets
merged_data = pd.merge(life_exp_df, spending_df, left_on=[
                       'Country', 'Year'], right_on=['Entity', 'Year'])

print("\nMerged Dataset Columns:")
print(list(merged_data.columns))


cleaned_data = merged_data.dropna(
    subset=['Life expectancy ', 'Current health expenditure (CHE) as percentage of gross domestic product (GDP) (%)'])

# Vitual Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=cleaned_data,
    x="Current health expenditure (CHE) as percentage of gross domestic product (GDP) (%)",
    y="Life expectancy ",
    alpha=0.7,
    color="teal"
)

plt.title("Global Health Spending vs. Life Expenditure",
          fontsize=14, fontweight="bold")
plt.xlabel("Current Health Expenditure (% of GDP)", fontsize=12)
plt.xlabel("Life Expectancy at Birth (Years)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

# Saving visual file instanly for GitHub and display it
plt.savefig("health_spending_vs_life_expectancy.png",
            dpi=300, bbox_inches='tight')
print("\n Success! Image is saved as health_spending_vs_life_expectancy.png ")
