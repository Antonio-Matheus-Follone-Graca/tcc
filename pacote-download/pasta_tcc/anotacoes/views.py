from django.shortcuts import render,redirect,get_object_or_404

from anotacoes.forms import FormAnotacoes

# importando model de anotacoes

from anotacoes.models import Anotacoes

from django.contrib import messages

# importando model de user 

from django.contrib.auth.models import User


# importando model de anotacoes 
from anotacoes.models import Anotacoes

# importando model de grupos 

from grupos.models import Grupo


# Create your views here.


# manda para a pagina de  formulário 
def form_anotacoes(request):
     # pegando o grupo pelo id do usuario 
     valores_grupos = Grupo.objects.filter(fk_pessoa_id = request.user.id)
     # chamando formulario 
     form_anotacoes = FormAnotacoes()
     contexto = {'form_anotacoes':form_anotacoes,'grupo':valores_grupos}
     return render(request,'form_anotacoes.html',contexto)


# faz o insert das anotações 
def insert_anotacoes(request):
     # se o usuario clicou no post 

     if request.method ==  'POST': 
          # pegando os dados do formulario
          form_anotacoes = FormAnotacoes(request.POST) 
          contexto = {'form_anotacoes':form_anotacoes}
          
          titulo = request.POST['title']
          mensagem = request.POST['body']
          grupo = request.POST['fk_grupo']
          
          
          if form_anotacoes.is_valid():
                # pegando usuario que fez a anotação  
               user = get_object_or_404(User, pk = request.user.id)
               # se estiver vazio é pq no campo select o usuario não selecionou nenhum grupo 
               if grupo.strip() == "" :
                  objeto_grupo = None
               
               else:
                    # pegando o objeto do grupo 
                    objeto_grupo= get_object_or_404(Grupo, pk=grupo)
              
               # grupo = get_object_or_404(Grupo, pk = grupo)
              
              
               anotacoes = Anotacoes.objects.create(title = titulo, body = mensagem,fk_pessoa = user,fk_grupo= objeto_grupo)
               anotacoes.save()
               return redirect('dashboard')
          
          else:
               return render(request,'form_anotacoes.html',contexto)
          
               
          return render(request,'dashboard.html')
     
     # se o usuario tentar acessar esse metodo sem clicar no enviar formulario 

     # o redireciona para a página do formulario
     else:
          return redirect('form_anotacoes')
     

def deleta_anotação(request,anotacao_id):
     if request.method == 'GET':
          # pega a receita pelo id do parametro funcao 
      anotacao = get_object_or_404(Anotacoes,pk = anotacao_id)
      anotacao.delete()
      # redirecionando para a dashboard
      return redirect('dashboard')


     else: 
          # redirecionando para a dashboard
          return redirect('dashboard') 



def editar_anotação(request, editar_anotacao_id):
    # é requisição do tipo get

    # validação, se clicou no link de editar retorna 
     anotacao_edit = Anotacoes.objects.get(id = editar_anotacao_id)
     form = FormAnotacoes(instance= anotacao_edit) # coloca valores no formulario 
     contexto = {'form_anotacoes_atualizar':form,'id_anotacao':editar_anotacao_id}
    
   
     return render(request,'editar_anotacoes.html',contexto)

     '''if request.method == 'GET':
          pass 



     


     else:
          return redirect('dashboard')
     '''



def atualizar_anotacao(request):
     if request.method == 'POST':
          # pegando o id da anotação 
          anotacao_id = request.POST['id_anotacao']
          form_anotacoes_atualizar = FormAnotacoes(request.POST)
          # pois se acontecer um erro no formulario, a pagina será recarregada e o campo id estará com valor nulo 
          contexto = {'form_anotacoes_atualizar':form_anotacoes_atualizar,'id_anotacao':anotacao_id}
          if form_anotacoes_atualizar.is_valid():
               # pegando receita no banco de dados via id 
               # pk = primary key 
               anotacao_update = Anotacoes.objects.get(pk = anotacao_id)

               # alterando os dados 

               anotacao_update.titulo = request.POST['titulo']
               anotacao_update.mensagem = request.POST['mensagem']

               # atualizando a anotação 
               anotacao_update.save()
               return redirect('dashboard') 
          
          else:
               anotacao_id = anotacao_id
               return render(request,'editar_anotacoes.html',contexto)

          

     else :
          return redirect('dashboard')      

   

   
    
          

   
   
   