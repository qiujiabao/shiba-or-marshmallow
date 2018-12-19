import React from 'react';

export default class App extends React.Component {
  render() {
    return (
     <div>
       <h1>Image url:</h1>
       <form onsubmit="load('sending')">
           <input type="text" name="url" />
           <input type="submit" value="OK" />
       </form>
     </div>);
  }
}