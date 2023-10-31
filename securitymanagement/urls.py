from django.urls import path
from . import views

urlpatterns = [

#login pages
    path("loginpage", views.loginpage, name="loginpage"),
    path("loginguard", views.loginguard, name="loginguard"),
    path("loginfelo", views.loginfelo, name="loginfelo"),
    path("loginadmin", views.loginadmin, name="loginadmin"),

#homepages
    path("felohome", views.felohome, name="felohome"),
    path("Securityhome",views.Securityhome,name="Securityhome"),



#securitypages
    path("register_visitor",views.register_visitor,name="register_visitor"),
    path("Security_incidentreport",views.Security_incidentreport,name="Security_incidentreport"),
    path("Security_shift",views.Security_shift,name="Security_shift"),


#felopages



    
    path("feloviewsecurity",views.feloviewsecurity, name="feloviewsecurity"),
    path("feloaddshift",views.feloaddshift,name="feloaddshift"),
    path("addsecuritydata",views.addsecuritydata,name="addsecuritydata"),
    path("feloviewvisitor",views.feloviewvisitor,name="feloviewvisitor"),
    path("feloviewincident",views.feloviewincident,name="feloviewincident"),



    path('updelshift/', views.updelshift, name='updelshift'),
    path('delete_shift/<int:pk>/', views.delete_shift, name='delete_shift'),
    path('update_shift/<int:pk>/', views.update_shift, name='update_shift'),

#felo update page


    path("shiftedit", views.shiftedit, name="shiftedit"),

#admin

    path("adminhomepage", views.adminhomepage, name='adminhomepage'),
 



    path('delete_incident/<int:incident_id>/', views.delete_incident, name='delete_incident'),
   




    path('adminvisitor/', views.adminvisitor, name='adminvisitor'),
    path('adminvisitor/updatevisitor/<str:visitorIc>',views.updatevisitor, name='updatevisitor'),
]

