from wheelcms_axle.templates import template_registry
from wheelcms_spokes.page import PageType

def frontpage_context(node):
    return dict(carousel=[node.get(i) for i in ('/pic-1', '/pic-2', '/pic-3')])


template_registry.register(PageType, "wheelsite_site/page_frontpage_view.html",
                           "Frontpage view", context=frontpage_context)

