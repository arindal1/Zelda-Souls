from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    """
    Import a CSV layout as a 2D list.

    Args:
        path (str): Path to the CSV file.

    Returns:
        list: 2D list representing the CSV layout.
    """
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
    return terrain_map

def import_folder(path):
    """
    Import images from a folder.

    Args:
        path (str): Path to the folder containing images.

    Returns:
        list: List of pygame surfaces.
    """
    surface_list = []

    # Walk through the directory and get the list of image files
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            # Load the image and convert it to alpha format
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list

