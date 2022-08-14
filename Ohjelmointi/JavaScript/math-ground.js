const shapearea = require("./shape-area.js")

const userInput = process.argv[2]
const Carea = shapearea.circleArea(userInput)
const Sarea = shapearea.squareArea(userInput)

console.log(Carea)
console.log(Sarea)