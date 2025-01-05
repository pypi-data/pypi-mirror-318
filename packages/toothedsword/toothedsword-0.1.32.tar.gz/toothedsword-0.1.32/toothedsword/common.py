
import sys
import os
import re
import glob
import json


def local_xyz2lonlat(xj, yj, zj, lon0, lat0, alt0=0):

    x0, y0, z0 = llr2xyz(0, 0, R=6371)
    x = zj+x0+alt0
    y = xj
    z = yj

    x, y, z = Rotate(2, 0-lat0, x, y, z)
    x, y, z = Rotate(3, lon0, x, y, z)
    alt = np.sqrt(x**2+y**2+z**2) - 6371

    lon = np.arctan2(y,x)
    lat = np.arctan2(z,np.sqrt(x**2 + y**2))
    lon = lon / np.pi * 180
    lat = lat / np.pi * 180
    return lon, lat, alt


def get_range_id(lon, lat, z, i, j, k, xlim, ylim, zlim):
    id =\
         (lon.flatten()[i] >= xlim[0]) &\
         (lon.flatten()[j] >= xlim[0]) &\
         (lon.flatten()[k] >= xlim[0]) &\
         (lon.flatten()[i] <= xlim[1]) &\
         (lon.flatten()[j] <= xlim[1]) &\
         (lon.flatten()[k] <= xlim[1]) &\
         (lat.flatten()[i] >= ylim[0]) &\
         (lat.flatten()[j] >= ylim[0]) &\
         (lat.flatten()[k] >= ylim[0]) &\
         (lat.flatten()[i] <= ylim[1]) &\
         (lat.flatten()[j] <= ylim[1]) &\
         (lat.flatten()[k] <= ylim[1]) &\
         (z.flatten()[i] >= zlim[0]) &\
         (z.flatten()[j] >= zlim[0]) &\
         (z.flatten()[k] >= zlim[0]) &\
         (z.flatten()[i] <= zlim[1]) &\
         (z.flatten()[j] <= zlim[1]) &\
         (z.flatten()[k] <= zlim[1])
    return id


def triangle_area_3d(x1, x2, x3, y1, y2, y3, z1, z2, z3):
    
    # 计算每个三角形的顶点坐标
    A = np.column_stack((x1, y1, z1))
    B = np.column_stack((x2, y2, z2))
    C = np.column_stack((x3, y3, z3))

    # 计算向量 AB 和 AC
    AB = B - A
    AC = C - A

    # 计算叉积
    cross_product = np.cross(AB, AC)

    # 计算每个三角形的面积
    areas = 0.5 * np.linalg.norm(cross_product, axis=1)
    return areas


def area_by_xyz(x1, y1, x2, y2, x3, y3):
    return 0.5 * np.abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

