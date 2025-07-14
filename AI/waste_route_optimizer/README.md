# Waste Route Optimizer for SDG 11 (Sustainable Cities)

## 🗺️ Project Overview
Optimizes waste collection routes by **grouping bins into geographic zones** using K-Means clustering, reducing truck travel distance and fuel consumption.

## 📦 Files
- `waste_route_optimizer.py`: Main script (clusters bins by proximity).
- `waste_bins.csv`: Input data (bin coordinates).
- `zones_assigned.csv`: Output with zone labels.
- `waste_zones.png`: Visualization of zones.

## 🛠️ How to Run
1. Install dependencies:
   ```bash
   pip install pandas scikit-learn matplotlib
