import pandas as pd
import os

# Extract function is already implemented for you 
def extract(store_data, extra_data):
    extra_df = pd.read_parquet(extra_data)
    merged_df = store_data.merge(extra_df, on = "index")
    return merged_df

# Call the extract() function and store it as the "merged_df" variable
merged_df = extract(grocery_sales, "extra_data.parquet")

# Create the transform() function with one parameter: "raw_data"
def transform(raw_data):
  # Write your code here
    raw_data.fillna(
        {
            'CPI': raw_data['CPI'].mean(),
              'Weekly_Sales': raw_data['Weekly_Sales'].mean(),
              'Unemployment': raw_data['Unemployment'].mean(),
        }, inplace = True
    )

    raw_data["Date"] = pd.to_datetime(raw_data["Date"], format = "%Y-%m-%d")
    raw_data["Month"] = raw_data["Date"].dt.month
    raw_data = raw_data.loc[raw_data["Weekly_Sales"] > 10000, :]
    raw_data = raw_data.drop(["index", "Temperature", "Fuel_Price", "MarkDown1", "MarkDown2", "MarkDown3", "MarkDown4", "MarkDown5", "Type", "Size", "Date"], axis = 1)
    return raw_data

# Call the transform() function and pass the merged DataFrame
clean_data = transform(merged_df)

# Create the avg_weekly_sales_per_month function that takes in the cleaned data from the last step
def avg_weekly_sales_per_month(clean_data):
    # Write your code here
    holidays_sales = clean_data[["Month", "Weekly_Sales"]]
    holidays_sales = (holidays_sales.groupby("Month").agg(Avg_Sales = ("Weekly_Sales", "mean")).reset_index().round(2))
    return holidays_sales

# Call the avg_weekly_sales_per_month() function and pass the cleaned DataFrame
agg_data = avg_weekly_sales_per_month(clean_data)

# Create the load() function that takes in the cleaned DataFrame and the aggregated one with the paths where they are going to be stored
def load(full_data, full_data_file_path, agg_data, agg_data_file_path):
    # Write your code here
    full_data.to_csv(full_data_file_path, index = False)
    agg_data.to_csv(agg_data_file_path, index = False)

# Call the load() function and pass the cleaned and aggregated DataFrames with their paths 
load(clean_data, "clean_data.csv", agg_data, "agg_data.csv")

# Create the validation() function with one parameter: file_path - to check whether the previous function was correctly executed
def validation(file_path):
    # Write your code here
    file_exists = os.path.exists(file_path)
    if not file_exists:
        raise Exception(f"There is no file at the path {file_path}")
    
    # Call the validation() function and pass first, the cleaned DataFrame path, and then the aggregated DataFrame path
validation("clean_data.csv")
validation("agg_data.csv")