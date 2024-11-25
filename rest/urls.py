from django.urls import path
import rest.views

urlpatterns = [
    path('', rest.views.home, name='home'),        # Root URL for home
    path('home', rest.views.home, name='home'),
    path('brand', rest.views.Brand, name='brand'),
    path('media',rest.views.media, name = 'media'),
    path('media_adm',rest.views.media_adm, name = 'media_adm'),
    path('media_add_adm',rest.views.media_add_adm, name = 'media_add_adm'),
    path('media_edit_adm/<id>',rest.views.media_edit_adm, name = 'media_edit_adm'),
    path('media_delete_adm/<id>',rest.views.media_delete_adm, name = 'media_delete_adm'),
    path('our_peolpe', rest.views.our_people, name='our_peolpe'),   # '/home' URL
    path('our_people_adm', rest.views.our_people_adm, name='our_people_adm'),
    path('ourpeople_edit_adm/<id>', rest.views.our_people_edit_adm, name='ourpeople_edit_adm'),  #
    path('ourpeople_delete_adm/<id>', rest.views.ourpeople_delete_adm, name='ourpeople_delete_adm'),
    path('our_people_add_adm', rest.views.our_people_add_adm, name='our_people_add_adm'),
    path('mission_vision', rest.views. missionvision, name='mission_vision'),
    path('mission_vision_adm', rest.views.mission_vision_adm, name='mission_vision_adm'),
    path('mission_add_adm', rest.views. mission_add_adm, name='mission_add_adm'),
    path('mission_edit_adm/<id>', rest.views. mission_edit_adm, name='mission_edit_adm'),
    path('mission_delete_adm/<id>', rest.views.mission_delete_adm, name='mission_delete_adm'),
    path('missionvision', rest.views.missionvision, name='missionvision'),
    path('Chairman', rest.views.Chairman, name='Chairman'),
    path('chairman_add_adm', rest.views.chairman_add_adm, name='chairman_add_adm'),
    path('chairman_edit_adm/<id>', rest.views. chairman_edit_adm, name='chairman_edit_adm'),
    path('chairman_delete_adm/<id>', rest.views.chairman_delete_adm, name='chairman_delete_adm'),
    path('chairman_adm', rest.views. chairman_adm, name='chairman_adm'),
    path('img_rest_adm/<id>', rest.views. img_rest_adm, name='img_rest_adm'),
    path('img_rest_add_adm', rest.views. img_rest_add_adm, name= 'img_rest_add_adm'),
    path('img_rest_edit_adm/<id>', rest.views. img_rest_edit_adm, name= 'img_rest_edit_adm'),
    path('img_rest_delete_adm/<id>', rest.views. img_rest_delete_adm, name= 'img_rest_delete_adm'),
    path('manage_restaurant_adm', rest.views. manage_restaurant_adm, name='manage_restaurant_adm'),
    path('manage_restaurant_edit_adm/<id>', rest.views.manage_restaurant_edit_adm, name='manage_restaurant_edit_adm'),
    path('manage_restaurant_add_adm', rest.views. manage_restaurant_add_adm, name='manage_restaurant_add_adm'),
    path('manage_restaurant_delete_adm/<id>', rest.views. manage_restaurant_delete_adm, name='manage_restaurant_delete_adm'),
    path('restaurant_description_adm/<id>', rest.views. restaurant_description_adm, name='restaurant_description_adm'),
    path('register', rest.views.register, name='register'),  # '/register' URL
    path('Login', rest.views.Login_view, name='Login'),
    path('about', rest.views.about, name='about'),
    path('Careers', rest.views.Careers, name='Careers'),
    path('Careers_job_application/<id>', rest.views.Careers_job_application, name='Careers_job_application'),
    path('contact', rest.views.contact, name='contact'),
    path('contact_adm', rest.views.contact_adm, name='contact_adm'),
    path('contact_add_adm', rest.views.contact_add_adm, name='contact_add_adm'),
    path('contact_description_adm/<id>', rest.views. contact_description_adm, name='contact_description_adm'),
    path('contact_edit_adm/<id>', rest.views.contact_edit_adm, name='contact_edit_adm'),
    path('contact_delete_adm/<id>', rest.views.contact_delete_adm, name='contact_delete_adm'),
    path('booking', rest.views.booked, name='booking'),
    path('admin_home', rest.views.admin_home, name='admin_home'),  # Admin home URL    # '/login' URL
    path('login', rest.views.login, name='login'),  # Ensure you have this line
    path('homepage_edit', rest.views.edit_content, name='homepage_edit'),
    path('add_home', rest.views.add_home, name='add_home'),
    path('admin_homepage_add',rest.views.admin_homepage_add, name='admin_homepage_add'),
    path('admin_homepage_edit/<int:id>/', rest.views.admin_homepage_edit, name='admin_homepage_edit'),  #
    path('delete_restaurant/<int:id>/', rest.views.delete_restaurant, name='delete_restaurant'),
    path('about_adm', rest.views.about_adm, name='about_adm'),
    path('about_add_adm', rest.views.about_add_adm, name='about_add_adm'),
    path('about_delete_adm/<id>', rest.views.about_delete_adm, name='about_delete_adm'),
    path('about_edit_adm/<id>',rest.views.about_edit_adm, name='about_edit_adm'),
    path('admin_profile', rest.views.admin_profile, name='admin_profile'),
    path('admin_edit', rest.views.admin_profile_edit, name='admin_edit'),
    path('subscription_adm',rest.views.Subscription_adm, name='subscription_adm'),
    path('subscription_home',rest.views.subscription_home_add, name='subscription_home'),
    path('subscription_delete_adm/<id>',rest.views.subscription_delete_adm, name='subscription_delete_adm'),
    path('contact_home',rest.views.contact_cust, name='contact_home'),
    path('restaurant_detail/<id>',rest.views.restaurant_detail, name='restaurant_detail'),
    path('careers_adm',rest.views.careers_adm, name='careers_adm'), 
    path('careers_add_adm',rest.views.careers_add_adm, name='careers_add_adm'),
    path('careers_edit_adm/<id>',rest.views.careers_edit_adm, name='careers_edit_adm'),
    path('careers_delete_adm/<id>',rest.views.careers_delete_adm, name='careers_delete_adm'),
    path('views_application_adm/<id>',rest.views.views_application_adm, name='views_application_adm'),
    path('views_application_delete_adm/<id>', rest.views.views_application_delete_adm, name='views_application_delete_adm'),
    path('job_details/<id>',rest.views.job_deatails, name='job_details'),
    path('search/', rest.views.search, name='search'),

   
  
]

