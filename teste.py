  def realizar_programado(self):
        valor = float(self.valor_pagamento.get())
        data = str(self.data_credito.get())
        if conta.PagamentoProgramado(self.usuario, valor, data):
            return self.janela(conta.PagamentoProgramado(self.usuario, valor, data))
        else:
            return self.janela(conta.PagamentoProgramado(self.usuario, valor, data))
