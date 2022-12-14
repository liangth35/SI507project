from flask import Flask, render_template, request
import time
import requests
import pandas as pd
import datetime
import json
class Node:
    def __init__(self, datatuple=None):
        if datatuple is not None:
            self.id = datatuple[0]
            self.name = datatuple[1][0]
            self.date = pd.to_datetime(datatuple[1][1])
            if self.date is None:
                self.date = pd.to_datetime('2077-01-01')
            self.oriPrice = datatuple[1][2]
            self.discPrice = datatuple[1][3]
            self.rating = datatuple[1][4]
            if self.rating is None:
                self.rating = 0
            self.reviews = datatuple[1][5]
            self.link = datatuple[1][6]
            self.desc = datatuple[1][7]
            self.indices = [self.discPrice, self.date, self.rating]
        self.left = None
        self.right = None

    def disp(self):
        print(self.id,self.name,self.date,self.oriPrice,self.discPrice,self.rating,self.reviews,self.link,self.desc)
    
    def dispTree(self):
        if self.left:
            self.left.dispTree()
        self.disp()
        if self.right:
            self.right.dispTree()
    
def constructTree(nodeList, depth=0):
    try:
        axis = depth % len(nodeList[0].indices)
    except: #list empty
        return None
    nodeList.sort(key = lambda x: x.indices[axis])
    median = len(nodeList)//2
    medianNode = nodeList[median]
    medianNode.left = constructTree(nodeList[:median], depth+1)
    medianNode.right = constructTree(nodeList[median+1:], depth+1)
    return medianNode

def rangesearch(tree, bounds=[[0,999], [pd.to_datetime('1970-01-01'), pd.to_datetime('2023-01-01')], [0,100]], depth=0):
    res = []
    try:
        axis = depth % len(tree.indices)
    except: #tree empty
        return res
    if tree.indices[0]>=bounds[0][0] and tree.indices[0]<=bounds[0][1] \
    and tree.indices[1]>=bounds[1][0] and tree.indices[1]<=bounds[1][1]\
    and tree.indices[2]>=bounds[2][0] and tree.indices[2]<=bounds[2][1]:
        res.append(tree)
        # res[0].desc=[lowerBound[axis],upperBound[axis]]
        if tree.left is None and tree.right is None:
            return res
    if tree.indices[axis]<bounds[axis][1]:
        res += rangesearch(tree.right, bounds, depth+1)
    if tree.indices[axis]>bounds[axis][0]:
        res += rangesearch(tree.left, bounds, depth+1)
    return res




app = Flask(__name__)

sorttype,priceLower,priceUpper,dateLower,dateUpper,ratingLower,ratingUpper = None,None,None,None,None,None,None
discount=""
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["GET","POST"])
def result():
    sorttype = request.form["sort"]
    priceLower = request.form["priceLower"]
    priceUpper = request.form["priceUpper"]
    dateLower = request.form["dateLower"]
    dateUpper = request.form["dateUpper"]
    ratingLower = request.form["ratingLower"]
    ratingUpper = request.form["ratingUpper"]
    try:
        discount = request.form["discount"]
    except:
        discount=""
    reslist=rangesearch(tree, [[float(priceLower),float(priceUpper)], [pd.to_datetime(dateLower), pd.to_datetime(dateUpper)],[int(ratingLower),int(ratingUpper)]])
    return render_template('result.html',priceLower=priceLower,priceUpper=priceUpper,\
        dateLower=dateLower,dateUpper=dateUpper,ratingLower=ratingLower,ratingUpper=ratingUpper,sorttype=sorttype,discount=discount)

if __name__ == '__main__':  
    gameFile = open('gameData.json','r')
    gameData = json.load(gameFile)
    gameFile.close()

    nodeList = []
    for a in gameData.items():
        nodeList.append(Node(a))
    tree = constructTree(nodeList)
    
    print('starting Flask app', app.name)
    app.run(host= '127.0.0.1', port=5001, debug=True)
    