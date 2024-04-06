import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the file name of the Excel workbook
file_name = r"E:\Work\Data science NEL project\NEL Test Results.xlsx"

# Read the Excel file into a pandas DataFrame, selecting only the columns you need
try:
    df = pd.read_excel(file_name, header=None, usecols="A:I")  # Assuming columns A to F have the data
    print("Excel file loaded successfully!")
except FileNotFoundError:
    print(f"Error: {file_name} not found.")

# Name the headers after the specified names
if 'df' in locals():
    column_names = ["Test Type", "Meter", "Diameters", "Nominal Velocity","crap", "%Error", "Crap2", "Table", "Date of Test"]
    df.columns = column_names
    df = df.drop([0, 1])  # Remove the first two rows which are now used as headers

    # Convert columns to appropriate data types if needed
    df['Nominal Velocity'] = pd.to_numeric(df['Nominal Velocity'], errors='coerce')
    df['%Error'] = pd.to_numeric(df['%Error'], errors='coerce')

    # Take the absolute value of the %Error column
    df['%Error'] = df['%Error'].abs()

    # Create a large plot with all subplots shown
    num_diameters = len(df['Diameters'].unique())
    num_test_types = len(df['Test Type'].unique())

    # Set consistent colors for specific meters
    meter_colors = {'ABB': 'red', 'Eight Path Nivus': 'green', 'Four Path Nivus': 'blue'}

    fig, axes = plt.subplots(num_diameters, num_test_types, figsize=(15, 15))

    for i, diameter in enumerate(df['Diameters'].unique()):
        for j, test_type in enumerate(df['Test Type'].unique()):
            ax = axes[i, j]
            test_type_df = df[(df['Diameters'] == diameter) & (df['Test Type'] == test_type)]

            # Plot each meter separately with consistent colors
            for meter in test_type_df['Meter'].unique():
                meter_df = test_type_df[test_type_df['Meter'] == meter]
                color = meter_colors.get(meter, 'black')  # Get color for the meter
                ax.scatter(meter_df['Nominal Velocity'], meter_df['%Error'], label=f'Meter: {meter}', color=color)

            ax.set_title(f'Diameter: {diameter}, Test Type: {test_type}', fontsize=7)  # Set font size for title
            ax.set_xlabel('Nominal Velocity', fontsize=7)
            ax.set_ylabel('%Error', fontsize=7)
            ax.legend()

    plt.tight_layout()

    # Save the plot as a high-resolution PDF
    plt.savefig('output.pdf', dpi=300)

    plt.show()
