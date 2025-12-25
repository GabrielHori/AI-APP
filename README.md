🤖 Horizon IA App

Application desktop permettant d’installer, gérer et lancer des IA locales automatiquement, en fonction de la configuration matérielle de l’utilisateur.

L’objectif est de rendre l’IA locale accessible, simple et propre, sans bidouilles ni lignes de commande complexes.

✨ Objectifs du projet

Simplifier l’installation d’IA locales (LLM, modèles Ollama, etc.)

Adapter automatiquement les modèles à la configuration du PC

Offrir une interface claire, moderne et épurée

Centraliser la gestion des IA dans une seule application

Fonctionner 100% en local (privacy by design)

🚀 Fonctionnalités (v1)

🖥️ Détection automatique de la configuration matérielle
(CPU, RAM, GPU, VRAM)

🤖 Sélection intelligente des modèles IA compatibles

📦 Installation guidée des modèles (via Ollama)

💬 Interface de chat pour interagir avec les IA locales

🧭 Dashboard simple pour gérer les modèles installés

🧠 Backend stable et extensible (préparé pour la v2)

🎨 Design & UX

Design sobre, propre et épuré

Esthétique Liquid Metal / glassy / minimal

Focus sur la lisibilité, la fluidité et l’expérience utilisateur

UI pensée comme un outil pro, pas une démo

🛠️ Technologies utilisées
Backend

Python

FastAPI – API rapide et robuste

Uvicorn – Serveur ASGI

Ollama – Gestion des modèles IA locaux

Frontend

React

Vite

Tailwind CSS

Architecture modulaire et maintenable

Desktop

Electron

Communication frontend ↔ backend en local

📁 Structure du projet (Frontend)
```bash
frontend/
├── public/
│   └── vite.svg
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── AIChatPanel.jsx
│   │   ├── MainPanel.jsx
│   │   ├── Sidebar.jsx
│   │   └── TopBar.jsx
│   ├── layouts/
│   │   └── AppLayout.jsx
│   ├── pages/
│   │   └── Dashboard.jsx
│   ├── App.jsx
│   ├── main.jsx
│   ├── index.css
│   └── App.css
├── index.html
├── package.json
├── vite.config.mjs
├── tailwind.config.js
└── README.md
```

```bash
🧩 Architecture globale
Electron (Desktop App)
        │
        ▼
Frontend (React + Vite)
        │
        ▼
Backend (FastAPI)
        │
        ▼
Ollama / IA locales
```

🔒 Philosophie

🔐 Respect de la vie privée (aucun cloud imposé)

⚡ Performance locale

🧠 IA accessible sans expertise technique

🧱 Base solide pour évolutions futures (plugins, profils, marketplace IA…)

🛣️ Roadmap (v2 – à venir)

Profils utilisateurs

Gestion avancée des ressources

Téléchargement automatique de modèles recommandés

Presets par usage (dev, créatif, rédaction, etc.)

Plugins & extensions

Monitoring des performances IA

👤 Auteur

Gabriel (Horizon)
Développeur & créateur du projet Horizon
Projet personnel orienté IA locale, UX et outils intelligents
