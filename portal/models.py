#-*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------------------------
# Modelo de 'Projetos', 'Descritivo da oferta' e 'NIIC'
#
# Author: Roberto Ferreira Junior (roberto.ferreira@eng.it)
#		  Claudia Tizue Gombata   (claudia.gombata@eng.it)
#
# Version: 1.0 started (01/08/2010)
#-------------------------------------------------------------------------------------------------------------------

from django.db import models

##################################
####         PROJETOS         ####
##################################

class Projetos(models.Model):

    #FIELDS
    nome_projeto = models.CharField("Projeto", max_length=150, null='true',)
    desc_oferta = models.CharField("Descrição da oferta", max_length=500, null='true',) #aumentar
    integrador = models.CharField("Integrador", max_length=150, null='true',)
    contend_provider = models.CharField("Contend Provider", max_length=150, null='true',)
    marca_servico = models.CharField("Marca do Serviço", max_length=150, null='true',)
    valor_retry = models.IntegerField("Valor de retry", null='true',)
    la =  models.IntegerField("Large account", null='true',)
    lanc_comercial = models.DateField("Lançamento comercial", null='true')
    term_projeto = models.DateField("Término do projeto", null='true')
    data_acordo = models.DateField("Data de Acordo", null='true')
    data_revisao = models.DateField("Data de Revisão", null='true')
    ura_id =  models.IntegerField("URA ID", null='true')
    ura_desc = models.CharField("Descição URA",max_length=150, null='true')

    STATUS = (
        ('F', 'Fechado'),
        ('A', 'Aberto'),
        )
    status =  models.CharField("Status",max_length=2, choices=STATUS, null='true',)

    TIPO_SERVICO_TIM = (
        ('C', 'Cross'),
        ('W', 'White Label'),
        )
    tipo_servico_tim =  models.CharField("Tipo de Serviço Tim",max_length=2, choices=TIPO_SERVICO_TIM, null='true',)

    MOTIVO_DA_OFERTA = (
        ('NO', 'Nova oferta'),
        ('AO', 'Alteração da oferta'),
        ('MO', 'Migração da oferta'),
        ('AT', 'Associação de tarifa'),
        ('SO', 'Suspenção da oferta'),
        ('CO', 'Cancelamento da oferta'),
        )
    motivo_oferta = models.CharField("Motivo da oferta",max_length=2, choices=MOTIVO_DA_OFERTA, null='true',)

    ABRANGENCIA = (
        ('R', 'Regional'),
        ('N', 'Nacional'),
        )
    abrangencia = models.CharField("Abrangência", max_length=2, choices=ABRANGENCIA, null='true',)

    TIPO_SERVICO = (
        ('IN', 'Interatividades'),
        ('DW', 'Downloads'),
        ('CA', 'Canais de assinatura SMS'),
        ('PC', 'Pacotes de conteudo'),
        ('OT', 'Outros'),
        )
    tipo_servico =  models.CharField("Tipo de Serviço", max_length=2, choices=TIPO_SERVICO, null='true',)

    #FOREIGN KEY "Perfil_Servico"
    perfil_servico = models.ForeignKey('PerfilServico', null='true', blank='true')

    def __unicode__(self):
        return self.nome_projeto

#################################
#  RELAÇÕES N -> 1 'PROJETOS'   #
#################################

# Para cada "PROJETO" eu tenho varios Header Enrichment #
class HeaderEnrich(models.Model):
    #FIELDS
    url = models.URLField("Url")
    wap = models.BooleanField("Wap")
    web = models.BooleanField("Web")
    #FOREIGN KEY "Projetos"
    projetos = models.ForeignKey('Projetos')

# Para cada "PROJETO" eu tenho varias estimativas de trafego/receita para cada mes do ano. #
class TrafReceita(models.Model):
    #FIELDS
    mes = models.IntegerField("Mês")
    ano = models.IntegerField("Ano")
    trafego = models.IntegerField("Trafego")
    receita = models.IntegerField("Receita")
    #FOREIGN KEY "Projetos"
    projetos = models.ForeignKey('Projetos')

# Para cada "PROJETO" eu tenho varias tarifas e descri��es. #
class TarifarProj(models.Model):
    #FIELDS
    tarifa_proj = models.IntegerField("Tarifa")
    desc_tarifa = models.CharField("Descrição da tarifa", max_length=200)
    #FOREIGN KEY "Projetos"
    projetos = models.ForeignKey('Projetos')

# Para cada "PROJETO" eu tenho varios planejamentos de midia. #
class PlanejMidia(models.Model):
    #FIELDS
    PLANOS_DE_MIDIA = (
        ('IT', 'Internet'),
        ('TV', 'TV'),
        ('RD', 'Radio'),
        ('RV', 'Revista'),
        ('ME', 'Midia Exterior'),
        ('OT', 'Outros'),
        )
    plan_midia = models.CharField("Planejamento de midia",max_length=2, choices=PLANOS_DE_MIDIA)
    desc_plan_midea = models.CharField("Planejamento de midia", max_length=200)
    #FOREIGN KEY "Projetos"
    projetos = models.ForeignKey('Projetos')

###################
#  TABELAS FATO   #
###################

# Relaciona Projeto com Tipo de Servico
class RelProjTipoServico(models.Model):
    #FOREIGN KEY "Projetos" && "Motivo_Oferta"
    projetos = models.ForeignKey(Projetos)
    tipo_servico = models.ForeignKey('TipoServico')

#############################################
#  RELA��ES N -> 1 'Rel_Proj_Tipo_Servico'  #
#############################################

class TipoServico(models.Model):
    #FIELDS
    desc_tipo_servico = models.CharField(max_length=200)

################################
###    PERFIL DO SERVICO     ###
################################

class PerfilServico(models.Model):
    #FIELDS
    csp_desc = models.CharField("CSP id",max_length=200)

#########################################
#  RELA��ES N -> 1 'PERFIL DO SERVICO'  #
#########################################

class RelatorioDw(models.Model):
    #FIELDS
    grupo = models.CharField("Grupo", max_length=100)
    servico = models.CharField("Serviço", max_length=100)
    fornecedor = models.CharField("Fornecedor", max_length=100)
    aplicacao = models.CharField("Aplicação", max_length=100)
    qtd_ass_diarias = models.IntegerField("Quantidade de assinaturas diárias")
    qtd_evt = models.IntegerField("Quantidade de Eventos")
    qtd_msg_saintes = models.IntegerField("Quantidade de mensagens saintes")
    qtd_download_ativ = models.IntegerField("Quantidade de download ativos")
    qtd_pacotes = models.IntegerField("Quantidade de pacotes")
    #FOREIGN KEY "Perfil_Servico"
    perfil_servico = models.ForeignKey('PerfilServico')

class SintaxeSms(models.Model):
    #FIELDS
    servico = models.CharField("Serviço",max_length=100)
    nome_canal = models.CharField("Nome do canal", max_length=100)
    cmd_ativ_canal = models.CharField("Comando de ativação do canal", max_length=100)
    div_midia = models.CharField("Divulgação na midia", max_length=100)
    cmd_desv_canal = models.CharField("Comando de desativação do canal", max_length=100)
    cmd_rec_ultimo  =  models.CharField("Comando receber ultimo", max_length=100)
    freq_cat = models.CharField("Frequência da categoria", max_length=100)
    #FOREIGN KEY "Perfil_Servico"
    perfil_servico = models.ForeignKey('PerfilServico')

class DadosSdpInteratividade(models.Model):
    #FIELDS
    interatividade = models.CharField("Interatividade", max_length=100)
    #FOREIGN KEY "Perfil_Servico"
    perfil_servico = models.ForeignKey('PerfilServico')

class DadosSdpSubOsp(models.Model):
    #FIELDS
    servico = models.CharField("Serviço", max_length=100)
    sender_mt_conteudo = models.CharField("Sender do MT de conteúdo", max_length=100)
    #FOREIGN KEY "Perfil_Servico"
    perfil_servico = models.ForeignKey('PerfilServico')

class DadosCanaisSmsSub(models.Model):
    #FIELDS
    servico = models.CharField("Serviço",max_length=100)
    mod_recebimento =	 models.CharField("Modelo de recebimento", max_length=100)
    #FOREIGN KEY "Perfil_Servico"
    perfil_servico = models.ForeignKey('PerfilServico')

##########################################
#  RELA��ES 1 -> 1  'PERFIL DO SERVICO'  #
##########################################

class ViasSolicitacao(models.Model):
    #FIELDS
    sms_teste =  models.CharField("SMS teste", max_length=60)
    sms_prod = models.CharField("SMS produção", max_length=60)
    mms_teste = models.CharField("MMS teste", max_length=60)
    mms_prod = models.CharField("MMS produção",max_length=60)
    web_teste =  models.CharField("WEB teste", max_length=60)
    web_prod = models.CharField("WEB produção", max_length=60)
    wap_teste =  models.CharField("WAP teste", max_length=60)
    wap_prod = models.CharField("WAP produção", max_length=60)
    ura_teste = models.CharField("URA teste", max_length=60)
    ura_prod = models.CharField("URA produção", max_length=60)
    url_crc = models.URLField("Acesso a interface de suporte do CRC do Provider")
    perfil_servico = models.OneToOneField('PerfilServico')

class EstimativaTrafego(models.Model):
    #FIELDS
    PERIODO = (
        ('D', 'Diario'),
        ('M', 'Mensal'),
        )
    vol_med = models.IntegerField("Volume médio")
    vol_med_periodo =  models.CharField("Periodo", max_length=2, choices=PERIODO)
    vol_pico =  models.IntegerField("Volume pico")
    vol_pico_periodo =  models.CharField("Periodo", max_length=2, choices=PERIODO)

    #FOREIGN KEY "Perfil_Servico"
    perfil_servico = models.OneToOneField('PerfilServico')

#############################################
#  RELA��ES N -> 1 com 'Estimativa Trafego' #
#############################################

class HoraPico(models.Model):
    PERIODO = (
        ('D', 'Diario'),
        ('M', 'Mensal'),
        )

    #FIELDS
    hora_inicio = models.IntegerField("Hora inicio")
    hora_fim = models.IntegerField("Hora fim")
    hora_pico_col = models.CharField("Período", max_length=2, choices=PERIODO)
    #FOREIGN KEY "Perfil_Servico"
    estimativa_trafego = models.ForeignKey('EstimativaTrafego')

#############################################
#  RELAÇÕES N -> 1 com:					    #
#		-Dados_Sdp_Interatividade           #
#		-Dados_Canais_Sms_Sub      		    #
# 		-Dados_Sdp_Sub_Osp			  	    #
#############################################

class Tripleta(models.Model):

    #FIELDS
    ser1 = models.IntegerField("SER1")
    ser2 = models.IntegerField("SER2")
    ser_3 = models.IntegerField("SER3")
    preco = models.IntegerField("Preço")
    s_desc_fatura = models.CharField("Descrição na fatura", max_length=200)
    #FOREIGN KEY "Perfil_Servico"
    dados_sdp_interatividade = models.ForeignKey(DadosSdpInteratividade)
    dados_sdp_sub_osp = models.ForeignKey(DadosSdpSubOsp)
    dados_canais_sms_sub = models.ForeignKey('DadosCanaisSmsSub')

    ############
    ## RUBISH ##
    ############

    # """
    # # Relaciona Projeto com motivo da oferta
    # class Rel_Proj_Motivo(models.Model):
    # #PRIMARY KEY
    # i_id = models.AutoField(primary_key=True)
    # #FOREIGN KEY "Projetos" && "Motivo_Oferta"
    # i_id_projetos = models.ForeignKey(Projetos)
    # i_id_motivo_oferta = models.ForeignKey(Motivo_Oferta)

    # ##########################################
    # #  RELA��ES N -> 1  'Rel_Proj_Motivo'    #
    # ##########################################

    # class Motivo_Oferta(models.Model):
    # #PRIMARY KEY
    # i_id = models.AutoField(primary_key=True)
    # #FIELDS
    # s_desc_motivo_oferta = models.CharField("Descri��o motivo da ofera", max_length=200)
    # """