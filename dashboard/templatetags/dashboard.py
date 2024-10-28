from django.template import Library
from django.urls import (
    reverse
)

register = Library()

@register.simple_tag(
    takes_context=True
)
def is_current_page_child_of(
    context,
    parent_url: str,
    is_view: bool=True
):
    current_path = context.request.path
    result = True
    
    if is_view:
        parent_url = reverse(parent_url)
    
    if parent_url.endswith('/'):
        parent_url = parent_url[:-1]
    
    if current_path.endswith('/'):
        current_path = current_path[:-1]
       
    parent_url_slices = parent_url.split('/')
    current_path_slices = current_path.split('/')
    
    for i in range(len(parent_url_slices)):
        parent_slice = parent_url_slices[i]
        current_path_slice = current_path_slices[i]
        
        if parent_slice != current_path_slice:
            result = False
            break

    return result