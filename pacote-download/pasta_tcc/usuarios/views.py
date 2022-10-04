
from django.shortcuts import render, redirect
from anotacoes.models import Anotacoes

# importando o forms 

from usuarios.forms import LoginForms,CadastroForms


# importando model user 

from django.contrib.auth.models import User
# importando biblioteca para login 

from django.contrib import auth, messages

# Create your views here.


# rota aonde fica a página de login
def index(request):
    form = LoginForms()
    # passando o form para dicionario
    contexto = {'login_form':form}
    return render(request,'index.html',contexto)


# view que recebe o formulário de login 
def logar(request):
    # validando se formulário foi enviado ou não 
    if request.method ==  'POST': 
        
        # pegando dados do formulário para verificar o login
        form = LoginForms(request.POST)
        contexto = {'login_form':form}

        email = request.POST['email_username']
        senha = request.POST['senha']
        # verificando se o formulário foi preenchido corretamente(sem erros no formulario)

        # se for valido, sem erros  
        if form.is_valid():
           

            if  User.objects.filter(email = email).exists():
                # filtrando o registro do usuario pelo email, onde pego o username pelo email, gambiarar do django pois só faz login pelo username e senha
                nome = User.objects.filter(email = email).values_list('username',flat = True).get()
                #autenticando o usuário 
                user = auth.authenticate(request,username= nome,password = senha)

                    # se o user e senha não estão corretos
                   
                if user is not None:
                    print('login realizado com sucesso')
                    auth.login(request,user)
                    print(f'login realizado com sucesso\n {user}')
                    return redirect('dashboard')
                           
                else:
                    messages.error(request, 'senha errada')
                    return render(request,'index.html',contexto)
            else:
                messages.error(request, 'email não existe em nosso banco de dados')
                return render(request,'index.html',contexto)


        # form invalidio
        else:
            print('formulario invalido')
            contexto = {'login_form':form}
            return render(request,'index.html',contexto)

    else:
        return redirect('index')

    return render(request,'index.html',contexto) 
       
   
   

  

# view que redireciona para a página de criar conta 
def cadastrar(request):
    formulario_cadastro = CadastroForms()
    # passando o form para dicionario
    contexto = {'formulario_cadastro':formulario_cadastro}
    # mandando o formulario para a pagina de cadastro 
    return render(request,'cadastrar.html',contexto)


# view que cria a conta, que recebe os dados do formulário formCriarConta
def insertUsuario(request):
    # se o usuario clicou no enviar formulario
    if request.method == 'POST':
        # pegando os dados do formulario  da requisicao POST
        formulario_cadastro = CadastroForms(request.POST)

        # pegando os valores de cada campo 
        username = request.POST['username']
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']        
        # if para ver se o formulário está, valido não tem nenhum erro
        if formulario_cadastro.is_valid():
           # criando usuario
            user = user = User.objects.create_user(username=username, email=email,password=senha,first_name=nome, last_name=sobrenome, is_superuser= False)
            user.save()
           
           # redirecionando para à pagina de login 
            return redirect('index')
        
        else:
            contexto = {'formulario_cadastro':formulario_cadastro}
            return render(request,'cadastrar.html',contexto)
        
    else:
        return redirect('cadastrar')



# so realiza o des-logout
def logout(request):
    # deslogando o usuario
    auth.logout(request)
    # redirecionando para a pagina principal 
    return redirect('index')


# mostrando as anotações dos usuarios 
def dashboard(request):
    # verifica se o usuario está logado 
    if request.user.is_authenticated: 
        id = request.user.id 

        # guardando anotacoes do usuario via select pelo seu id 
        anotacoes = Anotacoes.objects.filter(fk_pessoa_id = id)

        # dicionario com as anotacoes 
        dados = {
            'anotacoes' : anotacoes
        }
        return render(request,'dashboard.html',dados) 
    
    else:
        return redirect('index')


