from .models import Board, Comment
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from django.views import View

import requests, json
import pandas as pd
from .forms import BoardForm


def home(request):
    return render(request, 'home.html')

########################################################################
###                         api                                      ###
########################################################################

# @login_required
# @csrf_exempt
class Boardapi(generic.TemplateView):
    def get(self, request):
        url = 'http://127.0.0.1:8080/boardapi/'
        datas = requests.get(url).json()

        # print(datas)
        # print(type(datas))

        df = pd.DataFrame(datas)

        # print(df)
        # print(type(df))

        blist = [tuple(r) for r in df.to_numpy()]

        return render(self.request, 'boardapi_list.html', {
            "board_list" : blist
            })
    

class Boardapi_detail(generic.DetailView):
    def get(self, request, *args, **kwargs):
        datas = {
            'pk': self.kwargs['pk']
        }

        url = 'http://127.0.0.1:8080/boardapi/'+str(datas['pk'])+'/'

        bdetail = requests.get(url, params=datas).json()

        print(bdetail)
        # print(type(bdetail))

        return render(self.request, 'boardapi_view.html', {
            "board_detail" : bdetail
            })


def Boardapi_writeview(request):
    return render(request, 'boardapi_write.html')

# @csrf_exempt
class Boardapi_insert(generic.CreateView):
    model = Board
    fields = '__all__'
    # template_name = 'boardapi_list.html'

    def post(self, request):
        # b_title = requests.get('b_title')
        # b_writer = requests.get('b_writer')
        # b_note = requests.get('b_note')

        url = 'http://localhost:8080/boardapi/create/'

        # datas = {
        #     'b_title': 'b_title',
        #     'b_writer': 'b_writer',
        #     'b_note': 'b_note',
        # }

        datas = {
            'b_title': request.POST.get('b_title'),
            'b_writer' : request.POST.get('b_writer'),
            'b_note' : request.POST.get('b_note'),
        }

        # bcreate = requests.post(url, data=datas).json()
        bcreate = requests.post(url, data=datas)

        print(datas)
        print(bcreate)
        print(type(bcreate))


        return redirect(reverse('board'))
        
        # return render(self.request, 'boardapi_list.html', {
        #     "board_create" : bcreate
        #     })


class Boardapi_edit(generic.DetailView):
    def get(self, request, *args, **kwargs):
        datas = {
            'pk': self.kwargs['pk']
        }

        url = 'http://127.0.0.1:8080/boardapi/'+str(datas['pk'])+'/'

        bdetail = requests.get(url, params=datas).json()

        # print(bdetail)
        # print(type(bdetail))

        return render(self.request, 'boardapi_edit.html', {
            "board_detail" : bdetail
            })


# class Boardapi_update(generic.UpdateView):
#     # model = Board
#     # form_class = BoardForm

#     def update(self, request, *args, **kwargs):
#         data = {
#             'pk': self.kwargs['pk'],
#             'b_title': requests.POST.get['b_title'],
#             'b_note': requests.POST.get['b_note']
#         }

#         url = 'http://localhost:8080/boardapi/'+str(data['pk'])+'/update/'

#         # bupdate = requests.put(url, data=json.dumps(data))
#         bupdate = requests.put(url, datas=data)
        
#         print(bupdate)

#         def get_success_url(self):
#             return reverse('board_detail', kwargs={'pk': self.object.board.pk})

class Boardapi_update(View):
    def put(self, request, *args, **kwargs):
        data = {
            'pk': self.kwargs['pk'],
            'b_title': requests.POST.get['b_title'],
            'b_note': requests.POST.get['b_note']
        }

        url = 'http://localhost:8080/boardapi/'+str(data['pk'])+'/update/'

        # bupdate = requests.post(url, data=data)
        bupdate = requests.put(url, json={'query':data})
        
        print(bupdate)

        def get_success_url(self):
            return reverse('board_detail', kwargs={'pk': self.object.board.pk})


class Boardapi_delete(generic.DeleteView):
    def delete(self, request, *args, **kwargs):
        datas = {
            'pk': self.kwargs['pk']
        }

        url = 'http://127.0.0.1:8080/boardapi/'+str(datas['pk'])+'/delete/'

        # bdelete = requests.delete(url, params=datas).json()
        bdelete = requests.delete(url, params=datas)

        print(bdelete)
        print(type(bdelete))

        return redirect(reverse('board'))

        # def delete(request, *args, **kwargs):
        # datas = {
        # 'pk': kwargs['pk']
        # }

        # url = 'http://127.0.0.1:8080/boardapi/'+str(datas['pk'])+'/delete/'

        # # bdelete = requests.delete(url, params=datas).json()
        # bdelete = requests.delete(url, params=datas)

        # print(bdelete)
        # print(type(bdelete))

        # return redirect(reverse('board'))

        # return render(self.request, 'boardapi_list.html', {
        #     "board_detail" : bdelete
        #     })
        
    


######################  Comment ##########################

class Commentapi_list(generic.TemplateView):
    model = Comment
    fields = '__all__'

    def post(self, request):
        datas = {
            'pk': self.kwargs['pk']
        }

        url = 'http://127.0.0.1:8080/boardapi/'  + str(datas['pk']) + '/comment/'
        clist = requests.get(url, params=datas).json()

        print(datas)
        print(type(datas))

        # df = pd.DataFrame(datas)

        print(clist)
        print(type(clist))

        # blist = [tuple(r) for r in df.to_numpy()]

        return render(self.request, 'boardapi_view.html', {
            "comment_list" : clist
            })

class Commentapi_create(generic.TemplateView):
    model = Comment
    fields = '__all__'
    
    def post(self, request, *args, **kwargs):
        datas = {
            'board_id': self.kwargs['pk'],
            'c_writer' : request.POST.get('c_writer'),
            # 'c_writer' : self.request.user,
            'c_note' : request.POST.get('c_note'),
        }

        url = 'http://127.0.0.1:8080/boardapi/'  + str(datas['board_id']) + '/comment/'
        ccreate = requests.post(url, params=datas)

        print(datas)

        print(ccreate)
        print(type(ccreate))

        return render(self.request, 'boardapi_view.html', {
            "comment_list" : ccreate
        })
    
    def get_sucess_url(self):
        return reverse('BoardDetailView', kwargs = {'pk': self.object.board.pk})




# class signup(apiview):
#     def post(self, request):
#         url = 'http://127.0.0.1:8080/rest-auth/signup'
        
#         user= User()
#         username = request.POST.get(self.username)
#         pw1 = request.POST.get(self.password1)
#         pw2 = request.POST.get(self.password2)
        
#         msg = {
#             "비번 틀림"
#         }

#         if pw1 == pw2:
#             pw = pw1
#             user.name = username
#             user.save()

#         else:
#             return render(request, '/signup', context=msg)
        
#         data {
#                 'pw' : 'password',
#                 'username': 'username',
#         }

#         datas = json.dumps(data)
#         result = requests.post(url, data=datas).json()

#######################

# POST

# def login(request):
#     url = 'http://127.0.0.1:8080/rest_auth/login/
#     id = request.data.get('id')
#     password = request.data.get('password')

#     my_data = {
#         'param1':'id',
#         'param2':'password',
#     }

#     post = requests.post(url, data=my_data).json()
    
#     if id is not None:
#         return response(status=200)
#     else:
#         return response(status=401)



####################### LOGIN #######################



#로그인
def Login(request):
    return render(request, 'accounts/login.html')


class LoginView(LoginView):
    template_name = 'accounts/login.html'

    def post(self, request):
        data = {
            'username' : request.POST.get('username'),
            'password' : request.POST.get('password'),
        }

        url = 'http://localhost:8080/rest-auth/login/'

        blogin = requests.post(url, data=data)

        print(data)
        print(blogin)

        url2 = 'http://localhost:8080/rest-auth/user/'
        blogin2 = requests.get(url2).json
        print(blogin2)

        # if data.objects.filter(username = data['username'], password = data['password']).exists() == True :
        #     return JsonResponse({"message": "로그인에 성공하셨습니다."}, status = 200)
        # else:
        #     return JsonResponse({"message" : "아이디나 비밀번호가 일치하지 않습니다."}, status = 401)

        return redirect('/')


# 로그아웃

def Logout(request):
    return render(request, 'accounts/logout.html')


class LogoutView(LogoutView):
    def post(self, request):
        url = 'http://localhost:8080/rest-auth/logout/'

        blogout = requests.post(url)
        print(blogout)

        return redirect('/')


#회원가입
# class CreateView(View):
#     def post(self, request):
#         data = json.loads(request.body)
#         User(
#             user_id     = data['user_id'],
#             email       = data['email'],
#             password    = data['password'],
#         )

#         if User.objects.filter(user_id = data['user_id']).exists() == True:
#             return JsonResponse({"message" : "이미 존재하는 아이디입니다."}, status = 401)

#         else:
#             User.objects.create(user_id = data['user_id'], email = data['email'], password = data['password'])
#             return JsonResponse({"message" : "회원으로 가입되셨습니다."}, status = 200)