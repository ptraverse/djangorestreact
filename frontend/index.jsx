'use strict';

var React = require('react');
var ReactDOM = require('react-dom');

class WelcomeThing extends React.Component {
    render() {
        return <div>Lets all drink at the {this.props.foo}</div>;
    }
};

ReactDOM.render(
    <WelcomeThing foo="Bar" />,
    document.getElementById('heading')
);

class UserThing extends React.component {
    
}