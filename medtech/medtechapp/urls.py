from django.urls import path,include,re_path
from . import views
# from django.urls import include,re_path
from django.conf.urls import url
# from django.conf.urls.static import static
# from django.conf import settings
urlpatterns = [
    path('',views.homepage,name='home'),
    path('signup/',views.signup,name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('logout/',views.logout,name='logout'),
    path('appointment/',views.appointment,name='appointment'),
    path('organdonation/',views.organdonation,name='organdonation'),
    # path('homeremedies/',views.homeremedies,name='homeremedies'),
    re_path(r'^map/(?P<newentrytable_id>[0-9]+)/$',views.map,name='map'),
    re_path('thankyou/',views.thankyou,name='thankyou'),
    # path('request1/',views.request1,name='request1'),
    # re_path(r'^homeremedies/$',views.homeremedies,name='homeremedies'),
    # re_path(r'^homeremedies/(?P<solutions_id>[0-9]+)/$', views.display,name='display'),

    re_path(r'^homeremedies/$',views.homeremedies,name="homeremedies"),
    #homeremedies/21/
    re_path(r'^homeremedies/(?P<solutions_id>[0-9]+)/$', views.display,name="display"),
    re_path(r'^newentry/$',views.newentry,name="newentry"),
    re_path(r'^orgdonation/$',views.orgdonation,name="orgdonation"),
    re_path(r'^organ1/$',views.organ1,name="organ1"),
    re_path(r'^viewpatient/$',views.viewpatient,name="viewpatient"),
    re_path(r'^donatortq/$',views.donatortq,name="donatortq"),
    re_path(r'^doctormap/$',views.doctormap,name="doctormap"),
    re_path(r'^doctordisplay/$',views.doctordisplay,name="doctordisplay"),
    # path('request1/',views.request1,name="request1"),
]