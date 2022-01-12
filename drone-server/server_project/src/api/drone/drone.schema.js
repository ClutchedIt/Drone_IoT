const mongoose = require('mongoose');

let droneSchema = mongoose.Schema({
    dueDate: Date,
    idPersona: Number,
    idDrone: Number,
    power: Number,
    distance: Number,
    velocity: Number,
    wind: Number ,
    height: Number,
    drone: String
});

module.exports = mongoose.model('drone', droneSchema);