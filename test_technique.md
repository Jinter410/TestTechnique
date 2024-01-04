# Test technique Python Selenium

Ce test technique consiste à évaluer les capacités du candidat à créer une "API" qui accepte des instructions codées en JSON pour exécuter des actions via Selenium. L'API doit être capable de prendre des captures d'écran, de naviguer sur une page web, de cliquer sur des éléments et d'exécuter de courts scripts JavaScript. L'installation d'un plugin pour supprimer les pop-ups de cookies sera considérée comme un bonus.

Nous vous fournissons un exemple du format JSON standard que l'API doit prendre en entrée.

## Format JSON des Instructions

```json
{
  "actions": [
    {
      "type": "navigate",
      "url": "https://example.com"
    },
    {
      "type": "click",
      "selector": "#buttonId" // css selector could be div.<class_name> -> div.login_link
    },
    {
      "type": "execute_script",
      "script": "return document.title;"
    },
    {
      "type": "screenshot",
      "filename": "screenshot.png"
    },
    {
      "type": "install_plugin",
      "plugin_name": "cookie_popup_blocker" // download in local and install it from selenium
    }
  ]
}
```

## Exigences du Test Technique

1.  Créer une classe API Python qui interagit avec Selenium.
2.  L'API doit lire le fichier JSON avec les instructions et les exécuter séquentiellement.
3.  Il faut intégrer des méthodes pour naviguer sur une page, cliquer sur des éléments, exécuter des scripts JavaScript et prendre des captures d'écran en format PNG.
4.  Les temps d'attentes de chargement des pages ne doivent pas être hard-codés
5.  (Bonus) Ajouter la fonctionnalité d'installer un plugin pour bloquer les pop-ups de cookies.
6.  Suivre les bonnes pratiques de développement Python: code clair, orienté objet, documentation docstrings, et tests unitaires.
7.  Le code doit être publié sur github et le lien envoyer a l'adresse t.perrin@digitalkin.ai une fois le test terminé.

Le test doit être réalisé en deux heures, de sorte que le candidat ne doit pas développer la totalité de l'API mais doit montrer sa capacité à concevoir et coder rapidement des parties cruciales en se concentrant sur les bonnes pratiques de développement.
L'API doit tout de même être executable, ainsi un membre de DigitalKin pourra tester le code avec un fichier d'instruction JSON, ce qui permettra d'évaluer les fonctionnalitées réalisées.

