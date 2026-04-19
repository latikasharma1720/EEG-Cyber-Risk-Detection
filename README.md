EEG-Based Cyber Risk Detection

This project focuses on detecting human cybersecurity risk using EEG (electroencephalogram) signals. It analyzes cognitive responses to identify user susceptibility to phishing attacks and insider threat behavior.

The project combines neuroscience and cybersecurity to build a system that can classify user behavior as safe or high-risk based on brain signal patterns.

Objectives:

Process and analyze EEG data for cybersecurity use cases
Identify cognitive patterns linked to phishing susceptibility
Detect potential insider threat behavior
Build a machine learning model for risk classification

Pipeline:

EEG Data Preprocessing
Filtering
Artifact removal
Epoching
Feature Extraction
Time-domain and frequency-domain features

Model Development
Classification of safe vs high-risk behavior

Tech Stack:

Data Processing & ML:

Python
NumPy, Pandas
MNE (EEG processing)
Scikit-learn 

Cybersecurity & Threat Analysis:

MITRE ATT&CK Framework (behavior mapping)
Phishing Simulation / Attack Scenario Design
Insider Threat Modeling
Threat Behavior Analysis

Monitoring & Analysis (Planned):

Splunk / Wazuh (for log correlation with user behavior)
ELK Stack (for visualization and analysis)

Current Work:

Developing preprocessing scripts for EEG data
Cleaning and preparing signals for analysis
Setting up the data pipeline

Expected Outcomes:

Reliable classification of user behavior based on EEG signals
Early detection of phishing susceptibility
Identification of insider threat risk patterns
