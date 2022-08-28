/* First React App
This code helps to continously aske the user for data and to display it in a dynamic way
New components will be created based on the user's inputs 
There will also be an option to delete such components

Ana Paula Katsuda, A01025303
*/


//Import libraries
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Post from '../Components/post';

// 
class Name extends React.Component {

  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Name:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Name />
  </React.StrictMode>
);

/*References
https://www.youtube.com/watch?v=ivM4Yfks_sk
 */