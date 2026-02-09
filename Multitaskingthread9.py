import threading

def Display(No1, no2,no3):
    print("Inside display: ", No1,no2,no3)

def main():

    t=threading.Thread(target=Display,args=(11,21,22,))
    t.start()
    
   
    
if __name__=="__main__":
    main()