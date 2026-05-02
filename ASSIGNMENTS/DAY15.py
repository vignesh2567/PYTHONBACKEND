
#CODE TO CREATE CUSTOM CLASS AND OBJECT

class APPS: #CLASS

    def appdetails(a):
        a.appname = input ("Enter the decided app name: ")
        a.appnet = input ("Need internet connection(Y/N): ")
        a.apptype = input ("Enter the type of app(Social media,gaming,Education etc): ")
        a.appsize = input ("Enter the app size: ")
        a.appadict = input ("Is this app adictive or not(Y/N): ")

    def displayad(a):
        print ("AppName =",a.appname)
        print ("Internet connection:",a.appnet)
        print ("AppType=",a.apptype)
        print ("AppSize=",a.appsize)
        print ("ADDICTION=",a.appadict)

app1=APPS()


app1.appdetails()
app1.displayad()
