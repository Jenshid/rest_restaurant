from django.contrib.auth.models import User, auth
from . models import *
from .models import HomepageContent
from django.contrib import messages
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from tinymce.models import HTMLField
from django.core.mail import send_mail,  EmailMessage




def home(request):
    bgb = HomepageContent.objects.all()
    gjh = AboutUs.objects.all()
    bnm = Ourpeople.objects.all()
    return render(request, 'index1.html',{'bgb':bgb,'gjh':gjh,'bnm':bnm})

def register(request):
    return render(request, 'registration.html')


  



def restaurant_description_adm(request, id):
    wer =  Manage_Restaurant.objects.get(id = id)
    return render(request, 'tem/description_adm.html',{'wer':wer})



def booked(request):
    return render(request, 'booking.html')



# Login page view
def Login_view(request):
    return render(request, 'login.html')


def admin_home(request):
    return render(request, 'admin.html')


def add_home(request):
    gtg = HomepageContent.objects.all()
    for t in gtg:
        messages.success(request, 'Content already added')
        return redirect('homepage_edit')
    return render(request, 'tem/home_edit.html')



def edit_content(request):
    gtg = HomepageContent.objects.all()
    return render(request, 'tem/homepage_edit.html',{'gtg':gtg})



def our_people(request):
    return render(request, 'tem/our_people.html')




def nave(request):
    return render(request, 'tem/nave.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request, 'registration.html', {'error': 'Username is already taken'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'registration.html', {'error': 'Email is already registered'})
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                registration = Registration(user=user, Password=password, User_role='admin')
                registration.save()
                return redirect('login')  # Redirect to login page after successful registration
        else:
            return render(request, 'registration.html', {'error': 'Passwords do not match'})

    return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        # Get the username and password from the login form
        username = request.POST.get("user_name")
        password = request.POST.get("pword")

        user = auth.authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Invalid credentials')
            return redirect('login')

        # Log the user in
        auth.login(request, user)

        # Check if the user is registered as an admin
        if Registration.objects.filter(user=user, Password=password).exists():
            bb = Registration.objects.get(user=user, Password=password)
            request.session['logg'] = bb.id  # Save the user ID in the session
            return redirect('admin_home')  # Redirect to the admin home page

        # If the user is not an admin, show the login page with an error
        return render(request, 'login.html', {'error': 'You are not authorized to access the admin page.'})
    
    # Render the login page if request method is GET
    return render(request, 'login.html')



def admin_homepage_edit(request, id):
    gtg = HomepageContent.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('pg_pic')
        imges = request.FILES.get('img_bg') 
        
        gtg.main_title = title  

        if imges: 
            fs = FileSystemStorage()
            fs.save(imges.name, imges)  
            gtg.image = imges  

        gtg.save()  
        messages.success(request, 'Updated successfully' if id else 'Added successfully')
        return redirect('homepage_edit')

    return render(request, 'tem/restaurant_edit.html', {'gtg': gtg})


def delete_restaurant(request,id):
   HomepageContent.objects.get(id=id).delete()
   messages.success(request, 'Deleted successfully')
   return redirect('homepage_edit')


def admin_profile(request):
    tt = Registration.objects.get(id = request.session['logg'])
    return render(request, 'tem/admin_profile.html',{'hyh':tt})


def admin_homepage_add(request):
    if request.method == 'POST':
       title = request.POST.get('pg_pic')
       imges = request.FILES['img_bg']
       fs = FileSystemStorage()
       fs.save(imges.name, imges)
       gtg = HomepageContent()
       gtg.main_title = title
       gtg.image = imges
       gtg.save()
       messages.success(request, 'added successfully')
       return redirect('homepage_edit')
    return render(request, 'tem/home_edit.html')



def admin_profile_edit(request):
    bb = Registration.objects.get(id = request.session['logg'])
    asd = bb.user.pk
    kl =User.objects.get(id = asd)
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        a = User.objects.all().exclude(username = kl.username)
        for t in a:
            if t.username == user_name:
                messages.success(request, 'Username taken . please try another')
                return redirect('admin_profile_edit')
            elif t.email == email:
                messages.success(request, 'Email taken . please try another')
                return redirect('admin_profile_edit')
            
        passwords = make_password(password)
        kl.username = user_name
        kl.email = email
        kl.password = passwords
        kl.save()
        user = auth.authenticate(username = user_name, password =password)
        auth.login(request, user)

        b = bb.id
        a = int(b)
        request.session['logg'] = a     
            
        bb.Password= password
        bb.User_role = 'admin'
        bb.user = kl
        bb.save()
        messages.success(request, 'Updated successfully')
            # Save the user ID in the sessio
        return redirect('admin_profile')
    return render(request, 'tem/adminprofile_edit.html', {'bb': bb, 'kl' :kl})
        


def about(request):
    gjh = AboutUs.objects.all()
    return render(request, 'tem/about.html',{'gjh':gjh})


def about_adm(request):
    gjh = AboutUs.objects.all()
    return render(request, 'tem/about_adm.html',{'gjh':gjh})


def about_delete_adm(request, id):
   AboutUs.objects.get(id=id).delete()
   messages.success(request, 'Deleted successfully')
   return redirect('about_adm')


def about_add_adm(request):
    hyh = AboutUs.objects.all()
    if hyh:
        messages.success(request, 'Content already added')
        return redirect('about_adm') 
    if request.method == 'POST':
        about_content = request.POST.get('about_content')
        AboutUs.objects.create(content = about_content)
        return redirect('about_adm')
    return render(request, 'tem/about_add_adm.html')


def about_edit_adm(request, id):
    gjh = AboutUs.objects.get(id = id)
    if request.method == 'POST':
        content = request.POST.get('content')
        gjh.content = content
        gjh.save()
        messages.success(request, 'Content updated successfully!')
        return redirect('about_adm')  # Redirect to the about page after updating.
    return render(request, 'tem/about_edit_adm.html', {'gjh': gjh})


def our_people(request):
    bnm = Ourpeople.objects.all()
    return render(request, 'tem/our_people.html',{'bnm':bnm})

def our_people_adm(request):
    bnm = Ourpeople.objects.all()
    return render(request, 'tem/our_people_adm.html',{'bnm':bnm})


def our_people_add_adm(request):
    bnm = Ourpeople.objects.all()
    if bnm:
        messages.success(request, 'Content already added')
        return redirect('our_people_adm') 
    if request.method == 'POST':
        ourpeople_content = request.POST.get('ourpeople_content')
        Ourpeople.objects.create(content = ourpeople_content)
        return redirect('our_people_adm')
    return render(request, 'tem/ourpeople_add_adm.html')


def ourpeople_delete_adm(request, id):
   Ourpeople.objects.get(id=id).delete()
   messages.success(request, 'Deleted successfully')
   return redirect('our_people_adm')



def our_people_edit_adm(request, id):
    bnm = Ourpeople.objects.get(id = id)
    if request.method == 'POST':
        content = request.POST.get('content')
        bnm.content = content
        bnm.save()
        messages.success(request, 'Content updated successfully!')
        return redirect('our_people_adm')  # Redirect to the about page after updating.
    return render(request, 'tem/ourpeople_edit_adm.html', {'bnm': bnm})


def missionvision(request):
    zxc = Mission_vision.objects.all()
    return render(request, 'tem/mission_vision.html',{'zxc':zxc})


def mission_vision_adm(request):
    zxc = Mission_vision.objects.all()
    return render(request, 'tem/mission_vision_adm.html',{'zxc':zxc})


def mission_add_adm(request):
    zxc = Mission_vision.objects.all()
    if zxc:
        messages.success(request, 'Content already added')
        return redirect('mission_vision_adm') 
    if request.method == 'POST':
        mission_vision_content = request.POST.get('mission_vision_content')
        Mission_vision.objects.create(content = mission_vision_content)
        return redirect('mission_vision_adm')
    return render(request, 'tem/mission_add_adm.html')

def mission_edit_adm(request, id):
    zxc = Mission_vision.objects.get(id = id)
    if request.method == 'POST':
        content = request.POST.get('content')
        zxc.content = content
        zxc.save()
        messages.success(request, 'Content updated successfully!')
        return redirect('mission_vision_adm')  # Redirect to the about page after updating.
    return render(request, 'tem/mission_edit_adm.html', {'zxc': zxc})

def mission_delete_adm (request, id):
    Mission_vision.objects.get(id=id).delete()
    messages.success(request, 'Deleted successfully')
    return redirect('mission_vision_adm')


def Chairman(request):
    uio= chairman.objects.all()
    return render(request, 'tem/chairman.html',{'uio':uio})


def chairman_adm(request):
    uio= chairman.objects.all()
    return render(request, 'tem/chairman_adm.html',{'uio':uio})

def chairman_add_adm(request):
    uio= chairman.objects.all()
    if uio:
        messages.success(request, 'Content already added')
        return redirect('chairman_adm') 
    if request.method == 'POST':
        chairman_content = request.POST.get('chairman_content')
        chairman.objects.create(content = chairman_content)
        return redirect('chairman_adm')
    return render(request, 'tem/chairman_add_adm.html')

def chairman_edit_adm(request, id):
    uio = chairman.objects.get(id = id)
    if request.method == 'POST':
        content = request.POST.get('content')
        uio.content = content
        uio.save()
        messages.success(request, 'Content updated successfully!')
        return redirect('chairman_adm')  # Redirect to the about page after updating.
    return render(request, 'tem/chairman_edit_adm.html', {'uio': uio})

def chairman_delete_adm (request, id):
    chairman.objects.get(id=id).delete()
    messages.success(request, 'Deleted successfully')
    return redirect('chairman_adm')


def manage_restaurant_adm(request):
    ert= Manage_Restaurant.objects.all()
    return render(request, 'tem/manage_restaurant_adm.html',{'ert':ert})

def manage_restaurant_add_adm(request):
    ert= Manage_Restaurant.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        location_type = request.POST.get('location_type')
        home_page_order = request.POST.get('home_page_order')
        brand_page_order = request.POST.get('brand_page_order')
        reservation_url = request.POST.get('reservation_url')
        instagram_link = request.POST.get('instagram_link')
        facebook_link = request.POST.get('facebook_link')
        twitter_link = request.POST.get('twitter_link')
        image = request.FILES.get('image')
        logo = request.FILES.get('logo')
        description = request.POST.get('description') 
        
        ert = Manage_Restaurant.objects.create(
            name=name,
            
            location_type=location_type,
            home_page_order=home_page_order,
            brand_page_order=brand_page_order,
            reservation_url=reservation_url,
            instagram_link=instagram_link,
            facebook_link=facebook_link,
            twitter_link=twitter_link,
            image=image,
            logo=logo,
            description=description
            
        )
        messages.success(request, 'Restaurant added successfully.')
        return redirect('manage_restaurant_adm')  
    return render(request, 'tem/manage_restaurant_add_adm.html',{'ert':ert})


def manage_restaurant_edit_adm(request, id):
    ert = Manage_Restaurant.objects.get(id = id)
    
    if request.method == 'POST':
        # Get updated values from the form
        name = request.POST.get('name')
        location_type = request.POST.get('location_type')
        home_page_order = request.POST.get('home_page_order')
        brand_page_order = request.POST.get('brand_page_order')
        reservation_url = request.POST.get('reservation_url')
        instagram_link = request.POST.get('instagram_link')
        facebook_link = request.POST.get('facebook_link')
        twitter_link = request.POST.get('twitter_link')
        image = request.FILES.get('image')
        logo = request.FILES.get('logo')
        description = request.POST.get('description')
        
        # Update the restaurant object with new values
        ert.name = name
        ert.location_type = location_type
        ert.home_page_order = home_page_order
        ert.brand_page_order = brand_page_order
        ert.reservation_url = reservation_url
        ert.instagram_link = instagram_link
        ert.facebook_link = facebook_link
        ert.twitter_link = twitter_link
        ert.description = description
        
        # Update the image and logo if new files are provided
    
        if image:
            tyu = FileSystemStorage()
            tyu.save(image.name, image)
            ert.image = image
        if logo:
            tyu = FileSystemStorage()
            tyu.save(logo.name, logo)
            ert.logo = logo


        ert.save()

        
        
        # Save the changes to the
        
        messages.success(request, 'Restaurant details updated successfully.')
        return redirect('manage_restaurant_adm')
    
    return render(request, 'tem/manage_restaurant_edit_adm.html', {'ert': ert})

def manage_restaurant_delete_adm(request , id):
    Manage_Restaurant.objects.get(id = id).delete()
    messages.success(request, 'Restaurant deleted successfully.')

    return redirect('manage_restaurant_adm')

    


def img_rest_adm(request ,id):
    jkl = Manage_Restaurant.objects.get(id=id)
    request.session['manage_rest_img'] = int(jkl.id)
    mnb = Images_rest.objects.filter(restaurant_img_id=id)
    return render(request, 'tem/img_rest_adm.html',{'mnb':mnb})


def img_rest_add_adm(request ):
    if request.method == 'POST':
        qwe = Manage_Restaurant.objects.get(id = request.session['manage_rest_img'])
        image = request.FILES.get('image')
        if image:
            tyu = FileSystemStorage()
            tyu.save(image.name, image)
            Images_rest.objects.create(restaurant_img= qwe,img=image)
        messages.success(request, 'Image added successfully.')
        asd = '/img_rest_adm/'+str(qwe.id)
        return redirect(asd)
    return render(request,'tem/img_rest_add_adm.html')

def img_rest_edit_adm(request, id):
    ert = Images_rest.objects.get(id = id)
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            tyu = FileSystemStorage()
            tyu.save(image.name, image)
            ert.img = image
            ert.save()
        messages.success(request, 'Image updated successfully.')
        asd = '/img_rest_adm/'+str(ert.restaurant_img_id)
        return redirect(asd)
    return render(request,'tem/img_rest_edit_adm.html',{'ert':ert})

def img_rest_delete_adm(request, id):
    ert = Images_rest.objects.get(id=id)
    ert.delete()
    messages.success(request, 'Deleted successfully')
    asd = '/img_rest_adm/'+str(ert.restaurant_img_id)
    return redirect(asd)

def media(request):
    zse= Media_media.objects.all()
    return render(request, 'tem/media.html',{'zse':zse})

def media_adm(request):
    zse= Media_media.objects.all()
    return render(request, 'tem/media_adm.html',{'zse':zse})

def media_add_adm(request):
    zse= Media_media.objects.all()
    if request.method == 'POST':
        content= request.POST.get('content')
        title= request.POST.get('title')
        Media_media.objects.create(content=content,  title= title)
        messages.success(request, 'Media added successfully.')
        return redirect('media_adm')
    return render(request, 'tem/media_add_adm.html',{'zse':zse})


def media_edit_adm(request, id):
    zse = Media_media.objects.get(id = id)
    if request.method == 'POST':
        content = request.POST.get('content')
        title= request.POST.get('title')
        zse.content = content
        zse.title = title
        zse.save()
        messages.success(request, 'Media updated successfully!')
        return redirect('media_adm') 
    return render(request, 'tem/media_edit_adm.html', {'zse': zse})

def media_delete_adm(request, id):
    zse = Media_media.objects.get(id=id)
    zse.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('media_adm')


def Subscription_adm(request):
    vcx= Subscription.objects.all()
    return render(request, 'tem/subscription_adm1.html',{'vcx':vcx})

def subscription_home_add(request):
    email= request.POST.get('email')
    Subscription.objects.create(email=email)
    messages.success(request, 'Subscription added successfully.')
    return redirect('home')

def subscription_delete_adm(request , id):
    vcx = Subscription.objects.get(id=id)
    vcx.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('subscription_adm')

def contact(request):
    bmw = contact_US.objects.last()
    return render(request, 'tem/contact.html',{'bmw': bmw})

def contact_adm(request):
    bmw = contact_US.objects.last()
    return render(request, 'tem/contact_adm1.html', {'bmw': bmw})


def contact_add_adm(request):
    bmw = contact_US.objects.all() 
    if request.method == 'POST':
        title = request.POST.get('title')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        email = request.POST.get('email')
        pinterest_link = request.POST.get('pinterest_link')
        instagram_link = request.POST.get('instagram_link')
        facebook_link = request.POST.get('facebook_link')
        twitter_link = request.POST.get('twitter_link')
        contact_email = request.POST.get('contact_email')
        
        contact_US.objects.create(
            title=title,
            place=place,
            phone=phone,
            description=description,
            email=email,
            pinterest_link=pinterest_link,
            instagram_link=instagram_link,
            facebook_link=facebook_link,
            twitter_link=twitter_link,
            contact_email=contact_email
        )
        
        messages.success(request, 'Contact added successfully.')
        return redirect('contact_adm')
    
    return render(request, 'tem/contact_add_adm.html', {'bmw': bmw})

def contact_edit_adm(request, id):
    bmw =  contact_US.objects.get(id = id)
    if request.method == 'POST':
        title = request.POST.get('title')
        place = request.POST.get('place')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        email = request.POST.get('email')
        pinterest_link = request.POST.get('pinterest_link')
        instagram_link = request.POST.get('instagram_link')
        facebook_link = request.POST.get('facebook_link')
        twitter_link = request.POST.get('twitter_link')
        contact_email = request.POST.get('contact_email')
        
        bmw.title=title
        bmw.place=place
        bmw.phone=phone
        bmw.description=description
        bmw.email=email
        bmw.pinterest_link=pinterest_link
        bmw.instagram_link=instagram_link
        bmw.facebook_link=facebook_link
        bmw.twitter_link=twitter_link
        bmw.contact_email=contact_email
        bmw.save()
        
        messages.success(request, 'Contact updated successfully.')
        return redirect('contact_adm')
    
    return render(request, 'tem/contact_edit_adm.html', {'bmw':bmw})



def contact_delete_adm (request, id):
    bmw = contact_US.objects.get(id=id)
    bmw.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('contact_adm')


def contact_description_adm (request, id):
    bmw = contact_US.objects.get(id = id)
    return render(request, 'tem/contact_description_adm.html',{'bmw':bmw})

def contact_cust(request):
    tgt = contact_US.objects.last()
    to_emm = str(tgt.contact_email)
    email = "muhamedjenshid@gmail.com"
    nam = request.POST.get('nam')
    emm = request.POST.get('emm')
    subj = request.POST.get('subj')
    phone = request.POST.get('phone')
    msg = request.POST.get('msg')
    t_a = 'Name: ' + nam + '\nEmail: ' + emm + '\nSubject: ' + subj + '\nPhone: ' + phone + '\nMessage: ' + msg + '.'
    send_mail('Customer message ', t_a, email, [to_emm], fail_silently=False)
    messages.success(request, 'Successfully Sent Mail')
    return redirect('contact')



def Brand(request):
    international_brands = Manage_Restaurant.objects.filter(location_type='international')
    local_brands = Manage_Restaurant.objects.filter(location_type='local')
    return render(request, 'tem/brand.html',{'international':international_brands,'local':local_brands})


def restaurant_detail(request, id):
    wert = Manage_Restaurant.objects.get(id=id)
    ded = Images_rest.objects.filter(restaurant_img = wert)
    international_brands = Manage_Restaurant.objects.filter(location_type='international')
    local_brands = Manage_Restaurant.objects.filter(location_type='local')
    return render(request, 'tem/inter_restaurant1.html', {
        'wert': wert,
        'ded': ded,
        'international_brands': international_brands,
        'local_brands': local_brands
    })




def Careers (request):
    cvb = Careers_us.objects.all()
    return render(request, 'tem/Careers.html',{'cvb':cvb})  

def job_deatails(request, id):
    cvb = Careers_us.objects.get(id=id) 
    return render(request, 'tem/job_details.html',{'cvb':cvb}) 


def views_application_adm(request, id):
    cvb = Careers_us.objects.get(id=id)
    # Get all job applications related to the specific Careers_us object
    dfg = JobApplication.objects.filter(career= cvb)
    for t in dfg:
        print(t.id)
    
    return render(request, 'tem/views_application_adm.html', {
        'dfg': dfg,  # Job applications related to the selected Careers_us job
        'cvb': cvb,  # The selected Careers_us job details
    })


def views_application_delete_adm(request, id):
    JobApplication.objects.get(id=id).delete()
    messages.success(request, 'Deleted successfully')
    return redirect('careers_adm')


def careers_adm(request):
    cvb =  Careers_us.objects.all()
    return render(request, 'tem/careers_adm1.html',{'cvb':cvb})

def careers_add_adm(request):
    if request.method == 'POST':
        # Retrieve each field from the POST request
        brand = request.POST.get('brand')
        department = request.POST.get('department')
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        contact_email = request.POST.get('contact_email')
        job_code = request.POST.get('job_code')
        job_responsibilities = request.POST.get('job_responsibilities')
        job_requirement = request.POST.get('job_requirement')
        salary_range = request.POST.get('salary_range')
        age_limit = request.POST.get('age_limit')
        place = request.POST.get('place')
        employment_type = request.POST.get('employment_type')  # Ensure this matches the form field name
       
        # Create a new Careers_us instance
        Careers_us.objects.create(
            brand=brand,
            department=department,
            job_title=job_title,
            job_description=job_description,
            contact_email=contact_email,
            job_code=job_code,
            job_responsibilities=job_responsibilities,
            job_requirement=job_requirement,
            salary_range=salary_range,
            age_limit=age_limit,
            place=place,
            employment_type=employment_type 
             # Correct field name
        )

        # Display a success message and redirect
        messages.success(request, 'Career added successfully.')
        return redirect('careers_adm')

    return render(request, 'tem/careers_add_adm1.html')
  

def careers_edit_adm(request, id):
    cvb = Careers_us.objects.get(id=id)
    if request.method == 'POST':
        brand = request.POST.get('brand')
        department = request.POST.get('department')
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        contact_email = request.POST.get('contact_email')
        job_code = request.POST.get('job_code')
        job_responsibilities = request.POST.get('job_responsibilities')
        job_requirement = request.POST.get('job_requirement')
        salary_range = request.POST.get('salary_range')
        age_limit = request.POST.get('age_limit')
        place = request.POST.get('place')
        employment_type = request.POST.get('employment_type') 
       
        cvb.brand=brand
        cvb.department=department
        cvb.job_title=job_title
        cvb.job_description=job_description
        cvb.contact_email=contact_email
        cvb.job_code=job_code
        cvb.job_responsibilities=job_responsibilities
        cvb.job_requirement=job_requirement
        cvb.salary_range=salary_range
        cvb.age_limit=age_limit
        cvb.place=place
        cvb.employment_type=employment_type
        
        cvb.save()
        
        messages.success(request, 'Career updated successfully.')
        return redirect('careers_adm')
    
    return render(request, 'tem/careers_edit_adm.html', {'cvb':cvb})

def careers_delete_adm (request, id):
    cvb = Careers_us.objects.get(id=id)
    cvb.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('careers_adm')


def Careers_job_application(request, id):
    cvb = Careers_us.objects.get(id=id)  # Fetch the specific Careers_us object using the id

    if request.method == 'POST':
        # Collect data from the form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')  # Assuming address is textual data
        position = request.POST.get('position')
        cv = request.FILES.get('cv')  # Fetch the uploaded CV file

        # Save the uploaded CV to the file system
        fs = FileSystemStorage()
        file_path = fs.save(cv.name, cv)

        # Save the application details to the database
        er = JobApplication.objects.create(
            full_name = full_name,
            email = email,
            phone = phone,
            address = address,
            position = position,
            cv = file_path,  # Save the file path to the database
            career = cvb
        )

        # Send a thank-you email to the applicant
        applicant_message = 'Thank you for applying. We will contact you soon.'
        send_mail(
            'Job Application Received',
            applicant_message,
            'muhamedjenshid@gmail.com',  # Sender email
            [email],  # Recipient email (applicant)
            fail_silently=False
        )

        # Fetch the admin email from Careers_us
        admin_email_add = cvb.contact_email  # Dynamically use contact_email

        # Send an email notification to the admin with the CV file attached
        admin_email = EmailMessage(
            'New Job Application Received',
            f"Details:\n\n"
            f"Name: {full_name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Address: {address}\n"
            f"Position: {position}\n\n"
            f"CV is attached below.",
            'muhamedjenshid@gmail.com',  # Sender email
            [admin_email_add],  # Correctly pass the email address in the list
        )

        # Attach the CV to the email if it exists
        if cv:
            cv.seek(0)  # Ensure the file pointer is at the start
            admin_email.attach(cv.name, cv.read(), cv.content_type)

        admin_email.send(fail_silently=False)

        # Display a success message and redirect to the careers page
        messages.success(request, 'Job application submitted successfully. Please check your email.')
        return redirect('Careers')  # Ensure 'Careers' matches your URL name in `urls.py`

    # Render the application form for GET requests
    return render(request, 'tem/careers_job_application.html', {'cvb': cvb})


def search(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    homepage_results = []
    restaurant_results = []
    career_results = []
    Subscription_results  =[]
    AboutUs_results  =[]
    Ourpeople_results  =[]
    Mission_vision_results  =[]
    chairman_results  =[]
    Media_media_results  =[]
    JobApplication_results  =[]


    if query:
        homepage_results = HomepageContent.objects.filter(
        Q(main_title__icontains=query) |
        Q(sub_title__icontains=query)  
        )

        restaurant_results = Manage_Restaurant.objects.filter(
        Q(name__icontains=query) |
        Q(location_type__icontains=query) |
        Q(description__icontains=query) |
        Q(reservation_url__icontains=query)  |
        Q(instagram_link__icontains=query) |
        Q(facebook_link__icontains=query) |
        Q(twitter_link__icontains=query) 
    
        )  
      

        career_results = Careers_us.objects.filter(
                Q(job_title__icontains=query) | 
                Q(job_description__icontains=query) | 
                Q(brand__icontains=query) | 
                Q(department__icontains=query) |
                Q(place__icontains=query) |
                Q(employment_type__icontains=query) |
                Q(age_limit__icontains=query) |
                Q(contact_email__icontains=query) |
                Q(job_code__icontains=query) 
                

            )
        

        Subscription_results = Subscription.objects.filter(
                Q( email__icontains=query)
            )
        

        AboutUs_results = AboutUs.objects.filter(
                Q(content__icontains=query) 
        )


        Ourpeople_results = Ourpeople.objects.filter(
             Q(content__icontains=query) 
        )


        Mission_vision_results = Mission_vision.objects.filter(
             Q(content__icontains=query) 
        )


        chairman_results = chairman.objects.filter(
             Q(content__icontains=query) 
        )


        Media_media_results = Media_media.objects.filter(
            Q(content__icontains=query) |
            Q(title__icontains=query) 
        )

        JobApplication_results = JobApplication.objects.filter(
             Q(full_name__icontains=query) |
             Q(email__icontains=query) |
             Q(phone__icontains=query) |
             Q(address__icontains=query) |
             Q(position__icontains=query) |
             Q(cv__icontains=query)  # Assuming cv is a file field in the JobApplication model
         )
            



    context = {
        'query': query,
        'homepage_results': homepage_results,
        'restaurant_results': restaurant_results,
        'career_results': career_results,
        'Subscription_results': Subscription_results,
        'AboutUs_results': AboutUs_results,
        'Ourpeople_results': Ourpeople_results,
        'Mission_vision_results': Mission_vision_results,
        'chairman_results': chairman_results,
        'Media_media_results': Media_media_results,
        'JobApplication_results': JobApplication_results,
    }
    return render(request, 'tem/Search1.html', context)
 