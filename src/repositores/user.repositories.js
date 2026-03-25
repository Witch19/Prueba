const users = [];

function getAllUsers() {
    return users;
}

function encontrarEmail(email){
    const normalEmail = email.toLowerCase().trim();
    return users.find((user)=> user.mail === normalEmail);
}

function createUser(user){
    users.push(user);
    return user;
}

module.exports = {
    getAllUsers,
    encontrarEmail,
    createUser
}
