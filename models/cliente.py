"""
Módulo Cliente - Representa um cliente do restaurante Midnight Kitchen.

Cada cliente tem uma história, um segredo conectado ao passado do Master,
e um prato favorito que pode desbloquear memórias.
"""


class Cliente:
    """
    Representa um cliente que visita o restaurante.

    Atributos:
        nome (str): Nome completo do cliente
        idade (int): Idade em anos
        profissao (str): Profissão ou ocupação atual
        descricao (str): Descrição visual / primeira impressão
        humor (str): Estado emocional atual (ex: "pensativo", "cansado", "ansioso")
        prato_favorito (str): Nome do prato que tem significado especial
        segredo (str): O que o cliente esconde (conexão com o Master)
        confianca (int): Nível de confiança no Master (0-100)

    Exemplo de uso:
        >>> yuki = Cliente(
        ...     nome="Yuki Tanabe",
        ...     idade=28,
        ...     profissao="Fotógrafa",
        ...     descricao="Uma jovem com câmera antiga no pescoço",
        ...     humor="pensativa",
        ...     prato_favorito="Tamago Gohan",
        ...     segredo="Fotografou um incêndio há 10 anos"
        ... )
        >>> print(yuki.apresentar())
        >>> print(yuki.reagir("pergunta_trabalho"))
    """

    def __init__(
        self,
        nome: str,
        genero_masculino: bool,
        idade: int,
        profissao: str,
        descricao: str,
        humor: str,
        prato_favorito: str,
        segredo: str,
        confianca: int = 0
    ):
        """
        Inicializa um novo cliente com seus atributos.

        Args:
            nome: Nome completo do cliente
            idade: Idade em anos
            profissao: Profissão ou ocupação
            descricao: Descrição visual (primeira impressão)
            humor: Estado emocional inicial
            prato_favorito: Prato com significado especial
            segredo: Conexão oculta com o passado do Master
            confianca: Nível inicial de confiança (padrão: 0)

        TODO (Iuri): Implemente este método!

        Dica: Use 'self.atributo = valor' para cada parâmetro.
        Exemplo: self.nome = nome

        São 8 atributos para inicializar (todos os parâmetros acima).
        """
        # ════════════════════════════════════════════════════════════
        # 📝 SEU CÓDIGO AQUI (aproximadamente 8 linhas)
        # ════════════════════════════════════════════════════════════
        
        self.nome = nome
        self.genero_masculino = genero_masculino
        self.idade = idade
        self.profissao = profissao
        self.descricao = descricao
        self.humor = humor
        self.prato_favorito = prato_favorito
        self.segredo = segredo
        self.confianca = confianca

    def apresentar(self) -> str:
        """
        Retorna a primeira impressão do cliente ao entrar no restaurante.

        Returns:
            String formatada descrevendo o cliente.

        Exemplo de saída esperada:
            "Uma jovem com câmera antiga no pescoço entra no restaurante.
             Ela parece pensativa.
             — Boa noite... ainda está aberto?"

        TODO (Iuri): Implemente este método!

        Dica: Use f-strings para interpolar os atributos.
        Exemplo: f"Texto com {self.atributo} aqui"

        Estrutura sugerida:
        1. Linha 1: Descrição física (self.descricao)
        2. Linha 2: Estado emocional (self.humor)
        3. Linha 3: Uma fala de chegada (pode ser fixa ou variar com humor)

        Use \\n para quebras de linha dentro da string.
        """
        # ════════════════════════════════════════════════════════════
        # 📝 SEU CÓDIGO AQUI (aproximadamente 5-8 linhas)
        # ════════════════════════════════════════════════════════════
        if self.genero_masculino:
            return f'{self.descricao} entra no restaurante.\nEle parece {self.humor}.\n— Boa noite... ainda está aberto?'
        else:
            return f'{self.descricao} entra no restaurante.\nEla parece {self.humor}.\n— Boa noite... ainda está aberto?'

    def reagir(self, acao: str) -> str:
        """
        Retorna a reação do cliente a uma ação do jogador.

        Args:
            acao: Tipo de ação realizada. Valores possíveis:
                  - "silencio": Master fica em silêncio
                  - "pergunta_trabalho": Pergunta sobre o trabalho
                  - "pergunta_pessoal": Pergunta algo pessoal
                  - "oferece_cha": Oferece chá silenciosamente

        Returns:
            String com a reação do cliente.

        TODO (Iuri): Implemente este método!

        Dica: Use if/elif/else para diferentes ações.

        Estrutura sugerida:
            if acao == "silencio":
                return "..."
            elif acao == "pergunta_trabalho":
                return "..."
            # ... etc
            else:
                return "O cliente olha sem entender."

        Bônus: Faça a reação variar com self.humor ou self.confianca!
        """
        # ════════════════════════════════════════════════════════════
        # 📝 SEU CÓDIGO AQUI (aproximadamente 10-15 linhas)
        # ════════════════════════════════════════════════════════════
        if acao == "silencio":
            return "O cliente olha ao redor, desconfortável com o silêncio."
        elif acao == "pergunta_trabalho":
            return "O cliente sorri levemente e começa a falar sobre seu trabalho."
        elif acao == "pergunta_pessoal":
            return "O cliente hesita, claramente desconfortável com a pergunta."
        elif acao == "oferece_cha":
            return "O cliente aceita o chá com um sorriso agradecido."
        else:
            return "O cliente olha sem entender."

    def aumentar_confianca(self, quantidade: int) -> None:
        """
        Aumenta o nível de confiança do cliente.

        Args:
            quantidade: Quanto aumentar (pode ser negativo para diminuir)

        TODO (Iuri): Implemente este método!

        Dica:
        - Some a quantidade ao self.confianca
        - Garanta que confianca nunca fique abaixo de 0 ou acima de 100
        - Use min() e max() ou condicionais para limitar

        Exemplo com min/max:
            self.valor = max(0, min(100, self.valor + quantidade))
        """
        # ════════════════════════════════════════════════════════════
        # 📝 SEU CÓDIGO AQUI (aproximadamente 2-3 linhas)
        # ════════════════════════════════════════════════════════════
        self.confianca = max(0, min(100, self.confianca + quantidade))

    def pode_revelar_segredo(self) -> bool:
        """
        Verifica se o cliente confia o suficiente para revelar seu segredo.

        Returns:
            True se confianca >= 80, False caso contrário.

        TODO (Iuri): Implemente este método!

        Dica: É uma única linha com return e uma comparação.
        """
        # ════════════════════════════════════════════════════════════
        # 📝 SEU CÓDIGO AQUI (1 linha)
        # ════════════════════════════════════════════════════════════
        return self.confianca >= 80

# ════════════════════════════════════════════════════════════════════
# ÁREA DE TESTES - Execute este arquivo diretamente para testar
# ════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Teste básico - descomente após implementar

    print("=" * 60)
    print("TESTANDO CLASSE CLIENTE")
    print("=" * 60)

    # Criar um cliente de teste
    yuki = Cliente(
        nome="Yuki Tanabe",
        genero_masculino=False,
        idade=28,
        profissao="Fotógrafa freelancer",
        descricao="Uma jovem com uma câmera antiga pendurada no pescoço",
        humor="pensativa",
        prato_favorito="Tamago Gohan",
        segredo="Fotografou um incêndio devastador há 10 anos"
    )

    # Teste 1: Verificar atributos
    print("\n[Teste 1] Atributos:")
    print(f"  Nome: {yuki.nome}")
    print(f"  Idade: {yuki.idade}")
    print(f"  Profissão: {yuki.profissao}")
    print(f"  Confiança inicial: {yuki.confianca}")

    # Teste 2: Apresentação
    print("\n[Teste 2] Apresentação:")
    print(yuki.apresentar())

    # Teste 3: Reações
    print("\n[Teste 3] Reações:")
    print(f"  Silêncio: {yuki.reagir('silencio')}")
    print(f"  Pergunta trabalho: {yuki.reagir('pergunta_trabalho')}")
    print(f"  Oferece chá: {yuki.reagir('oferece_cha')}")

    # Teste 4: Sistema de confiança
    print("\n[Teste 4] Confiança:")
    print(f"  Confiança inicial: {yuki.confianca}")
    print(f"  Pode revelar segredo? {yuki.pode_revelar_segredo()}")

    yuki.aumentar_confianca(50)
    print(f"  Após +50: {yuki.confianca}")

    yuki.aumentar_confianca(40)
    print(f"  Após +40: {yuki.confianca}")
    print(f"  Pode revelar segredo agora? {yuki.pode_revelar_segredo()}")

    # Teste de limites
    yuki.aumentar_confianca(100)  # Não deve passar de 100
    print(f"  Após +100 (deve ser 100): {yuki.confianca}")

    yuki.aumentar_confianca(-200)  # Não deve ficar negativo
    print(f"  Após -200 (deve ser 0): {yuki.confianca}")

    print("\n" + "=" * 60)
    print("TESTES CONCLUÍDOS!")
    print("=" * 60)
