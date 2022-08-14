/* shape-area.js */
const PI = Math.PI;

// Define and export circleArea() and squareArea() below

module.exports.circleArea = function(radiusLength){
    return PI*radiusLength*radiusLength

}

function squareArea(sideLength){
    return sideLength * sideLength
}

module.exports.squareArea = squareArea
