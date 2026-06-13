import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_advisory(context_dict):
    """
    Generate a safety advisory message based on context information.
    
    Args:
        context_dict (dict): Dictionary with 'station', 'risk_level', and 'area_info'
        
    Returns:
        str: Safety advisory message (2-3 sentences)
    """
    station = context_dict.get('station', 'Unknown')
    risk_level = context_dict.get('risk_level', 'Unknown')
    area_info = context_dict.get('area_info', '')
    
    # Create a prompt for the AI model
    prompt = f"""Based on the following information, write a short, friendly safety advisory message (2-3 sentences) for residents:

Location: {station}
Risk Level: {risk_level}
Area Context: {area_info}

The advisory should be appropriate for the risk level and consider the specific characteristics of the area. Be concise, clear, and actionable."""
    
    # Placeholder function for AI model integration
    # This can be replaced with actual API calls to IBM Granite, OpenAI, or other models
    advisory = _call_ai_model(prompt, risk_level, station, area_info)
    
    return advisory


def _call_ai_model(prompt, risk_level, station, area_info):
    """
    Placeholder function for AI model API call.
    Replace this with actual API integration (IBM Granite, OpenAI, etc.)
    
    Args:
        prompt (str): The full prompt to send to the AI
        risk_level (str): Risk level for fallback logic
        station (str): Station name for fallback logic
        area_info (str): Area information for fallback logic
        
    Returns:
        str: Generated advisory message
    """
    # TODO: Replace with actual AI API call
    # Example for IBM Granite:
    # from ibm_watsonx_ai.foundation_models import Model
    # model = Model(model_id="ibm/granite-...", ...)
    # response = model.generate_text(prompt=prompt, ...)
    # return response
    
    # Example for OpenAI:
    # import openai
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # return response.choices[0].message.content
    
    # Fallback: Rule-based advisory generation
    return _generate_fallback_advisory(risk_level, station, area_info)


def _generate_fallback_advisory(risk_level, station, area_info):
    """
    Generate a rule-based advisory when AI model is not available.
    
    Args:
        risk_level (str): Risk level (Low, Moderate, High, Severe)
        station (str): Station name
        area_info (str): Area information
        
    Returns:
        str: Generated advisory message
    """
    # Extract key characteristics from area_info
    is_coastal = 'coastal' in area_info.lower() or 'harbor' in area_info.lower()
    is_low_lying = 'low-lying' in area_info.lower()
    has_wetlands = 'wetland' in area_info.lower()
    near_river = 'river' in area_info.lower()
    is_it_corridor = 'IT corridor' in area_info.lower()
    
    if risk_level == "Low":
        advisory = f"Weather conditions in {station} are currently stable with minimal flood risk. "
        advisory += "Continue normal activities, but stay informed about weather updates. "
        advisory += "Keep emergency contacts handy as a precaution."
        
    elif risk_level == "Moderate":
        advisory = f"Moderate rainfall is expected in {station}. "
        if is_low_lying or has_wetlands:
            advisory += "Low-lying areas may experience waterlogging, so avoid unnecessary travel through these zones. "
        elif is_coastal:
            advisory += "Coastal areas should monitor tide levels and avoid beach areas during high tide. "
        elif near_river:
            advisory += "Stay away from river banks and monitor water levels. "
        else:
            advisory += "Main roads may experience temporary waterlogging. "
        advisory += "Keep emergency supplies ready and stay updated with local weather alerts."
        
    elif risk_level == "High":
        advisory = f"High rainfall alert for {station}! "
        if is_low_lying or has_wetlands:
            advisory += "Severe flooding is likely in low-lying areas. Avoid all non-essential travel and move to higher ground if needed. "
        elif is_coastal:
            advisory += "Coastal flooding is possible with heavy rains and high tides. Stay away from waterfront areas and secure your property. "
        elif near_river:
            advisory += "River overflow is possible. Evacuate low-lying areas near the river basin immediately. "
        elif is_it_corridor:
            advisory += "Major waterlogging expected in IT corridor areas. Work from home if possible and avoid commuting. "
        else:
            advisory += "Significant flooding expected. Avoid travel and stay indoors. "
        advisory += "Keep emergency kit ready and follow official evacuation orders if issued."
        
    else:  # Severe
        advisory = f"SEVERE FLOOD WARNING for {station}! "
        if is_low_lying or has_wetlands:
            advisory += "Extreme flooding imminent in low-lying areas. Evacuate immediately to higher ground and follow emergency services guidance. "
        elif is_coastal:
            advisory += "Dangerous coastal flooding expected. Evacuate waterfront areas immediately and move inland to safety. "
        elif near_river:
            advisory += "Critical river overflow expected. Mandatory evacuation of all riverside areas. Move to designated emergency shelters. "
        else:
            advisory += "Life-threatening flood conditions. Evacuate to higher ground immediately. "
        advisory += "Do not attempt to travel. Contact emergency services if you need assistance."
    
    return advisory


# Test section
if __name__ == "__main__":
    # Import functions from previous agents
    from agent1_risk import get_rainfall_info
    from agent2_context import get_location_context
    
    print("=== Agent 3: Advisory Generation Test ===\n")
    
    # Test 1: High risk scenario
    print("Test 1: High Risk Scenario (Sholinganallur, 1993-05-16)")
    print("-" * 60)
    station = "Sholinganallur"
    date = "1993-05-16"
    
    rainfall_info = get_rainfall_info(station, date)
    if rainfall_info:
        context = get_location_context(station, rainfall_info['risk_level'])
        if context:
            print(f"Station: {station}")
            print(f"Date: {date}")
            print(f"Rainfall: {rainfall_info['rainfall_mm']} mm")
            print(f"Risk Level: {rainfall_info['risk_level']}")
            print(f"\nArea Info: {context['area_info']}")
            print(f"\nSafety Advisory:")
            print(generate_advisory(context))
    
    # Test 2: Moderate risk scenario
    print("\n\nTest 2: Moderate Risk Scenario (Chennai port trust, 1993-03-03)")
    print("-" * 60)
    station = "Chennai port trust"
    date = "1993-03-03"
    
    rainfall_info = get_rainfall_info(station, date)
    if rainfall_info:
        context = get_location_context(station, rainfall_info['risk_level'])
        if context:
            print(f"Station: {station}")
            print(f"Date: {date}")
            print(f"Rainfall: {rainfall_info['rainfall_mm']} mm")
            print(f"Risk Level: {rainfall_info['risk_level']}")
            print(f"\nArea Info: {context['area_info']}")
            print(f"\nSafety Advisory:")
            print(generate_advisory(context))
    
    # Test 4: Manual context dictionary - Severe risk
    print("\n\nTest 4: Manual Context Dictionary - Severe Risk")
    print("-" * 60)
    severe_context = {
        'station': 'Sholinganallur',
        'risk_level': 'Severe',
        'area_info': 'Sholinganallur: low-lying IT corridor area near wetlands, known for severe flooding during heavy monsoon, especially in 2015.'
    }
    print(f"Station: {severe_context['station']}")
    print(f"Risk Level: {severe_context['risk_level']}")
    print(f"Area Info: {severe_context['area_info']}")
    print(f"\nSafety Advisory:")
    print(generate_advisory(severe_context))
    
    # Test 5: Manual context dictionary - Low risk
    print("\n\nTest 5: Manual Context Dictionary - Low Risk")
    print("-" * 60)
    low_context = {
        'station': 'Sholinganallur',
        'risk_level': 'Low',
        'area_info': 'Sholinganallur: low-lying IT corridor area near wetlands, known for severe flooding during heavy monsoon, especially in 2015.'
    }
    print(f"Station: {low_context['station']}")
    print(f"Risk Level: {low_context['risk_level']}")
    print(f"Area Info: {low_context['area_info']}")
    print(f"\nSafety Advisory:")
    print(generate_advisory(low_context))
    
    print("\n" + "=" * 60)
    print("Note: Compare the tone difference between Severe and Low risk advisories!")
    
    # Test 3: Low risk scenario
    print("\n\nTest 3: Low Risk Scenario (Chennai nungambakkam, 1993-03-03)")
    print("-" * 60)
    station = "Chennai nungambakkam"
    date = "1993-03-03"
    
    rainfall_info = get_rainfall_info(station, date)
    if rainfall_info:
        context = get_location_context(station, rainfall_info['risk_level'])
        if context:
            print(f"Station: {station}")
            print(f"Date: {date}")
            print(f"Rainfall: {rainfall_info['rainfall_mm']} mm")
            print(f"Risk Level: {rainfall_info['risk_level']}")
            print(f"\nArea Info: {context['area_info']}")
            print(f"\nSafety Advisory:")
            print(generate_advisory(context))

# Made with Bob
