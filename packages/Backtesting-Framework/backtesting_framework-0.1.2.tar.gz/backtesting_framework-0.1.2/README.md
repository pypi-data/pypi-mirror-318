# Framework de Backtesting de Stratégies d’Investissement

## Overview

Ce dépôt contient un framework de backtesting conçu pour tester, analyser et comparer différentes stratégies d’investissement sur des données historiques. Il est flexible, extensible, et adapté à divers types d'actifs financiers tels que les actions, les crypto-monnaies ou autres instruments financiers.

---

## Fonctionnalités principales

- **Gestion des données** :
  - Prise en charge des fichiers CSV et Parquet, ou directement des `DataFrame` pandas.
  - Compatible avec des sources de données externes telles que `yfinance` ou `pandas-datareader`.
  - Données indexées par des dates avec prise en charge de colonnes personnalisées (e.g., `Close`, `Open`, indicateurs financiers).

- **Stratégies d’investissement** :
  - Définition des stratégies via une classe abstraite ou des décorateurs pour une flexibilité maximale.
  - Stratégies prédéfinies incluses : Moyenne Mobile, Quality, Value, MinVariance, PairsTrading, etc.
  - Support pour des stratégies mono-actif ou multi-actifs.

- **Backtesting performant** :
  - Gestion des coûts de transaction, slippage, et ajustements basés sur la volatilité cible.
  - Options de rebalancement flexibles : journalier, hebdomadaire, mensuel, etc.

- **Analyse des résultats** :
  - Statistiques détaillées : rendement total, ratio de Sharpe, drawdown maximum, VaR, etc.
  - Comparaison des performances entre plusieurs stratégies.

- **Visualisation avancée** :
  - Graphiques interactifs avec `matplotlib`, `seaborn` ou `plotly` :
    - Rendements cumulés.
    - Heatmaps des rendements mensuels.
    - Distribution des rendements quotidiens.

---

## Installation

Installez le framework directement depuis PyPI :

```bash
pip install Backtesting-Framework
```
Les dépendances sont gérées via pyproject.toml.

---

## Structure

```plaintext
Backtesting-Framework/ 
├── backtesting_framework/ 
├── Core/ # Composants principaux du framework. 
│ ├── init.py # Initialisation du module Core. 
│ ├── app.py # Gestionnaire principal de l'application. 
│ ├── Backtester.py # Composant central pour exécuter les backtests. 
│ ├── Calendar.py # Gestion des calendriers de trading et des dates. 
│ ├── Main.py # Point d'entrée pour l'exécution du framework. 
│ ├── Result.py # Classe pour gérer et analyser les résultats du backtest. 
│ └── Strategy.py # Classe abstraite définissant la structure des stratégies. 
├── Strategies/ # Implémentations des stratégies prédéfinies. 
│ ├── Utils/ # Fonctions utilitaires pour le traitement des données et autres. 
│ │ ├── init.py # Initialisation du module Utils. 
│ │ └── Tools.py # Fonctions utilitaires spécifiques. 
│ └── init.py # Fichier d'initialisation du module principal. 
├── Datasets/ # Données d'exemple utilisées pour les tests et le développement. 
├── tests/ # Tests unitaires pour valider le fonctionnement du framework. 
│ ├── init.py # Initialisation du module de tests. 
│ └── test_backtester.py # Tests pour le composant Backtester. 
├── Framework de Backtesting de Stratégies d’Investissement.ipynb # Jupyter Notebook de démonstration du framework. 
├── pyproject.toml # Configuration du projet et gestion des dépendances avec Poetry. 
├── README.md # Documentation du projet (vous y êtes).
```
---

## Utilisation

Le fichier Jupyter Notebook `Framework de Backtesting de Stratégies d’Investissement.ipynb` agit comme un guide utilisateur complet. Il présente les principales classes du framework, leurs arguments et leur fonctionnement. Vous y trouverez des exemples concrets pour la gestion des données, la création et l'exécution de stratégies, ainsi que l'analyse et la visualisation des résultats. Ce notebook est un excellent point de départ pour comprendre comment utiliser efficacement le framework et pour expérimenter avec vos propres stratégies d'investissement.


---

## Auteurs

- **Nassim BOUSSAID**
- **Nicolas COUTURAUD**
- **Kartty MOUROUGAYA**
- **Hugo SOULIER**

Sous la supervision de **M. Rémi Genet**.

---

## Licence

Ce projet est sous licence MIT.