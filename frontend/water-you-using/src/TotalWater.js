import React from 'react';




class TotalWater extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      waterOunces:1000, 
      domain: props.domain
    };
  }
  componentDidMount(){
    //get total water today
    var totalWaterJSON
    var totalWaterNum
    var http_req2 = new XMLHttpRequest();
        http_req2.open("GET",this.state.domain + 'gettodaysusage/mitchell/testpassmitchell',false);
        http_req2.send(null);
        totalWaterJSON = JSON.parse(http_req2.responseText)
        totalWaterNum = totalWaterJSON[0].text
        this.setState({
          ...this.state,
          waterOunces:totalWaterNum,
        })
  }
  render() {
    return <div><br/><div><center><div class="ui teal massive label">
        {this.state.waterOunces}
    </div></center>
    <div class="label"><font color = "White">
      Gallons of Water Used Today</font> <br /><br />
    </div>
  </div> </div>
}
}

export default TotalWater;