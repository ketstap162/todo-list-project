from django.urls import path

from todo.views import (
    index,
    TaskListView, remark_task, TaskCreateView, TaskUpdateView, TaskDeleteView,
    TagListView, TagCreateView, TagUpdateView, TagDeleteView,
)


urlpatterns = [
    path("", index, name="index"),

    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/remark", remark_task, name="task-remark"),
    path("tasks/create", TaskCreateView.as_view(), name="tasks-create"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="tasks-update"),
    path("tasks/<int:pk>/delete", TaskDeleteView.as_view(), name="tasks-delete"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),

]

app_name = "todo"
