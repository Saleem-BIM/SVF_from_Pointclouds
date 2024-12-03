from src.svf_calculator import calculate_svf
from src.visualization import visualize_svf

# File paths
point_cloud_file = "data/example.ply"
svf_file = "data/svf_values.npy"

# Parameters
radius = 5.0

# Step 1: Calculate SVF
calculate_svf(point_cloud_file, svf_file, radius=radius)

# Step 2: Visualize SVF
visualize_svf(point_cloud_file, svf_file)
