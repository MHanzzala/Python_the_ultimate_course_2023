import cv2
import pandas as pd
import sys
import pytesseract
from pdf2image import convert_from_path
from pytesseract import Output
import PySimpleGUI as sg


pd.set_option('mode.chained_assignment', None)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
config = ('-l eng --oem 1 --psm 3 --psm 13')

img=None
df=None
cord={'CompanyName':[80,193,340,70],
      'product':[90,790,660,48],
      'amount':[1250,790,200,48],
      'price':[1480,790,140,48]
     }
dataDic = { "productNamePath":[],
            "productQuantityPath":[],
            "productIncomePath":[],
             "productName":[],
             "productQuantity":[],
             "productIncome":[]}
def convertPDF2Img():
    
    img = convert_from_path('D:\\My Files\\Courses\\Python\\67_OCR\\invoice1.pdf')
    img[0].save('D:\\My Files\\Courses\\Python\\67_OCR\\invoice1.jpg', 'JPEG')
    
def readInvoice():
    global img
    img = cv2.imread("D:\\My Files\\Courses\\Python\\67_OCR\\invoice1.jpg")
    
def extractProductInfo(info, numberOfFields, step, keyToStore):
    name=info
    x=cord[name][0]
    y=cord[name][1]
    w=cord[name][2]
    h=cord[name][3]
    for i in range (0,numberOfFields):  
        crop_img = img[y:y+h, x:x+w]
        y=y+step 
        path = "D:\\My Files\\Courses\\Python\\67_OCR\\"+str(info)+str(i)+".jpg"
        dataDic[keyToStore].append(path)
        cv2.imwrite(path, crop_img)
def OCR(path,key):
    for imgPath in dataDic[path]:
        img = cv2.imread(imgPath)
        
        if path=="productNamePath":
            config = ('-l eng --oem 1 --psm 3 ')
        else :
            config = ('-l eng --oem 1 --psm 3 --psm 6')
            img = cv2.GaussianBlur(img, (5, 5), 0)
        d = pytesseract.image_to_data(img, output_type=Output.DICT, config=config)
        #skip if page is empty or giving empty strings
        if not any(s.strip() for s in d['text']): continue


       # print(dataDic[key])
        d['text'] = [x for x in d['text'] if x]
        s=' '.join(d['text'])
        dataDic[key].append(s)
        print(dataDic[key])
        

    
def dbIntegrityCheck():
    l=[]
    for v in  dataDic.values():
        l.append(len(v))
    print("Integrity is:", all(x == l[0] for x in l))
    print(l)
def getDB(path):
    global df
    df = pd.read_csv(path)

def getDBitemIndex(entry):
 
    return df.index[df['Item']==entry].tolist()

def subtractQuantity(quantity, index):
    global df
    df["Quantity"][index]=int(df["Quantity"][index])- int(quantity)

def addProductIncome(income, index):
    global df
    df["Income"][index]=int(df["Income"][index])+ int(income)

def getQuantity(index):
    return dataDic["productQuantity"][index]

def getIncome(index):
    return dataDic["productIncome"][index]

def proccesDB():
    for i,item in enumerate(dataDic['productName']):
        index=getDBitemIndex(item)
        index=index[0]
        print(index)
        subtractQuantity(getQuantity(i),index)
        addProductIncome(getIncome(i),index)


def run():   
    convertPDF2Img()
    readInvoice()
    extractProductInfo("product", 17, 50, "productNamePath")
    extractProductInfo("amount", 17, 50, "productQuantityPath")
    extractProductInfo("price", 17, 50, "productIncomePath")
    OCR("productNamePath","productName")
    OCR("productQuantityPath","productQuantity")
    OCR("productIncomePath","productIncome")
     
    getDB("D:\\My Files\\Courses\\Python\\67_OCR\\FinancialSheet.csv")
    proccesDB()
    df.to_csv("D:\\My Files\\Courses\\Python\\67_OCR\\out.csv", index=False)
     

run()