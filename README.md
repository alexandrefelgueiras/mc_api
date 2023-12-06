# API Margem Certa!

## Índice

- [Sobre](#sobre)
- [Instalação](#instalação)
- [Uso](#uso)
- [Endpoints](#endpoints)
- [Exemplos](#exemplos)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Sobre

Esta API destina-se a uma aplicação que calcula a Margem de Contribuição de itens de comercializados por uma empresa.
A margem de contribuição é um conceito financeiro que representa a diferença entre as receitas totais obtidas com a venda de produtos ou serviços e os custos variáveis associados à produção ou prestação desses produtos ou serviços. Em outras palavras, é o valor que contribui para cobrir os custos fixos e, eventualmente, gerar lucro.

A fórmula básica da margem de contribuição é:

$$\ Margem de Contribuição = Receitas Totais - Custos Varriáveis Totais$$

Onde:

**Receitas Totais** são as vendas totais geradas pela empresa.
**Custos Variáveis Totais** são os custos diretamente associados à produção ou prestação de serviços, que variam de acordo com o volume de produção ou vendas.

A margem de contribuição é uma métrica importante para as empresas, pois fornece informações sobre quanto dinheiro está disponível para cobrir os custos fixos (como aluguel, salários, utilidades) e contribuir para o lucro após a cobertura desses custos. Se a margem de contribuição for negativa, significa que as receitas não são suficientes para cobrir os custos variáveis, e a empresa pode estar operando com prejuízo.

É importante ressaltar que a margem de contribuição não leva em consideração os custos fixos, como despesas administrativas e depreciação. Portanto, embora a margem de contribuição forneça informações sobre a rentabilidade operacional, outras análises, como a margem de lucro líquido, são necessárias para avaliar a lucratividade global da empresa.

Esta é uma versão simplificada dados sao inseridos como parâmetros de entrada como:

 1. Nome do Cliente;
 2. Descrição do item comercializado;
 3. Número da Proposta Comercial;
 4. Número do Item da Proposta;
 5. Preço total;
 6. Custo total.

 7. Campo calculado: Margem de Contribuição Absoluta ($Margem_{abs}$):
	 $$\ Margem_{abs} = Preço_{total} - Custo_{total}$$
	 
 8. Campo calculado: Margem de Contribuição Relativa ($Margem_{rel}$):
	 $$Margem_{rel} =\left(\frac{Margem_{abs}}{Preço_{total}}\right)\times 100$$

 Versões futuras desta aplicação irão implementar cálculos de compensação de impostos, se aplicável, e adição de outros custos variáveis como comissões de venda.
 Este produto destina-se a ser uma ferramenta muito simples e prática que ajude empresas na precificação de produtos e garantindo mais lucro e reduzindo riscos.

 ## Instalação

### Baixe os arquivos da API necessários do repositório no gitHub




### Criaçao e Instalaçao de Ambientes Virtuais

A criação de um ambiente virtual no Windows e em sistemas Linux/macOS (OS X) envolve etapas um pouco diferentes. Vomos fornecer instruções passo a passo para ambos os sistemas operacionais:

- [Windows](#windows)
- [Linux/macOS (OS X)](#linux/macos (os x))

#### Windows:

1. Instale o Python:

Se você ainda não tem o Python instalado, faça o download e instale a versão mais recente do Python a partir do site oficial do Python.

2. Abra o PowerShell:

Abra o PowerShell como administrador. Você pode fazer isso clicando com o botão direito no ícone do PowerShell e escolhendo "Executar como administrador". 

3. Instale o virtualenv:

```powershell```
``` 
pip install virtualenv
```

4. Navegue até o diretório do seu projeto

Use o comando 'cd' para navegar até o diretório do seu projeto.

5. Crie um ambiente virtual

```powershell```
``` 
python -m venv venv
```
6. Ative o amviente virtual:


```powershell```
``` 
venv\scripts\activate
```
#### Linux/macOS (OS X)

1. Abra um terminal:

Abra um terminal no seu sistema.

2. Instale o Python:

Muitos sistemas Linux/macOS já têm o Python instalado. Caso não tenha, você pode instalá-lo usando o gerenciador de pacotes do seu sistema.

No Ubuntu, por exemplo:

```bash```
```
sudo apt-get update
sudo apt-get install python3
```
3. Instale o virtualenv:

```bash```
```
pip install virtualenv
```

4. Navegue até o diretório do seu projeto:

Use o comando cd para navegar até o diretório do seu projeto.

5. Crie um ambiente virtual:

```bash```
```
python3 -m venv venv
```
6. Ative o ambiente virtual:

```bash```
```
source .venv/bin/activate
```
### Instalaçao das bibliotecas


 ## Uso

 ## Endpoints

 ## Exemplos

 ## Contribuiçao

 ## Licença

