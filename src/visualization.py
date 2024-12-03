import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def visualize_svf(point_cloud_file, svf_file):
    """
    Visualize the point cloud with SVF values.

    Parameters:
        point_cloud_file (str): Path to the input point cloud file (.ply).
        svf_file (str): Path to the SVF values file (.npy).
    """
    # Load the point cloud and SVF values
    print(f"Loading point cloud from {point_cloud_file}...")
    pcd = o3d.io.read_point_cloud(point_cloud_file)
    points = np.asarray(pcd.points)

    print(f"Loading SVF values from {svf_file}...")
    svf_values = np.load(svf_file)

    # Normalize SVF values for coloring
    svf_norm = (svf_values - np.min(svf_values)) / (np.max(svf_values) - np.min(svf_values))
    colors = np.c_[svf_norm, svf_norm, svf_norm]  # Grayscale colors
    pcd.colors = o3d.utility.Vector3dVector(colors)

    # Visualize
    print("Visualizing point cloud...")
    o3d.visualization.draw_geometries([pcd])

def plot_svf_2d(points, svf_values):
    """
    Plot a 2D scatter plot of SVF values.

    Parameters:
        points (numpy.ndarray): Nx3 array of point cloud coordinates.
        svf_values (numpy.ndarray): SVF values.
    """
    print("Creating 2D scatter plot...")
    plt.figure(figsize=(16, 10))
    scatter = plt.scatter(points[:, 0], points[:, 1], c=svf_values, cmap='viridis', s=1)
    plt.colorbar(scatter, label="SVF")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Sky View Factor (SVF) 2D Visualization")
    plt.show()
