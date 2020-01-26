import React from 'react'
import TotalWater from './TotalWater'
import WaterBreakdown from './WaterBreakdown'
import WaterTimeline from './WaterTimeline'


function Content(props){
    if(props.page === 'TotalWater'){
        return <TotalWater domain = {props.domain}/>
    }
    else if(props.page === 'WaterBreakdown'){
        return <WaterBreakdown domain = {props.domain}/>
    }
    else if(props.page === 'WaterTimeline'){
        return <WaterTimeline domain = {props.domain} />
    }
    else{
        return <p></p>
    }
}


export default Content