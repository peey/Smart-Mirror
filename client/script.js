var exampleSocket = new WebSocket("ws://localhost:8765");

var passiveModes = ['quote', 'weather', 'news', 'time']

passiveModeInterval = setInterval(function () {
  if (vm.mode() == "passive") {
    var item = passiveModes[Math.floor(Math.random()*passiveModes.length)];
    vm.type(item)
  }
}, 20 * 1000)


exampleSocket.onmessage = function (event) {
  try {
    var o = JSON.parse(event.data)
  } catch(e) {
    var o = {}
    o.text = event.data
    o.type = "text"
  }
  console.log("got message", o)

  switch (o.type) {
    case "command":
      switch(o.command) {
        case "active-mode": vm.mode("active"); break;
        case "passive-mode": vm.mode("passive"); break;
      }
      break;
    case "image":
      vm.type("image")
      vm.imageSrc(o.src)
      break;
    case "text":
      vm.type("text")
      vm.text(o.text)
      break;
    case "json":
      vm.type("json")
      vm.json(JSON.stringify(o.json, null, 2))
      break;
    case "news":
      vm.type("news")
      vm.news(ko.mapping.fromJS(o.items)())
      break;
    case "weather":
      vm.type("weather")
      vm.weather.intent(o.intent)
      vm.weather.location(o.location? o.location: "")
      vm.weather.data(o.data instanceof Array? o.data : [o.data])
      console.log("completed without error")
      break;
    case "tic-tac-toe":
      vm.type("tic-tac-toe")
      vm.ticTacToe(o.data)
      break;
    case "dictionary":
      vm.dictionary.word(o.word)
      vm.dictionary.meanings(o.meanings)
      vm.type("dictionary")
      break;
    case "wikipedia":
      vm.dictionary.word(o.word)
      vm.dictionary.summary(o.summary)
      vm.type("wikipedia")
      break;
    case "send-mail":
      vm.smail.recipient(o.recipient)
      vm.smail.subject(o.subject)
      vm.smail.body(o.body)
      vm.type("send-mail")
      break;
    case "check-mail":
      vm.cmails(o.mails)
      vm.type("check-mail")
      break;
    case "quote":
      vm.quote.quote(o.quote)
      vm.quote.author(o.author)
      vm.type("quote")
      break;
  }
}

exampleSocket.onopen = function () {
  vm.text("Connected to the server!")
}

function sendText(msg) {
  exampleSocket.send(msg);
}

var vm = {
  text: ko.observable("Hello, connecting to server"),
  type: ko.observable(""),
  json: ko.observable("{}"),
  imageSrc: ko.observable(""),
  news: ko.observableArray([]),
  mode: ko.observable("passive"),
  weather: {
    intent: ko.observable(""),
    location: ko.observable(""),
    data: ko.observableArray([{
      tempMin: 1,
      tempMax: 1,
      summary: "Ko breaks without this",
      icon: "",
      humidity: "",
      pressure: ""
    },
    {
      tempMin: 1,
      tempMax: 1,
      summary: "Ko breaks without this",
      icon: ""
    },
    {
      tempMin: 1,
      tempMax: 1,
      summary: "Ko breaks without this",
      icon: ""
    }])
  },
  ticTacToe: ko.observableArray(["", "", "", "", "", "", "", "", ""]),
  dictionary: {
    word: ko.observable("Test word"), meanings: ko.observableArray([{"type": "Test Adjective", meanings: ["hi", "hi2"]}])},
  wikipedia: {
    word: ko.observable("Test word"),
    summary: ko.observable("Test Summary")
  },
  smail: {
    recipient: ko.observable(""),
    subject: ko.observable(""),
    body: ko.observable("")
  },
  quote: {
    quote: ko.observable(""),
    author: ko.observable("")
  },
  cmails: ko.observableArray([{"from": "test", "subject": "test"}]),
  time: ko.observable("10:00 AM")
}

function fmtTime() {
  var date = new Date();
  var hrs = date.getHours()
  var ampm = "AM"
  if (hrs > 12) {
    ampm = "PM"
    hrs = hrs % 12
  }
  var mints = date.getMinutes()
  // zerofilling
  if (hrs < 10) {
    hrs = "0" + hrs
  }

  if (mints < 10) {
    mints = "0" + mints
  }

  return hrs + ":" + mints + " " + ampm
}

vm.time(fmtTime())
timeInterval = setInterval(function () {
  vm.time(fmtTime())
}, 1000)

ko.applyBindings(vm)
