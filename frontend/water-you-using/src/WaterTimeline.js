import React from 'react'
import {VictoryChart, VictoryLine, VictoryAxis} from 'victory'
import {Dropdown} from 'semantic-ui-react'

var hourlyJSON = null
var dailyJSON = null
var weeklyJSON = null
var monthlyJSON = null
var yearlyJSON = null
var hourly = []
var daily = []
var weekly = []
var monthly = []
var yearly = []

const date = new Date()
const today = date.getDay()
const thisHour = date.getHours()
const hoursToday = []
const todayThisWeek = []

var x = thisHour;
for(var i = 0; i < 24;i++){
    if (x < 0) {
        x = 23;
        hoursToday[i] = x;
        x--;
    }
    else {
        hoursToday[i] = x;
        x--;
    }
}
var y = today
for(var i = 0; i < 7; i++){
    if(y < 0){
        y = 6
    }
    switch(y){
        case 0:
            todayThisWeek[i] = 'SUN';
            break;
        case 1:
            todayThisWeek[i] = 'MON';
            break;
        case 2:
            todayThisWeek[i] = 'TUE';
            break;
        case 3:
            todayThisWeek[i] = 'WED';
            break;
        case 4:
            todayThisWeek[i] = 'THU';
            break;
        case 5: 
            todayThisWeek[i] = 'FRI';
            break;
        case 6: 
            todayThisWeek[i] = 'SAT'
            break;
        default:
            todayThisWeek[i] = 'MON'
    }
    y--
}


//http://dorm.buttersalt.me:5000/lasttimevolume/mitchell/testpassmitchell/bathroom
//Returns a float with the water usage in the last hour for "bathroom"


class WaterTimeline extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            option: 'hourly',
            domain: props.domain
        };
      }

    setTimeFrame(optionChoice) {
        this.setState({
        ...this.state,
        option: optionChoice})
    }
    
    componentDidMount(){
        //parse hours JSON
        var http_req = new XMLHttpRequest();
        http_req.open("GET",this.state.domain + 'breakdown/mitchell/testpassmitchell/HOURLY_DATA_POINT',false);
        http_req.send(null);
        hourlyJSON = JSON.parse(http_req.responseText)
        //parse hours
        hourly[0] = hourlyJSON[0].h1
        hourly[1] = hourlyJSON[0].h2
        hourly[2] = hourlyJSON[0].h3
        hourly[3] = hourlyJSON[0].h4
        hourly[4] = hourlyJSON[0].h5
        hourly[5] = hourlyJSON[0].h6
        hourly[6] = hourlyJSON[0].h7
        hourly[7] = hourlyJSON[0].h8
        hourly[8] = hourlyJSON[0].h9
        hourly[9] = hourlyJSON[0].h10
        hourly[10] = hourlyJSON[0].h11
        hourly[11] = hourlyJSON[0].h12
        hourly[12] = hourlyJSON[0].h13
        hourly[13] = hourlyJSON[0].h14
        hourly[14] = hourlyJSON[0].h15
        hourly[15] = hourlyJSON[0].h16
        hourly[16] = hourlyJSON[0].h17
        hourly[17] = hourlyJSON[0].h18
        hourly[18] = hourlyJSON[0].h19
        hourly[19] = hourlyJSON[0].h20
        hourly[20] = hourlyJSON[0].h21
        hourly[21] = hourlyJSON[0].h22
        hourly[22] = hourlyJSON[0].h23
        hourly[23] = hourlyJSON[0].h24

        //parse daily JSON
        var http_req2 = new XMLHttpRequest();
        http_req2.open("GET",this.state.domain + 'breakdown/mitchell/testpassmitchell/DAILY_DATA_POINT',false);
        http_req2.send(null);
        dailyJSON = JSON.parse(http_req2.responseText)
        //parse days
        daily[0] = dailyJSON[0].d1
        daily[1] = dailyJSON[0].d2
        daily[2] = dailyJSON[0].d3
        daily[3] = dailyJSON[0].d4
        daily[4] = dailyJSON[0].d5
        daily[5] = dailyJSON[0].d6
        daily[6] = dailyJSON[0].d7

        //update now!
        this.setTimeFrame('hourly')

    }

    render(){
        if(this.state.option === 'hourly'){
            return <div><br/>
            <center><div class="ui teal massive label"><font color = "White">&nbsp;&nbsp;&nbsp;&nbsp;Your  Water  Usage  by  Hour,  for  the  Past  24  Hours &nbsp;&nbsp;&nbsp;&nbsp;</font></div></center><br/>
            <center>
                <div class = "ui blue large label"><Dropdown text='Time Frame Selection'>
                <Dropdown.Menu>
                    <Dropdown.Item text='24 Hours' onClick = {() => this.setTimeFrame('hourly')} />
                    <Dropdown.Item text='7 Days' onClick = {() => this.setTimeFrame('daily')}/>
                    
                    </Dropdown.Menu>
                </Dropdown> 
                </div><br />
            </center><br />
            <VictoryChart>
            <VictoryLine
                style={{ data: { stroke: "#dce8fc", strokeWidth: 5} }}
                data={[
                    { x: hoursToday[23] , y: hourly[0]},
                    { x: hoursToday[22] , y: hourly[1]},
                    { x: hoursToday[21] , y: hourly[2]},
                    { x: hoursToday[20] , y: hourly[3]},
                    { x: hoursToday[19] , y: hourly[4]},
                    { x: hoursToday[18] , y: hourly[5]},
                    { x: hoursToday[17] , y: hourly[6]},
                    { x: hoursToday[16] , y: hourly[7]},
                    { x: hoursToday[15] , y: hourly[8]},
                    { x: hoursToday[14] , y: hourly[9]},
                    { x: hoursToday[13] , y: hourly[10]},
                    { x: hoursToday[12] , y: hourly[11]},
                    { x: hoursToday[11] , y: hourly[12]},
                    { x: hoursToday[10] , y: hourly[13]},
                    { x: hoursToday[9] , y: hourly[14]},
                    { x: hoursToday[8] , y: hourly[15]},
                    { x: hoursToday[7] , y: hourly[16]},
                    { x: hoursToday[6] , y: hourly[17]},
                    { x: hoursToday[5] , y: hourly[18]},
                    { x: hoursToday[4] , y: hourly[19]},
                    { x: hoursToday[3] , y: hourly[20]},
                    { x: hoursToday[2] , y: hourly[21]},
                    { x: hoursToday[1] , y: hourly[22]},
                    { x: hoursToday[0] , y: hourly[23]}
                ]}
            />
            <VictoryAxis
                label="Hours"
                orientation="bottom"
                style={{
                    axis: {stroke: "#dce8fc"},
                    axisLabel: {fontSize: 15, padding: 30, fill:"#dce8fc"},
                    tickLabels: {fontSize: 10, fill:"#dce8fc"}
                    }}
                scale = {{x:"time"}}
            />
            <VictoryAxis dependentAxis
            height = {1000}
            width = {1000}
                label="Volume(Gallons)"
                orientation="left"
                style={{
                    axis: {stroke: "#dce8fc"},
                    axisLabel: {fontSize: 15, padding: 35, fill:"#dce8fc"},
                    tickLabels: {fontSize: 10, fill:"#dce8fc"}
                    }}
                scale = {{y:"linear"}}
            />
            
            </VictoryChart>
            </div>
        }
        else {
            return <div><br/>
            <center><div class="ui teal massive label"><font color = "White">&nbsp;&nbsp;&nbsp;&nbsp;Your  Water  Usage  by  Day  for  the  Past  Week&nbsp;&nbsp;&nbsp;&nbsp;</font></div></center><br/>
            <center>
                <div class = "ui blue large label"><Dropdown text='Time Frame Selection'>
                <Dropdown.Menu>
                    <Dropdown.Item text='24 Hours' onClick = {() => this.setTimeFrame('hourly')} />
                    <Dropdown.Item text='7 Days' onClick = {() => this.setTimeFrame('daily')}/>
                    </Dropdown.Menu>
                </Dropdown> 
                </div><br />
            </center><br />
            <VictoryChart>
            <VictoryLine
                width = {1300}
                style={{ data: { stroke: "#dce8fc", strokeWidth: 5} }}
                data={[
                { x: todayThisWeek[6], y: daily[0]},
                { x: todayThisWeek[5], y: daily[1]},
                { x: todayThisWeek[4], y: daily[2]},
                { x: todayThisWeek[3], y: daily[3]},
                { x: todayThisWeek[2], y: daily[4]},
                { x: todayThisWeek[1], y: daily[5]},
                { x: todayThisWeek[0], y: daily[6]}
                ]}
            />
            <VictoryAxis
                label="Day"
                orientation="bottom"
                style={{
                    axis: {stroke: "#dce8fc"},
                    axisLabel: {fontSize: 15, padding: 30, fill:"#dce8fc"},
                    tickLabels: {fontSize: 10, fill:"#dce8fc"}
                    }}
                scale = {{x: "time"}}
            />
            <VictoryAxis dependentAxis 
                label="Volume(Gallons)"
                scale ={{y:"linear"}}
                style={{
                    axis: {stroke: "#dce8fc"},
                    axisLabel: {fontSize: 15, padding: 35,fill:"#dce8fc"},
                    tickLabels: {fontSize: 8, fill:"#dce8fc"}
                    }}
                orientation="left"
            />
            </VictoryChart>
            </div>
        }
        
    }

}

//<Dropdown.Item text='4 Weeks' onClick = {() => this.setTimeFrame('weekly')}/>
//<Dropdown.Item text='12 Months' onClick = {() => this.setTimeFrame('monthly')}/>
//<Dropdown.Item text='10 Years' onClick = {() => this.setTimeFrame('yearly')}/>


export default WaterTimeline