# Aplicaciones Distribuidas

**Ejercicios**

1. [Sockets](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main?tab=readme-ov-file#Sockets)
3. [WebSockets](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main?tab=readme-ov-file#Web-Sockets)
2. [RMI JDBC](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main?tab=readme-ov-file#rmi-jdbc)
4. [SOAP JDBC](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main?tab=readme-ov-file#soap-jdbc)
5. [Rest JDBC](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main?tab=readme-ov-file#rest-spring-boot)
6. [GraphQL](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main?tab=readme-ov-file#graphql)


##  _**Sockets**_

>Realizado desde JAVA, servidor y cliente

 _*Repositorio: [puedes descargar el ejercicio Sockets desde aqui](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main/1.Sockets)*_ 


### Funcionamiento

>_Mensaje Enviado desde el cliente_
>>![imagen cliente](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/enviado_socket.png)


> _Mensaje recibido ene el servidor_
>>![imagen servidor](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/recibido_socket.png)

_[⇧ Regresar al menú](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main?tab=readme-ov-file#aplicaciones-distribuidas)_


## Web sockets

>  _*Repositorio: [puedes descargar el ejercicio Web Sockets desde aqui](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main/WebSockets)*_ 

Para este ejercicio se trabajó de la siguiente manera
1. Servidor: Node.JS con Express con la liberia de **Sockets** alojado en el servicio web de Render
2. Cliente: HTML, CSS Y JS alojada en github pages
3. Base de datos: Alojada en el servicio de Supabase

**Sitio web Cliente**
_*[Ir al sitio web](https://delacruz20.github.io/Aplicaciones-Distribuidas/WebSockets/SocketClient/)*_

### Diagrama
>![imagen bd](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/Diagramas/webSockets.png)

[⇧ Regresar al menú](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main?tab=readme-ov-file#aplicaciones-distribuidas)


## _**RMI JDBC**_
>Realizado desde JAVA, servidor y cliente

 _*Repositorio: [puedes descargar el ejercicio RMI JDBC desde aqui](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main/3.RMI%20JDBC)*_ 
 
### Funcionamiento

>_Servidor iniciado_
>>![imagen cservidor](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/serviodr_rmi.png)

>_Operación desde el cliente_
>>![imagen cliente](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/operacion_rmi.png)

> _Resultado_
>>![imagen resultado](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/resultado_rmi.png)

_[⇧ Regresar al menú](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main?tab=readme-ov-file#aplicaciones-distribuidas)_

## _**Soap JDBC**_

>Servicio web SOAP implementado en Java utilizando el framework JAX-WS. Este servicio web tiene cuatro operaciones: suma, resta, multiplicación y división. Cada operación realiza el cálculo respectivo y guarda la operación y el resultado en una base de datos utilizando JDBC.

>Cliente realizado en Python

 _*Repositorio: [puedes descargar el ejercicio SOAP JDBC desde aqui](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main/4.Soap%20JDBC)*_ 

### Funcionamiento

>Servidor iniciado
>>![imagen cservidor](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/servidor_soap.png)
	
>_Operación desde el cliente_
>>![imagen cliente](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/cliente_soap.png)

> _BD MySQL_
>>![imagen bd](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/mysql_soap.png)

_[⇧ Regresar al menú](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main?tab=readme-ov-file#aplicaciones-distribuidas)_

#### Diagrama
>![imagen bd](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/Diagramas/SOAP.jpg)

## _**Rest Spring Boot**_

>Esta API REST, desarrollada con Spring Boot, maneja las operaciones CRUD para el modelo de datos `UsuarioModel`. Utiliza un controlador (`UsuarioController`) que define rutas para obtener, guardar, buscar por prioridad y eliminar usuarios. El servicio (`UsuarioService`) implementa la lógica de negocio, interactuando con el repositorio (`UsuarioRepository`) que extiende `CrudRepository` para facilitar el acceso a la base de datos. La integración con Spring Boot permite una configuración simplificada y un desarrollo ágil, aprovechando las capacidades de Spring Data para gestionar las entidades, los datos son almacenados en MySQL.

>Cliente en JavaScript interactúa con una API REST para gestionar usuarios mediante las siguientes funciones: `fetchUsers`, que obtiene y muestra todos los usuarios; `createUser`, que crea un nuevo usuario enviando los datos ingresados en un formulario; `deleteUser`, que elimina un usuario específico por su ID; y `fetchUserById`, que obtiene y muestra los detalles de un usuario por su ID. Las solicitudes HTTP se realizan utilizando `fetch` y los resultados se manejan para actualizar dinámicamente el contenido de la página web.

 _*Repositorio: [puedes descargar el ejercicio SOAP JDBC desde aqui](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main/5.Rest%20JDBC)*_ 

### Funcionamiento

>Servidor iniciado
>>![imagen cservidor](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/servidor_rest.png)
	
>_Operación desde el cliente_
>>![imagen cliente](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/cliente_rest.png)

> _BD MySQL_
>>![imagen bd](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/mysql_rest.png)

_[⇧ Regresar al menú](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main?tab=readme-ov-file#aplicaciones-distribuidas)_

#### Diagrama
>![imagen bd](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/Diagramas/REST.jpg)

## GraphQL

> _*Repositorio: [puedes descargar el ejercicio SOAP JDBC desde aqui](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main/6.GraphQL)*_ 

Para este ejercicio se trabajó de la siguiente manera

1. Servidor: Node.JS con GraphQL y Apollo alojado en el servicio web de Render
2. Cliente: HTML, CSS Y JS alojada en github pages
3. Base de datos: Alojada en mongoDB con el servicio de Atlas 

URL para realizar pruebas con el servidor desplegado (Metodo _POST_ puedes utilizar la extesion de VS Thhunder Client ): _*https://graphql-psn7.onrender.com/graphql/users*_

Cuerpo para las distintas peticiones desde el cliente

1. Obtener usuarios
```GraphQL
query {
  getAllUsers {
    id
    name
    email
    password
  }
}
```
2. Crear usuario
```GraphQL
mutation {
  createUser(name: "<NAME>", email: "<EMAIL>", password: "<PASSWORD>") {
    id
    name
    email
  }
}
```
3. Actualizar usuario
```GraphQL
mutation {
  updateUser(id: "<USER_ID>", name: "<NAME>", email: "<EMAIL>") {
    id
    name
    email
  }
}

```
4. Eliminar usuario
```GraphQL
mutation {
  deleteUser(id: "<USER_ID>")
}
```

### Funcionamiento

>Servidor iniciado
>>![imagen cservidor](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/servidor_graphql.png)
	
>_Operación desde el cliente_
>>![imagen cliente](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/cliente_graphql.png)

> _BD MongoDB Atlas_
>>![imagen bd](https://github.com/Delacruz20/Aplicaciones-Distribuidas/blob/main/images_funcionamiento/mongodb_graphql.png)

[⇧ Regresar al menú](https://github.com/Delacruz20/Aplicaciones-Distribuidas/tree/main?tab=readme-ov-file#aplicaciones-distribuidas)
