from django.shortcuts import get_object_or_404, render

from app.models import Aboutus, BlogContent, BlogHead, IndustryBranch, IndustrySettings, ProjectContent, ProjectHead, ServiceContent, ServiceHead, SlideShow, TeamContent, TeamHead, Testimonial, WhyusContent, WhyusHead

# Create your views here.

def index(request):
    about=Aboutus.objects.all()
    settings=IndustrySettings.objects.all()
    industry_branch = IndustryBranch.objects.all()
    blog_content = BlogContent.objects.all()
    blog_head = BlogHead.objects.all()
    whyus_content = WhyusContent.objects.all()
    whyus_head = WhyusHead.objects.all()
    service_content = ServiceContent.objects.all()
    service_head = ServiceHead.objects.all()
    team_content = TeamContent.objects.all()
    team_head = TeamHead.objects.all()
    testmonial = Testimonial.objects.all()
    slide_show = SlideShow.objects.all()
    project_content = ProjectContent.objects.all()
    project_head = ProjectHead.objects.all()

    return render(request,'index.html',{'about':about, 'settings':settings,'industry_branch':industry_branch, 'blog_content':blog_content, 'blog_head':blog_head, 'whyus_content':whyus_content,
    'whyus_head':whyus_head, 'service_content':service_content, 'service_head':service_head,'team_content':team_content,'team_head':team_head,
    'testmonial':testmonial, 'slide_show':slide_show, 'project_content':project_content,'project_head':project_head})


def service(request,id):
    servicecontent_id = get_object_or_404(ServiceContent,pk=id)
    service_content = ServiceContent.objects.get(id=servicecontent_id.id)
    service=ServiceContent.objects.all()
    settings = IndustrySettings.objects.all()
    context ={
        'service':service,
        'service_content':service_content,
        'settings':settings
    
    }
    return render(request,'partials/service.html',context)    

def aboutus(request):
    aboutus=Aboutus.objects.all()
    settings = IndustrySettings.objects.all()
    context ={
        'aboutus':aboutus,
        'settings': settings
    }
    return render(request,'partials/aboutus.html',context)    



def project(request,id):
    project_id = get_object_or_404(ProjectContent,pk=id)
    project = ProjectContent.objects.get(id=project_id.id)
    settings = IndustrySettings.objects.all()
    context ={
        'project':project,
        'settings': settings
    }

    return render(request,'partials/project.html',context)    


def blog(request,id):
    blog_id = get_object_or_404(BlogContent,pk=id)
    blog = BlogContent.objects.get(id=blog_id.id)
    settings = IndustrySettings.objects.all()
    post = BlogContent.objects.all().order_by('-id')[:3][::-1]
    tags = BlogContent.objects.all()
    context = {
        'blog':blog,
        'settings': settings,
        'post':post,
        'tags':tags
    }

    return render(request,'partials/blog.html',context)  


def contact(request):
    branch = IndustryBranch.objects.all()
    aboutus = Aboutus.objects.all()
    settings = IndustrySettings.objects.all()
    context = {
        'branch': branch,
        'settings': settings,
        'aboutus': aboutus,
    }


    return render(request,'partials/contact.html',context) 
