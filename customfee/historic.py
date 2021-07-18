from datetime import datetime

from customfee.models import CustomFeeHistoric


class Historic:
    def __init__(self, request):
        self.client_id = request.data.get("client")
        self.taker_fee = request.data.get("taker")
        self.maker_fee = request.data.get("maker")
        self.expires_at = request.data.get("expires_at")
        self.staff_email = request.data.get("staff_email")
        self.register_type = request.data.get("register_type")
        self.observation = request.data.get("observation")

    def _format_date(self):
        print(self.expires_at)
        self.expires_at = datetime.strptime(self.expires_at, '%d-%m-%Y')
    
    def _add_custom_fee_id(self):

        last_register = (
            CustomFeeHistoric.objects.order_by('custom_fee_id')
            .last()
        )
        last_client_register = (
            CustomFeeHistoric.objects.filter(client_id=self.client_id)
            .order_by('custom_fee_id', 'expires_at')
            .last()
        )
        
        # Se não tiver nenhum será o primeiro registro
        if not CustomFeeHistoric.objects.all().exists():
            custom_fee_id = 1
        # Se for uma chamada de create, será uma nova ficha para o cliente
        elif self.register_type == 'create':
            custom_fee_id = last_register.custom_fee_id + 1      
        # Se for update é pq o cliente já teve uma custom_fee criada
        elif self.register_type == 'update':
            
            # A cada update um novo registro no histórico é criado, assim
            # alteramos o expires_at do ultimo registro para a data atual para
            # fechar o periodo daquele registro e iniciamos um novo com a data
            # de criação do dia e a nova data de exxpiração.    
            last_client_register.expires_at = datetime.now()
            last_client_register.save()

            # Como é uma atualização de uma custom_fee criada no passado
            # utilizamos o mesmo index da anterior para exista um histórico
            # dos updates daquela ficha.
            custom_fee_id = last_client_register.custom_fee_id
        
        return custom_fee_id

    def _historic_register(self):

        self._format_date()
        
        info = CustomFeeHistoric(
                custom_fee_id=self._add_custom_fee_id(),
                client_id=self.client_id,
                taker_fee=self.taker_fee,
                maker_fee=self.maker_fee,
                created_at=datetime.now(),
                expires_at=self.expires_at,
                staff_email=self.staff_email,
                register_type=self.register_type,
                observation=self.observation,
            )
        info.save()
