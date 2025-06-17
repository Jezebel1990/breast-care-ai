# Análise de Dados sobre Câncer de Mama com IA

 > Este projeto demonstra o uso de Machine Learning (Random Forest) para análise de dados relacionados ao diagnóstico de câncer de mama, com backend em Python (Flask) e frontend simples em HTML, CSS e JavaScript.

 ##  Objetivo
Visualizar de forma interativa as principais métricas de avaliação de um modelo de classificação binária (Benigno x Maligno), com foco em conscientização, educação e interpretação de resultados de IA na saúde.

##  Tecnologias Utilizadas
Backend:
- Python 3
- Flask (servidor web)
- Scikit-learn (treinamento e avaliação do modelo)
- Matplotlib e Seaborn (geração dos gráficos)

Frontend:
- HTML5
- CSS3
- JavaScript (Fetch API)
- Gráficos estáticos em PNG

##  Funcionalidades
✅ Treinamento de um RandomForestClassifier com o dataset de câncer de mama (sklearn)
✅ Geração automática de 4 gráficos de avaliação:
- Curva ROC (AUC-ROC)
- Precisão (TP vs FP)
- Recall/Sensibilidade (TP vs FN)
- F1-Score (Precisão vs Recall)

✅ API REST em /api/resultados que entrega as métricas em JSON
✅ Frontend dinâmico consumindo os dados da API e exibindo os gráficos com interpretação em linguagem simples.

## Exemplo de Resposta da API
```json
{
  "precision": 0.92,
  "recall": 0.89,
  "f1_score": 0.90,
  "auc_roc": 0.95
}
```


 ## Como Executar Localmente
1. Crie e ative um ambiente virtual (venv):

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / MacOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

 2. Instale as dependências Python:
```bash 
  pip install -r requirements.txt
```

3. Execute a aplicação Flask:

```bash
python app.py
```

4. Acesse no navegador:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

## Sobre o Dataset
O projeto utiliza o Wisconsin Breast Cancer Dataset, disponível diretamente na biblioteca scikit-learn, sem uso de dados pessoais ou sensíveis.


## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.

Feito com ♥ por [Jezebel Guedes](https://www.linkedin.com/in/jezebel-guedes/) 👋 Entre em contato!

--- 
## ⚠️ Disclaimer
🔔 Este projeto é apenas para fins educacionais e de conscientização. Não deve ser usado para diagnósticos médicos reais.
