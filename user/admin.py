from django.contrib import admin
from .models import *
# Register your models here.
class contactInfoAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Email','Mobile','Msg')

admin.site.register(contactInfo,contactInfoAdmin)
#################################################
class ugalleryAdmin(admin.ModelAdmin):
    list_display = ('id','gdes','picture')

admin.site.register(ugallery,ugalleryAdmin)
################################################
class myregisterAdmin(admin.ModelAdmin):
    list_display = ('rno','name','mobile','email','passwd','course','year','pic')

admin.site.register(myregister,myregisterAdmin)
#############################################
class teacherregAdmin(admin.ModelAdmin):
    list_display = ('id','name','post','relcourse','profilepic')

admin.site.register(teacherreg,teacherregAdmin)
#############################################
class assignmenttblAdmin(admin.ModelAdmin):
    list_display = ('id','atitle','adesc','course','semester','asub','assignby','assigndate','totalmarks','lastdate','status','attachfile')

admin.site.register(assignmenttbl,assignmenttblAdmin)
###############################################
class studentanswerAdmin(admin.ModelAdmin):
    list_display = ('id','sid','asid','sremark','sanswer','marks','submitdate')

admin.site.register(studentanswer,studentanswerAdmin)
#############################################
class lecturecatAdmin(admin.ModelAdmin):
    list_display = ('id','category','cpic')

admin.site.register(lecturecat,lecturecatAdmin)
#######################################################
class lecturevideoAdmin(admin.ModelAdmin):
    list_display = ('id','vlink','vtitle','vdes','vcategory')

admin.site.register(lecturevideo,lecturevideoAdmin)