# Flood Risk Advisory System

An AI-powered, multi-agent pipeline that predicts flood risk from historical rainfall data and generates clear, actionable safety advisories for residents of flood-prone Chennai localities.

Built as part of the **1M1B – IBM SkillsBuild AI + Sustainability Virtual Internship**, aligned with **SDG 11 (Sustainable Cities and Communities)** and **SDG 13 (Climate Action)**.

## How It Works

The system uses three AI agents orchestrated in sequence:

1. **Agent 1 – Risk Predictor** (`agent1_risk.py`)
   Reads rainfall data for a given station and date from `cleaned_rain_multistation_sample.csv` and classifies flood risk based on rainfall thresholds:
   - Below 7.5mm → Low
   - 7.5–35.5mm → Moderate
   - 35.5–124.5mm → High
   - Above 124.5mm → Severe

2. **Agent 2 – Context Helper** (`agent2_context.py`)
   Looks up the station's area description from `locations_info.txt` (terrain, drainage, flood history) and combines it with the risk level into a summary.

3. **Agent 3 – Action Advisor** (`agent3_advisor.py`)
   Uses an LLM (IBM Granite) to turn the summary into a friendly, tone-appropriate safety message — calm for Low risk, urgent for Severe risk.

The **orchestrator** (`main.py`) runs all three agents for a chosen station and date, and prints the final advisory.

## Files

| File | Description |
|------|-------------|
| `agent1_risk.py` | Rainfall risk classification |
| `agent2_context.py` | Location context lookup |
| `agent3_advisor.py` | AI-generated safety advisory |
| `main.py` | Orchestrator connecting all agents |
| `cleaned_rain_multistation_sample.csv` | Sample multi-station rainfall data |
| `locations_info.txt` | Area descriptions per station |

## Example OutputStation: Sholinganallur

Rainfall: 46.1 mm | Risk Level: High

Area Info: Low-lying IT corridor area near wetlands, known for severe flooding during heavy monsoon.
Safety Advisory: High rainfall alert for Sholinganallur! Severe flooding is likely in

low-lying areas. Avoid all non-essential travel and move to higher ground if needed.

## Responsible AI

- **Fairness**: Same thresholds applied uniformly across all stations.
- **Transparency**: Risk levels use explainable, rule-based logic.
- **Ethics**: Advisories direct users to official emergency services, not replace them.
- **Privacy**: Uses only public rainfall and geographic data — no personal information.

## Author

Sneha Kanojiya — Thakur College of Engineering and Technology
