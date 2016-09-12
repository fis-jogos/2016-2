Trabalho Bonus 01 (caça aos bugs)
=================================

Entrega: a qualquer momento
Grupos: individual

Os bugs encontrados na FGAme e bibliotecas auxiliares (smallshapes, smallvectors,
pygeneric e colortools) podem render estrelas na disciplina.

Cada bug original reportado no Github concede uma estrela de bônus para o 
usuário. Para receber o bônus, no entanto, as seguintes regras devem ser 
satisfeitas:

    * O bug deve ser original: procure no tracker do github se alguém já não 
      reportou este bug ou algo muito parecido.
    * As suas bibliotecas devem estar atualizadas e o bug ainda deve existir 
      nas últimas versões.
      (para atualizar, rode `pip3 install FGAme -U`)
    * O bug deve ser reprodutível. 
    * Você deve isolar um caso simples que reproduza o bug e não simplesmente
      copiar e colar centenas de linhas de código nas quais você está trabalhando.
      Tente identificar se trata-se de um bug da FGAme ou de uma das bibliotecas
      auxiliares.
    * Deve ser um bug da FGAme e não do seu código!
    * A descrição do bug deve ser clara e mostrar a mensagem de erro apresentada
      (copie e cole o stack trace).
      
Uma vez que você tenha reportado o bug ele está **capturado** e você pode ganhar
estrelas adicionais com ele. 

    * Você ganha uma estrela a mais se criar um teste unitário que mostre uma
      ocorrência do bug. O teste deve ser codificado para falhar no estado atual
      do código, mas passar se o mesmo estiver funcionando corretamente.
      
      Digamos que você descobriu que a smallvectors está calculando o módulo de um
      vetor nulo incorretamente, retornando o valor de 1. O teste deve ser escrito
      com o valor correto esperado. Para isso, vá no arquivo src/smallvectors/test_vector.py e acrescente o código:
      
      ```python
      class VectorBase(...):
        def test_null_vector_have_null_norm(self, null):
            assert null.norm() == 0.0
      ``` 
    
    * Você ganha **pelo menos** uma estrela a mais pela resolução do bug. Bugs
      complexos fornecem mais estrelas. Consulte o professor caso esteja 
      interessado.
      
