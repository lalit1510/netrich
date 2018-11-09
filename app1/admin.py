from django.contrib import admin
from app1.models import Course,Student



class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','course','city','mode_of_payment','fees','fees_date')
    list_filter = ('student_status','fees_date','payment_status')
    search_fields = ('mobile',)
    date_hierarchy = 'fees_date'
    ordering = ('fees', 'fees_date')



admin.site.register(Course)
admin.site.register(Student,StudentAdmin)
