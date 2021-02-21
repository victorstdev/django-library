# django-library
Projeto pra um sistema de biblioteca em Django

## Descrição Básica
#### Funções do sistema
  - Avisar os usuários que possuem atraso de devoluções
#### Funções do bibliotecário (admin)
  - Manter livros
  - Aprovar reservas de livros
#### Funções do leitor (usuário)
  - Cadastro/Login
  - Visualizar lista de livros
  - Solicitar reserva de livro
## Banco de Dados

Leitor  | Tipo
---     | ---
nome    | `string`
senha   | `string`

Livro   | Tipo
---     | ---
nome    | `string`
autor   | `string`
cópias  | `int`

Reserva | Tipo
---     | ---
leitor  | `Leitor`
livro   | `Livro`
data da solicitação | `date`
dias de reserva | `int`
data da reserva | `date`
pedido aprovado | `boolean`
