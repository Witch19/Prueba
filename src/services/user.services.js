const {validarEmail} = require('../validador/email.validador');
const { randomUUID } = require('crypto');
const appError = require('../errores/app.error');
const repoUser = require('../repositores/user.repositories');

function createUser({email, name}){
    if(!name || typeof name !== 'string'){
        throw new appError('campo obligatiorio name')
    }
    if(!email || typeof email !== 'string'){
        throw new appError('campo obligatiorio email')
    }
    
    if(!validarEmail(email)){
        throw new appError('El email no consta con un formato válido')
    }

    const existenteUser = repoUser.encontrarEmail(email);
    if(existenteUser){
        throw new appError('Ya existe este correo')
    }

    const nuevoUser = {
        id: randomUUID(),
        name: name.trim(),
        email: email.toLowerCase().trim()
    }

    return repoUser.createUser(nuevoUser);

}

function listUser(){
    return repoUser.getAllUsers();
}

module.exports = {
    createUser,
    listUser
}