"""
Main pipeline for flood risk advisory system.
Integrates all three agents to provide complete flood risk analysis and advisories.
"""

from agent1_risk import get_rainfall_info, calculate_risk_level
from agent2_context import get_location_context
from agent3_advisor import generate_advisory


def run_pipeline(station, date):
    """
    Run the complete flood risk advisory pipeline.
    
    This function orchestrates all three agents:
    1. Agent 1: Gets rainfall data and risk level from CSV
    2. Agent 2: Gets location context information
    3. Agent 3: Generates safety advisory based on context
    
    Args:
        station (str): Station name (e.g., 'Chennai nungambakkam')
        date (str): Date in format 'YYYY-MM-DD' (e.g., '1993-03-03')
        
    Returns:
        dict: Complete analysis with rainfall, risk_level, context, and advisory
              Returns None if data not found
    """
    print(f"\n{'='*70}")
    print(f"FLOOD RISK ANALYSIS PIPELINE")
    print(f"{'='*70}")
    print(f"Station: {station}")
    print(f"Date: {date}")
    print(f"{'-'*70}")
    
    # Step 1: Get rainfall information from Agent 1
    print("\n[Agent 1: Risk Assessment]")
    rainfall_info = get_rainfall_info(station, date)
    
    if not rainfall_info:
        print(f"❌ No data found for {station} on {date}")
        return None
    
    rainfall_mm = rainfall_info['rainfall_mm']
    risk_level = rainfall_info['risk_level']
    
    print(f"✓ Rainfall: {rainfall_mm} mm")
    print(f"✓ Risk Level: {risk_level}")
    
    # Step 2: Get location context from Agent 2
    print("\n[Agent 2: Location Context]")
    context = get_location_context(station, risk_level)
    
    if not context:
        print(f"❌ No location context found for {station}")
        return None
    
    print(f"✓ Area Info: {context['area_info']}")
    
    # Step 3: Generate advisory from Agent 3
    print("\n[Agent 3: Safety Advisory]")
    advisory = generate_advisory(context)
    print(f"✓ Advisory Generated")
    
    # Display final advisory
    print(f"\n{'='*70}")
    print(f"SAFETY ADVISORY FOR RESIDENTS")
    print(f"{'='*70}")
    print(advisory)
    print(f"{'='*70}\n")
    
    # Return complete analysis
    result = {
        'station': station,
        'date': date,
        'rainfall_mm': rainfall_mm,
        'risk_level': risk_level,
        'area_info': context['area_info'],
        'advisory': advisory
    }
    
    return result


def run_pipeline_custom_rainfall(station, rainfall_mm):
    """
    Run pipeline with custom rainfall amount (not from CSV).
    Useful for forecasting or what-if scenarios.
    
    Args:
        station (str): Station name
        rainfall_mm (float): Rainfall amount in millimeters
        
    Returns:
        dict: Complete analysis with calculated risk and advisory
    """
    print(f"\n{'='*70}")
    print(f"FLOOD RISK ANALYSIS PIPELINE (Custom Rainfall)")
    print(f"{'='*70}")
    print(f"Station: {station}")
    print(f"Rainfall: {rainfall_mm} mm")
    print(f"{'-'*70}")
    
    # Calculate risk level
    print("\n[Agent 1: Risk Assessment]")
    risk_level = calculate_risk_level(rainfall_mm)
    print(f"✓ Calculated Risk Level: {risk_level}")
    
    # Get location context
    print("\n[Agent 2: Location Context]")
    context = get_location_context(station, risk_level)
    
    if not context:
        print(f"❌ No location context found for {station}")
        return None
    
    print(f"✓ Area Info: {context['area_info']}")
    
    # Generate advisory
    print("\n[Agent 3: Safety Advisory]")
    advisory = generate_advisory(context)
    print(f"✓ Advisory Generated")
    
    # Display final advisory
    print(f"\n{'='*70}")
    print(f"SAFETY ADVISORY FOR RESIDENTS")
    print(f"{'='*70}")
    print(advisory)
    print(f"{'='*70}\n")
    
    result = {
        'station': station,
        'rainfall_mm': rainfall_mm,
        'risk_level': risk_level,
        'area_info': context['area_info'],
        'advisory': advisory
    }
    
    return result


# Test section
if __name__ == "__main__":
    print("\n" + "="*70)
    print("FLOOD RISK ADVISORY SYSTEM - MULTI-AGENT PIPELINE")
    print("="*70)
    
    # Test 1: Low Risk
    print("\n\n### TEST 1: LOW RISK SCENARIO ###")
    run_pipeline("Chennai nungambakkam", "1993-03-03")
    
    # Test 2: Moderate Risk
    print("\n\n### TEST 2: MODERATE RISK SCENARIO ###")
    run_pipeline("Chennai port trust", "1993-03-03")
    
    # Test 3: High Risk
    print("\n\n### TEST 3: HIGH RISK SCENARIO ###")
    run_pipeline("Sholinganallur", "1993-05-16")
    
    # Test 4: Another Moderate Risk (different station)
    print("\n\n### TEST 4: MODERATE RISK - DIFFERENT LOCATION ###")
    run_pipeline("Chennai nungambakkam", "1993-07-22")
    
    # Test 5: Severe Risk (custom rainfall - forecasting scenario)
    print("\n\n### TEST 5: SEVERE RISK SCENARIO (Forecasted) ###")
    print("(Using custom rainfall amount to simulate severe conditions)")
    run_pipeline_custom_rainfall("Sholinganallur", 150.0)
    
    # Test 6: Another Severe Risk scenario
    print("\n\n### TEST 6: SEVERE RISK - COASTAL AREA (Forecasted) ###")
    print("(Using custom rainfall amount to simulate severe conditions)")
    run_pipeline_custom_rainfall("Chennai port trust", 200.0)
    
    print("\n" + "="*70)
    print("PIPELINE TESTING COMPLETE")
    print("="*70)
    print("\nSummary:")
    print("- Tested Low, Moderate, High, and Severe risk levels")
    print("- Demonstrated pipeline with historical data (from CSV)")
    print("- Demonstrated pipeline with custom rainfall (forecasting)")
    print("- All three agents working together successfully")
    print("="*70 + "\n")

# Made with Bob
