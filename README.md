<h1>Práctica: Plataforma de Blogging - Práctica de Python, Django y
REST-KeepCoding Master</h1>

Plataforma de blogging llamada Wordplease en la cual los usuarios puedan
registrarse para crear su blog personal.

## Sitio Web
	* **URL / aparecerán los últimos posts publicados por los usuarios
	* **URL /blogs/ mostrará un listado de los blogs de los usuarios que hay en la plataforma
	* **URL /blogs/<nombre_usuario>/ mostrará todos los post del usuario ordenados de más actual a más antiguo
	* **URL /blogs/<nombre_usuario>/<post-id> mostrará el detalle de un post
    * **URL /new-post mostrará el formulario para crear un nuevo post con autenticación
    * **URL /login mostrará el formulario para hacer login en la plataforma
    * **URL /logout podrás hacer logout de la plataforma
    * **URL /signup mostrará el formulario para registrar usuarios en la plataforma

## API
    * **GET	Users list	/api/v1/users/
    * **POST Sign up	/api/v1/users/
    * **GET	User detail	/api/v1/users/<user_id>
    * **PUT User update	/api/v1/users/<user_id>
    * **DELETE  User delete	/api/v1/users/<user_id>
    * **GET	Posts list	/api/v1/posts/
    * **POST    New post	/api/v1/posts/
    * **GET	Post detail	/api/v1/posts/<user_id>
    * **PUT	Post update	/api/v1/posts/<user_id>
    * **DELETE	Post delete	/api/v1/posts/<user_id>
    * **GET	Blogs list	api/v1/blogs/