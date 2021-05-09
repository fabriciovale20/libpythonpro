class Enviador:
    def enviar(self, remetente, destinatario, assunton, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente inválido: {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass
