function validarEmail(mail){
    if(typeof mail !== 'string')return false;
    const trimEmail = mail.trim();
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    return regex.test(trimEmail);
}

module.exports = {
    validarEmail
}