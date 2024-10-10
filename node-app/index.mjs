import fs from "fs";

fs.appendFile("my-file.txt", "Файл сохранен", (err) => {
  if (err) {
    throw err;
  } else {
    console.log("Файл сохранен");
  }
});
