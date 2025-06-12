import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, roc_curve, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

print("--- Parte 1: Preparação do Ambiente e Geração de Dados ---")

 # Gerar um dataset de classificação binária com 1000 amostras, 20 features e classes desbalanceadas
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10,
                           n_redundant=10, n_classes=2, random_state=42, weights=[0.9, 0.1])

print(f"Formato dos dados (X): {X.shape}")
print(f"Formato dos rótulos (y): {y.shape}")
print(f"Contagem de classes (0s e 1s): {np.bincount(y)}")
print(f"Proporção da classe minoritária: {np.bincount(y)[1] / len(y):.2f}")

# 1.2 Divisão dos Dados em Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print(f"\nFormato dos dados de treino (X_train): {X_train.shape}")
print(f"Formato dos dados de teste (X_test): {X_test.shape}")
print(f"Contagem de classes no treino: {np.bincount(y_train)}")
print(f"Contagem de classes no teste: {np.bincount(y_test)}")

print("\n--- Parte 2: Treinamento do Modelo de Classificação ---")

# 2.1 Inicializar e Treinar o Modelo
model = LogisticRegression(solver='liblinear', random_state=42) # 'liblinear' é bom para datasets menores
model.fit(X_train, y_train)

print("Modelo de Regressão Logística treinado com sucesso.")
print("\n--- Parte 2: Treinamento do Modelo de Classificação ---")

# 2.1 Inicializar e Treinar o Modelo
model = LogisticRegression(solver='liblinear', random_state=42) # 'liblinear' é bom para datasets menores
model.fit(X_train, y_train)

print("Modelo de Regressão Logística treinado com sucesso.")

print("\n--- Parte 3: Realização de Previsões e Cálculo de Métricas ---")

# 3.1 Previsões no Conjunto de Teste
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1] # Probabilidades da classe positiva (classe 1)

print("Previsões realizadas no conjunto de teste.")

# 3.2 Matriz de Confusão
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nMatriz de Confusão:")
print(conf_matrix)

# Exibição da Matriz de Confusão (opcional, para melhor visualização)
plt.figure(figsize=(6, 5))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Previsto 0', 'Previsto 1'], yticklabels=['Real 0', 'Real 1'])
plt.xlabel('Previsão')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()


# 3.3 Cálculo das Métricas

# Precisão (Precision)
# TP / (TP + FP) - Proporção de verdadeiros positivos entre todas as previsões positivas
precision = precision_score(y_test, y_pred)
print(f"\nPrecisão (Precision): {precision:.4f}")

# Recall (Sensibilidade ou Cobertura)
# TP / (TP + FN) - Proporção de verdadeiros positivos entre todas as amostras reais positivas
recall = recall_score(y_test, y_pred)
print(f"Recall (Sensibilidade): {recall:.4f}")

# F1-Score
# Média harmônica entre Precisão e Recall - Bom para classes desbalanceadas
f1 = f1_score(y_test, y_pred)
print(f"F1-Score: {f1:.4f}")

 
# Requer as probabilidades da classe positiva
roc_auc = roc_auc_score(y_test, y_prob)
print(f"AUC-ROC: {roc_auc:.4f}")


print("\n--- Parte 4: Visualização da Curva ROC ---")

# Cálculo da curva ROC
fpr, tpr, thresholds = roc_curve(y_test, y_prob)

# Plotagem da curva ROC
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Curva ROC (AUC = {roc_auc:.4f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Classificador Aleatório')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Taxa de Falsos Positivos (FPR)')
plt.ylabel('Taxa de Verdadeiros Positivos (TPR - Recall)')
plt.title('Curva ROC')
plt.legend(loc="lower right")
plt.grid(True)
plt.show()

print("\nAnálise das Métricas:")
print("A Precisão, Recall e F1-Score fornecem uma visão do desempenho do modelo em relação à classe positiva.")
print("A AUC-ROC oferece uma medida agregada da capacidade discriminatória do modelo em diferentes limiares.")
print("Em datasets desbalanceados, Recall e F1-Score são frequentemente mais informativos que a Precisão ou a Acurácia (que não foi calculada explicitamente aqui, mas pode ser inferida).")
print("Um modelo com alta AUC-ROC é capaz de separar bem as classes, mesmo que o limiar padrão de 0.5 não resulte nas melhores métricas de precisão/recall.")