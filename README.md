<h1 align="center">Bienvenue sur le readme de SoftDesk 👋</h1>
<p align="center">
  <a href="https://twitter.com/LaurentJouron">
    <img alt="Twitter: LaurentJouron" 
      src="https://img.shields.io/twitter/follow/LaurentJouron.svg?style=social" target="_blank" />
  </a>
  <a href="https://github.com/LaurentJouron">
    <img alt="GitHub followers" 
      src="https://img.shields.io/github/followers/LaurentJouron?style=social" />
  </a>
</p>

<p align="center">
    <img align="left"
      width="50px" 
      src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToscdusMNjQbffwasgiLuCsbCNZisJRE95Fg&usqp=CAU" />
</p>

### `--- Explication en français ---`

---

Cet exercice a été réalisé dans le cadre d'une formation

Version 0.0.01

---

<h1 align="center">But de l'application</h1>

<h3> Développement d'une Application de Suivi de Problèmes avec SoftDesk.</h3>

La société SoftDesk, spécialisée dans l'édition de logiciels de développement et de collaboration, a entrepris la création d'une application de suivi de problèmes destinée aux entreprises clientes (B2B). Cette application, disponible sur le web, Android et iOS, permet aux utilisateurs de gérer des projets, résoudre des problèmes techniques et suivre leur progression. Vous avez été embauché en tant qu'ingénieur logiciel backend pour créer un backend performant et sécurisé pour cette application.

---

<h1 align="center">Langages et outils</h1>

<table>
  <tr>
    <td align="center">
      <a href="https://www.python.org/">
        <img width="130px"
          src="https://img.shields.io/badge/Python-yellow" /><br />
        <sub><b>Doc Python</b></sub></a><br />
      <a href="https://www.python.org/" title="Téléchargez Python" ></a> 
    </td>
    <td align="center">
      <a href="https://www.djangoproject.com/">
        <img width="130px"
          src="https://img.shields.io/badge/Django-vert" /><br />
        <sub><b>Doc Django</b></sub></a><br />
      <a href="https://www.djangoproject.com/" title="Doc Django"></a> 
    </td>
    <td align="center">
      <a href="https://www.django-rest-framework.org/">
        <img width="350px"
          src="https://img.shields.io/badge/DjangoRESTframework-red"/><br />
        <sub><b>Doc Django REST framework</b></sub></a><br />
      <a href="https://www.django-rest-framework.org/" title="Doc Django REST framework"></a> 
    </td>
  </tr>
</table>

<table>
  <tr>
    <td align="center">
      <a href="https://visualstudio.microsoft.com/fr/">
        <img width="120px"
          src="https://img.shields.io/badge/VSCode-blue"/><br />
        <sub><b>Visuable Studio Code</b></sub></a><br />
      <a href="https://visualstudio.microsoft.com/fr/" title="Visuable Studio Code"></a>
    </td>
    <td align="center">
      <a href="https://www.postman.com/api-documentation-tool/">
        <img width="130px" src="https://img.shields.io/badge/Postman-orange"/><br />
        <sub><b>Postman</b></sub></a><br />
      <a href="https://www.postman.com/api-documentation-tool/" title="Postman"></a>
    </td>
    <td align="center">
      <a href="https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html#">
        <img width="160px"
          src="https://img.shields.io/badge/SimpleJWT-blue"/><br/>
        <sub><b>Simple JWT</b></sub></a><br />
      <a href="https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html#" title="Simple JWT"></a>
    </td>
    <td align="center">
      <a href="https://pipenv.pypa.io/en/latest/">
        <img width="110px"
          src="https://img.shields.io/badge/Pipenv-grey"/><br/>
        <sub><b>Doc pipenv</b></sub></a><br />
      <a href="https://pipenv.pypa.io/en/latest/" title="Pipenv"></a>
    </td>
  </tr>
</table>

---

<h1 align="center">Installation de l'API</h1>

* Cloner le projet avec l'url suivante :
  * ``git clone https://github.com/LaurentJouron/SoftDesk.git``
* Déplacez vous dans le dossier:
  * ``cd SoftDesk``
* Créer un répertoire avec le nom .venv
  * ``mkdir .venv``
* Installer les dépendances nécessaires:
  * ``pipenv install``
* Activez l'environnement virtuel:
  * ``pipenv shell``
* Démarrer le serveur Django:
  * ``python manage.py runserver``

---

<h1 align="center">Détails utilisateur</h3>

8 utilisateurs ont étés créer.

* Ils utilisent tous le même mot de passe.
  * ``test``
* Il y a un superuser:
  * ``Laurent``
* Des users qui font parti du staff et qui sont actifs:
  * ``Thierno``
  * ``Louis``
  * ``Antoine``
  * ``Thierry``
  * ``Severine``

* Un users qui a fait pas parti du staff mais qui n'est plus actif:
  * ``Virginie``
  * ``Stephane``
---


<h1 align="center">Points de terminaison</h1>

* Méthode: GET
  * Récupérer la liste de projet rattaché à l'utilisateur connecté: ``/projects/ ``
  * Récupérer les détails d'un projet via son id: ``/projects/{id}/``
  * Récupérer la liste de tous les utilisateurs attaché à un projet: ``/projects/{id}/users/``
  * Récupérer la liste des issues lié à un projet: ``/projects/{id}/issues/``
  * Récupérer les détails d'un issue via son id: ``/projects/{id}/issues/{id}``
  * Récupérer la liste des commentaires liés à un issues: ``/projects/{id}/issues/{id}/comments/``
  * Récupérer un commentaire via son id: ``/projects/{id}/issues/{id}/comments/{id}``
* Méthode: POST
  * Création d'un utilisateur: ``/signup/``
  * Connexion de l'utilisateur: ``/login/``
  * Création d'un projet: ``/projects/``
  * Création d'un contributeur à un projet: ``/projects/{id}/users/``
  * Création d'un issue dans un projet: ``/projects/{id}/issues/``
  * Création d'un commentaire sur un issue: ``/projects/{id}/issues/comments/``
* Méthode: PUT
  * Mettre à jour un projet: ``/projects/{id}/``
  * Mettre à jour un issue: ``/projects/{id}/issues/{id}``
  * Mettre à jour un comment: ``/projects/{id}/issues/{id}/comments/{id}``
* Méthode: DELETE
  * Supprimer un projet et ses issues: ``/projects/{id}/``
  * Supprimer un utilisateur d'un projet: ``/projects/{id}/users/{id}``
  * Supprimer un issue d'un projet: ``/projects/{id}/issues/{id}``
  * Supprimer un comment: ``/projects/{id}/issues/{id}/comments/{id}``


---

<h1 align="center">Configuration de Postman</h1>

Réaliser cette opération à chaque requête si nécessaire.

* Configuration de la requête
  * Ouvrez l'application Postman sur votre ordinateur.
  * Assurez-vous que vous avez déjà obtenu un jeton ``CSRF access``

* Configuration de l'en-tête d'autorisation
  * Dans Postman, cliquez sur l'onglet ``Authorization``
  * Dans la cellule ``Type`` sélectionnez ``Bearer Token``
  * Si besoin, dans la cellule ``Token``, collez le jeton ``CSRF access``

---

<h1 align="center">Auteur et collaborateurs</h1>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LaurentJouron">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlW-w7O7g3hQTw8qcIAy3LCRhiHg5tUPfvVg&usqp=CAU"
          width="100px;"/><br />
        <sub><b>Laurent Jouron</b></sub></a><br />
      <a href="https://openclassrooms.com/fr/" title="Étudiant">🈸</a>
      <a href="https://github.com/LaurentJouron/Books-online" title="Codeur de l'application">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/thierhost">
        <img src="https://avatars.githubusercontent.com/u/7854284?s=100&v=4"
          width="100px;"/><br />
        <sub><b>Thierno Thiam</b></sub></a><br />
      <a href="https://github.com/thierhost" title="Mentor de Laurent">👨‍🏫</a> 
      <a href="https://www.python.org/dev/peps/pep-0008/" title="Doc PEP 8">📄</a>
    </td>
  </tr>
</table>
