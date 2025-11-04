from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Agenda

class AgendaCRUDTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='12345')
        self.client.login(username='admin', password='12345')
        self.contato = Agenda.objects.create(
            nome_completo='João Silva',
            telefone='123456789',
            email='joao@email.com',
            observacao='Contato teste'
        )

    def test_listar_contatos(self):
        response = self.client.get(reverse('listar_contatos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'João Silva')

    def test_cadastrar_contato(self):
        response = self.client.post(reverse('cadastrar_contato'), {
            'nome_completo': 'Maria Souza',
            'telefone': '987654321',
            'email': 'maria@email.com',
            'observacao': 'Novo contato'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Agenda.objects.filter(nome_completo='Maria Souza').exists())

    def test_atualizar_contato(self):
        response = self.client.post(reverse('atualizar_contato', args=[self.contato.id]), {
            'nome_completo': 'João Atualizado',
            'telefone': '123456789',
            'email': 'joao@email.com',
            'observacao': 'Editado'
        })
        self.assertEqual(response.status_code, 302)
        self.contato.refresh_from_db()
        self.assertEqual(self.contato.nome_completo, 'João Atualizado')

    def test_remover_contato(self):
        response = self.client.post(reverse('remover_contato', args=[self.contato.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Agenda.objects.filter(id=self.contato.id).exists())

    def test_requer_login(self):
        self.client.logout()
        response = self.client.get(reverse('listar_contatos'))
        self.assertRedirects(response, '/login/?next=/contatos/')