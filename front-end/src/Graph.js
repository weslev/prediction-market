import React, { Component } from 'react';
import M from 'materialize-css';
import Plot from 'react-plotly.js';

//https://towardsdatascience.com/plotly-experiments-bar-column-plots-71dd32eed7ef
const Graph = props => {
	return (
		<Plot className="col s6 m6 l6"
			data={[
				{
					x: [1,2,3],//[...Array(props.data_vals.length).keys()],
					y: [2,6,3],//props.data_vals,
					mode: 'lines',
					marker: {color: 'blue'},
				}
			]}
			layout={{
				"width": props.width, 
				"height": props.height, 
				"title": props.title
			}}
		/>
	);
}

export default Graph