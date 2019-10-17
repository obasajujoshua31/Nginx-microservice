const express = require("express");

const app = express();

app.get("/", (req, res) => {
  return res.send("App is Application 1 microservice");
});

app.listen(1000, () => {
  console.log("server started at port 1000");
});
