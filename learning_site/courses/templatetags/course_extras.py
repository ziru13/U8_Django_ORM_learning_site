from django import template
from django.utils.safestring import mark_safe

import markdown2

from ..models import Course
# from learning_site.courses.models import Course  #这个会出错

register = template.Library()


@register.simple_tag
def newest_course():
    """ Gets the most recent course that was added to the library. """
    # return Course.objects.latest('created_at')
    return Course.objects.filter(published=True).latest('created_at')  # 8.2.5

# register.simple_tag('newest_course')


@register.inclusion_tag("courses/course_nav.html")
def nav_courses_list():
    """Return dictionary of courses to display as navigation pane"""
    # courses = Course.objects.all()[:5]
    courses = Course.objects.filter(published=True)[:5]   # 8.2.5
    return {'courses': courses}


# register.inclusion_tag('courses/course_nav.html')(nav_courses_lists)

@register.filter('time_estimate')
def time_estimate(word_count):
    """Estimates the number of minutes it'll take to complete a step based on the passed-in wordcount."""
    minutes = round(word_count / 20)
    return minutes


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """Converts markdown text to HTML"""
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
