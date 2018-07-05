from collections import namedtuple
from math import sqrt
import random
from PIL import Image
import webcolors
# try:
#     import Image
# except ImportError:
#     from PIL import Image

Point = namedtuple('Point', ('coords', 'n', 'ct'))
Cluster = namedtuple('Cluster', ('points', 'center', 'n'))

"""For each pixel in the image, return the RGB value a it"""
def get_points(img):
    points = []
    w, h = img.size
    # for each pixel in the image, get the color
    for count, color in img.getcolors(w * h):
        points.append(Point(color, 3, count))
    print (points[1000:1010])
    return points

rtoh = lambda rgb: '#%s' % ''.join(('%02x' % p for p in rgb))

"""Returns actual colors codes from image"""
def colorz(filename, n=3, mindiff=1):
    # img = Image.open(filename)
    img = filename

    # Reduce image size and crop into center
    # img.thumbnail((200, 200))
    # img = img.crop((50, 50, 100, 100))
    
    # img.save("./Data/proccessed/img2.jpg")
    w, h = img.size

    points = get_points(img)
    """Maps to colors to @n amount of clusters"""
    clusters = kmeans(points, n, mindiff)
    rgbs = [map(int, c.center.coords) for c in clusters]
    return map(rtoh, rgbs)

def euclidean(p1, p2):
    """Quickly and efficently calculates euclidean distance"""
    return sqrt(sum([
        (p1.coords[i] - p2.coords[i]) ** 2 for i in range(p1.n)
    ]))

def calculate_center(points, n):
    vals = [0.0 for i in range(n)]
    plen = 0
    for p in points:
        plen += p.ct
        for i in range(n):
            vals[i] += (p.coords[i] * p.ct)
    return Point([(v / plen) for v in vals], n, 1)

"""K-Means implementation

"""
def kmeans(points, k, min_diff):
    clusters = [Cluster([p], p, p.n) for p in random.sample(points, k)]

    while 1:
        plists = [[] for i in range(k)]

        for p in points:
            smallest_distance = float('Inf')
            for i in range(k):
                distance = euclidean(p, clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    idx = i
            plists[idx].append(p)

        diff = 0
        for i in range(k):
            old = clusters[i]
            center = calculate_center(plists[i], old.n)
            new = Cluster(plists[i], center, old.n)
            clusters[i] = new
            diff = max(diff, euclidean(old.center, new.center))

        if diff < min_diff:
            break

    return clusters


def closest_color(requested_color):
    """Finds closest Euclidean color name"""
    min_colors = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def get_color_name(requested_color):
    """"Returns color name for given color"""
    if isinstance(requested_color, str):
        color = hex_to_rgb(requested_color)
    else:
        color = requested_color
    try:
        closest_name = actual_name = webcolors.rgb_to_name(color)
    except ValueError:
        closest_name = closest_color(color)
        actual_name = None
    return actual_name, closest_name

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def get_color(file):
    """Takes in a image file, returns the name of item color """
    col = colorz(file,3,1)
    top_three_colors = []
    for a in col:
        color_hex = a
        actual_name, closest_name = get_color_name(color_hex)
        top_three_colors.append((closest_name, a))
        
    
    # actual_name, closest_name, hex_name = get_color_name(color_hex)
    return top_three_colors