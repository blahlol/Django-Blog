from django.urls import path
from . import views

app_name="articles" #this acts as a namespace so that we can call links as {% url 'articles:create' %} if we dont add the namespace and call link just as {% url 'list' %} and there are other urls with same names in different apps then it may lead to an error.
urlpatterns=[
    path('create/',views.article_create,name="create"), #if this link was below a link with url params, then that link would execute and we would get another page that isnt intended. In this case the below link would get triggered and we would get a article detail page instead.
    path('approve/<status>/<id>',views.approve,name="approve"),
    path('delete/<id>/',views.article_delete,name="delete"),
    path('edit/<id>/',views.article_edit,name="edit"),
    path('like/<id>/',views.article_like,name='like'),
    path('comment/<id>/',views.article_comment,name="comment"),
    path('add_comment/<id>/<comment>/',views.article_add_comment,name="add_comment"),
    path('<type>/',views.article_list,name="list"),
    #links like this which take url parameters must always be added towards the end
    ]
