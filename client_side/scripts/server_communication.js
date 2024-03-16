// sth like that, dont quote me

import React from 'react';
import axios from 'axios';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {message: ""};
  }

  componentDidMount() {
    // GET request to the Python server
    axios.get('http://localhost:5000/api/data')
      .then(response => {
        this.setState({ message: response.data.message });
        console.log(response.data);
      });
  }

  postData = () => {
    // POST request to the Python server
    axios.post('http://localhost:5000/api/data', {key: 'value'})
      .then(response => {
        this.setState({ message: response.data.message });
        console.log(response.data);
      });
  }
  
  render() {
    return (
      <div>
        <h3>Response from server:</h3>
        <p>{this.state.message}</p>
        <button onClick={this.postData}>POST Data</button>
      </div>
    );
  }
}

export default App;