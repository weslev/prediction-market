import React, { Component } from 'react';
import M from 'materialize-css';



class Card extends Component {

  constructor(props) {
    super(props);

    this.state = {
      "side": "",
      "order_type": ""
    }

    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  handleSubmit(e) {
    console.log(this.state)
    e.preventDefault()
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    })
  }

  render() {
    return(
      <form onSubmit={ this.handleSubmit }>
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
            <input className="with-gap" type="radio" name="order_type" value="no" onChange={this.handleChange}/>
            <span>Sell</span>
          </label>
        </div>
        <div className="row">
          <input min={0} step={1} type="number" name="quantity" onChange={this.handleChange} />
        </div>
        <div className="row">
          <input className="btn" type="submit" />
        </div>
      </form>
    )
  }
}

export default Card

