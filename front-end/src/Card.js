import React, { Component } from 'react';
import M from 'materialize-css';
import axios from "axios";

class Card extends Component {

  constructor(props) {
    super(props);

    this.state = {
      "player": "lorenzo",
      "event": this.props.title,
    }

    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  handleSubmit(e) {
    let data = this.state
    axios.post("http://localhost:8000/order/", { data })
    .then(res => {
      console.log(res)
    })
    e.target.reset();
    document.getElementById("test5").textContent = 0.5
    e.preventDefault()
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    })
  }

  nice(event) {
    let val = event.target.value
    this.setState({
      [event.target.name]: val
    })
    
    document.getElementById("test5").textContent = val.toString()
  }

  render() {
    return(
      <form onSubmit={ this.handleSubmit }>
        <div className="row">
          <h5 className="center-align">{ this.props.title } </h5>
        </div>
        <div className="row">
          { this.props.children }
        </div>
        <div className="row">
          <label className="col">
            <input className="with-gap" type="radio" name="side" value="yes" onChange={this.handleChange}/>
            <span>Yes</span>
          </label>
          <label className="col">
            <input className="with-gap" type="radio" name="side" value="no" onChange={this.handleChange}/>
            <span>No</span>
          </label>
        </div>
        <div className="row">
          <label className="col">
            <input className="with-gap" type="radio" name="order_type" value="buy"  onChange={this.handleChange}/>
            <span>Buy</span>
          </label>
          <label className="col">
            <input className="with-gap" type="radio" name="order_type" value="sell" onChange={this.handleChange}/>
            <span>Sell</span>
          </label>
        </div>
        <div className="row">
          <label>Size of the Order</label>
          <input min={0} step={1} type="number" name="quantity" defaultValue="0" onChange={this.handleChange} />
        </div>
        <div className="row">
          <label>Price</label>
          <input name="price" type="range" min="0" max="1" defaultValue="0.5" step="0.01" onChange={ this.nice.bind(this) } />
          <p id="test5" className="center-align">0.5</p>
        </div>
        <div className="row">
          <input className="btn" type="submit" />
        </div>
      </form>
    )
  }
}

export default Card

