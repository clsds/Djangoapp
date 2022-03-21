from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">欢迎光临</h1>'
    line2 = '<a href="/play/">点这里有惊喜</a>'
    #line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fpicture.ik123.com%2Fuploads%2Fallimg%2F161129%2F4-161129164943.jpg&refer=http%3A%2F%2Fpicture.ik123.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1650463339&t=febfffba1cffbf2dd6fbf9e87c6b5c5f" width=1500>'
    return HttpResponse(line1 + line2) 
    
def play(request):
    line1 = '<h1 style="text-align: center">恭喜你浪费了一秒钟</h1>'
    line2 = '<a href="/">返回</a>'
    return HttpResponse(line1 + line2) 
    