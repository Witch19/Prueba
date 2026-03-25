const express = require('express');
const userRoutes = require('./routes/user.routes');

const app = express();

app.use(express.json());

app.use('/api', userRoutes);

app.get('/health', (req, res) => {
    res.status(200).json({
        status: 'success',
        message: 'OK'
    });
});

app.use((req, res) => {
    res.status(404).json({
        message: 'Ruta no encontrada'
    });
});

app.use((err, req, res, next) => {
    console.error(err);
    const statusCode = err.statusCode || 500;
    res.status(statusCode).json({
        message: err.message || 'Error interno del servidor'
    });
});

module.exports = app;