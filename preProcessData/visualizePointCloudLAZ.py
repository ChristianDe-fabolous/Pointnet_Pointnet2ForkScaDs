
import csv
import os
import laspy as lp
import pandas as pd
import open3d as o3d
from plyfile import PlyData, PlyElement
import numpy as np
import shutil
import argparse

def normalize_coordinates(df, point_cloud):
    scale_x = point_cloud.header.scale[0]
    offset_x = point_cloud.header.offset[0]
    scale_y = point_cloud.header.scale[1]
    offset_y = point_cloud.header.offset[1]
    scale_z = point_cloud.header.scale[2]
    offset_z = point_cloud.header.offset[2]
    df['X'] = df['X'] * scale_x + offset_x
    df['Y'] = df['Y'] * scale_y + offset_y
    df['Z'] = df['Z'] * scale_z + offset_z
    return df
def normalize_colors(df):
    color_min = 255
    color_max = 65535
    df['red'] = (df['red'] - color_min) / (color_max - color_min)
    df['green'] = (df['green'] - color_min) / (color_max - color_min)
    df['blue'] = (df['blue'] - color_min) / (color_max - color_min)
    return df

def visualizePointCloudLAZ():
    filepath = '/home/christian/Desktop/rawDataScaDs/Nord/de-zent-230322_part_00_01/filtered_6342_113839.laz' 
    las_file = filepath
    point_cloud = lp.read(las_file)
    # Create a new dictionary to hold our data
    data = {}
    for dimension in point_cloud.point_format.dimensions:
        data[dimension.name] = getattr(point_cloud, dimension.name)
    print(data)
    print(len(data))
    # Convert dictionary to pandas DataFrame
    df = pd.DataFrame(data)
    df = normalize_coordinates(df, point_cloud)
    df = normalize_colors(df)

    # Load PointCloud into PCD
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(df[['X', 'Y', 'Z']].values)
    pcd.colors = o3d.utility.Vector3dVector(df[['red', 'green', 'blue']].values)
    # show entire point cloud
    o3d.visualization.draw_geometries([pcd])



if __name__ == '__main__':
    visualizePointCloudLAZ()