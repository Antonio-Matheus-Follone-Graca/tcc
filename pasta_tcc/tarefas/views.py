from django.shortcuts import render,redirect,get_object_or_404
import tarefas

from tarefas.forms import FormTarefas

# importando model de anotacoes



from django.contrib import messages

# importando model de user 

from django.contrib.auth.models import User

# importando model de tarefa 

from tarefas.models import Tarefas


from grupos.models import Grupo



# Create your views here.



# renderiza  o formulario de tarefas
def form_tarefas(request):
    # pegando o grupo pelo id do usuario 
    valores_grupos = Grupo.objects.filter(fk_pessoa_id = request.user.id)
   
 
    # chamando formulario 
    form_tarefas = FormTarefas()
    contexto = {'form_tarefa':form_tarefas,'grupo':valores_grupos}
    return render(request,'form_tarefas.html',contexto) 



def insert_tarefa(request):
    if request.method == 'POST':
        # pegando dados
        form_tarefas = FormTarefas(request.POST)
        contexto = {'form_tarefa':form_tarefas}

        titulo = request.POST['title']
        mensagem = request.POST['body']
        grupo = request.POST['fk_grupo']
        date_start = request.POST['date_start']
        date_completion = request.POST['date_completion']
        status = request.POST['status']
        
        
        if form_tarefas.is_valid():
            # pegando usuario que fez a anotação  
            user = get_object_or_404(User, pk = request.user.id)
            # se estiver vazio é pq no campo select o usuario não selecionou nenhum grupo 
            if grupo.strip() == "" :
                objeto_grupo = None
  
            else:
                # pegando o objeto do grupo 
                objeto_grupo= get_object_or_404(Grupo, pk=grupo)
            
            
            tarefa = Tarefas.objects.create(title = titulo, body = mensagem , fk_pessoa = user, fk_grupo = objeto_grupo, date_start = date_start, date_completion = date_completion, status = status)
            
            # fazendo o insert 


            tarefa.save()

            return redirect('listar_tarefas')
        
        # se o formulario não for valido

        else:
            return render(request,'form_tarefas.html',contexto)
 
        


       
 

  

    
    else:
        return render(request,'form_tarefas.html',contexto)
        



def listar_tarefas(request):
    # listando grupos do usuario via select pelo seu 
    tarefas = Tarefas.objects.filter(fk_pessoa_id = request.user.id)
    #dicionario com as tarefas  para o  template 

    dados = {
        'tarefas': tarefas
    
    }
    
    return render(request,'listar_tarefas.html',dados) 


def deletar_tarefa(request,tarefa_id): 

    if request.method == 'GET':
        print('TESTTANDO ')
        # pega a receita pelo id do parametro funcao 
        tarefas = get_object_or_404(Tarefas,pk = tarefa_id)
        tarefas.delete()
        # redirecionando para a dashboard
        return redirect('dashboard')
    else: 
      # redirecionando para a dashboard
      return redirect('dashboard') 



# manda para o formulario de editar 
def editar_tarefa(request, id_editar_tarefa):

    if request.method == 'GET':

        # pega todos os da anotação pelo id dela 
        tarefa_edit = Tarefas.objects.get(id = id_editar_tarefa)
     
     
     
        # pegando o grupo atual do usuario 
        grupo_edit = tarefa_edit.fk_grupo
        # pegando os grupos que pertence à ele, caso ele queira mudar 
        valores_grupos_editar = Grupo.objects.filter(fk_pessoa_id = request.user.id)
        form = FormTarefas(instance= tarefa_edit) # coloca valores no formulario 
        contexto = None; 
        if grupo_edit is None:
            # não passo a grupo grupo_edit para o template senão dará erro 
            contexto= {'form_tarefa_atualizar':form,'id_tarefa':id_editar_tarefa,'valores_grupos_editar':valores_grupos_editar}

        # é pq tem grupo na anotação 
        else:
            valores_grupos_editar = valores_grupos_editar.exclude(id = grupo_edit.id)
            contexto= {'form_tarefa_atualizar':form,'id_tarefa':id_editar_tarefa,'grupo_edit':grupo_edit,'valores_grupos_editar':valores_grupos_editar}
    

    

        return render(request,'editar_tarefa.html',contexto)
    
    else:
        return redirect('dashboard')



# atualiza a tarefa em si 


def atualizar_tarefa(request):
    if request.method == 'POST':
        # pegando o id da tarefa
        tarefa_id = request.POST['id_tarefa'] 
        form_tarefa_edit = FormTarefas(request.POST)

        # criando contexto com id do usuario 

        # pois se acontecer um erro no formulario, a pagina será recarregada e o campo id  estará com valor nulo 

        contexto ={
            'form_tarefa_atualizar' : form_tarefa_edit,
            'id_tarefa' : tarefa_id
        }

        if form_tarefa_edit.is_valid():
            # pegando o id da tarefa no banco de dados
            # pk = primary key 
            tarefa_update = Tarefas.objects.get(pk = tarefa_id)

            # alterando os dados
            tarefa_update.title = request.POST['title']
            tarefa_update.body = request.POST['body']
            tarefa_update.date_start = request.POST['date_start']
            tarefa_update.date_completion = request.POST['date_completion']
            tarefa_update.status = request.POST['status']
            tarefa_update.fk_grupo_id = request.POST['fk_grupo_edit']
            

            # atualizando a tarefa

            # se deu tudo certo 
            tarefa_update.save()
            return redirect('dashboard')
        
        else:
            tarefa_id = tarefa_id
            return render(request,'editar_tarefa.html',contexto)

    else:
        return redirect('dashboard') 




# atualiza a data da tarefa con
 
 
 
 
 
 
 
 
 
 
 

  
 
 
 
 
  
 

 

 
 