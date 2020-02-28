
from django.urls import path
from Employee import views

urlpatterns = [
    path("",views.emp),
    path("show",views.show),
    path("edit/<int:id>",views.edit),
    path("update/<int:id>",views.update),
    path("delete/<int:id>",views.destroy),

    path("basic",views.basic),

]
