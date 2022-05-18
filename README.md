# Grupo9

# Nombre del proyecto: Guido's Pizza

## Integrantes del grupo:
- Flavia Ailen Mañuico Quequejana - 202110207
- Maria Fernanda Surco Vergara - 202110358
- Alvaro Riojas Baldeon - 201710184

## Descripción del Proyecto:

Este proyecto consiste en una página web de la pizzería “Don Guido 's Pizza”, en la cual se ofrece el servicio de delivery. 
Antes de mostrar el menú de la pizzería, la página pide ingresar a una cuenta, en caso de no tener cuenta hay una sección donde te envía  a poder registrarse. Una vez dentro de tu cuenta la página muestra los diferentes productos (pizzas, entradas, postres, lasagna, combos y bebidas) y permite al cliente poder comprar a través de esta web. 



## Misión, Visión y Objetivos:

Nuestra misión es crear un servidor web  de confianza donde el usuario puede comprar su comida
Nuestra visión es poder crear un pagina web eficiente que satisfaga  las necesidades del usuario al pedir comida a  domicilio

Nuestros objetivos son:
 - Ofrecer los  productos de la pizzeria
 - Todos los productos se conduzcan adecuadamente al carrito de compras
 - Se concrete satisfactoriamente la compra del usuario




## Información acerca de las librerías/frameworks/plugins utilizadas en Front-end, Back-end y Base de datos:
Las librerías que hemos utilizado son:
- Datetime: librería que nos permite saber la fecha y hora,  en la que el usuario realiza su pedido
- Flask: Es un “micro” Framework escrito en Python y desarrollado para simplificar y hacer más fácil la creación de Aplicaciones Web bajo el patrón MVC.
- flask_sqlalchemy: Un ORM que nos permite trabajar con las tablas de la base de datos como si estas fueran objetos.
- Flask-migrate:Es una extensión que maneja la migración de la base de datos SQLAlchemy para las aplicaciones Flask.
- Werkzeug.security: librería que nos ayudó a poder poner la contraseña del usuario en un estilo incógnito, para garantizar la seguridad del usuario.
- flask-login: libreria que nos servirá para poder gestionar la sesion y tambien para manejar las tareas de login y logout.


## Información acerca de los API. Requests y Responses de cada endpoint utilizado en el sistema:
- ‘/’
- ‘/guidos/login’
- '/registrarse'
- '/logout'
- '/entradas'
- '/pizzas'
- '/lasagnas'
- '/combos'
- '/bebidas'
- '/postres'
- '/pedidos'
- '/pedidos/<pedido_id>/delete-pedido'
- '/guidos/create_user'
- '/pizzas/selecc'
- '/entradas/selecc'
- '/bebidas/selecc'
- '/postres/selecc'
- '/lasagnas/selecc'
- '/combos/selecc'
 
## Hosts:
- Puerto: 5000

## Manejo de Errores
- 404: Página no encontrada
