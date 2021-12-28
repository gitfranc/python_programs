from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404


from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    ''' The homepage of the learning notes '''
    return render(request, "learning_notes_apps/index.html")


def topics(request):
    ''' Display all of topics '''
    # topics = Topic.objects.order_by("date_added")
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {"topics": topics}
    return render(request, "learning_notes_apps/topics.html", context)

@login_required
def topic(request,topic_id):
    ''' List the special topic and all items '''
    topic = Topic.objects.get(id=topic_id)
    # Verify that the request subject belongs to the current user
    check_topic_owner(request,topic)
    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request,"learning_notes_apps/topic.html", context)

def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404

@login_required
def new_topic(request):
    ''' Add new topic '''
    if request.method != "POST":
        # Create new form when no data
        form = TopicForm()
    else:
        # Deal with POST data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("learning_notes_apps:topics")

    # Dispply empty form or invaild form
    context = {"form": form}
    return render(request, "learning_notes_apps/new_topic.html", context)

@login_required
def new_entry(request,topic_id):
    ''' Add new entry in the specical topic '''

    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request,topic)

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_notes_apps:topic", topic_id=topic_id)

    context = {"topic": topic, "form": form}
    return render(request, "learning_notes_apps/new_entry.html", context)

@login_required
def edit_entry(request,entry_id):
    ''' edit the entry '''

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request,topic)

    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_notes_apps:topic", topic_id=topic.id)


    context = {"entry": entry, "topic": topic, "form": form}
    return render(request,"learning_notes_apps/edit_entry.html",context)
