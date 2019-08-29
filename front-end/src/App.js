import React, { Component } from 'react';
import axios from "axios";


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {}
  }

  fun() {

    const stuff = {
      "asset": "dodgecoin",
      "orderType": "sell",
      "size": 11,
      "ask": 0.3
    } 

    axios.post("http://localhost:8000/order/", stuff )
      .then(res => {
        console.log(res);
        console.log(res.data);
      })
  }

  render() {
    return(
      <button onClick={ this.fun.bind(this) }>Go</button>
    )
  }
}

export default App;
