import React, { Component } from "react"

export default class Post extends Component {
    render()
    {
        return(
            <div>
                id = {this.props.id}
                <br/>
                {this.props.body}
                <br/>
            </div>
        )
    }
}