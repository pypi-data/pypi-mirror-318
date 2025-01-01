import pandas as pd
import numpy as np

def analyze_categorical_columns(csv_file_path, max_unique_values=50, unique_ratio_threshold=0.1, cardinality_threshold=10):
    df = pd.read_csv(csv_file_path)
    categorical_analysis = {}
    for column in df.columns:
        if df[column].dtype not in ['object', 'category']:
            continue
        unique_values = df[column].nunique()
        unique_ratio = unique_values / len(df)
        unique_list = df[column].dropna().unique().tolist()
        is_categorical = (unique_values <= max_unique_values) or (unique_ratio <= unique_ratio_threshold)
        if is_categorical:
            ordinal_keywords = ['low', 'medium', 'high', 'first', 'second', 'third', 'level']
            is_ordinal = any(
                keyword in str(value).lower()
                for value in unique_list
                for keyword in ordinal_keywords
            )
            encoding_suggestion = None
            if is_ordinal:
                encoding_suggestion = "Ordinal Encoding"
            elif unique_values <= cardinality_threshold:
                encoding_suggestion = "One-Hot Encoding"
            else:
                encoding_suggestion = "Frequency/Target/Hashing Encoding"
            additional_notes = []
            if df[column].isnull().sum() > 0:
                additional_notes.append("Contains missing values")
            if unique_values == df.shape[0]:
                additional_notes.append("Unique values equal to number of rows")
            categorical_analysis[column] = {
                'is_categorical': True,
                'unique_values': unique_values,
                'unique_values_list': unique_list,
                'is_ordinal': is_ordinal,
                'encoding_suggestion': encoding_suggestion,
                'additional_notes': additional_notes
            }
    return categorical_analysis

def print_categorical_analysis(analysis):
    if not analysis:
        print("No categorical columns found.")
        return
    print("-" * 50)
    print("Categorical Columns Analysis:")

    for column, details in analysis.items():
        print(f"\nColumn: {column}")
        print(f"Unique Values: {details['unique_values']}")
        print(f"Encoding Suggestion: {details['encoding_suggestion']}")

        print("\nUnique Values:")
        for value in details['unique_values_list'][:10]:
            print(f"  - {value}")
        if len(details['unique_values_list']) > 10:
            print(f"  ... and {len(details['unique_values_list']) - 10} more")

        if details['additional_notes']:
            print("\nAdditional Notes:")
            for note in details['additional_notes']:
                print(f"  - {note}")


def cat_bool(path):
    categorical_analysis = analyze_categorical_columns(path)
    df = pd.read_csv(path)
    print("-" * 50)
    for column in df.columns:
      is_categorical = column in categorical_analysis
      print(f"Column '{column}' is categorical: {is_categorical}")
    print_categorical_analysis(categorical_analysis)
    
