
from django.contrib import admin

from app.models import Aboutus, BlogContent, BlogHead, Category, ContactHead, IndustryBranch, IndustrySettings, ProjectContent, ProjectHead, ServiceContent, ServiceHead, SlideShow, TeamContent, TeamHead, Testimonial, WhyusContent, WhyusHead, Tags

# Register your models here.
class AboutusAdmin(admin.ModelAdmin):
    list_display = ('title','description','aboutus_image')
    list_filter= ("title", )

admin.site.register(Aboutus,AboutusAdmin)


class SlideShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slide_image')
    list_filter = ("title", )

admin.site.register(SlideShow, SlideShowAdmin)


class ServiceHeadAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ("title", )

admin.site.register(ServiceHead, ServiceHeadAdmin)


class ServiceContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon','service_image')
    list_filter = ("title", )

admin.site.register(ServiceContent, ServiceContentAdmin)


class WhyusHeadAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ("title", )


admin.site.register(WhyusHead, WhyusHeadAdmin)


class WhyusContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')
    list_filter = ("title", )

admin.site.register(WhyusContent, WhyusContentAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position','comment', 'testimonial_image')
    list_filter = ("name","position" )


admin.site.register(Testimonial, TestimonialAdmin)


class ProjectHeadAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ("title", )

admin.site.register(ProjectHead, ProjectHeadAdmin)


class ProjectContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category',
                    'tag', 'client', 'challange', 'solution', 'date_created', 'time_duration', 'image_project')
    list_filter = ("title","category","tag","client","date_created", )

admin.site.register(ProjectContent,ProjectContentAdmin)


class TeamHeadAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ("title", )

admin.site.register(TeamHead,TeamHeadAdmin)


class TeamContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'fb_account',
                    'twitter_account', 'linkedin_account', 'image_team')
    list_filter = ("name", "position" )

admin.site.register(TeamContent, TeamContentAdmin)


class BlogHeadAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ("title", )

admin.site.register(BlogHead, BlogHeadAdmin)


class BlogContentAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'category',
                    'tag',  'date_created', 'image_blog')
    list_filter = ("title", "category", "tag",)

admin.site.register(BlogContent, BlogContentAdmin)


class IndustryBranchAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'branch_phone',
                    'branch_email',  'branch_address')
    list_filter = ("branch_name", "branch_phone", "branch_email",)


admin.site.register(IndustryBranch, IndustryBranchAdmin)

admin.site.register(Category)
admin.site.register(Tags)


class IndustrySettingsAdmin(admin.ModelAdmin):
    list_display = ('mission', 'vision',
                    'goal',  'phone','email','office_time','facebook','instagram','twitter','linkedin')
admin.site.register(IndustrySettings, IndustrySettingsAdmin)



