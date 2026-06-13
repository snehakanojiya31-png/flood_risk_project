import csv
import os
from datetime import datetime

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CSV_FILE = os.path.join(SCRIPT_DIR, 'cleaned_rain_multistation_sample.csv')


def calculate_risk_level(rainfall_mm):
    """
    Calculate risk level based on rainfall amount.
    
    Rules:
    - Below 7.5mm = Low
    - 7.5 to 35.5mm = Moderate
    - 35.5 to 124.5mm = High
    - Above 124.5mm = Severe
    
    Args:
        rainfall_mm (float): Rainfall amount in millimeters
        
    Returns:
        str: Risk level (Low, Moderate, High, or Severe)
    """
    if rainfall_mm < 7.5:
        return "Low"
    elif rainfall_mm < 35.5:
        return "Moderate"
    elif rainfall_mm < 124.5:
        return "High"
    else:
        return "Severe"


def get_rainfall_info(station, date, csv_file=None):
    """
    Get rainfall amount and risk level for a specific station and date.
    
    Args:
        station (str): Station name (e.g., 'Chennai nungambakkam')
        date (str): Date in format 'YYYY-MM-DD' (e.g., '1993-03-03')
        csv_file (str): Path to the CSV file (default: uses script's directory)
        
    Returns:
        dict: Dictionary with rainfall_mm and risk_level, or None if not found
    """
    if csv_file is None:
        csv_file = DEFAULT_CSV_FILE
    
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['station'].strip().lower() == station.strip().lower() and row['date'] == date:
                    rainfall = float(row['rainfall_mm'])
                    risk = row['risk_level']
                    return {
                        'rainfall_mm': rainfall,
                        'risk_level': risk
                    }
        return None
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def print_rainfall_info(station, date, csv_file=None):
    """
    Print rainfall amount and risk level for a specific station and date.
    
    Args:
        station (str): Station name (e.g., 'Chennai nungambakkam')
        date (str): Date in format 'YYYY-MM-DD' (e.g., '1993-03-03')
        csv_file (str): Path to the CSV file (default: uses script's directory)
    """
    info = get_rainfall_info(station, date, csv_file)
    
    if info:
        print(f"Station: {station}")
        print(f"Date: {date}")
        print(f"Rainfall: {info['rainfall_mm']} mm")
        print(f"Risk Level: {info['risk_level']}")
    else:
        print(f"No data found for station '{station}' on date '{date}'")


# Example usage
if __name__ == "__main__":
    print("=== Test 1: Query Chennai port trust on 1993-03-03 ===")
    info = get_rainfall_info("Chennai port trust", "1993-03-03")
    if info:
        print(f"Rainfall: {info['rainfall_mm']} mm")
        print(f"Risk Level: {info['risk_level']}")
    else:
        print("No data found")
    
    print("\n=== Test 2: Calculate risk level for 50mm rainfall ===")
    risk_50 = calculate_risk_level(50)
    print(f"Rainfall: 50 mm -> Risk Level: {risk_50}")
    
    print("\n=== Test 3: Calculate risk level for 200mm rainfall ===")
    risk_200 = calculate_risk_level(200)
    print(f"Rainfall: 200 mm -> Risk Level: {risk_200}")

# Made with Bob
