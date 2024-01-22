from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')
    # creating an index view here 
    # when a user tries to access the index path (defined in urls.py in learning logs), they will be shown an HTML page
    # defined in index.html, which needs to be made
        # note that the path should be /<app_folder>/templates/learning_logs/index.html
        # so "learning_logs/templates/learning_logs/index.html" in this case

def topics(request):
    """Topics page (view)"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    # adding information needed to properly render the Topics page
    
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
    # adding information needed to properly render an individual Topic page