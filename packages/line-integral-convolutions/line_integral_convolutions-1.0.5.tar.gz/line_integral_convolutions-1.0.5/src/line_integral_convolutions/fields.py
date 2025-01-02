## This file is part of the "line-integral-convolutions" project.
## Copyright (c) 2024 Neco Kriel.
## Licensed under the MIT License. See LICENSE for details.


## ###############################################################
## IMPORT MODULES
## ###############################################################
import numpy as np


## ###############################################################
## EXAMPLE VECTOR FIELDS
## ###############################################################
def vfield_lotka_volterra(size: int):
    bounds_rows = (-5, 10)
    bounds_cols = (-5, 10)
    coords_row = np.linspace(bounds_rows[0], bounds_rows[1], size)
    coords_col = np.linspace(bounds_cols[0], bounds_cols[1], size)
    mg_x, mg_y = np.meshgrid(coords_col, coords_row, indexing="xy")
    x_capacity = 8
    y_growth = 3
    y_decay = 2
    vcomp_rows = mg_x * (1 - mg_x / x_capacity) - mg_y * mg_x / (1 + mg_x)
    vcomp_cols = y_growth * mg_y * mg_x / (1 + mg_x) - y_decay * mg_y
    vfield = np.array([vcomp_rows, vcomp_cols])
    return {
        "name": "lotka_volterra",
        "vfield": vfield,
        "streamlength": size // 4,
        "num_rows": size,
        "num_cols": size,
        "bounds_rows": bounds_rows,
        "bounds_cols": bounds_cols,
    }


def vfield_flowers(size: int):
    bounds_rows = (-10, 10)
    bounds_cols = (-10, 10)
    coords_row = np.linspace(bounds_rows[0], bounds_rows[1], size)
    coords_col = np.linspace(bounds_cols[0], bounds_cols[1], size)
    mg_x, mg_y = np.meshgrid(coords_col, coords_row, indexing="xy")
    vcomp_rows = np.cos(mg_x / 2)
    vcomp_cols = np.cos(mg_y / 2)
    vfield = np.array([vcomp_rows, vcomp_cols])
    return {
        "name": "flowers",
        "vfield": vfield,
        "streamlength": size // 4,
        "num_rows": size,
        "num_cols": size,
        "bounds_rows": bounds_rows,
        "bounds_cols": bounds_cols,
    }


def vfield_circles(size: int):
    bounds_rows = (-10, 10)
    bounds_cols = (-10, 10)
    coords_row = np.linspace(bounds_rows[0], bounds_rows[1], size)
    coords_col = np.linspace(bounds_cols[0], bounds_cols[1], size)
    mg_x, mg_y = np.meshgrid(coords_col, coords_row, indexing="xy")
    vcomp_rows = np.cos(mg_y / 2)
    vcomp_cols = np.cos(mg_x / 2)
    vfield = np.array([vcomp_rows, vcomp_cols])
    return {
        "name": "circles",
        "vfield": vfield,
        "streamlength": size // 4,
        "num_rows": size,
        "num_cols": size,
        "bounds_rows": bounds_rows,
        "bounds_cols": bounds_cols,
    }


def vfield_swirls(size: int):
    bounds_rows = (-10, 10)
    bounds_cols = (-10, 10)
    coords_row = np.linspace(bounds_rows[0], bounds_rows[1], size)
    coords_col = np.linspace(bounds_cols[0], bounds_cols[1], size)
    mg_x, mg_y = np.meshgrid(coords_col, coords_row, indexing="xy")
    vcomp_rows = np.sin((mg_y + mg_x) / 3)
    vcomp_cols = np.cos((mg_x - mg_y) / 3)
    vfield = np.array([vcomp_rows, vcomp_cols])
    return {
        "name": "swirls",
        "vfield": vfield,
        "streamlength": size // 3,
        "num_rows": size,
        "num_cols": size,
        "bounds_rows": bounds_rows,
        "bounds_cols": bounds_cols,
    }


## END OF EXAMPLE VECTOR FIELDS
