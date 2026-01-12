"""
Cliente - Um visitante do Midnight Kitchen.

Cada cliente tem um estado emocional que pode mudar durante a conversa.
Quando o cliente se abre o suficiente, revela seu prato favorito.
Ao receber esse prato, uma memoria importante e desbloqueada.
"""


class Cliente:
    """Representa um cliente que visita o restaurante."""

    # Estados possiveis: fechado -> cauteloso -> aberto -> vulneravel
    ESTADOS = ["fechado", "cauteloso", "aberto", "vulneravel"]

    def __init__(
        self,
        nome: str,
        idade: int,
        profissao: str,
        descricao: str,
        genero_masculino: bool,
        prato_favorito: str,
        memoria: str
    ):
        """Inicializa o cliente com seus dados e estado inicial."""
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.descricao = descricao
        self.genero_masculino = genero_masculino
        self.prato_favorito = prato_favorito
        self.memoria = memoria
        self.estado = "fechado"
        self.prato_descoberto = False
        self.memoria_revelada = False

    def apresentar(self) -> str:
        """Retorna a descricao visual do cliente ao entrar."""
        return f'{self.descricao}' # o estado atual deve ser inferido da descrição, não implicitamente citado aqui.

    def mudar_estado(self, direcao: int) -> str:
        """
        Muda o estado emocional do cliente.
        direcao: +1 para abrir, -1 para fechar
        Retorna o novo estado.
        """
        indice_atual = self.ESTADOS.index(self.estado)
        novo_indice = max(0, min(len(self.ESTADOS) - 1, indice_atual + direcao))
        self.estado = self.ESTADOS[novo_indice]
        return self.estado

    def esta_aberto(self) -> bool:
        """Verifica se o cliente esta pronto para revelar o prato favorito."""
        return self.estado == self.ESTADOS[2]

    def descobrir_prato(self) -> str:
        """
        Marca o prato como descoberto e retorna o nome.
        So funciona se o cliente estiver "aberto".
        """
        if self.estado == 'aberto' and not self.prato_descoberto:
            self.prato_descoberto = True
            return self.prato_favorito
        return None

    def receber_prato(self, nome_prato: str) -> str:
        """
        Cliente recebe um prato. Se for o favorito, revela a memoria.
        Retorna a memoria ou None.
        """
        if self.prato_descoberto and nome_prato == self.prato_favorito:
            self.estado = self.ESTADOS[3]  # Fica vulneravel
            self.memoria_revelada = True
            return self.memoria
        return None

    def foi_sucesso(self) -> bool:
        """Verifica se a noite foi bem sucedida com este cliente."""
        if self.memoria_revelada:
            return True
        return False


# Testes
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE - CLIENTE")
    print("=" * 50)

    yuki = Cliente(
        nome="Yuki Tanabe",
        idade=28,
        profissao="Fotografa",
        descricao="Uma jovem com camera antiga no pescoco",
        genero_masculino=False,
        prato_favorito="Tamago Gohan",
        memoria="Fotos de um incendio que ela nunca conseguiu olhar"
    )

    # Teste apresentacao
    print(f"\n1. Apresentacao:\n{yuki.apresentar()}")

    # Teste mudanca de estado
    print(f"\n2. Estado inicial: {yuki.estado}")
    yuki.mudar_estado(+1)
    print(f"3. Apos +1: {yuki.estado}")
    yuki.mudar_estado(+1)
    print(f"4. Apos +1: {yuki.estado}")

    # Teste descoberta do prato
    prato = yuki.descobrir_prato()
    print(f"6. Prato: {prato}")

    # Teste receber prato
    memoria = yuki.receber_prato("Tamago Gohan")
    print(f"7. Memoria: {memoria}")

    # Teste sucesso
    print(f"\n8. Sucesso? {yuki.foi_sucesso()}")

    print("\n" + "=" * 50)
