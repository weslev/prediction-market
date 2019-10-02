import React, { Component } from 'react';
import axios from "axios";
import M from 'materialize-css';
import Card from "./Card.js";
import Graph from "./Graph.js";


class App extends Component {

  constructor(props) {
    super(props);

    let url = window.location.href.split("/")
    let participantID = url.pop()
    let sessionID = url.pop()

    this.state = {
      "location": "main",
      "user": participantID,
      "data": {}
    }
  }

  componentDidMount() {
    M.AutoInit();
  }

  nice() {

    axios.post("http://localhost:8000/oracle/", {"spec": "transactions"} )
      .then(res => {
        console.log(res);
        console.log(res.data);
        this.setState(res.data)
      })
  }

  render() {
    switch(this.state.location) {
      case "login":
        return(
          <div>
            <h2>Login</h2>
          </div>
        )
      case "main":
        return(
          <div className="container">
            <Card>
              <Graph width={ 300 } height={ 300 } title={ "test1" } />
            </Card>
            <button onClick={ this.nice.bind(this) }>Test</button>
          </div>
        );
    }
  }
}

export default App;
