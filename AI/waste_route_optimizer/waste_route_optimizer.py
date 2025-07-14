# waste_route_optimizer.py
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load bin locations (latitude/longitude)."""
    return pd.read_csv(file_path)

def cluster_zones(df, n_zones=4):
    """Group bins into zones based on proximity."""
    X = df[["Latitude", "Longitude"]]
    kmeans = KMeans(n_clusters=n_zones, random_state=42)
    df["Zone"] = kmeans.fit_predict(X)
    return df

def plot_zones(df):
    """Visualize zones on a map."""
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Longitude"], df["Latitude"], c=df["Zone"], cmap="tab10", alpha=0.7)
    plt.title("Waste Collection Zones (Proximity-Based)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.colorbar(label="Zone ID")
    plt.grid(True)
    plt.savefig("waste_zones.png")  # Save the plot
    plt.show()

if __name__ == "__main__":
    # Load data (columns: Bin_ID, Latitude, Longitude)
    df = load_data("waste_bins.csv")  
    
    # Cluster into zones
    df = cluster_zones(df)
    
    # Save results
    df.to_csv("zones_assigned.csv", index=False)
    print("Zones assigned and saved to 'zones_assigned.csv'.")
    
    # Generate zone map
    plot_zones(df)