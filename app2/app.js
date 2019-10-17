const express = require("express");

const app = express();

app.get("/", (req, res) => {
  return res.send("App is Application 2 microservice");
});

app.listen(1001, () => {
  console.log("server started at port 1001");
});
