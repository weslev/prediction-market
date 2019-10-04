import React, { Component } from 'react';
import M from 'materialize-css';
import Plot from 'react-plotly.js';

//https://towardsdatascience.com/plotly-experiments-bar-column-plots-71dd32eed7ef
class Graph extends Component {

	constructor(props) {
    	super(props);
    }

    render() {
    	return(
			<Plot className="col s6 m6 l6"
				data={[
					{
						x: [...Array(this.props.data_vals.length).keys()],
						y: this.props.data_vals,
						mode: 'lines',
						marker: {color: 'blue'},
					}
				]}
				layout={{
					"width": this.props.width, 
					"height": this.props.height, 
					"title": this.props.title
				}}
			/>
    	)
    }
}

export default Graph