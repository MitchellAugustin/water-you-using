import React from 'react'

class Tips extends React.Component{
    state = {tips: ["Don't keep the faucet running while brushing your teeth!", 
    "Get a toilet cistern from your water provider",
    "Take shorter showers! Aerated shower heads and shower regulators can decrease shower water usage as well.",
    "Use full loads in the dishwasher and the laundry machine",
    "Check your house for any dripping taps. They can waste up to 5500 litres a year"]}
    render(){
        var tipNumber = Math.floor(Math.random() * 5);
        return <div>
            <p><font color = "#FFFFE0">Tip of the day: {this.state.tips[tipNumber]}</font></p><br />
        </div>
    }
}

export default Tips
