# importando django forms 


from django.shortcuts import render,redirect,get_object_or_404


from django import forms

from tarefas.models import Tarefas




class  FormTarefas(forms.ModelForm):
   
    # puxando os campos da tabela 
    class Meta:
        model = Tarefas

     
        exclude = ['fk_pessoa','fk_grupo','date',]        
      
        labels = {
         'title': ('Título  da tarefa'),
         'body': ('Corpo'),
         'date_completion': ('Data que tenho que concluir a tarefa'),
         'date_start': ('Data de inicio da tarefa ')
     }
       
       
       
       
     
     
     
     
     
   