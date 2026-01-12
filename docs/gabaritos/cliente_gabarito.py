"""
GABARITO - Cliente
NAO MOSTRAR AO APRENDIZ

Este arquivo contem a implementacao completa esperada.
Usar como referencia para guiar o aprendiz.
"""


class Cliente:
    """Representa um cliente que visita o restaurante."""

    # Estados possiveis de abertura emocional
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
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.descricao = descricao
        self.genero_masculino = genero_masculino
        self.prato_favorito = prato_favorito
        self.memoria = memoria

        # Estado inicial
        self.estado = "fechado"
        self.prato_descoberto = False
        self.memoria_revelada = False

    def apresentar(self) -> str:
        """Retorna a descricao visual do cliente ao entrar."""
        pronome = "Ele" if self.genero_masculino else "Ela"
        return f"{self.descricao} entra no restaurante.\n{pronome} parece {self.estado}."

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

    def esta_vulneravel(self) -> bool:
        """Verifica se o cliente esta pronto para revelar o prato favorito."""
        return self.estado == "vulneravel"

    def descobrir_prato(self) -> str:
        """
        Marca o prato como descoberto e retorna o nome.
        So funciona se o cliente estiver vulneravel.
        """
        if self.esta_vulneravel() and not self.prato_descoberto:
            self.prato_descoberto = True
            return self.prato_favorito
        return None

    def receber_prato(self, nome_prato: str) -> str:
        """
        Cliente recebe um prato. Se for o favorito, revela a memoria.
        Retorna a reacao do cliente.
        """
        if nome_prato == self.prato_favorito and self.prato_descoberto:
            self.memoria_revelada = True
            return self.memoria
        return None

    def foi_sucesso(self) -> bool:
        """Verifica se a noite foi bem sucedida com este cliente."""
        return self.memoria_revelada


# Testes
if __name__ == "__main__":
    print("=" * 50)
    print("TESTE DO GABARITO - CLIENTE")
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

    print(f"\n1. Apresentacao:\n{yuki.apresentar()}")

    print(f"\n2. Estado inicial: {yuki.estado}")

    yuki.mudar_estado(+1)
    print(f"3. Apos abrir: {yuki.estado}")

    yuki.mudar_estado(+1)
    yuki.mudar_estado(+1)
    print(f"4. Apos abrir mais: {yuki.estado}")

    print(f"5. Esta vulneravel? {yuki.esta_vulneravel()}")

    prato = yuki.descobrir_prato()
    print(f"6. Prato descoberto: {prato}")

    memoria = yuki.receber_prato("Tamago Gohan")
    print(f"7. Memoria revelada: {memoria}")

    print(f"8. Foi sucesso? {yuki.foi_sucesso()}")

    print("\n" + "=" * 50)
