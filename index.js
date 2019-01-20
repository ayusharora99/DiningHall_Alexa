'use strict';
const Alexa = require('alexa-sdk');
const AWS = require('aws-sdk');
var s3 = new AWS.S3();

var params = {Bucket: 'dininghall', Key: 'NineTenbreakfast.txt'}

const handlers = {
    'LaunchRequest': function () {
        // Triggered when User says: "Alexa, open UCSC Dining Hall"
        this.emit(':ask', 'Welcome to UCSC Dining Halls, which meal at which dining hall would you like to hear about? ')
    },
    'PlayMealIntent': async function () {
        try{
        var speechOutput = '';
        //this.response.speak('Hi there!')
        var meal = this.event.request.intent.slots.meal.value.toLowerCase()
        var dininghall = this.event.request.intent.slots.dining_hall.value.toLowerCase()
    
        this.response.speak("You are asking for " + meal + " at " + dininghall)
        if(meal == "breakfast" && (dininghall == "college 9" || dininghall == "college 10" || dininghall == "college 910" || dininghall == "college 9 and 10" || dininghall == "nine ten" || dininghall == "nine and ten" || dininghall == "910")){
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'NineTenbreakfast.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at College Nine and Ten right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("NineTenbreakfast.txt")
            console.log("this is the value: " + food)
            this.response.speak("College nine and ten has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "lunch" && (dininghall == "college 9" || dininghall == "college 10" || dininghall == "college 910" || dininghall == "college 9 and 10" || dininghall == "nine ten" || dininghall == "nine and ten" || dininghall == "910")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'NineTenlunch.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at College Nine and Ten right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("NineTenlunch.txt")
            console.log("this is the value: " + food)
            this.response.speak("College nine and ten has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "dinner" && (dininghall == "college 9" || dininghall == "college 10" || dininghall == "college 910" || dininghall == "college 9 and 10" || dininghall == "nine ten" || dininghall == "nine and ten" || dininghall == "910")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'NineTendinner.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at College Nine and Ten right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("NineTendinner.txt")
            console.log("this is the value: " + food)
            this.response.speak("College nine and ten has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "late night" && (dininghall == "college 9" || dininghall == "college 10" || dininghall == "college 910" || dininghall == "college 9 and 10" || dininghall == "nine ten" || dininghall == "nine and ten" || dininghall == "910")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'NineTenlateNight.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at College Nine and Ten right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("NineTenlateNight.txt")
            console.log("this is the value: " + food)
            this.response.speak("College nine and ten has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        }
        
        else if(meal == "breakfast" && (dininghall == "cowell stevenson" || dininghall == "cowell" || dininghall == "stevenson" || dininghall == "cowell and stevenson")){
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'CowellStevensonbreakfast.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("CowellStevensonbreakfast.txt")
            console.log("this is the value: " + food)
            this.response.speak("Cowell Stevenson has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "lunch" && (dininghall == "cowell stevenson" || dininghall == "cowell" || dininghall == "stevenson" || dininghall == "cowell and stevenson")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'CowellStevensonlunch.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("CowellStevensonlunch.txt")
            console.log("this is the value: " + food)
            this.response.speak("Cowell Stevenson has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "dinner" && (dininghall == "cowell stevenson" || dininghall == "cowell" || dininghall == "stevenson" || dininghall == "cowell and stevenson")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'CowellStevensondinner.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("CowellStevensondinner.txt")
            console.log("this is the value: " + food)
            this.response.speak("Cowell Stevenson has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "late night" && (dininghall == "cowell stevenson" || dininghall == "cowell" || dininghall == "stevenson" || dininghall == "cowell and stevenson")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'CowellStevensonlateNight.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("CowellStevensonlateNight.txt")
            console.log("this is the value: " + food)
            this.response.speak("Cowell Stevenson has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        }
        
        else if(meal == "breakfast" && (dininghall == "rachel carson oakes" || dininghall == "rachel carson" || dininghall == "oakes" || dininghall == "college eight" || dininghall == "carson")){
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'CarsonOakesbreakfast.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("CarsonOakesbreakfast.txt")
            console.log("this is the value: " + food)
            this.response.speak("Rachel Carson Oakes has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "lunch" && (dininghall == "rachel carson oakes" || dininghall == "rachel carson" || dininghall == "oakes" || dininghall == "college eight" || dininghall == "carson")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'CarsonOakeslunch.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("CarsonOakeslunch.txt")
            console.log("this is the value: " + food)
            this.response.speak("Rachel Carson Oakes has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "dinner" && (dininghall == "rachel carson oakes" || dininghall == "rachel carson" || dininghall == "oakes" || dininghall == "college eight" || dininghall == "carson")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'CarsonOakesdinner.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("CarsonOakesdinner.txt")
            console.log("this is the value: " + food)
            this.response.speak("Rachel Carson Oakes has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "late night" && (dininghall == "rachel carson oakes" || dininghall == "rachel carson" || dininghall == "oakes" || dininghall == "college eight" || dininghall == "carson")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'CarsonOakeslateNight.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("CarsonOakeslateNight.txt")
            console.log("this is the value: " + food)
            this.response.speak("Rachel Carson Oakes has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        
        else if(meal == "breakfast" && (dininghall == "crown merrill" || dininghall == "crown" || dininghall == "merrill" || dininghall == "merrill crown" || dininghall == "crown and merrill" || dininghall == "merril")){
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'CrownMerrilbreakfast.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("CrownMerrilbreakfast.txt")
            console.log("this is the value: " + food)
            this.response.speak("Crown Merrill has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "lunch" && (dininghall == "crown merrill" || dininghall == "crown" || dininghall == "merrill" || dininghall == "merrill crown" || dininghall == "crown and merrill" || dininghall == "merril")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'CrownMerrillunch.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("CrownMerrillunch.txt")
            console.log("this is the value: " + food)
            this.response.speak("Crown Merrill has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "dinner" && (dininghall == "crown merrill" || dininghall == "crown" || dininghall == "merrill" || dininghall == "merrill crown" || dininghall == "crown and merrill" || dininghall == "merril")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'CrownMerrildinner.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("CrownMerrildinner.txt")
            console.log("this is the value: " + food)
            this.response.speak("Crown Merrill has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        
        else if(meal == "late night" && (dininghall == "crown merrill" || dininghall == "crown" || dininghall == "merrill" || dininghall == "merrill crown" || dininghall == "crown and merrill" || dininghall == "merril")) {
            this.response.speak("There is no late night available at " + dininghall + ".")
            this.emit(':responseReady')
        }
        
        else if(meal == "breakfast" && (dininghall == "porter kresge" || dininghall == "porter" || dininghall == "kresge" || dininghall == "kresge porter" || dininghall == "porter and kresge")){
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'PorterKresgebreakfast.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("PorterKresgebreakfast.txt")
            console.log("this is the value: " + food)
            this.response.speak("Porter Kresge has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "lunch" && (dininghall == "porter kresge" || dininghall == "porter" || dininghall == "kresge" || dininghall == "kresge porter" || dininghall == "porter and kresge")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'PorterKresgelunch.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("PorterKresgelunch.txt")
            console.log("this is the value: " + food)
            this.response.speak("Porter Kresge has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        else if(meal == "dinner" && (dininghall == "porter kresge" || dininghall == "porter" || dininghall == "kresge" || dininghall == "kresge porter" || dininghall == "porter and kresge")) {
            var obj = new AWS.S3({params: {Bucket: 'dininghall', Key: 'PorterKresgedinner.txt'}});
            var temp = this
            obj.headObject(function(err) {
              if (err) {
                  console.log("File is not present");
                  temp.response.speak("There is no " + meal + " at " + dininghall + " right now.")
                  temp.emit(':responseReady')
              }
              else console.log("File is present");
            });
            var food = await getObjData("PorterKresgedinner.txt")
            console.log("this is the value: " + food)
            this.response.speak("Porter Kresge has " + food + " available for " + meal + ".")
            this.emit(':responseReady')
        } 
        
        else if(meal == "late night" && (dininghall == "porter kresge" || dininghall == "porter" || dininghall == "kresge" || dininghall == "kresge porter" || dininghall == "porter and kresge")) {
            this.response.speak("There is no late night available at " + dininghall + ".")
            this.emit(':responseReady')
        } else {
            this.response.speak("I didn't understand what you're asking for. Try again by saying, 'Alexa open UCSC dining hall' and asking again")
        }
    
        }catch(err){
            console.log(err)
        }
    },
    'AMAZON.HelpIntent': function () {

    },
    'AMAZON.CancelIntent': function () {

    },
    'AMAZON.StopIntent': function () {
 
    },
    'Unhandled': function () {
        this.emit(':ask', "this is a help messsage for unhandled", "this is a help messsage for unhandled");
    }
};

function getObjData(keyName) {
    return new Promise((resolve, reject) => {
        var params = {
              Bucket: "dininghall", 
              Key: keyName
             };
             console.log(keyName)
            s3.getObject(params, function(err, data) {
                if(err) {
                    reject(err)
                } else {
                    var objectData = data.Body.toString('utf-8');
                    resolve(objectData)
                    console.log(typeof(objectData))
                }
            });
    });
}

exports.handler = function (event, context, callback) {
    const alexa = Alexa.handler(event, context, callback);
    alexa.registerHandlers(handlers);
    alexa.execute();
    console.log('this is finished')
};
