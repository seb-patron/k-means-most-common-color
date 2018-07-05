from utils import *
from utils import *
from PIL import *
import pandas as pd
import numpy as np
import webcolors
import csv
from urllib.request import urlopen
import io

if __name__ == '__main__':
    import sys
    import time
    sys.stderr.write("mindiff %s\n" % (1))
    start = time.time()
    # with open('./Data/raw/products-2017-08-24-3.csv')
    # df = pd.read_csv('./data/raw/products-2017-08-24-3.csv')
    # print (df.head)
    # for index, row in df.iterrows():
    #     # print (row['Product SKU'])
    #     try:
    #         img_url = row['Product Images'][18:].split('|')[0]
    #     except:
    #         print ('error getting product URL')

        # open up image from url and read it in
    try:
        # fd = urlopen('./almond-blossom')
        # print (fd)
        # image_file = io.BytesIO(fd.read())
        # im = Image.open(image_file)
        with open('almond-blossom.jpg', 'rb') as f:
            im = Image.open(io.BytesIO(f.read()))
    
        color = get_color(im)
        # row['GPS Color'] = color
        # df.set_value(index,'GPS Color',color)
        # df.loc[index, 'GPS Color']=color
        print (color)
        print ("Execution time", (time.time()-start)*1000)
    except:
        print ('exception called')
    #     color = 'na'
    #     df.set_value(index,'GPS Color',color)
        
    #     # print (img_url)
    #     if index % 100 == 0:
    #         df.to_csv('./data/interim/out.csv')
    # print (df.columns.values)

    # df.to_csv('./data/processed/out.csv')
# fname = "ultralight.jpg"
# print (get_color(fname))