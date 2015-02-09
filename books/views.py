 # -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from books.models import Book
from django.http import HttpResponseRedirect
from books.forms import ContactForm
from django.template import RequestContext, loader, Context
from books.models import Publisher



# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('请输入搜索内容')
        elif len(q) > 20:
            errors.append('搜索内容不能超过20个字符')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd.get('email', 'noreply@example.com'),
            #     ['siteowner@example.com'],
            # )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!', 'message': 'I am a xxx'}
        )
    return render_to_response('contact_form.html', RequestContext(request, {'form': form}))

# def foobar_view(request, template_name):
#     m_list = Book.objects.filter(is_new=True)
#     return render_to_response(template_name, {'m_list': m_list})

# def view_1(request):
#     #...
#     t = loader.get_template('template1.html')
#     c = Context({
#         'app': 'My app',
#         'user': request.user,
#         'ip_address': request.META['REMOTE_ADDR'],
#         'message': 'I am view 1.'
#     })
#     return t.render(c)
#
# def view_2(request):
#     #...
#     t = loader.get_template('template2.html')
#     c = Context({
#         'app': 'My app',
#         'user': request.user,
#         'ip_address': request.META['REMOTE_ADDR'],
#         'message': 'I am the second view .'
#     })