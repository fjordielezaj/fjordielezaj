from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
     # URL pattern for user login using the CustomLoginView
    path('login/', CustomLoginView.as_view(), name='login'),
    # URL pattern for user logout using the LogoutView
    # The next_page parameter specifies where the user will be redirected after logout.
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # URL pattern for user registration using the RegisterPage view
    path('register/',RegisterPage.as_view(), name='register'),
    
    # Root URL pattern for displaying a list of tasks using the TaskList view
    path('', TaskList.as_view(), name='tasks'),
    # URL pattern for displaying the details of a specific task using the TaskDetail view
    # <int:pk> is a URL parameter representing the primary key of the task to be displayed.
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    # URL pattern for creating a new task using the TaskCreate view
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    # URL pattern for updating an existing task using the TaskUpdate view
    # <int:pk> is a URL parameter representing the primary key of the task to be updated.
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
     # URL pattern for deleting a specific task using the DeleteView view
    # <int:pk> is a URL parameter representing the primary key of the task to be deleted.
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    ]