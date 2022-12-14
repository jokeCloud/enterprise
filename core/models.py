import uuid

from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split(',')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Servico', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Feature(Base):
    ICON_CHOICES = (
        ('lni-rocket', 'Bootstrap 4 Based'),
        ('lni-laptop-phone', 'Fully Responsive'),
        ('lni-cog', 'HTML-CSS-SASS'),
        ('lni-leaf', 'Modern Design'),
        ('lni-layers', 'Multi-templates'),
        ('lni-leaf', 'Contact-Form'),
    )
    HORIZONTAL_CHOICES = (
        ('fadeInRight', 'Direita'),
        ('fadeInLeft', 'Esquerda'),
    )
    feature = models.CharField('Feature', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=20, choices=ICON_CHOICES)
    lado = models.CharField('Lado', max_length=20, choices=HORIZONTAL_CHOICES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.feature


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey(
        'core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={
                           'thumb': {'width': 480, 'height': 480, 'crop': True}})  # noqa
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Plano(Base):
    ICON_CHOICES = (
        ('lni-package', 'Caixa'),
        ('lni-drop', 'Gota'),
        ('lni-star', 'Estrela'),
    )
    DESTAQUE_CHOICE = (
        ('active-tb', 'Sim'),
        ('no-active-tb', 'Não'),
    )
    icone = models.CharField('Icone', max_length=12, choices=ICON_CHOICES)
    preco = models.IntegerField('Preço')
    plano = models.CharField('Plano', max_length=100)
    usuario = models.IntegerField('Usuário')
    armazenamento = models.IntegerField('Armazenamento')
    suporte = models.TextField('Suporte', max_length=200)
    atualizacao = models.TextField('Atualização', max_length=200)
    destaque = models.CharField(
        'Destaque?', max_length=20, choices=DESTAQUE_CHOICE)

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    def __str__(self):
        return self.plano


class Testemunho(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey(
        'core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    testemunho = models.TextField('Testemunho', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={
                           'thumb': {'width': 120, 'height': 120, 'crop': True}})  # noqa
    nota = models.IntegerField('Nota')

    class Meta:
        verbose_name = 'Testemunho'
        verbose_name_plural = 'Testemunhos'

    def __str__(self):
        return self.nome
