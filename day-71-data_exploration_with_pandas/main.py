import pandas as pd


def main():
    df = pd.read_csv("salaries_by_college_major.csv")
    clean_df = df.dropna()
    print(clean_df['Starting Median Salary'].idxmax())
    print(f"**********************Highest starting salary**********************\n"
          f"{clean_df.loc[clean_df['Starting Median Salary'].idxmax()]}\n"
          f"**********************Highest starting salary**********************\n")
    print(f"**********************Highest Mid-Career salary**********************\n "
          f"{clean_df.loc[clean_df['Mid-Career Median Salary'].idxmax()]}\n"
          f"**********************Highest Mid-Career salary**********************\n")
    print(f"**********************Lowest starting salary**********************\n"
          f"{clean_df.loc[clean_df['Starting Median Salary'].idxmin()]}\n"
          f"**********************Lowest starting salary**********************\n")
    print(f"**********************Lowest Mid-Career salary**********************\n "
          f"{clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]}\n"
          f"**********************Lowest Mid-Career salary**********************")


if __name__ == "__main__":
    main()
