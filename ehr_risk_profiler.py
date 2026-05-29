import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
patient_data_path = os.path.join(
    script_dir, 'datasets', 'healthcare_dataset.csv')

try:
    df = pd.read_csv(patient_data_path)
    print("EHR Patient ecords loaded successfully!")
except FileNotFoundError:
    print(f"Error: Could not locate the patient file at: {patient_data_path}")
    exit()

print("\nAvailable Database Columns:")
print(list(df.columns))

# RULE: Patient must be over 60 years old AND have an 'Abnormal' or 'Inconclusive' Test Result
age_condition = df['Age'] > 60
test_condition = df['Test Results'].isin(['Abnormal', 'Inconclusive'])

high_risk_patients = df[age_condition & test_condition]

# Calculate Hospital System Metrics
total_patients = len(df)
flagged_pattients = len(high_risk_patients)
risk_percentage = (flagged_pattients / total_patients) * 100

print(f"\nHospital System isk Audit Summary ---")
print(f"Total Patient Records Screened: {total_patients}")
print(f"High-Risk patients Flagged: {flagged_pattients}")
print(f"System-Wide Risk Prevalence: {risk_percentage:.2f}%")

output_excel_path = os.path.join(
    script_dir, 'high_risk_clinical_priority_list.xlsx')
high_risk_patients.to_excel(output_excel_path, index=False)
