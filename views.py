from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.


def project(request): 
    if (request.method=="POST"):
        data=request.POST
        
        CustomerId=data.get('textCustomerId')
        CreditScore=data.get('textCreditScore')
        Geography=data.get('textGeography')
        Gender=data.get('textGender')
        Age=data.get('textAge')
        Tenure=data.get('textTenure')
        Balance=data.get('textBalance')
        NumOfProducts=data.get('textNumberOfProducts')
        HasCrCard=data.get('textHasCrCard')
        IsActiveMember=data.get('textIsActiveMember')
        EstimatedSalary=data.get('textEstimatedSalary')
        
        if('buttonpredict' in request.POST):
           import pandas as pd
           path="C:\\Users\\91831\\Desktop\\intenship\\2023_24projects\\2023_projects\\44_customerchurnClassification\\Churn_Modelling.csv"
           data=pd.read_csv(path)

           data['Geography']=data['Geography'].map({'Germany':1,'France':2,'Spain':3})
           data['Gender']=data['Gender'].map({'Male':1,'Female':0})
           #print(data)
           inputs=data.drop(['Exited','Surname','RowNumber'],axis=1)
           output=data['Exited']
           #print(output)
           #print(inputs)
           import sklearn
           from sklearn.model_selection import train_test_split
           x_train,x_test, y_train, y_test = train_test_split(inputs,output,train_size=0.8)
           #print(x_train)
           #print(x_test)
           #print(y_train)
           #print(y_test)
           from sklearn.naive_bayes import GaussianNB
           model=GaussianNB()
           model.fit(x_train,y_train)

            #print("accuracy:",model.score(inputs,outputs)*100)
           y_pred=model.predict(x_test)
            #print(y_pred)

           result=model.predict([[int(CustomerId or 0),int(CreditScore or 0),int(Geography or 0),int(Gender or 0),int(Age or 0),int(Tenure or 0),float(Balance or 0),int(NumOfProducts or 0),int(HasCrCard or 0),int(IsActiveMember or 0),float(EstimatedSalary or 0)]])
           if result==1:
                return HttpResponse('exited')
           else:
                return HttpResponse('not exited')

        return render(request,'project.html',context={'result':result})   
    return render(request,'project.html')



from django.shortcuts import render

# Create your views here.
def Pulsar(request): 
    if (request.method=="POST"):
        data=request.POST
        Mean_Integrated=float(data.get('textMean_Integrated'))
        SD=float(data.get('textSD'))
        EK=float(data.get('textEK'))
        Skewness=float(data.get('textSkewness'))
        Mean_DMSNR_Curve=float(data.get('textMean_DMSNR_Curve'))
        SD_DMSNR_Curve=float(data.get('textSD_DMSNR_Curve'))
        EK_DMSNR_Curve=float(data.get('textEK_DMSNR_Curve'))
        Skewness_DMSNR_Curve=float(data.get('textSkewness_DMSNR_Curve'))
        
        if('buttonpredict' in request.POST):
            import pandas as pd
            path="C:\\Users\\91831\\Desktop\\proj\\2023_24projects\\2023_projects\\42_pulsarclassification\\Pulsar.csv"
            data=pd.read_csv(path)
            #print(data)


            inputs=data.drop('Class',axis=1)
            outputs=data['Class']

            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,outputs,test_size=0.5)
            #print(x_train)
            #print(x_test)
            #print(y_train)
            #print(y_test)

            from sklearn.naive_bayes import GaussianNB
            model=GaussianNB()
            model.fit(x_train,y_train)


            #print("accuracy:",model.score(inputs,outputs)*100)
            y_pred=model.predict([[103.015625,39.341649,0.323328,1.051164,3.121237,21.744669,7.735822,63.171909]])
            #print(y_pred)

            acc=model.score(inputs,outputs)
            #print(acc*100)


            result=model.predict([[Mean_Integrated,SD,EK,Skewness,Mean_DMSNR_Curve,SD_DMSNR_Curve,EK_DMSNR_Curve,Skewness_DMSNR_Curve]])


            return render(request,'Pulsar.html',context={'result':result})   
    return render(request,'Pulsar.html')