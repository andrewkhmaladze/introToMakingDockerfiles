const express = require('express');
const app = express();
 
const PORT = process.env.PORT || 3000;
const MESSAGE = process.env.MESSAGE || "Hello from Docker!";
 
app.get('/', (req, res) => {
  res.send(`<h1>${MESSAGE}</h1>`);
});
 
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
 
.dockerignore
 
node_modules
npm-debug.log
