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

### ``--- Explication en français ---``
___________

Cet exercice a été réalisé dans le cadre d'une formation 
___________

<h1 align="center">But de l'application</h1>



___________

<h1 align="center">Langage</h1>


<p align="center">Les applications ont étés développées en Python - Django - Djando REST framework</p>

<table>
  <tr>
    <td align="center">
      <a href="https://www.python.org/">
        <img width="230px"
          src="https://www.python.org/static/img/python-logo.png" /><br />
        <sub><b>Téléchargez Python</b></sub></a><br />
      <a href="https://www.python.org/" title="Téléchargez Python" ></a> 
    </td>
    <td align="center">
      <a href="https://www.djangoproject.com/">
        <img width="200px"
          src="https://static.djangoproject.com/img/logos/django-logo-negative.png" /><br />
        <sub><b>Doc Django</b></sub></a><br />
      <a href="https://www.djangoproject.com/" title="Doc Django"></a> 
    </td>
    <td align="center">
      <a href="https://www.django-rest-framework.org/">
        <img width="140px"
          src="https://storage.caktusgroup.com/media/blog-images/drf-logo2.png" /><br />
        <sub><b>Doc Django REST framework</b></sub></a><br />
      <a href="https://www.django-rest-framework.org/" title="Doc Django REST framework"></a> 
    </td>
  </tr>
</table>

___________

<h1 align="center">EDI</h1>


<p align="left">L'EDI utilisé pour la programmation est Visual Studio Code.

<table>
  <tr>
    <td align="center">
      <a href="https://visualstudio.microsoft.com/fr/">
        <img width="130px"
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-H3CcAG7w2nXSnlqldVWR-ER4mvFfLgqYxA&usqp=CAU" /><br />
        <sub><b>Visuable Studio Code</b></sub></a><br />
      <a href="https://visualstudio.microsoft.com/fr/" title="Visuable Studio Code"></a>
    </td>
  </tr>
</table>

___________

<h1 align="center">Installation de l'API</h1>

Pour installer les dépendances du projet, nous utilisons l'outil pipenv que vous devez avoir pré-installé sur votre ordinateur.
  <a href="https://github.com/pypa/pipx" title="Visuable Studio Code" target="_blank">Documentation pypa/pipx</a>

  * ``pip install pipx``
  * ``pipx ensurepath``
  * ``pipx install pipenv``

Pour commencer il faut cloner le projet grâce à l'url suivante :
  * ``git clone https://github.com/LaurentJouron/SoftDesk.git``

Il faut se déplacer dans le dossier:
  * ``cd SoftDesk``

Voici la procédure pour afficher la page d'accueil du site:

Créer un répertoire avec le nom .venv
  * ``mkdir .venv``

Installer les bibliothèques nécessaires avec
  * ``pipenv install``

Activer l'environnement de travail (environnement virtuel) avec
  * ``pipenv shell``

Démarrer le serveur de développement de Django avec
  * ``python manage.py runserver``

___________


<h1 align="center">Effectuer une requête POST avec le jeton CSRF (Postman)</h1>
<h3>Obtenez le jeton CSRF</h3>

* Ouvrez votre navigateur (par exemple, Google Chrome) et accédez à l'URL de votre application Django Rest Framework.

* Ouvrez les outils de développement du navigateur en appuyant sur F12 ou en faisant un clic droit sur la page, puis en sélectionnant "Inspecter".

* Accédez à l'onglet "Network" dans les outils de développement.

* Rechargez la page de votre application.

* Dans la liste des requêtes qui apparaît dans l'onglet "Network", trouvez la requête qui correspond à la page que vous avez rechargée. Cliquez sur cette requête pour afficher les détails.

* Dans les en-têtes de la requête, recherchez "Set-Cookie" et trouvez la valeur associée à "csrftoken". Cette valeur est votre jeton CSRF.

<h3>Créez une nouvelle requête dans Postman</h3>

* Ouvrez l'application Postman sur votre ordinateur.

* Cliquez sur le bouton "New" pour créer une nouvelle requête.

* Dans le champ "Request Name", donnez un nom significatif à votre requête.

* Dans le champ "Request URL", saisissez l'URL de votre API Django Rest Framework où vous souhaitez effectuer la requête POST.

* Dans le champ "Request Method", sélectionnez "POST" dans le menu déroulant.

<h3>Ajoutez l'en-tête CSRF à la requête</h3>

* Cliquez sur l'onglet "Headers" sous l'URL de la requête.

* Cliquez sur le bouton "+", à droite de "Key", pour ajouter un nouvel en-tête.

* Dans le champ "Key", saisissez "X-CSRFToken".

* Dans le champ "Value", collez la valeur du jeton CSRF que vous avez obtenu à l'étape 1.

<h3>Configurez le corps de la requête</h3>

* Cliquez sur l'onglet "Body" sous l'URL de la requête.

* Choisissez la méthode d'envoi des données appropriée pour votre API (par exemple, "raw" pour envoyer des données JSON).

* Dans le corps de la requête, entrez les données requises selon les spécifications de votre API. Assurez-vous de respecter le format attendu par l'API (par exemple, JSON ou x-www-form-urlencoded).

<h3>Envoyez la requête</h3>

* Cliquez sur le bouton "Send" pour envoyer la requête POST à votre API Django Rest Framework avec le jeton CSRF inclus dans l'en-tête "X-CSRFToken".

* Vous devriez recevoir une réponse de l'API, indiquant que la requête a été traitée avec succès ou affichant toute erreur éventuelle.
___________

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