import React from 'react'
import {Progress, Label} from 'semantic-ui-react';
import ReactInterval from 'react-interval';
import PieChart from 'react-minimal-pie-chart';
import {VictoryPie} from 'victory';
import {VictoryBar} from 'victory';
import {Dropdown} from 'semantic-ui-react'


var request = require('request')

let kitchenData = [0.0,1.0,2.0,3.0,4.0]
let toiletData = [0.0,1.0,2.0,3.0,4.0]
let faucetData = [0.0,1.0,2.0,3.0,4.0]
let json1
let json2
let json3
//var data = [13,50,40,130,200,800,1000,1500,2000,5000,10000,30000,60000,50000,300000]

//Use this URL for the bar chart breakdown: http://dorm.buttersalt.me:5000/geteventdata/mitchell/testpassmitchell/DAILY_DATA_POINT
//Use this URL for the pie chart breakdown (breakdown by device): http://dorm.buttersalt.me:5000/geteventdata/mitchell/testpassmitchell/toilet/DAILY_DATA_POINT

class WaterBreakdown extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      option: 'hourly', 
      toilet: 35, 
      faucet: 40, 
      kitchen: 55,
      domain: props.domain
    };
  }
    componentDidMount(){
        var http_req = new XMLHttpRequest();
        http_req.open("GET",this.state.domain + 'lasttimevolume/mitchell/testpassmitchell/kitchen',false);
        http_req.send(null);
        json1 = http_req.responseText
        json1 = JSON.parse(json1)
        kitchenData[0] = json1[0].hour
        kitchenData[1] = json1[0].day
        kitchenData[2] = json1[0].week
        kitchenData[3] = json1[0].month
        kitchenData[4] = json1[0].year

        var http_req2 = new XMLHttpRequest();
        http_req2.open("GET",this.state.domain + 'lasttimevolume/mitchell/testpassmitchell/bathroom',false);
        http_req2.send(null);
        json2 = http_req2.responseText
        json2 = JSON.parse(json2)
        toiletData[0] = json2[0].hour
        toiletData[1] = json2[0].day
        toiletData[2] = json2[0].week
        toiletData[3] = json2[0].month
        toiletData[4] = json2[0].year
        
        var http_req3 = new XMLHttpRequest();
        http_req3.open("GET",this.state.domain + 'lasttimevolume/mitchell/testpassmitchell/faucet',false);
        http_req3.send(null);
        json3 = http_req3.responseText
        console.log(json3)
        json3 = JSON.parse(json3)
        console.log(json3)
        faucetData[0] = json3[0].hour
        faucetData[1] = json3[0].day
        faucetData[2] = json3[0].week
        faucetData[3] = json3[0].month
        faucetData[4] = json3[0].year
        this.setTimeFrame('hourly')
    }
    
    
    setTimeFrame(optionChoice) {
        var timeIndex = 0;
            //JSON file will return all water events in the last day
            //Therefore, this method should loop through all provided objects and 
        if(optionChoice === 'hourly'){
            timeIndex = 0;
        }
        else if(optionChoice === 'daily'){
            timeIndex = 1;
        }
        else if(optionChoice === 'weekly') {
            timeIndex = 2
        }
        else if(optionChoice === 'monthly') {
            timeIndex = 3
        }
        else {
            timeIndex = 4
        }
        if(kitchenData[timeIndex] === 0 && toiletData[timeIndex] === 0 && faucetData[timeIndex] === 0){
          this.setState({
            ...this.state,
            option: optionChoice,
            kitchen: 1,
            toilet: 1,
            faucet: 1
          })
        }
        else{ 
          this.setState({
            ...this.state,
            option: optionChoice,
            kitchen: kitchenData[timeIndex],
            toilet: toiletData[timeIndex],
            faucet: faucetData[timeIndex]
          })
        }
      }

    render(){  
        return <div><br/><br/>
  <center><div class="ui teal massive label"><font color = "White">Breakdown by Device: {this.state.option}</font></div></center><br/>
        <center><div class = "ui blue large label"><Dropdown text='Time Frame Selection'>
    <Dropdown.Menu>
      <Dropdown.Item text='Past Hour' onClick = {() => this.setTimeFrame('hourly')} />
      <Dropdown.Item text='Past Day' onClick = {() => this.setTimeFrame('daily')}/>
      <Dropdown.Item text='Past Week' onClick = {() => this.setTimeFrame('weekly')}/>
      <Dropdown.Item text='Past Month' onClick = {() => this.setTimeFrame('monthly')}/>
      <Dropdown.Item text='Past Years' onClick = {() => this.setTimeFrame('yearly')}/>
    </Dropdown.Menu>
  </Dropdown> </div><br /></center>
        
          <VictoryPie
          animate={{
            duration: 1000,
            easing: "bounce"
          }}
          colorScale = "cool"
         style={{ labels: { fill: "white", fontStyle: "bold"} }}
         labelRadius={({ innerRadius }) => innerRadius + 70 }
         labels={({ datum }) => `${datum.x}: ${datum.y}`}
  data={[
    { x: "Toilet", y: Math.round(this.state.toilet)},
    { x: "Faucet", y: Math.round(this.state.faucet) },
    { x: "Kitchen", y: Math.round(this.state.kitchen) }
  ]}
/>
<center><div class="ui teal massive label"><font color = "White">Volume Breakdown: {this.state.option}</font></div></center><br />
<center><div class = "ui blue large label"><Dropdown text='Time Frame Selection'>
    <Dropdown.Menu>
      <Dropdown.Item text='Past Hour' onClick = {() => this.setTimeFrame('hourly')} />
      <Dropdown.Item text='Past Day' onClick = {() => this.setTimeFrame('daily')}/>
      <Dropdown.Item text='Past Week' onClick = {() => this.setTimeFrame('weekly')}/>
      <Dropdown.Item text='Past Month' onClick = {() => this.setTimeFrame('monthly')}/>
      <Dropdown.Item text='Past Years' onClick = {() => this.setTimeFrame('yearly')}/>
    </Dropdown.Menu>
  </Dropdown> </div><br /></center>
<VictoryBar
animate={{
  duration: 1000,
  easing: "bounce"
}}
  barRatio = {1.5}
  data={[
    { x: "Toilet", y: Math.round(this.state.toilet) },
    { x: "Faucet", y: Math.round(this.state.faucet) },
    { x: "Kitchen", y: Math.round(this.state.kitchen) }
  ]}
  labels={({ datum }) => `${datum.x}: ${datum.y}`}
  style={{ labels: { fill: "white" }, data: { fill: "#ADD8E6" }}}
/>
        </div>
    }
}

export default WaterBreakdown