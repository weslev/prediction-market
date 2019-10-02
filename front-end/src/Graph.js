import React, { Component } from 'react';
import M from 'materialize-css';
import Plot from 'react-plotly.js';


class Graph extends Component {

	constructor(props) {
    	super(props);
    }

    render() {
    	return(
			<Plot
				data={[
					{
						x: [0, 1, 2, 3, 4],
						y: [0, 2, 6, 3, 5],
						mode: 'lines',
						marker: {color: 'blue'},
					}
				]}
				layout={
					{ 
						width: this.props.width, 
						height: this.props.height, 
						title: this.props.title
					}
				}
			/>
    	)
    }
}

export default Graph