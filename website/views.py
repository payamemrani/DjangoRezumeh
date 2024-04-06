from django.shortcuts import render

def index_view(request):
    contex={'name':'پیام عمرانی','job':'برنامه نویس','birthday':'۱۳۶۱','location':'تهران','email':'shanditom@gmail.com','mobile':'۰۹۱۲۸۳۶۹۸۶۶'}
    return render(request,'website/rezumeh.html',contex)
