const axios = require('axios'); // or import axios from 'axios'

axios.get('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => {
    console.log(response.data); // Data is automatically parsed JSON
  })
  .catch(error => {
    console.error('Error:', error);
  });
