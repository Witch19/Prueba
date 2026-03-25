const userServices = require('../services/user.services');

function createUser(req, res, next){
    try{
        const user = userServices.createUser(req.body);
        res.status(201).json({
            status: 'success',
            data: user
        })
    } catch (err) {
        next(err);
    }
}

function getAllUsers(req, res, next){
    try{
        const users = userServices.listUser();
        res.status(200).json({
            status: 'success',
            data: users
        })
    } catch (err) {
        next(err);
    }
}

module.exports = {
    createUser,
    getAllUsers
}