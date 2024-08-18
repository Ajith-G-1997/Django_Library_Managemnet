from django.contrib import admin
from .models import Book, Member, Loan

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publisher', 'publication_date')
   
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'membership_date')
   
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'loan_date', 'return_date')
    
admin.site.register(Book,BookAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Loan,LoanAdmin)