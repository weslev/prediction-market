import React, { Component } from 'react';
import axios from "axios";


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {}
  }

  order(orderType) {

    const stuff = {
      "asset": "dodgecoin",
      "orderType": orderType,
      "size": 11,
    } 

    if (orderType == "buy") {
      stuff["bid"] = 0.3
    } else {
      stuff["ask"] = 0.3
    }

    axios.post("http://localhost:8000/order/", stuff )
      .then(res => {
        console.log(res);
        console.log(res.data);
      })
  }

  render() {
    return(
      <div>
        <button onClick={ this.order.bind(this, "buy") }>Buy</button>
        <button onClick={ this.order.bind(this, "sell") }>Sell</button>
      </div>
    )
  }
}

export default App;
