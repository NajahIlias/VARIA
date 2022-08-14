  const converters = require('./converters.js');

  const freezingPointC = 0;
  const boilingPointC = 100;
   
  const freezingPointF = celsiusToFahrenheit(freezingPointC);
  const boilingPointF = celsiusToFahrenheit(boilingPointC);
   
  console.log(`The freezing point of water in Fahrenheit is ${freezingPointF}`);
  console.log(`The boiling point of water in Fahrenheit is ${boilingPointF}`);