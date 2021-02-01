from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from core.models import PontoTuristico
from atracoes.models import Atracao
from enderecos.models import Endereco
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer

class PontoTuristicoSerializer(ModelSerializer):

    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = [
            "id", 
            "nome", 
            "descricao", 
            "aprovado", 
            "foto", 
            "atracoes", 
            "endereco", 
            "comentarios", 
            "avaliacoes", 
            "descricao_completa", 
            "descricao_completa_2"]

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
    
    def criar_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def criar_endereco(self, endereco, ponto):
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.save()

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto = PontoTuristico.objects.create(**validated_data)
        
        self.criar_atracoes(atracoes, ponto)
        self.criar_endereco(endereco, ponto)

        return ponto