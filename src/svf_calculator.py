import numpy as np
from scipy.spatial import KDTree
import open3d as o3d

def calculate_svf(point_cloud_file, output_file, radius=5.0):
    """
    Calculate Sky View Factor (SVF) for a point cloud and save results.

    Parameters:
        point_cloud_file (str): Path to the input point cloud file (.ply).
        output_file (str): Path to save the SVF values (.npy).
        radius (float): Radius for neighbor search in SVF calculation.
    """
    # Load the point cloud
    print(f"Loading point cloud from {point_cloud_file}...")
    pcd = o3d.io.read_point_cloud(point_cloud_file)
    points = np.asarray(pcd.points)

    # Build KD-tree
    print("Building KD-tree...")
    tree = KDTree(points)

    # Calculate SVF for each point
    print(f"Calculating SVF for {len(points)} points...")
    svf_values = []
    for point in points:
        # Find neighbors within the radius
        indices = tree.query_ball_point(point, radius)
        neighbors = points[indices]

        # Calculate angles to neighbors
        angles = [np.arctan2((neighbor - point)[2], np.linalg.norm((neighbor - point)[:2])) for neighbor in neighbors]

        # Calculate SVF (proportion of visible sky)
        svf = 1 - (max(angles) - min(angles)) / (2 * np.pi)
        svf_values.append(svf)

    # Save SVF values
    svf_values = np.array(svf_values)
    np.save(output_file, svf_values)
    print(f"SVF values saved to {output_file}.")
