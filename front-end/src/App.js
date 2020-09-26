import React, { useState, useEffect } from 'react';
import axios from "axios";
import M from 'materialize-css';
import Card from "./Card.js";
import Graph from "./Graph.js";
/* eslint-disable no-unused-expressions */

const App = props => {

  // Participant ID from the URL
  let url = window.location.href.split("/")
  let participantID = url.pop()

  // State management
  const [stateData, setStateData] = useState({});
  const [location, setLocation] = useState("main"); 
  const [user, setUser] = useState(participantID);

  useEffect(() => {
    M.AutoInit();

    setInterval(() => {
      axios.post("http://localhost:8000/oracle/", {"spec": "transactions"} )
      .then(res => {
        let ob = {}
        Object.values(res.data).map((tx) => {
          ob[tx["event"]] = {
            "yes": [],
            "no": []
          }
        })
        Object.values(res.data).map((tx) => {
          ob[tx["event"]][tx["side"]].push(tx["price"])
        })
        this.setState({
          "data": ob
        })
      })
    }, 5000);
  }, []);
  
  // Function of generating cards
  const generateCards = () => {
    // Array of components
    let components = []
    // Maps over the keyss of data
    Object.keys(stateData).map((key) => {
      // Array of graphs
      let graphs = []
      //Maps over the data by the keys
      Object.keys(stateData[key]).map((side) => {
        // Pushes a graph into graph
        let graph = <Graph width={ 300 } height={ 300 } title={ side } data_vals={ stateData[key][side] } />
        graphs.push(graph)
      })
      // Pushes a component to the array of components
      let component = <div className="col s6 m6 l6"><Card title={ key }>{ graphs }</Card></div>
      components.push(component)
    })

    // Components returned
    return components
  }

  // The main page
  const mainPage = (
    <div className="container">
      <div className="row">
        <h5 className="center-align">Prediction Market</h5>
      </div>
      <div className="row">
          { 
            generateCards()
          }
      </div>
    </div>
  );

  // The default page
  const defaultPage = (
    <div className="container">
      <div className="row">
        <h5 className="center-align">Default</h5>
      </div>
    </div>
  )

  // The login page
  const loginPage = (
    <div>
      <h2>Login</h2>
    </div>
  );

  // Sets the page to be returned
  let returnPage = location == "main" ? mainPage : location == "login" ? loginPage : defaultPage;

  return (
    returnPage
  );
}

/*
class App extends Component {

  constructor(props) {
    super(props);

    let url = window.location.href.split("/")
    let participantID = url.pop()

    this.state = {
      "location": "main",
      "user": participantID,
      "data": {}
    }
  }

  componentDidMount() {
    M.AutoInit();

    setInterval(() => {
      axios.post("http://localhost:8000/oracle/", {"spec": "transactions"} )
      .then(res => {
        let ob = {}
        Object.values(res.data).map((tx) => {
          ob[tx["event"]] = {
            "yes": [],
            "no": []
          }
        })
        Object.values(res.data).map((tx) => {
          ob[tx["event"]][tx["side"]].push(tx["price"])
        })
        this.setState({
          "data": ob
        })
      })
    }, 5000)
  }

  generateCards() {
    let components = []
    Object.keys(this.state.data).map((key) => {
      let graphs = []
      Object.keys(this.state.data[key]).map((side) => {
        let graph = <Graph width={ 300 } height={ 300 } title={ side } data_vals={ this.state.data[key][side] } />
        graphs.push(graph)
      })
      let component = <div className="col s6 m6 l6"><Card title={ key }>{ graphs }</Card></div>
      components.push(component)
    })

    return components
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
        if (Object.keys(this.state.data).length > 0) {
          return(
            <div className="container">
              <div className="row">
                <h5 className="center-align">Prediction Market</h5>
              </div>
              <div className="row">
                  { 
                    this.generateCards()
                  }
              </div>
            </div>
          );
        } else {
          return(
            <div className="container">
                <div className="row">
                  <h5 className="center-align">Prediction Market</h5>
                </div>
            </div>
          )
        }
    }
  }
}*/

export default App;
