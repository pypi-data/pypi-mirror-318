# Change Log
Todas as grandes mudanças deste projeto serão documentadas neste arquivo.


## [3.2.1] - 2024-10-23

### Added

### Changed
1. Reestruturação das classes e arquivos.
### Fixed


## [3.2.0] - 2024-10-09

### Added

### Changed
1. Reestruturação das classes e arquivos.
### Fixed


## [3.1.11] - 2024-10-09

### Added

### Changed
1. Reestruturação das classes e arquivos.
### Fixed


## [3.1.7] - 2024-07-25

### Added

### Changed

### Fixed
1. Correção da falha no processamento do campo adicional (comentário) da pergunta de Múltipla Escolha


## [3.1.6] - 2024-07-04

### Added

### Changed

### Fixed
1. Correção de biblioteca na classe TransformUser


## [3.1.5] - 2024-05-20

### Added

### Changed
1. Melhoria no tratamento dos erros HTTP

### Fixed


## [3.1.4] - 2024-05-20

### Added

### Changed
1. Removido biblioteca psycopg2 sem utilização.

### Fixed


## [3.1.3] - 2024-04-30

### Added

### Changed

### Fixed
1. Tratamento de resposta com campo adicional (comentário)


## [3.1.2] - 2024-04-30

### Added

### Changed

### Fixed
1. Tratamento correto para lista de dicionários (campos de CPF, Telefone, etc...)


## [3.1.1] - 2024-04-29

### Added

### Changed
1. Mudança na lógica do processamento de dados (classe DataProcessing), tornando-a mais eficiente e rápida.

### Fixed


## [3.1.0] - 2024-04-29

### Added
1. Adicionado classes de tratamento dos dados

### Changed

### Fixed


## [3.0.0] - 2024-04-25

### Added

### Changed
1. Mudança da build e manutenção do pacote para o Poetry

### Fixed


## [2.0.6] - 2024-03-13

### Added

### Changed

### Fixed
1. Ordem da lógica de chamada da API para utilizar os safeguards.


## [2.0.5] - 2024-03-13

### Added

### Changed
1. Correção estrutura de try except de erros HTTPs.

### Fixed


## [2.0.4] - 2024-03-13

### Added
1. Inclusão de tratamento de erros HTTPs.

### Changed

### Fixed


## [2.0.3] - 2024-03-07

### Added
1. Inclusão de separador "__" para valores aninhados no json.

### Changed
1. Remoção da etapa para renomear as colunas do dataframe final, substituindo "." por "__" quando houver.

### Fixed


## [2.0.2] - 2024-03-06

### Added
1. Inclusão de etapa para renomear as colunas do dataframe final, substituindo "." por "__" quando houver.

### Changed

### Fixed


## [2.0.1] - 2024-02-28

### Added
1. Inclusão de contador de tempo de execução do processamento dos dados

### Changed
1. Alterado a estrutura da classe DataProcessing para otimização dos processos/tempo de execução.

### Fixed


## [2.0.0] - 2024-02-22

### Added
1. Classe DataProcessing.
   * Ela é responsável pelo tratamento dos dados, devendo receber uma lista como parâmetro de entrada.

### Changed
1. A classe GetEvaluations agora é responsável somente por receber os dados da API e armazena-los em uma lista.
2. O nome do script foi alterado para "api_evaluations.py" para melhor descrição.

### Fixed


## [1.1.17] - 2024-01-24

### Added
1. Validação de período máximo permitido (31 dias) entre a data de início e a data de término do request.
   * Essa validação se faz necessária para evitar sobrecarregamento da API.

### Changed

### Fixed


## [1.1.16] - 2024-01-22

### Added
1. Classe GetSuspiciousOccurrences.
   * Ela é responsável pelo retorno das ocorrências suspeitas.

### Changed
1. As funções equivalentes foram retiradas da classe GetQuestionnaire e transformadas em uma classe própria.

### Fixed


## [1.1.15] - 2024-01-22

### Added
1. Inclusão de novas funções para retornar as ocorrências suspeitas.

### Changed

### Fixed


## [1.1.10] - 2024-01-22

### Added
1. Classe GetQuestionnaire.
* Ela é responsável pelo retorno do número da versão do questionário de uma determinada pesquisa.

### Changed

### Fixed
