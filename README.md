# Física 3 Experimental - Engenharia Mecânica

Este repositório contém os experimentos práticos realizados na disciplina de Física 3 Experimental do curso de Engenharia Mecânica do IPRJ-UERJ. Os experimentos abordam conceitos fundamentais de eletromagnetismo através de análises teóricas e experimentais implementadas em Jupyter Notebooks.

## 📋 Estrutura do Repositório

- `exp1.ipynb` - Campo Elétrico e Potencial Elétrico
- `exp2.ipynb` - Resistência Elétrica e Lei de Ohm
- `exp3.ipynb` - Galvanômetros (Voltímetro e Amperímetro)
- `exp4.ipynb` - Ponte de Wheatstone
- `exp5.ipynb` - Capacitores e Circuitos RC
- `exp6.ipynb` - Lei de Ampère e Campo Magnético

## 🔬 Experimentos Realizados

### Experimento 1: Campo Elétrico e Potencial Elétrico

**Arquivo:** `exp1.ipynb`

**Objetivos:**

- Estudo de linhas equipotenciais
- Análise do campo elétrico através do potencial
- Ajuste de modelos logarítmicos para dados experimentais

**Principais Conceitos:**

- Potencial elétrico
- Linhas equipotenciais
- Relação entre campo elétrico e potencial

### Experimento 2: Resistência Elétrica e Lei de Ohm

**Arquivo:** `exp2.ipynb`

**Objetivos:**

- Estudo da resistência elétrica em função do comprimento do condutor
- Análise de circuitos série e paralelo
- Determinação da resistividade do material

**Principais Análises:**

- Resistência vs. número de espiras
- Resistência vs. comprimento do condutor
- Características V-I de diferentes configurações de resistores
- Cálculo da resistividade do material: `ρ = (a*d²)/(4*D)`

### Experimento 3: Galvanômetros

**Arquivo:** `exp3.ipynb`

**Objetivos:**

- Construção de voltímetros e amperímetros a partir de galvanômetros
- Cálculo de resistências série e paralelo para diferentes escalas
- Análise de precisão dos instrumentos construídos

**Principais Conceitos:**

- Funcionamento de galvanômetros
- Conversão para voltímetros (resistência série)
- Conversão para amperímetros (resistência paralelo)

### Experimento 4: Ponte de Wheatstone

**Arquivo:** `exp4.ipynb`

**Objetivos:**

- Análise de circuitos em ponte
- Comparação entre soluções analíticas e método nodal
- Estudo da sensibilidade da ponte

**Métodos Implementados:**

- **Solução Analítica:** Fórmula direta para Va
- **Método Nodal:** Resolução por sistema linear usando numpy
- Análise de correlação (R²) entre métodos

### Experimento 5: Capacitores e Circuitos RC

**Arquivo:** `exp5.ipynb`

**Objetivos:**

- Estudo do comportamento de capacitores em circuitos RC
- Análise de processos de carga e descarga
- Determinação da constante de tempo τ = RC

**Principais Análises:**

- Curvas de carga: `V(t) = V₀(1 - e^(-t/τ))`
- Curvas de descarga: `V(t) = V₀e^(-t/τ)`
- Ajuste exponencial de dados experimentais

### Experimento 6: Lei de Ampère e Campo Magnético

**Arquivo:** `exp6.ipynb`

**Objetivos:**

- Estudo da Lei de Ampère
- Análise do campo magnético em função da distância
- Verificação experimental da Lei de Faraday

**Principais Conceitos:**

- Campo magnético variável
- Lei de Ampère
- Indução eletromagnética

## 🛠️ Ferramentas e Bibliotecas Utilizadas

### Bibliotecas Python

- **NumPy**: Cálculos numéricos e arrays
- **Matplotlib**: Visualização de dados e gráficos
- **SciPy**: Ajuste de curvas e análise estatística
- **Pandas**: Manipulação e análise de dados

### Principais Funcionalidades

- Regressão linear e não-linear
- Ajuste de curvas exponenciais e logarítmicas
- Análise de correlação (R²)
- Resolução de sistemas lineares
- Visualização de dados experimentais

## 📊 Metodologia de Análise

### 1. Coleta de Dados

- Medições experimentais em laboratório
- Registro de incertezas e condições experimentais

### 2. Processamento de Dados

- Limpeza e organização dos dados
- Conversão de unidades quando necessário
- Cálculo de grandezas derivadas

### 3. Análise Estatística

- Ajuste de modelos teóricos aos dados experimentais
- Cálculo de coeficientes de correlação
- Estimativa de parâmetros e suas incertezas

### 4. Visualização

- Gráficos comparativos entre teoria e experimento
- Representação de ajustes lineares e não-lineares
- Análise de resíduos

## 👨‍🎓 Sobre

Este trabalho foi desenvolvido como parte dos estudos na disciplina de Física 3 Experimental do curso de Engenharia Mecânica.