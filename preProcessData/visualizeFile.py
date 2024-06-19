import laspy as lp
import open3d as o3d
import pandas as pd



def visualizePlyFile(filepath):
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


    pcd = o3d.io.read_point_cloud(filepath)
    print(pcd)
    # show entire point cloud
    o3d.visualization.draw_geometries([pcd])




def visualizeLazFile(filepath):
    las = laspy.read(filepath)
    print(las)

def visualizeTxtFile(filepath):
    pass



def visualizeFile(filepath):
    if filepath.endswith('.txt'):
        visualizeTxtFile(filepath)
    elif filepath.endswith('.ply'):
        visualizePlyFile(filepath)
    elif filepath.endswith('.laz'):
        visualizeLazFile(filepath)


if __name__ == '__main__':
    visualizeFile('/home/christian/Desktop/rawDataScaDs/buildings_zentrum_nord/DESN_000ZXDB.ply')