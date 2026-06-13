import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_LOCATIONS_FILE = os.path.join(SCRIPT_DIR, 'locations_info.txt')


def get_location_context(station, risk_level, locations_file=None):
    """
    Get location context information for a station.
    
    Args:
        station (str): Station name (e.g., 'Sholinganallur')
        risk_level (str): Risk level (e.g., 'High', 'Low', 'Moderate', 'Severe')
        locations_file (str): Path to locations info file (default: uses script's directory)
        
    Returns:
        dict: Dictionary with station, risk_level, and area_info, or None if not found
    """
    if locations_file is None:
        locations_file = DEFAULT_LOCATIONS_FILE
    
    try:
        with open(locations_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    # Check if the line starts with the station name (case-insensitive)
                    if line.lower().startswith(station.lower() + ':'):
                        return {
                            'station': station,
                            'risk_level': risk_level,
                            'area_info': line
                        }
        return None
    except FileNotFoundError:
        print(f"Error: File '{locations_file}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


# Test section
if __name__ == "__main__":
    # Import functions from agent1_risk.py
    from agent1_risk import calculate_risk_level, get_rainfall_info
    
    print("=== Combined Context Test ===")
    print("Querying Sholinganallur on 1993-05-16 (High rainfall date)\n")
    
    # Get rainfall info from agent1
    station = "Sholinganallur"
    date = "1993-05-16"
    rainfall_info = get_rainfall_info(station, date)
    
    if rainfall_info:
        print(f"Station: {station}")
        print(f"Date: {date}")
        print(f"Rainfall: {rainfall_info['rainfall_mm']} mm")
        print(f"Risk Level: {rainfall_info['risk_level']}")
        
        # Get location context from agent2
        context = get_location_context(station, rainfall_info['risk_level'])
        
        if context:
            print(f"\nLocation Context:")
            print(f"  {context['area_info']}")
            
            print(f"\n=== Full Context Dictionary ===")
            print(context)
        else:
            print(f"\nNo location context found for {station}")
    else:
        print(f"No rainfall data found for {station} on {date}")
    
    print("\n=== Additional Test: Calculate risk for custom rainfall ===")
    custom_rainfall = 100.0
    custom_risk = calculate_risk_level(custom_rainfall)
    print(f"Custom rainfall: {custom_rainfall} mm -> Risk Level: {custom_risk}")
    
    custom_context = get_location_context(station, custom_risk)
    if custom_context:
        print(f"Context for {station} at {custom_risk} risk:")
        print(f"  {custom_context['area_info']}")

# Made with Bob
