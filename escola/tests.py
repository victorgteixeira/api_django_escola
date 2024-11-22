from django.test import TestCase
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate

# Create your tests here.
class ModelEstudanteTestCase(TestCase):
    def setUp(self):
            self.estudante = Estudante.objects.create(
                    nome = 'Teste de Modelo',
                    email = 'testedemodelo@gmail.com',
                    cpf = '68195899056',
                    data_nascimento = '2023-02-02',
                    celular = '86 99999-9999'
            )
    def test_verifica_atributos_de_estudante(self):
            """Teste que verifica os atributos do modelo de Estudante"""
            self.assertEqual(self.estudante.nome,'Teste de Modelo')
            self.assertEqual(self.estudante.email,'testedemodelo@gmail.com')
            self.assertEqual(self.estudante.cpf,'68195899056')
            self.assertEqual(self.estudante.data_nascimento,'2023-02-02')
            self.assertEqual(self.estudante.celular,'86 99999-9999')


class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '68195899056',
            data_nascimento = '2023-02-02',
            celular = '86 99999-9999'
        )
        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

    def test_verifica_conteudo_dos_campos_serializados_de_estudante(self):
        """Teste que verifica o conteúdo dos campos que estão sendo serializados de estudante"""
        dados = self.serializer_estudante.data
        self.assertEqual(dados['nome'],self.estudante.nome)
        self.assertEqual(dados['email'],self.estudante.email)
        self.assertEqual(dados['cpf'],self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'],self.estudante.data_nascimento)
        self.assertEqual(dados['celular'],self.estudante.celular)


class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin',password='admin')
                
def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticação de um user com as credenciais corretas"""
        usuario = authenticate(username = 'admin',password='admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)
        
def test_autenticacao_user_com_username_incorreto(self):
        """Teste que verifica a autenticação com username incorreto"""
        usuario = authenticate(username = 'admn',password='admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
        
def test_autenticacao_user_com_senha_incorreta(self):
        """Teste que verifica a autenticação com senha incorreta"""
        usuario = authenticate(username = 'admin',password='adm')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
