from django.shortcuts import render

# Create your views here.
 
"""A view to return the shopping bag contents"""
def view_bag(request):
    return render(request, 'bag/bag.html')