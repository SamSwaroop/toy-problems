class LRU:
    def __init__(self,cache):
        print("This is the init method")
        self.cache=[]
        self.cache.append(cache)
        print(self.cache)
        

    def get(self):
        if(len(self.cache)==0):
            print("Sorry,cache memory is empty")
        else:
            return self.cache.pop(0)

        

    def Set(self,URL):
        if(len(self.cache)==5):
            print("Sorry,Cache size full. Removing the least recently used URL to accomodate new URLs")
            self.cache.pop(0)
            self.cache.append(URL)
            return(f"Added the URL : {URL}")

        else:
            self.cache.append(URL)
            return(f"Added the URL : {URL}")


    def display(self):
        return self.cache



class LRUtest(LRU):

    def __init__(self, URL):
        self.URL=URL
        
    def testSet(self):
        
        k=f"Added the URL : {self.URL}"
        d=LRU("www.google.com")
        assert k == d.Set("www.Facebook.com"),"Testing Successful for SET method"

    def testGet(self):
        j=self.URL
        a=LRU(j)
        i=a.get()
        assert j != i,"Testing Successful for GET method"
        #print("Hi")

    # def testDisplay(self):
    #     e=LRU("www.")




def main():
    print("enter an input of URL for LRUtest")
    v=str(input())
    g=LRUtest(v)
    z=True
    print("enter your choice")
    y=int(input())
    
    print("press 1 for testing set method")
    print("press 2 for testing get method")
    while(z):
        if(y==1):
            g.testSet()

        elif(y==2):
            g.testGet()

        else:
            print("invalid input")
            z=False

        
    # g.testSet()
    # g.testGet()


# def main():
#     k=LRU("www.Facebook.com")
#     x="Added the URL : www.google.com"
#     assert x == k.Set("www.Facebook.com"),"This is an error"



        

    
        


# def main():
#     print()
#     print()
#     print("Enter the first URL to be added to ")
#     g=str(input())
    
#     k=LRU(g)
#     print(f"Sucessfully added the first URL:{g}")
#     print()
#     j=True
#     while(j):
#         print()
#         print()
#         print("Enter your desired operation:")
#         print("Press 1 for setting URL into the LRU-cache")
#         print("Press 2 for getting URL from the LRU-cache")
#         print("Press 3 for displaying the LRU-cache")
#         print("Press 0 to exit")
#         n=int(input())
#         if(n==1):
#             print("Enter the URL to be set into the URL cache")
#             x=str(input())
#             print(k.Set(x))
#         elif(n==2):
#             print("Fetching the least recently used")
#             print(k.get())
#         elif(n==3):
#             print("The URL's present in LRU-cache are :")
#             h=[]
#             h=k.display()
#             print(h)
            
#         elif(n==0):
#             print("exit")
#             j=False
#         else:
#             print("Invalid Input")


if __name__=="__main__":
    main()