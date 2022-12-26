from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Felicity Jones'
        self.email = 'felicity@gmail.com'
        self.assunto = 'Um assunto qualquer'
        self.mensagem = 'Uma mensagem qualquer'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        self.form = ContatoForm(data=self.dados)

    def test_send_email(self):
        primeiro_formulario = ContatoForm(data=self.dados)
        primeiro_formulario.is_valid()
        primeiro_response = primeiro_formulario.send_mail()

        segundo_formulario = self.form
        segundo_formulario.is_valid()
        segundo_response = segundo_formulario.send_mail()

        self.assertEquals(primeiro_response, segundo_response)