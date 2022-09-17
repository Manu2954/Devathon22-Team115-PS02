# from crypt import methods
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
import os
from .models import Posts, StudProfile,ClubProfile
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib

# Create your views here.

def emails(a):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    myMail='manojkumarvaduka@gmail.com'
    password='jyinmkvvtcyzakyn'

    smtp.login(myMail,password)

    def message(subject="signup confirmation", 
            text="", img=None,
            attachment=None):
    
    # build message contents
        msg = MIMEMultipart()
      
    # Add Subject
        msg['Subject'] = subject  
      
    # Add text contents
        msg.attach(MIMEText(text))  
  
    # Check if we have anything
    # given in the img parameter
        if img is not None:
          
        # Check whether we have the lists of images or not!
            if type(img) is not list:  
            
              # if it isn't a list, make it one
                img = [img] 
  
        # Now iterate through our list
            for one_img in img:
            
              # read the image binary data
                img_data = open(one_img, 'rb').read()  
            # Attach the image data to MIMEMultipart
            # using MIMEImage, we add the given filename use os.basename
                msg.attach(MIMEImage(img_data,
                                 name=os.path.basename(one_img)))
  
    # We do the same for
    # attachments as we did for images
        if attachment is not None:
          
        # Check whether we have the
        # lists of attachments or not!
            if type(attachment) is not list:
            
              # if it isn't a list, make it one
                attachment = [attachment]  
  
            for one_attachment in attachment:
  
                with open(one_attachment, 'rb') as f:
                
                # Read in the attachment
                # using MIMEApplication
                    file = MIMEApplication(
                        f.read(),
                        name=os.path.basename(one_attachment)
                    )
                file['Content-Disposition'] = f'attachment;\
                filename="{os.path.basename(one_attachment)}"'
              
            # At last, Add the attachment to our message object
                msg.attach(file)
        return msg
  
  
# Call the message function
    msg = message("you are successfully registered to CLUB SPACE")
  
# Make a list of emails, where you wanna send mail
    to = [a]
  
# Provide some data to the sendmail function!
    smtp.sendmail(from_addr=myMail,
              to_addrs=to, msg=msg.as_string())
  
 # Finally, don't forget to close the connection
    smtp.quit()


def signup(request):
    if request.method=='POST':
        user=request.POST['name']
        emaill=request.POST['email']
        regId=request.POST['regId']
        password=request.POST['password']
        rpassword=request.POST['rpassword']
        data=StudProfile.objects.all()
        isDone=False
        found=True

        if password==rpassword:
            for d in data:

                if d.regId==regId and not d.done:
                    d.done=True
                    d.save()
                    found=True
                    break

                elif d.regId==regId and d.done:
                    isDone=True
                    found=True
                    break
                else :
                    found=False

            # if StudProfile.objects.filter(emaill=emaill):
            #     messages.info(request,"You are already registered!!")
            #     return redirect('signup')
            
            # elif StudProfile.objects.filter(user=user):
            #     messages.info(request,"Username already exists!! ")
            #     return redirect('signup')

            if found==False:
                messages.info(request,"the Id you entered doesn't exist")
                return redirect('signup')

            elif isDone==True:
                messages.info(request,"This Id was already registered")
                return redirect('signup')

            elif isDone==False :
                user = User.objects.create_user(username=user,email=emaill,password=password)
                user.save()

                userLogin = auth.authenticate(emaill=emaill,password=password,regId=regId)
                auth.login(request,userLogin)

                emails(emaill)
                return redirect('profilePg')

        else :
            messages.info(request,"Passwords are not same")
            return redirect("signup")  
    else :
        return render(request,'signup.html')

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        email=request.POST['email']
        regId=request.POST['regId']
        password=request.POST['password']
        dd=StudProfile.objects.all()
        chkId = False
        mId = False
        mFound=False

        for k in dd:
            if k.emaill == email and k.regId == regId:
                chkId=True
                mId=True
                mFound=True
                break
            elif k.emaill == email and k.regId != regId:
                mId=False

            else :
                mFound=False 
        user = auth.authenticate(username=username, email=email,password=password)
        
        if mFound==False or mId==False or chkId==False:
            messages.info(request,"""Credentials Invalid """)
            return redirect('login')

        if user is not None and chkId==True and mId == True and mFound==True:
            auth.login(request,user)
            return redirect('postf')
            

    else :
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def profilePg(request):


    userProfile = StudProfile.objects.all()

    if request.method == 'POST' :
        if request.FILES.get('image')==None:
            bio=request.POST['bio']
            userProfile.bio = bio


        if request.FILES.get('image')!=None:
            profileImg = request.POST['profileImg']
            bio=request.POST['bio']

            userProfile.profileImg=profileImg
            userProfile.bio = bio


        return redirect('profilePg')

    return render(request,'profilePg.html')

def postit(request):
    posts= Posts.objects.all()
    return render(request,"postit.html",{'posts':posts})

def clogin(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        clubId=request.POST['clubId']
        password=request.POST['password']
        dc=ClubProfile.objects.all()
        chkcId = False
        mcId = False
        mcFound=False

        for p in dc:
            if p.cemaill == email and p.clubId == clubId:
                chkcId=True
                mcId=True
                mcFound=True
                break
            elif p.cemaill == email and p.clubId != clubId:
                mcId=False

            else :
                mcFound=False 
        user = auth.authenticate(username=username,email=email,password=password)
        
        if mcFound==False or mcId==False or chkcId==False:
            messages.info(request,"""Credentials Invalid """)
            return redirect('clogin')

        if user is not None and chkcId==True and mcId == True and mcFound==True:
            auth.login(request,user)
            return redirect('postit')

    else :
        return render(request,'clogin.html')

def clogout(request):
    auth.clogout(request)
    return redirect('/')

def upload(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('img')
        venue = request.POST['venue']
        print(image)
        newPost = Posts.objects.create(username = user,imagee=image,venue=venue)
        newPost.save()
        return redirect('postit')
    return HttpResponse('<h1> Uploaded </h1>')

def postf(request):
    post = Posts.objects.all()
    return render(request,'postf.html',{'post':post})