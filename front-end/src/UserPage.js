import React, { useState, UseEffect } from 'react';
import M from 'materialize-css';

const UserPage = props => {

    const [name, setName] = useState("");
    const [capital, setCapital] = useState(0);

    const handleNameChange = e => {
        setName(e.target.value);
    }

    const handleCapitalChange = e => {
        setCapital(e.target.value);
    }

    const handleSubmit = e => {
        e.preventDefault();
        console.log(name + " " + capital)
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>Name:</label>
                <input onChange={handleNameChange} type="text" />
                <label>Capital:</label>
                <input onChange={handleCapitalChange} type="number" />
                <input type="submit"/>
            </form>
        </div>
    );
}

export default UserPage;