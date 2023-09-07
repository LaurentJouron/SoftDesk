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

Pour installer les dépendances du projet, nous utilisons l'outil pipenv que vous devez avoir pré-installé sur votre ordinateur.
<a href="https://github.com/pypa/pipx" title="pypa/pipx" target="_blank">Documentation pypa/pipx</a>

  * ``pip install pipx``
  * ``pipx ensurepath``
  * ``pipx install pipenv``

Commencez par cloner le projet grâce à l'url suivante :
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
* Des users qui ne font pas parti du staff et qui ne sont "plus" actifs:
  * ``Virginie``
  * ``Stephane``
---

<h1 align="center">Détails choices</h3>
Les tables choices on étés programmées de façon à pouvoir les faire évoluer si besoin. En utilisant postman, il faut saisir les IDs.

* Les types qui se trouve sur projects:
  * ``1: Back-end``
  * ``2: Front-end``
  * ``3: iOS``
  * ``4: Android``
* Les tag qui se trouve sur issues:
  * ``1: Bug``
  * ``2: Feature``
  * ``3: Task``
- Les status qui se trouve sur issues:
  * ``1: To do``
  * ``2: In progress``
  * ``3: Finished``
* Les priority qui se trouve sur issues:
  * ``1: Low``
  * ``2: Medium``
  * ``3: High``

---

<h1 align="center">Effectuer une requête POST avec le jeton CSRF (Postman)</h1>
<h3>Obtenez le jeton CSRF</h3>

- Ouvrez l'application Postman sur votre ordinateur.

- Cliquez sur le bouton "New" pour créer une nouvelle requête.

- Dans le champ "Request Name", donnez un nom significatif à votre requête.

- Dans le champ "Request URL", saisissez l'URL : http://127.0.0.1:8000/api/token/

- Dans le champ "Request Method", sélectionnez "POST" dans le menu déroulant.

- Dans l'onglet Body, séléctonnez raw, coller et cliquez sur send

```json
{
  "username": "Laurent",
  "password": "test"
}
```

- Cliquez sur l'onglet "Headers" sous l'URL de la requête. Vous obtiendrez votre Token.

Exemple:

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MTgzOTU3MiwiaWF0IjoxNjkxNzUzMTcyLCJqdGkiOiJlZTc2ODQ4YmYzNGQ0ODI1OTQ5YTcyYTE2NGI3YTJlNSIsInVzZXJfaWQiOjF9.M9eSGmRkcf1wMS2iDVe2l0PH8Zm9HDMi7eDUDF6QN_Q",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkxNzcxMTcyLCJpYXQiOjE2OTE3NTMxNzIsImp0aSI6IjhlNDA3MWEzYjhiNDRiMmNhOWRiM2IwZTU2MWU5OTMyIiwidXNlcl9pZCI6MX0.iT_s2w4pAhrP0kQLz3L5UV2BTLt0ycl7igIY6ZY5gX8"
}
```

- Copiez la clé access sans les doubles cotes ""

<h3>Nouelle requelle</h3>

- Cliquez sur le bouton "+", à droite de "Key", pour ajouter un nouvel en-tête.

- Dans Authorization - cliquez sur la combo type et selectionnez Bearer Token

- Collez le Token à la place indiquée.

- Dans le champ "Request Method", sélectionnez "GET" dans le menu déroulant.

- Cliquez sur l'onglet "Body" sous l'URL de la requête.

- Cliquez sur le bouton "Send" pour envoyer la requête GET à votre API Django Rest Framework avec le jeton CSRF inclus dans l'en-tête "X-CSRFToken".

- Vous devriez recevoir une réponse de l'API, indiquant que la requête a été traitée avec succès ou affichant toute erreur éventuelle.

---

<h1 align="center">Points de terminaison</h1>

<h3>Méthode: GET</h3>

- Récupérer la liste de projet rattaché à l'utilisateur connecté: `/projects/ `
- Récupérer les détails d'un projet via son id: `/projects/{id}/`
- Récupérer la liste de tous les utilisateurs attaché à un projet: `/projects/{id}/users/`
- Récupérer la liste des issues lié à un projet: `/projects/{id}/issues/`
- Récupérer la liste des commentaires liés à un issues: `/projects/{id}/issues/{id}/comments/`
- Récupérer un commentaire via son id: `/projects/{id}/issues/{id}/comments/{id}`

<h3>Méthode: POST</h3>

- Création d'un utilisateur: `/signup/`
- Connexion de l'utilisateur: `/login/`
- Création d'un projet: `/projects/`
- Création d'un contributeur à un projet: `/projects/{id}/users/`
- Création d'un issue dans un projet: `/projects/{id}/issues/`
- Création d'un commentaire sur un issue: `/projects/{id}/issues/comments/`

<h3>Méthode: PUT</h3>

- Mettre à jour un projet: `/projects/{id}/`
- Mettre à jour un issue: `/projects/{id}/issues/{id}`
- Mettre à jour un comment: `/projects/{id}/issues/{id}/comments/{id}`

<h3>Méthode: DELETE</h3>

- Supprimer un projet et ses issues: `/projects/{id}/`
- Supprimer un utilisateur d'un projet: `/projects/{id}/users/{id}`
- Supprimer un issue d'un projet: `/projects/{id}/issues/{id}`
- Supprimer un comment: `/projects/{id}/issues/{id}/comments/{id}`

---

<h1 align="center">Permissions</h1>

  - Si l'utilisateur n'est pas contributeur d'un projet --> Il ne doit le voir.

  - Interdiction à tout utilisateur autorisé autre que l'auteur d'émettre
    une requete d'actualisation et suppression d'un issues/project/commentaire.

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
