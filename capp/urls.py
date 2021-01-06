from django.urls import path
from capp import views
from django.contrib.auth import views as g

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('rg/',views.register,name="reg"),
	path('ds/',views.dashboard,name="dsh"),
	path('pf/',views.prfle,name="pfe"),
	path('upf/',views.updf,name="upfe"),
	path('st/',views.start,name="strt"),
	path('fun/',views.function,name="funcs"),
	path('quiz/',views.examonline,name="qui"),
	path('arr/',views.array,name="arrays"),
	path('pt/',views.point,name="pointer"),
	path('structures/',views.strcuni,name="struct"),
	path('Cdatacontrols/',views.cflow,name="cdf"),
	path('video/',views.index,name="vie"),
	path('sr/',views.strinr,name="stri"),
	path('lg/',g.LoginView.as_view(template_name="html/login.html"),name="lgn"),
	path('lgg/',g.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
]