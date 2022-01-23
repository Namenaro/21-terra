import base64
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
import torchvision.datasets as datasets
from random import choice
import random

class HtmlLogger:
    def __init__(self, name):
        self.name = name
        self.html = ''

    def add_text(self, text):
        self.html += text + '<br>'

    def add_fig(self, fig):
        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
        self.html += '<img src=\'data:image/png;base64,{}\'>'.format(encoded) + '<br>'
        plt.close(fig)

    def close(self):
        filename = self.name + '.html'
        with open(filename, 'w') as f:
            f.write(self.html)


def get_coords_for_radius(centerx, centery, radius):
    #|x|+|y|=radius ->  |y|=radius-|x|
    # x>0  -> y1 = radius-|x|
    X=[]
    Y=[]
    if radius == 0:
        return [centerx], [centery]

    for modx in range(0,radius+1):
        mody = radius - modx
        # x>0
        if modx!=0 and mody!=0:
            X.append(modx+centerx)
            Y.append(mody+centery)

            X.append(-modx + centerx)
            Y.append(mody + centery)

            X.append(modx + centerx)
            Y.append(-mody + centery)

            X.append(-modx + centerx)
            Y.append(-mody + centery)

        if modx==0 and mody!=0:
            X.append(modx+centerx)
            Y.append(mody+centery)

            X.append(modx + centerx)
            Y.append(-mody + centery)

        if modx!=0 and mody==0:
            X.append(modx+centerx)
            Y.append(mody+centery)

            X.append(-modx + centerx)
            Y.append(mody + centery)


    return X,Y

def get_coords_less_or_eq_raduis(centerx, centery, radius):
    XB = []
    YB = []
    for r in range(0, radius+1):
        X, Y = get_coords_for_radius(centerx, centery, r)
        XB = XB + X
        YB = YB + Y
    return XB, YB

def sense(picture, point):
    xlen=28
    ylen=28
    if point.x >= 0 and point.y >= 0 and point.x < xlen and point.y < ylen:
        return picture[point.y, point.x]
    else:
        return 0

def get_train_mnist():
    mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)
    return mnist_trainset

def get_numbers_of_type(the_number):
    mnist_train = get_train_mnist()
    np_images = mnist_train.train_data.numpy()
    np_labels = mnist_train.train_labels.numpy()
    results = []
    for i in range(len(np_labels)):
        if np_labels[i] == the_number:
            results.append(np_images[i])
    return np.array(results)

def etalons_of1():
    np_images = get_numbers_of_type(the_number=1)
    indexes = [0,7,28,18,27,41,76,98]
    exemplars = list([np_images[ind] for ind in indexes])
    return exemplars

def etalons_of3():
    np_images = get_numbers_of_type(the_number=3)
    indexes = [34,32,25,67,68,35, 210, 314,420, 496,620,659,635,667,733,715]
    exemplars = list([np_images[ind] for ind in indexes])
    return exemplars

def etalons_of6():
    np_images = get_numbers_of_type(the_number=6)
    indexes = [220,221,222,235,330]
    exemplars = list([np_images[ind] for ind in indexes])
    return exemplars

def get_diverse_set_of_numbers(n):
    mnist_train = get_train_mnist()
    np_images = mnist_train.train_data.numpy()[0:n]
    np_labels = mnist_train.train_labels.numpy()[0:n]
    return np_images, np_labels


def select_random_pic(pics):
    return choice(pics)

def select_random_xoord_on_pic(pic):
    maxX = pic.shape[1]
    maxY = pic.shape[0]
    x = random.randint(0, maxX - 1)
    y = random.randint(0, maxY - 1)
    return x,y

def apply_binary_unit_to_pic(pic, unit):
    ymax = pic.shape[0]
    xmax = pic.shape[1]
    XYs = []

    for y in range(0, ymax):
        for x in range(0, xmax):
            matches = unit.apply(pic, x, y)
            if len(matches) > 0:
                XYs.append([x,y])
    return XYs

def plot_numbered_points_on_pic(pic, X,Y):
    fig, ax = plt.subplots()
    plt.imshow(pic, cmap='gray_r')

    for i in range(len(X)):
        strmarker = '$' + str(i) + '$'
        plt.scatter(X[i], Y[i], s=100, c='yellow', marker=strmarker, alpha=0.9)

    plt.plot(X,Y)
    return fig

def plot_graph(X, Y):
    fig, ax = plt.subplots()
    ax.plot(X,Y, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
    return fig

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self, other):
        if other.x == self.x and other.y==self.y:
            return True
        return False


class SimpleSensor:
    def __init__(self):
        self.pic = etalons_of3()[0]

    def reset_picture(self,picture):
        self.pic = picture

    def measure(self, point):
        if sense(self.pic, point)>5:
            return 1
        return 0

import matplotlib.pyplot as plt
import math



class CoordSelector:
    def __init__(self, image,keys=None):
        self.image = image
        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.resultx = []
        self.resulty = []
        self.keys = keys
        if keys is not None:
            self.XY_info_dicts = []


    def onclick(self, event):
        print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
              ('double' if event.dblclick else 'single', event.button,
               event.x, event.y, event.xdata, event.ydata))
        x = math.ceil(event.xdata)
        y = math.ceil(event.ydata)

        plt.scatter(x, y, s=100, c='red', marker='o', alpha=0.4)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


        self.resultx.append(x)
        self.resulty.append(y)
        if self.keys is not None:
            info_dict = {}
            for key in self.keys:
                info_dict[key] = input(key + "=")
            self.XY_info_dicts.append(info_dict)



    def create_device(self):
        plt.imshow(self.image, cmap='gray_r')
        plt.show()
        if self.keys is None:
            return self.resultx, self.resulty
        return self.resultx, self.resulty, self.XY_info_dicts

def select_on_pic(pic, keys=None):
    devcr = CoordSelector(pic, keys)
    return devcr.create_device()


def get_point_handly(pic):
    X,Y = select_on_pic(pic, keys=None)
    return Point(X[0],Y[0])


def plot_contexts(cs, pic):
    fig, ax = plt.subplots()
    plt.imshow(pic, cmap='gray_r')
    for c in cs:
        color=np.random.rand(3,)
        i=0
        for point in c.points:
            strmarker = '$' + str(i) + '$'
            plt.scatter(point.x, point.y, s=100, c=[color], marker=strmarker, alpha=0.9)
            i+=1
    return fig

def get_random_pic_of_type(type=None):
    if type == None:
        mnist_train = get_train_mnist()
        pics = mnist_train.train_data.numpy()
    else:
        pics = get_numbers_of_type(type)
    return choice(pics)

def get_random_point():
    x= random.randint(0, 27)
    y = random.randint(0, 27)
    return Point(x,y)