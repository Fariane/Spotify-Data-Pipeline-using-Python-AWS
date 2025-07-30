#  🎵 Spotify Data Pipeline avec Python & AWS

## Présentation
Ce projet consiste à créer un pipeline ETL (Extract, Transform, Load) en utilisant les services AWS. Il récupère automatiquement des données depuis l’API Spotify, les transforme, puis les charge dans AWS pour analyse.
L’objectif est d’automatiser tout le processus afin de disposer chaque jour de données à jour sur des playlists Spotify, organisées proprement dans des tables (artistes, albums, songs) pour permettre des analyses plus poussées.

## Architecture
![Architecture Diagram](spotify_pipeline_architecture_dgrm.png)

Spotify API → AWS Lambda (Extraction) → Amazon S3 (Données brutes) ↑ CloudWatch (Déclencheur quotidien)

Amazon S3 (Données brutes) → AWS Lambda (Transformation) → Amazon S3 (Données transformées) ↑ Déclencheur via ajout d’objet

S3 (Données transformées) → AWS  Glue Crawler → Glue Data Catalog → Amazon Athena (requêtes SQL)


## Composants principaux

### Data Extraction
- **Spotify API :** Utilisée pour récupérer des données musicales : artistes, albums et songs.
- **Authentification :** Intégration du protocole OAuth 2.0 pour sécuriser l’accès aux endpoints de l’API.
- **Planification :** Un job CloudWatch lance la fonction Lambda tous les jours pour aller chercher les nouvelles données.
  
### Data Transformation
- **Nettoyage :** Traitement des valeurs manquantes, doublons, et incohérences dans les données brutes.
- **Structuration :**  Formatage des données en JSON ou CSV pour les rendre exploitables par les outils d’analyse.
- **Enrichissement :** Ajout d’attributs supplémentaires ou agrégation de données pour enrichir les analyses

### Data Loading
- **Amazon S3 :** Toutes les données (brutes & transformées) sont stockées ici.
- **AWS Glue:** Utilisé pour détecter automatiquement les schémas et créer un catalogue de données exploitable.
- **AWS Athena:** Permet d’exécuter des requêtes SQL directement sur les fichiers présents dans S3, sans base de données dédiée.
- **Partitionnement :** Organisation des données par date ou catégorie pour optimiser les performances des requêtes.

## Déroulement du pipeline
1. **Extraction des données :** Une fonction AWS Lambda est déclenchée quotidiennement via Amazon CloudWatch pour extraire les données de l’API Spotify. Les données brutes sont stockées dans Amazon S3.

2. **Transformation des données :** Une deuxième fonction Lambda s’exécute automatiquement lorsqu’un nouveau fichier est ajouté dans S3. Elle transforme les données et les enregistre dans un autre bucket S3.

3. **Catalogage des données :** AWS Glue Crawler détecte les schémas des fichiers transformés et met à jour le Glue Data Catalog.

4. **Analyse :** Amazon Athena permet d’interroger les données via SQL directement sur S3.


## Stack technique

### Programming Languages :
- **Python**  pour les interactions API et les scripts ETL

### Services AWS :
- **AWS Lambda :** pour tout automatiser (extraction + transformation)
- **Amazon CloudWatch :** pour planifier les exécutions
- **Amazon S3 :** pour stocker les données (brutes et transformées)
- **AWS Glue :** pour inférer les schémas et générer le catalogue
- **Amazon Athena:** pour l’analyse des données avec SQL

### Libraries:
- `spotipy` pour communiquer avec l’API Spotify, 
- `pandas` pour la manipulation des données,
- `boto3` pour interagir avec les services AWS.

## Avantages
- **Automatisation :** Le pipeline ETL automatise l’ensemble du processus, garantissant une mise à jour régulière des données sans intervention manuelle.
- **Scalabilité :** L’infrastructure AWS permet de gérer efficacement de grands volumes de données.
- **Flexibilité :** L’architecture modulaire facilite l’intégration d’autres sources de données ou d’outils analytiques.

## Améliorations futures
- **Dashboards interactifs :** Création de dashboards dynamiques avec des outils de data visualisation comme Tableau ou Power BI.
- **Advanced Analytics :** Intégration de modèles de machine learning pour prédire la popularité d’un song ou identifier des tendances musicales.
- **Streaming en temps réel :** Évolution vers une architecture de streaming pour traiter les données Spotify en direct.
