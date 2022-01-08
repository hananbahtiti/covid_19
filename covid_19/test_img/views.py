from django.http import request
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import Images
from django.contrib.auth.decorators import login_required
import cv2
import numpy as np
from keras.models import load_model
import h5py

@login_required
def total_cases(request):
    return render(request ,'test_img/HTML111.html')




@login_required    
def image_upload(request):
    data = {}
    form=Images(request.POST or None, request.FILES or None)
    data["info"]=form
    if request.POST:
        
        if form.is_valid():

            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            label_dict={0:'Covid19 Negative', 1:'Covid19 Positive'}
            img_size = 100
            path = 'C:/Users/User/Desktop/project_covid/covid_19%s'% new_form.Image.url
            print(path)
            img = cv2.imread(path)
            gray = cv2.cvtColor(np.float32(img), cv2.COLOR_RGB2GRAY)
            resized = cv2.resize(gray ,(img_size , img_size) )
            data_array = np.array(resized)/255
            data = resized.reshape(-1,img_size,img_size,1)
            model_loded = load_model(r"C:/Users/User/Desktop/project_covid/covid_19/test_img")
            predectied = model_loded.predict(data)
            result=np.argmax(predectied,axis=1)[0]
            accuracy=float(np.max(predectied,axis=1)[0])
            label=label_dict[result]


            data = {'label':label, 'result':result, 'accuracy':accuracy, 'url': new_form.Image.url, 'info': form}

            return render(request, 'test_img/test.html', data)
    return render(request, 'test_img/image_upload.html',data)









