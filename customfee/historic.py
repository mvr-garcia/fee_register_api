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

        last_index = CustomFeeHistoric.objects.order_by('custom_fee_id').last()
        
        # Se não tiver nenhum será o primeiro registro
        if not CustomFeeHistoric.objects.all().exists():
            custom_fee_id = 1
        # Se for uma chamada de create, será uma nova cf deste cliente
        elif self.register_type == 'create':
            custom_fee_id = last_index.custom_fee_id + 1      
        # Se for update, o cliente já deve estar no historico.obj
        elif self.register_type == 'update':
            
            # altera o expires_at do ultimo registro para a data atual
            last_client_index = CustomFeeHistoric.objects.filter(client_id=self.client_id).order_by('custom_fee_id').last()
            last_client_index.expires_at = datetime.now()
            last_client_index.save()

            # Como é uma atualização o index deve ser o mesmo anterior para
            # criar um histórico linear dessa 'ficha'
            last_client_index = CustomFeeHistoric.objects.filter(client_id=self.client_id).order_by('custom_fee_id', 'expires_at').last()
            custom_fee_id = last_client_index.custom_fee_id
        
        return custom_fee_id

    def _historic_maker(self):

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
